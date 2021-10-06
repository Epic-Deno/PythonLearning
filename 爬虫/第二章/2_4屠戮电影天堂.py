'''
Description: 2_4屠戮电影天堂
Author: Pony
Date: 2021-10-06 17:32:29
LastEditors: Pony
LastEditTime: 2021-10-06 18:23:38
FilePath: /爬虫/第二章/2_4屠戮电影天堂.py
'''
# 1. 定位到2020必看片
# 2. 从2021必看片中找到自页面的链接地址
# 3. 请求子页面的链接地址， 拿到我们想要的下载地址.....
import requests
import re
import csv
domain = "https://www.dytt89.com/"

resp = requests.get(domain, verify=False) #verify=False 去掉安全验证
resp.encoding = 'gb2312' # 指定字符集
# print(resp.text)

obj = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
objNew = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td '
                  r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
result = obj.finditer(resp.text)
child_href_list = []
for it in result:
    ul = it.group('ul')
    # print(ul)
    
    # 拿到ul 里面的li链接
    resultNew = objNew.finditer(ul)
    for itt in resultNew:
        # 拼接子页面的地址： 域名 + 子页面地址
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href) # 保存子页面链接地址
f = open("电影天堂.csv", mode="w")
csvWriter = csv.writer(f)
# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312' # 指定字符集
    result3 = obj3.search(child_resp.text)
    # print(result3.group('movie'))
    # print(result3.group('download'))
    dic = result3.groupdict()
    dic['href'] = href 
    csvWriter.writerow(dic.values()) # 写入数据
print('successfully')
resp.close()  # 关掉
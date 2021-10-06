'''
Description: 2_4屠戮番号网站
Author: Pony
Date: 2021-10-06 18:19:44
LastEditors: Pony
LastEditTime: 2021-10-07 01:49:51
FilePath: /爬虫/第二章/2_4屠戮番号网站.py
'''
import requests
import re
import csv

domain = "https://www.ganfanhao.xyz/"
def createCode(strNew, count = '8'):
    reg = ".{0," + count + "}"
    obj = re.compile(reg, re.S)
    result = obj.findall(strNew)
    lastResult = domain + 'magnet:?xt=urn:btih:'
    for i in result:
        if i:
            num = chr(int(i, 2) - 10)
            lastResult = lastResult + str(num)
    return lastResult
keyworld = input("输入演员名称")
param = {
    's': keyworld
}
# 初始的数据列表
baseResult = []

# 匹配规则
obj1 = re.compile(r'<a class="thumbnail" href="(?P<href>.*?)"', re.S)
obj2 = re.compile(r'<h1 class="focusbox-title">(?P<title>.*?)</h1>'
                  r'.*?<section class="container">.*?<article class="article-content">.*?<p>'
                  r'<img.*?data-lazy-src="(?P<imgUrl>.*?)"'
                  r'.*?<div class="cililian" id="ciliqu">.*?<blockquote>.*?reurl(?P<uCode>.*?)</script></p>.*?</div>', re.S)

# 循环5页
for page in range(1, 6):
    resp = requests.get(domain + 'fan/page/' + str(page), params=param)
    result1 = obj1.finditer(resp.text)
    baseResult.extend(result1)
# 拿到图片封面和链接地址
f = open(keyworld + ".csv", mode="w")
csvWriter = csv.writer(f)
for it in baseResult:
    href = domain + it.group('href').strip("/") # 链接
    child_resp = requests.get(href)
    # print(child_resp.text)
    result2 = obj2.search(child_resp.text)
    if result2:
        dic = result2.groupdict()
        dic['imgUrl'] = domain + dic['imgUrl'].strip("/") 
        dic['uCode'] = createCode(result2.group('uCode').lstrip("('").rstrip("'));")) 
        dic['href'] = href 
        csvWriter.writerow(dic.values()) # 写入数据
        # break
print('successfully')
resp.close()  # 关掉
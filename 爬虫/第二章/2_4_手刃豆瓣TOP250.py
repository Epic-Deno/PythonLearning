'''
Description: 爬取豆瓣
Author: Pony
Date: 2021-10-05 11:44:05
LastEditors: Pony
LastEditTime: 2021-10-06 00:42:37
FilePath: /爬虫/第二章/2_4_手刃豆瓣TOP250.py
'''
# 拿到页面源代码 requests
import requests
# 通过re来提取想要的有效信息 re
import re
import csv

url = "https://movie.douban.com/top250"
# 模拟客户端的头部
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
# 初始的数据列表
baseResult = []


for baseNum in  range(0, 10):
    param = {
        'start': baseNum * 25
    }
    resp = requests.get(url, params=param, headers=header)
    page_context = resp.text
    # print(baseNum, resp.request.url)

    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                            r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                            r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                            r'<span>(?P<count>.*?)人评价</span>', re.S)
                            # r'<span class="inq">(?P<motto>.*?)</span>'
    # 开始匹配
    result = obj.finditer(page_context)
    baseResult.extend(result)
f = open("豆瓣Top250.csv", mode="w")
csvWriter = csv.writer(f)
# print(baseResult)
for it in baseResult:
    # print('电影名称：' + it.group('name'))
    # print('电影评分：' + it.group('score'))
    # print('电影年份：' + it.group('year').strip() + '年')
    # print('评分人数：' + it.group('count').strip() + '人')
    dic = it.groupdict()
    dic['year'] = dic['year'].strip() # 年份前面有空格
    # dic['motto'] = dic['motto'] or " "
    csvWriter.writerow(dic.values()) # 写入数据
print("successfully!!!")
resp.close()  # 关掉


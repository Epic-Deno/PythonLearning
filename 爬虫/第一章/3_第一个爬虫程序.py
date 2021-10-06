'''
Description: 爬虫抓取测试
Author: Pony
Date: 2021-10-05 08:56:19
LastEditors: Pony
LastEditTime: 2021-10-05 09:58:56
FilePath: /爬虫/第一章/3_第一个爬虫程序.py
'''
# 爬虫：通过编写程序来获取互联网上的资源
# 百度： 
# 需求：用程序模拟浏览器。 输入一个地址。 网站中获取资源或者内容
from urllib.request import urlopen

url = "https://www.google.com"
# 访问网页
resp = urlopen(url)
# 输出结果
# print(resp.read().decode("utf-8"))
with open("index.html", mode="w") as f:
    f.write(resp.read().decode("utf-8")) # 读取网页的源代码
print("Over!!!")
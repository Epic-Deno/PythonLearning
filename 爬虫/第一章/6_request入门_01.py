'''
Description: 6_request入门_01
Author: Pony
Date: 2021-10-05 09:48:43
LastEditors: Pony
LastEditTime: 2021-10-05 10:52:09
FilePath: /爬虫/第一章/6_request入门_01.py
'''
# pip install requests
# 国内的源
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

import requests
query = input("输入你要查询的内容")
url =  f"https://cn.bing.com/search?q={query}"

dic = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

resp = requests.get(url, headers=dic) # 处理一个个小小反爬  添加user-agent

# print(resp.text) # 拿到源代码
with open("index.html", mode="w") as f:
    f.write(resp.text) # 读取网页的源代码
print("Over!!!")
resp.close()  # 关掉
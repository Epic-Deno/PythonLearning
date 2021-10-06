'''
Description: Created By Pony
Author: Pony
Date: 2021-10-05 10:41:06
LastEditors: Pony
LastEditTime: 2021-10-05 10:51:55
FilePath: /爬虫/第一章/8_requests入门_03.py
'''
import requests

url = "https://movie.douban.com/j/chart/top_list"

# 重新封装参数
params = {
    "type": 24,
    "interval_id": "100:90",
    "action": "", 
    "start": 0,
    "limit": 20
}

# 模拟客户端的头部
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

resp = requests.get(url=url, params=params, headers=header)

print(resp.json())
resp.close()  # 关掉
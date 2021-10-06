'''
Description: Created By Pony
Author: Pony
Date: 2021-10-06 00:53:12
LastEditors: Pony
LastEditTime: 2021-10-06 01:29:00
FilePath: /爬虫/第二章/2_4_包里爬取百度.py
'''
# 导入BaiduSpider
from pprint import pprint
from baiduspider import BaiduSpider

result = BaiduSpider().search_web('Python')
print(result)  # print
print('\n\n')
pprint(result)  # pprint
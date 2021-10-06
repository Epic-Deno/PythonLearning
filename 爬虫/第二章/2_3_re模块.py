'''
Description: re模块
Author: Pony
Date: 2021-10-05 11:20:12
LastEditors: Pony
LastEditTime: 2021-10-05 11:42:10
FilePath: /爬虫/第二章/2_1_re模块.py
'''
import re

# findall: 匹配字符串中的所有符合正则的内容
# lst = re.findall(r"\d+", "我的电话是：100000")
# print(lst)

# finditer: 匹配字符串所有内容返回的是迭代器, 在数组中拿到数据需要。group()
# it = re.finditer(r"\d+", "我的手机号码： 1829282828228")
# for i  in it:
#     print(i.group())

# search , 找到一个结果就返回， 返回结果是match对象， 拿到数据需要.group（） 全文匹配
# s = re.search(r"\d+", "我的电话号码是19298288")
# print(s.group())

# match是从头开始匹配
# s = re.search(r"\d+", "9298288")
# print(s.group())

# 预加载正则表达式
# obj = re.compile(r"\d+")

# ret = obj.finditer("大家好我的手机号码是10086")
# for it in ret:
#     print(it.group())

# rec = obj.findall("我有10000万")
# print(rec)

s = """"
<div class='01'><span id='1'>cook</span></div>
<div class='02'><span id='2'>faker</span></div>
<div class='03'><span id='3'>jobs</span></div>
<div class='04'><span id='4'>kobe</span></div>
"""

# (?P<分组名字>正则) 可以单独从正则匹配的内容进一步提取出内容
obj = re.compile(r"<div class='(?P<id>.*?)'><span id='\d+'>(?P<Pony>.*?)</span></div>", re.S) # res.S： 让.能换行

result = obj.finditer(s)
for it in result:
    print(it.group("Pony"))
    print(it.group("id"))

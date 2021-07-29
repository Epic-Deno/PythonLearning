# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 22:02:32 2018

@author: 10029
"""

import turtle

 #区域
def my_goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
def eyes():
    turtle.tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            turtle.lt(3)
            turtle.fd(a)
        else:
            a += 0.05
            turtle.lt(3)
            turtle.fd(a)
    turtle.tracer(True)
# 头  
turtle.pensize(3)
turtle.penup()
turtle.circle(150, 40)
turtle.pendown()
turtle.fillcolor('#00a0de')
turtle.begin_fill()
turtle.circle(150, 280)
turtle.end_fill()
#围巾
turtle.fillcolor('#e70010')
turtle.begin_fill()
turtle.seth(0)
turtle.fd(200)
turtle.circle(-5, 90)
turtle.fd(10)
turtle.circle(-5, 90)
turtle.fd(207)
turtle.circle(-5, 90)
turtle.fd(10)
turtle.circle(-5, 90)
turtle.end_fill()

# 脸
turtle.fd(183)
turtle.fillcolor('#ffffff')
turtle.begin_fill()
turtle.lt(45)
turtle.circle(120, 100)

turtle.seth(90)
eyes()

turtle.seth(180)
turtle.penup()
turtle.fd(60)
turtle.pendown()
turtle.seth(90)
eyes()

turtle.penup()
turtle.seth(180)
turtle.fd(64)
turtle.pendown()
turtle.seth(215)
turtle.circle(120, 100)
turtle.end_fill()

# 鼻子

my_goto(-10, 158)
turtle.fillcolor('#e70010')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# 嘴巴

my_goto(5, 148)
turtle.seth(270)
turtle.fd(100)
turtle.seth(0)
turtle.circle(120, 50)
turtle.seth(230)
turtle.circle(-120, 100)

# 胡须

my_goto(-37, 135)
turtle.seth(165)
turtle.fd(60)

my_goto(-37, 125)
turtle.seth(180)
turtle.fd(60)

my_goto(-37, 115)
turtle.seth(193)
turtle.fd(60)

my_goto(37, 135)
turtle.seth(15)
turtle.fd(60)

my_goto(37, 125)
turtle.seth(0)
turtle.fd(60)

my_goto(37, 115)
turtle.seth(-13)
turtle.fd(60)

my_goto(0, 0)
turtle.seth(0)
turtle.penup()
turtle.circle(150, 50)
turtle.pendown()
turtle.seth(30)
turtle.fd(40)
turtle.seth(70)
turtle.circle(-30, 270)


turtle.fillcolor('#00a0de')
turtle.begin_fill()

turtle.seth(230)
turtle.fd(80)
turtle.seth(90)
turtle.circle(1000, 1)
turtle.seth(-89)
turtle.circle(-1000, 10)



turtle.seth(180)
turtle.fd(70)
turtle.seth(90)
turtle.circle(30, 180)
turtle.seth(180)
turtle.fd(70)


turtle.seth(100)
turtle.circle(-1000, 9)

turtle.seth(-86)
turtle.circle(1000, 2)
turtle.seth(230)
turtle.fd(40)

turtle.circle(-30, 230)
turtle.seth(45)
turtle.fd(81)
turtle.seth(0)
turtle.fd(203)
turtle.circle(5, 90)
turtle.fd(10)
turtle.circle(5, 90)
turtle.fd(7)
turtle.seth(40)
turtle.circle(150, 10)
turtle.seth(30)
turtle.fd(40)
turtle.end_fill()

# 左手
turtle.seth(70)
turtle.fillcolor('#ffffff')
turtle.begin_fill()
turtle.circle(-30)
turtle.end_fill()

# 右手
my_goto(-133.97, -91.81)
turtle.seth(50)
turtle.fillcolor('#ffffff')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# 脚
my_goto(103.74, -182.59)
turtle.seth(0)
turtle.fillcolor('#ffffff')
turtle.begin_fill()
turtle.fd(15)
turtle.circle(-15, 180)
turtle.fd(90)
turtle.circle(-15, 180)
turtle.fd(10)
turtle.end_fill()

my_goto(-96.26, -182.59)
turtle.seth(180)
turtle.fillcolor('#ffffff')
turtle.begin_fill()
turtle.fd(15)
turtle.circle(15, 180)
turtle.fd(90)
turtle.circle(15, 180)
turtle.fd(10)
turtle.end_fill()

# 口袋
my_goto(-103.42, 15.09)
turtle.seth(0)
turtle.fd(38)
turtle.seth(230)
turtle.begin_fill()
turtle.circle(90, 260)
turtle.end_fill()

my_goto(5, -40)
turtle.seth(0)
turtle.fd(70)
turtle.seth(-90)
turtle.circle(-70, 180)
turtle.seth(0)
turtle.fd(70)

#铃铛
my_goto(-103.42, 15.09)
turtle.fd(90)
turtle.seth(70)
turtle.fillcolor('#ffd200')
turtle.begin_fill()
turtle.circle(-20)
turtle.end_fill()
turtle.seth(170)
turtle.fillcolor('#ffd200')
turtle.begin_fill()
turtle.circle(-2, 180)
turtle.seth(10)
turtle.circle(-100, 22)
turtle.circle(-2, 180)
turtle.seth(180-10)
turtle.circle(100, 22)
turtle.end_fill()
turtle.goto(-13.42, 15.09)
turtle.seth(250)
turtle.circle(20, 110)
turtle.seth(90)
turtle.fd(15)
turtle.dot(10)
my_goto(0, -150)

# 眼睛
turtle.seth(0)
my_goto(-20, 195)
turtle.fillcolor('#000000')
turtle.begin_fill()
turtle.circle(13)
turtle.end_fill()

turtle.pensize(6)
my_goto(20, 205)
turtle.seth(75)
turtle.circle(-10, 150)
turtle.pensize(3)

my_goto(-17, 200)
turtle.seth(0)
turtle.fillcolor('#ffffff')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
my_goto(0, 0)

turtle.exitonclick()
# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 1.py
@Author : wenjing
@Date : 2022/11/29 14:34
"""
from turtle import *  #用from ... import ... 导入库，后调用其函数只需写函数名

setup(500,500,1000,250)
seth(0)
for i in range(0, 400, 5):
    fd(i)
    left(90)
    fd(i)
    left(90)
hideturtle()  #隐藏画笔

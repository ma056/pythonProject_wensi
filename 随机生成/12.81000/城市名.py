# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 城市名.py
@Author : wenjing
@Date : 2022/12/8 17:23
"""
with open('1.txt', 'r', encoding='utf-8') as f:
    a = f.readlines()
    list1 = []
    for i in a:
        aa = i.split('\t')[-1].split('\n')[0].upper()
        list1.append(aa)
    print(a)
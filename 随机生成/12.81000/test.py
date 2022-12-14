# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : test.py
@Author : wenjing
@Date : 2022/12/8 11:50
"""
import random

start_num = ["3U", "NS", "8C", "CA", "SC", "MF", "EU", "ZH", "VD", "FM", "KN", "MU", "HU", "CN", "8L", "PN", "GS",
                  "HO", "BK", "G5", "9C", "JD"]
a = []
for i in range(0, 1300):
    random_pn = random.randrange(0, len(start_num))
    random_num = str(random.randint(100, 9999))
    phone_num = "{}{:0<3}".format(start_num[random_pn], random_num)
    a.append(phone_num)
    if len(phone_num)==5:
        print(phone_num)
aa = list(set(a))
print(a)
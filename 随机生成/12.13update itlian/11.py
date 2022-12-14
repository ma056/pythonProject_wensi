# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 11.py
@Author : wenjing
@Date : 2022/12/14 10:17
"""
from itertools import groupby, islice
myList = [True, True, False, False, True, False, True, False, False]
for k, g in groupby(myList):
    if k:

        a = sum(1 for _ in islice(g, 3))
        print(a)
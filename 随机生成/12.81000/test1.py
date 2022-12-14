# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : test1.py
@Author : wenjing
@Date : 2022/12/8 10:43
"""
'''
前三位固定：东方航空781；国际航空999；南方航空784；上海航空774；厦门航空731；深圳航空479；
海南航空880；山东航空324；四川航空876；华夏航空883；奥凯航空866；联合航空822
'''
import random
from random import shuffle
import itertools


# 航空
def aviation():
    pass


# 航班号 长度5/6位 前面两位固定,字母需大写：3U,NS,8C,CA,SC,MF,EU,ZH,VD,FM,KN,MU,HU,CN,8L,PN,GS,HO,BK,G5,9C,JD
def aviation_flight_number():
    ls = [random.randint(100, 9999) for i in range(1500)]
    st = list(set(ls))  # set()函数创建一个无序不重复元素集
    flight_number = st[0:1000]
    fixed_list = ["3U", "NS", "8C", "CA", "SC", "MF", "EU", "ZH", "VD", "FM", "KN", "MU", "HU", "CN", "8L", "PN", "GS",
                  "HO", "BK", "G5", "9C", "JD"]
    res_flight_number = []
    for filght_num in flight_number:
        fixed_num = random.choice(fixed_list)
        res_flight_number.append(f'{fixed_num}{filght_num}')
    new_res_flight_number = list(set(res_flight_number))
    # print(st)
    return new_res_flight_number


# 订单号 数字	11位
def aviation_order_no():
    ls = [random.randint(100, 99999999) for i in range(1500)]
    st = list(set(ls))  # set()函数创建一个无序不重复元素集
    flight_number = st[0:1000]


def main():
    pass


if __name__ == '__main__':
    main()
    aviation_flight_number()

# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 羊车门.py
@Author : wenjing
@Date : 2022/11/29 14:53
"""
# from random import *
#
# TIMES = 10000
# my_first_choice_n = 0  # 初始化不改选择的次数
# my_change_choice_n = 0  # 初始化更改选择的次数
# for i in range(TIMES):
#     car_inDoor = randint(0, 2)
#     my_guess = randint(0, 2)
#     if car_inDoor == my_guess:
#         my_first_choice_n += 1
#     else:
#         my_change_choice_n += 1
# print("不改选择:{}".format(my_first_choice_n / TIMES))
# print("更改选择:{}".format(my_change_choice_n / TIMES))
import random
change=0
notchange=0
#time表实验次数
count=eval(input("请输入实验次数："))
for i in range(count):
    car=random.randint(0,2)
    goat=random.randint(0,2)
    if(car==goat):
        change+=1
    else:
        notchange+=1
print("不换门得到汽车的机会：{}".format(change/count))
print("换门得到汽车的机会：{}".format(notchange/count))

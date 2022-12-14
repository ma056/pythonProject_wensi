# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : test_2.py
@Author : wenjing
@Date : 2022/12/8 14:02
"""
import random
from random import shuffle
import itertools
import pandas as pd
import string


def fast_food():
    type1, number1, txt1 = fast_food_order_no()
    type2, number2, txt2 = fast_food_tel_num()
    type3, number3, txt3 = fast_food_waybill_no()
    type4, number4, txt4 = fast_food_pick_code()

    type_list = type1 + type2 + type3 + type4
    number_list = number1 + number2 + number3 + number4
    txt_list = txt1 + txt2 + txt3 + txt4
    # print(type_list)
    return type_list, number_list, txt_list

# 订单编号 数字/数字加字母 13-19位 字母位置固定大写
def fast_food_order_no():
    # num1 = random.choice(string.ascii_uppercase)
    order_no = []
    for i in range(0, 1000):
        num1 = random.choice(string.ascii_uppercase)
        random_num = str(random.randint(1000000000000, 9999999999999999999))
        phone_num = f'{num1}{random_num}'
        order_no.append(phone_num)
    order_no_list = list(set(order_no))[0:1000]
    # print(order_no_list)
    return ["订单编号"] * 1000, [i for i in range(1, 1001)], order_no_list


# 虚拟手机号码 数字 11位
def fast_food_tel_num():
    tel_num = []
    for i in range(0, 1200):
        # random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(0, 99999999))
        phone_num = "{}{:0<8}".format(187, random_num)
        tel_num.append(phone_num)
    tel_num_list = list(set(tel_num))[0:1000]
    # print(tel_num_list)
    return ["虚拟手机号码"] * 1000, [i for i in range(1, 1001)], tel_num_list


# 运单号 可变4位
def fast_food_waybill_no():
    waybill_no = []
    for i in range(0, 1100):
        random_num = str(random.randint(1000, 9999))
        phone_num = f'909{random_num}'
        waybill_no.append(phone_num)
    waybill_no_list = list(set(waybill_no))[0:1000]
    # print(waybill_no_list)
    return ["运单号"] * 1000, [i for i in range(1, 1001)], waybill_no_list


#取件码 数字 四位以上
def fast_food_pick_code():
    pick_code = []
    for i in range(0, 1100):
        random_num = str(random.randint(1000, 99999))
        pick_code.append(random_num)
    pick_codeo_list = list(set(pick_code))[0:1000]
    # print(pick_codeo_list)
    return ["取件码"] * 1000, [i for i in range(1, 1001)], pick_codeo_list

def main():
    type_list,number_list, txt_list = fast_food()
    # print(type_list)
    df1 = pd.DataFrame({'种类': type_list,"编号":number_list,"文本":txt_list})

    with pd.ExcelWriter('数字字母收集excel_1.xlsx') as writer:
        df1.to_excel(writer, sheet_name='快餐', index=False)
if __name__ == '__main__':
    main()
# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : test_3.py
@Author : wenjing
@Date : 2022/12/8 14:34
"""
import random
from random import shuffle
import itertools
import pandas as pd
import re
import string


def retail():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = retail_shop_number()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = retail_order_num()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = retail_item_number()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = retail_models_number()
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = retail_vin_code()
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = retail_track_num()

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1+domain6_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2+domain6_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 +UtteranceType5_1+UtteranceType6_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 +UtteranceType5_2+UtteranceType6_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1+Category6_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2+Category6_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1+text6_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2+text6_2
    print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Shop Number   NumbersAndLetters   4 digits    格式为1个字母+3个数字
def retail_shop_number():
    shop_number = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_letters, 1))
        random_num = str(random.randint(0, 999)).zfill(3)
        shop_number.append(f'{num1}{random_num}')
    shop_number_list = list(set(shop_number))
    number = 10001 - len(shop_number_list)
    shop_number_list.extend([''] * number)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "Shop Number"] * 3000, ["Shop Number"] * 7000, shop_number_list[0:3000], shop_number_list[3001:10001]


# Order Number   NumbersOnly      16 digits 1122020000000000.0 格式为日、月、年+随机8位
def retail_order_num():
    order_num = []
    for i in range(0, 11000):
        year = str(random.randint(1940, 2020))
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 29)).zfill(2)
        random_num = str(random.randint(0, 99999999)).zfill(8)
        order_num.append(f'{day}{month}{year}{random_num}')
    order_num_list = list(set(order_num))
    # print(order_num_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Order Number"] * 3000, ["Order Number"] * 7000, order_num_list[0:3000], order_num_list[3001:10001]


# Item number?  NumbersOnly   12 digits    字母大写 204877000000.0
def retail_item_number():
    item_number = []
    for i in range(0, 11000):
        random_num = str(random.randint(0,999999999999)).zfill(12)
        item_number.append(random_num)
    item_number_list = list(set(item_number))
    # print(psw_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["LettersOnly"] * 3000, ["LettersOnly"] * 7000, \
           ["Item number?"] * 3000, ["Item number?"] * 7000, item_number_list[0:3000], item_number_list[3001:10001]


# models NumbersAndLetters   4-20 digits    CAF7230A
def retail_models_number():
    models_number = []
    for i in range(0, 11000):
        random_num1 = ''.join(random.sample(string.ascii_uppercase, 3))
        random_num2 = str(random.randint(1000, 9999999))
        random_num3 = ''.join(random.sample(string.ascii_uppercase, 1))
        models_number.append(f'{random_num1}{random_num2}{random_num3}')
    models_number_list1 = list(set(models_number))
    # print(psw_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
           ["models"] * 3000, ["models"] * 7000, models_number_list1[0:3000], models_number_list1[3001:10001]


# VIN code        NumbersAndLetters   17 digits    LFV2A2*********
def retail_vin_code():
    vin_code = []
    for i in range(0, 11000):
        random_num1 = ''.join(random.sample(string.ascii_uppercase, 3))
        random_num2 = str(random.randint(1000000, 9999999999999)).zfill(13)
        random_num3 = ''.join(random.sample(string.ascii_uppercase, 1))
        res_num = f'{random_num1}{random_num2}{random_num3}'
        vin_code.append(res_num)
    vin_code_list = list(set(vin_code))
    # print(psw_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
           ["VIN code"] * 3000, ["VIN code"] * 7000, vin_code_list[0:3000], vin_code_list[3001:10001]


# The tracking number?  NumbersOnly  12 digits
def retail_track_num():
    track_num = []
    for i in range(0, 11000):
        random_num2 = str(random.randint(100000000000, 999999999999))
        track_num.append(random_num2)
    track_num_list = list(set(track_num))
    # print(psw_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, ["The tracking number?"] * 3000,\
           ["The tracking number?"] * 7000, track_num_list[0:3000], track_num_list[3001:10001]





def main():
    domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2 = retail()
    # print(type_list)
    # df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    #
    # with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

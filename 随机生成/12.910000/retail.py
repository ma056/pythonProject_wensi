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
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = retail_commodity_barcode()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = retail_commodity_code()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = retail_commodity_code1()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = retail_car_type()
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = retail_vin()


    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 +UtteranceType5_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 +UtteranceType5_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2
    print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# 商品条形码 13位  NumbersOnly
def retail_commodity_barcode():
    commodity_barcode = []
    for i in range(0, 11000):
        random_num = str(random.randint(1000000000000, 9999999999999))
        commodity_barcode.append(random_num)
    commodity_barcode_list = list(set(commodity_barcode))
    # print(commodity_barcode_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "商品条形码"] * 3000, ["商品条形码"] * 7000, commodity_barcode_list[0:3000], commodity_barcode_list[3001:10001]


# 商品编码/ID LettersOnly   4位以上    字母大写
def retail_commodity_code():
    commodity_code = []
    for i in range(0, 10000):
        random_num1 = ''.join(random.sample(string.ascii_uppercase, 4))
        random_num2 = ''.join(random.sample(string.ascii_uppercase, 5))
        commodity_code.append(random_num1)
        commodity_code.append(random_num2)
    commodity_code_list = list(set(commodity_code))
    # print(psw_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["LettersOnly"] * 3000, ["LettersOnly"] * 7000, \
           ["商品编码/ID"] * 3000, ["商品编码/ID"] * 7000, commodity_code_list[0:3000], commodity_code_list[3001:10001]


# 商品编码/ID NumbersOnly   4位以上
def retail_commodity_code1():
    commodity_code1 = []
    for i in range(0, 11000):
        random_num = str(random.randint(1000, 9999999))
        commodity_code1.append(random_num)
    commodity_code_list1 = list(set(commodity_code1))
    # print(psw_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, \
           ["商品编码/ID"] * 3000, ["商品编码/ID"] * 7000, commodity_code_list1[0:3000], commodity_code_list1[3001:10001]


# 车型        NumbersAndLetters   CAF7230A    字母位置固定大写
def retail_car_type():
    car_type = []
    for i in range(0, 11000):
        random_num1 = ''.join(random.sample(string.ascii_uppercase, 3))
        random_num2 = str(random.randint(1000000000000, 9999999999999))
        random_num3 = ''.join(random.sample(string.ascii_uppercase, 1))
        res_num = f'{random_num1}{random_num2}{random_num3}'
        car_type.append(res_num)
    car_type_list = list(set(car_type))
    # print(psw_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
           ["车型"] * 3000, ["车型"] * 7000, car_type_list[0:3000], car_type_list[3001:10001]


# VIN码  17位 LFV2A2********* 字母位置固定大写
def retail_vin():
    vin = []
    for i in range(0, 11000):
        random_num1 = ''.join(random.sample(string.ascii_uppercase, 3))
        random_num2 = str(random.randint(10000000000000, 99999999999999))
        res_num = f'{random_num1}{random_num2}'
        vin.append(res_num)
    vin_list = list(set(vin))
    # print(psw_list)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
           ["VIN码"] * 3000, ["VIN码"] * 7000, vin_list[0:3000], vin_list[3001:10001]





def main():
    domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2 = retail()
    # print(type_list)
    # df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    #
    # with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

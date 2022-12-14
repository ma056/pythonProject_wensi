# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : Airline.py
@Author : wenjing
@Date : 2022/12/12 9:41
"""
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
import string
import pandas as pd


# 航空
def healthcare():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = healthcare_date_product()

    domain_list1 = domain1_1
    domain_list2 = domain1_2
    UtteranceType_list1 = UtteranceType1_1
    UtteranceType_list2 = UtteranceType1_2
    Category_list1 = Category1_1
    Category_list2 = Category1_2
    text_list1 = text1_1
    text_list2 = text1_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Date of production  8 digits NumbersOnly  日、月、年
def healthcare_date_product():
    date_product = []
    for i in range(0, 12000):
        # 出生年月日
        year = str(random.randint(1940, 2020))
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 29)).zfill(2)
        random_num = f'{day}.{month}.{year}'
        date_product.append(random_num)
    date_product_list = list(set(date_product))
    number = 10001 - len(date_product_list)
    date_product_list.extend([''] * number)
    # print(date_product_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Date of production"] * 3000, ["Date of production"] * 7000, date_product_list[0:3000], date_product_list[3001:10001]


def insurance():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = insurance_passport_number()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = insurance_license_plate()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = insurance_personal_id()

    domain_list1 = domain1_1 + domain2_1 +domain3_1
    domain_list2 = domain1_2 + domain2_2+domain3_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1+UtteranceType3_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2+UtteranceType3_2
    Category_list1 = Category1_1 + Category2_1+Category3_1
    Category_list2 = Category1_2 + Category2_2+Category3_2
    text_list1 = text1_1 + text2_1+text3_1
    text_list2 = text1_2 + text2_2+text3_2
    print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Passport Number   NumbersAndLetters  9 digits YA2672719       格式为2个字母+7个数字
def insurance_passport_number():
    passport_number = []
    for i in range(0, 110000):
        num1 = ''.join(random.sample(string.ascii_uppercase, 2))
        num2 = str(random.randint(0, 9999999)).zfill(7)
        passport_number.append(f'{num1}{num2}')
    passport_number_list = list(set(passport_number))
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "Passport Number"] * 3000, ["Passport Number"] * 7000, passport_number_list[0:3000], \
           passport_number_list[3001:10001]



# License plate number   NumbersAndLetters  7 digits 2个字母+3个数字+2个字母
def insurance_license_plate():
    license_plate = []
    for i in range(0, 110000):
        num1 = ''.join(random.sample(string.ascii_uppercase, 2))
        num2 = str(random.randint(0, 999)).zfill(3)
        num3 = ''.join(random.sample(string.ascii_uppercase, 2))
        license_plate.append(f'{num1}{num2}{num3}')
    license_plate_list = list(set(license_plate))
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "License plate number"] * 3000, ["License plate number"] * 7000, license_plate_list[0:3000], \
           license_plate_list[3001:10001]


# Personal identification number   NumbersAndLetters  16 digits RSSMRA70A01L726S 首字母（RSSMRA）出生年份（70）出生城镇（A01L）复选标记（726S）
def insurance_personal_id():
    personal_id = []
    for i in range(0, 110000):
        num1 = ''.join(random.sample(string.ascii_uppercase, 6))
        num2 = str(random.randint(0, 99)).zfill(2)
        num3_1 = ''.join(random.sample(string.ascii_uppercase, 1))
        num3_2 = str(random.randint(0, 99)).zfill(2)
        num3_3 = ''.join(random.sample(string.ascii_uppercase, 1))
        num4_1 = str(random.randint(0, 999)).zfill(3)
        num4_2 = ''.join(random.sample(string.ascii_uppercase, 1))
        personal_id.append(f'{num1}{num2}{num3_1}{num3_2}{num3_3}{num4_1}{num4_2}')
    personal_id_list = list(set(personal_id))
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "Personal identification number"] * 3000, ["Personal identification number"] * 7000, personal_id_list[0:3000], \
           personal_id_list[3001:10001]


def main():
    # aviation_domain_list1, aviation_domain_list2, aviation_UtteranceType_list1, aviation_UtteranceType_list2, aviation_Category_list1, \
    # aviation_Category_list2, aviation_text_list1, aviation_text_list2 = healthcare()
    food_domain_list1, food_domain_list2, food_UtteranceType_list1, food_UtteranceType_list2, food_Category_list1, food_Category_list2, \
    food_text_list1, food_text_list2 = insurance()




if __name__ == '__main__':
    main()

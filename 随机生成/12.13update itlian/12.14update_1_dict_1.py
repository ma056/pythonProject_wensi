# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 最终版.py
@Author : wenjing
@Date : 2022/12/13 11:38
"""
import exrex
import pandas as pd

RULE_DICT = {
    "airline Telephone number": r'^\d{12}$',
    "airline Flight number": r'^[A-Z]{2}\d{4}$',
    "airline order number": r'^[A-Za-z0-9]{6}$',
    "airline Boarding time": r'^[0-9]{4}$',

    "fast_food Confirmation number": r'^[0-9]{4,8}$',
    "fast_food order number": r'^((0[1-9])|((1|2)[0-9])|30|31)(0[1-9]|1[0-2])(19\d{2}|20\d{2})\d{8}$',
    "fast_food Shop Number": r'^[A-Za-z]{1}\d{3}$',

    "finance Stock number": r'^[A-Za-z]{3,4}\d{4}$',
    "finance Company tax Number1": r'^[A-Z]{2}\d{9}$',
    "finance Company tax Number2": r'^[A-Z]{8,20}$',
    "finance Bank card number": r'^\d{13,16}$',
    "finance Expiry date of bank card": r'^(0[1-9]|1[0-2])\d{2}$',
    "finance Contract Number": r'^[A-Z]{2}\d{2,18}$',
    "finance Bank account number": r'^\d{12}$',

    "healthcare Date of production": r'^((0[1-9])|((1|2)[0-9])|30|31)(0[1-9]|1[0-2])(19\d{2}|20\d{2})$',
    "healthcare Email Address": r'^[A-Za-z]{4,9}(@gmail\.com|@outlook\.it|@outlook\.com|@live\.it|@hotmail\.com)$',
    "healthcare Telephone Number": r'^0\d{9}$',
    "insurance Passport Number": r'^[A-Z]{2}\d{7}$',
    "insurance identity card": r'^[A-Z]{2}\d{5}[A-Z]{2}$',
    "insurance License plate number": r'^[A-Z]{2}\d{3}[A-Z]{2}$',
    "insurance Personal identification number/Codice fiscale": r'^[A-Z]{6}\d{2}[J|F|M|A|S|O|N|D]((0?[1-9])|((1|2)[0-9])|30|31)[A-Z]{1}\d{3}[A-Z]{1}$',
    "mediaInternetTelecom Order No.": r'^\d{19}$',
    "mediaInternetTelecom Refund Number": r'^\d{4,20}$',
    "mediaInternetTelecom Broadband number": r'^\d{4,20}$',
    "mediaInternetTelecom Wide band type": r'^\d{4}-\d{1,16}$',
    "mediaInternetTelecom Email Address": r'^[A-Za-z0-9]{4,9}(@gmail\.com|@outlook\.it|@outlook\.com|@live\.it|@hotmail\.com)$',
    "mediaInternetTelecom password1": r'^[a-z]{4,20}$',
    "mediaInternetTelecom password2": r'^\d{4,20}$',
    "mediaInternetTelecom password3": r'^[A-Za-z0-9]{4,20}$',
    "mediaInternetTelecom Verification code": r'^\d{4,20}$',
    "mediaInternetTelecom Sales/Collection": r'^\d{4,20}$',
    "mediaInternetTelecom Online account name": r'^[A-Za-z0-9]{4,20}$',

    "retail Order Number": r'^((0[1-9])|((1|2)[0-9])|30|31)(0[1-9]|1[0-2])(19\d{2}|20\d{2})\d{8}$',
    "retail Item number": r'^\d{12}$',
    "retail models": r'^[A-Z]{2}\d{3}[A-Z]{2}$',
    "retail VIN code": r'^[A-Z0-9]{17}$',
    "retail The tracking number": r'^\d{8,20}$',

    "travel Order Number": r'^\d{6}$',
    "travel Room Number": r'^\d{4,6}$',
    "travel Booking Number1": r'^[A-Z]{6}$',
    "travel Booking Number2": r'^[A-Z]{4}\d{3}$',
}


def get_data(d_type, u_type, c_type, rule):
    random_list = []
    list_len_dict = {}
    while len(random_list) < 10000:
        # rule = r'^[A-Z]{7,10}|[A-Z]{4,5}$'
        random_str = exrex.getone(rule)
        random_list.append(random_str)
        random_list = list(set(random_list))
        if len(random_list) not in list_len_dict.keys():
            list_len_dict[len(random_list)] = [1]
        else:
            list_len_dict[len(random_list)].append(1)
            if len(list_len_dict[len(random_list)]) > 100:
                break
    if len(random_list) < 10000:
        number = 10000 - len(random_list)
        random_list.extend([''] * number)
    return [d_type] * 3000, [d_type] * 7000, [u_type] * 3000, [u_type] * 7000, \
           [c_type] * 3000, [c_type] * 7000, random_list[0:3000], random_list[3000:10000]


# Boarding time  NumbersOnly	 4digits   W7PCYE
# def airline_boarding_time():
#     boarding_number = []
#     # while len(boarding_number) < 10000:
#     for i in range(0, 110000):
#         # rule = r'^[0-9]{4}$'
#         num = exrex.getone(RULE_DICT['airline Boarding time'])
#         boarding_number.append(num)
#     boarding_number = list(set(boarding_number))
#     number = 10000 - len(boarding_number)
#     boarding_number.extend([''] * number)
#     # print(boarding_number_list)
#     return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, \
#            ["Boarding time"] * 3000, ["Boarding time"] * 7000, boarding_number[0:3000], boarding_number[3000:10000]


def airline():
    # Telephone number/train number     NumbersOnly     12 digits
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Airline","NumbersOnly","Telephone number",RULE_DICT['airline Telephone number'])
    # Flight number  NumbersAndLetters	 6 digits   格式为2个字母+4个数字
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Airline","NumbersAndLetters","Flight number",RULE_DICT['airline Flight number'])
    # order number  NumbersAndLetters	 6 digits   W7PCYE
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Airline","NumbersAndLetters","order number",RULE_DICT['airline order number'])
    # Boarding time  NumbersOnly	 4digits   W7PCYE
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("Airline","NumbersOnly","Boarding time",RULE_DICT['airline Boarding time'])

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Shop Number   NumbersAndLetters   4 digits    格式为1个字母+3个数字
# def fast_food_shop_number():
#     shop_number = []
#     for i in range(0, 11000):
#         # rule = r'^[A-Za-z]{1}\d{3}$'
#         random_str = exrex.getone(RULE_DICT['fast_food Shop Number'])
#         shop_number.append(random_str)
#     shop_number_list = list(set(shop_number))
#     number = 10001 - len(shop_number_list)
#     shop_number_list.extend([''] * number)
#     return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
#            ["Shop Number"] * 3000, ["Shop Number"] * 7000, shop_number_list[0:3000], shop_number_list[3000:10000]


def fast_food():
    # Confirmation number NumbersOnly 4,8wei
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Fastfood","NumbersOnly","Confirmation number",RULE_DICT['fast_food Confirmation number'])
    # order number NumbersOnly 16 digits 1.12202E+15    1122020000000000.0 格式为日、月、年+随机8位
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Fastfood","NumbersOnly","order number",RULE_DICT['fast_food order number'])
    # Shop Number   NumbersAndLetters   4 digits    格式为1个字母+3个数字
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Fastfood","NumbersAndLetters","Shop Number",RULE_DICT['fast_food Shop Number'])

    domain_list1 = domain1_1 + domain2_1 + domain3_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2
    text_list1 = text1_1 + text2_1 + text3_1
    text_list2 = text1_2 + text2_2 + text3_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Expiry date of bank card NumbersOnly   4 digits
# def finance_expiry_date():
#     expiry_date = []
#     # while len(expiry_date) < 10000:
#     for i in range(0, 11000):
#         # rule =r'^(19\d{2}|20\d{2})(0[1-9]|1[0-2])$'
#         # rule = r'^(0[1-9]|1[0-2])\d{2}$'
#         random_str = exrex.getone(RULE_DICT['finance Expiry date of bank card'])
#         expiry_date.append(random_str)
#         expiry_date = list(set(expiry_date))
#     number = 10001 - len(expiry_date)
#     expiry_date.extend([''] * number)
#     # print(id_number_list)
#     return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
#         "Expiry date of bank card"] * 3000, ["Expiry date of bank card"] * 7000, \
#            expiry_date[0:3000], expiry_date[3000:10000]


def finance():
    # Stock number 7-8 digits  LettersOnly   Call1800 格式为3-4个字母+4个数字
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Finance","NumbersAndLetters","Stock number",RULE_DICT['finance Stock number'])
    # Company tax Number  NumbersAndLetters     11 digits   IT12345678901 格式为2个字母+9个数字
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Finance","NumbersAndLetters","Company tax Number",RULE_DICT['finance Company tax Number1'])
    # Company tax Number  LettersOnly 8-20
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Finance","LettersOnly","Company tax Number",RULE_DICT['finance Company tax Number2'])
    # Bank card number NumbersOnly   16 digits  1234 1234 1234 1234
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("Finance","NumbersOnly","Bank card number",RULE_DICT['finance Bank card number'])
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = get_data("Finance","NumbersOnly","Expiry date of bank card",RULE_DICT['finance Expiry date of bank card'])
    # Contract Number  NumbersAndLetters     4-20 digits   IT302930
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = get_data("Finance","NumbersAndLetters","Contract Number",RULE_DICT['finance Contract Number'])
    # Bank account number    NumbersOnly   12 digits  123456 如果后面的位数不足，则前面必须填零
    domain7_1, domain7_2, UtteranceType7_1, UtteranceType7_2, Category7_1, Category7_2, text7_1, text7_2 = get_data("Finance","NumbersOnly","Bank account number",RULE_DICT['finance Bank account number'])

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1 + domain6_1 + domain7_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2 + domain6_2 + domain7_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 +UtteranceType5_1 + UtteranceType6_1 + UtteranceType7_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 +UtteranceType5_2 + UtteranceType6_2 + UtteranceType7_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1 + Category6_1 + Category7_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2 + Category6_2 + Category7_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1 + text6_1 + text7_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2 + text6_2 + text7_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Date of production  8 digits NumbersOnly  日、月、年
# def healthcare_date_product():
#     date_product = []
#     while len(date_product) < 10000:
#         # 出生年月日
#         # rule = r'^((0[1-9])|((1|2)[0-9])|30|31)'
#         # day = exrex.getone(rule)
#         # rule1 = r'^(0[1-9]|1[0-2])'
#         # month = exrex.getone(rule1)
#         # rule2 = r'^(19\d{2}|20\d{2})'
#         # rule = r'^((0[1-9])|((1|2)[0-9])|30|31)(0[1-9]|1[0-2])(19\d{2}|20\d{2})$'
#         random_num = exrex.getone(RULE_DICT["healthcare Date of production"])
#         # random_num = f'{day}.{month}.{year}'
#         date_product.append(random_num)
#         date_product = list(set(date_product))
#     number = 10001 - len(date_product)
#     date_product.extend([''] * number)
#     # print(date_product_list)
#     return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
#         "Date of production"] * 3000, ["Date of production"] * 7000, date_product[0:3000], date_product[3000:10000]


def healthcare():
    # Date of production  8 digits NumbersOnly  日、月、年
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("HealthCare", "NumbersOnly", "Date of production", RULE_DICT["healthcare Date of production"])
    # Email Address LettersOnly abc@gmail.com
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("HealthCare", "LettersOnly", "Email Address", RULE_DICT["healthcare Email Address"])
    # Telephone Number  格式为0+9位     295732039       10digits
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("HealthCare", "NumbersOnly", "Telephone Number", RULE_DICT["healthcare Telephone Number"])

    domain_list1 = domain1_1 + domain2_1 + domain3_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2
    text_list1 = text1_1 + text2_1 + text3_1
    text_list2 = text1_2 + text2_2 + text3_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


def insurance():
    # rule1 = r'^[A-Z]{2}\d{7}$'
    # rule2 = r'^[A-Z]{2}\d{5}[A-Z]{2}$'
    # rule3 = r'^[A-Z]{2}\d{3}[A-Z]{2}$'
    # rule4 = r'^[A-Z]{6}\d{2}[J|F|M|A|S|O|N|D]((0?[1-9])|((1|2)[0-9])|30|31)[A-Z]{1}\d{3}[A-Z]{1}$'
    # Passport Number   NumbersAndLetters  9 digits YA2672719       格式为2个字母+7个数字
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Insurance","NumbersAndLetters","Passport Number",RULE_DICT['insurance Passport Number'])
    # identity card 9 NumbersAndLetters  #2个字母、5个数字和2个字母
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Insurance","NumbersAndLetters","identity card",RULE_DICT['insurance identity card'])
    # License plate number   NumbersAndLetters  7 digits 2个字母+3个数字+2个字母
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Insurance","NumbersAndLetters","License plate number",RULE_DICT['insurance License plate number'])
    # Personal identification number   NumbersAndLetters  16 digits RSSMRA70A01L726S 首字母（RSSMRA）出生年份（70）出生城镇（A01L）复选标记（726S）
    # 缩写6个字母，出生年份（00-99），1个字母出生月份（J、F、M、A、S、O、N、D），2个数字表示出生日期（01-31），1字母和3个数字表示生日，1个数字表示控制代码
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("Insurance","NumbersAndLetters","Personal identification number/Codice fiscale",RULE_DICT['insurance Personal identification number/Codice fiscale'])

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2
    text_list1 = text1_1 + text2_1+text3_1 + text4_1
    text_list2 = text1_2 + text2_2+text3_2 + text4_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


def mediaInternetTelecom():
    # rule1 = r'^\d{19}$'
    # rule2 = r'^\d{4,20}$'
    # # rule3 = r'^[1-9]{3,19}G$'
    # rule3 = r'^\d{4,20}$'
    # rule4 = r'^\d{4}-\d{1,16}$'
    # # rule6 = r'^[A-Za-z]{4,10}@gmail\.com$'
    # rule5 = r'^[A-Za-z0-9]{4,9}(@gmail\.com|@outlook\.it|@outlook\.com|@live\.it|@hotmail\.com)$'
    # rule6 = r'^[a-z]{4,20}$'
    # rule7 = r'^\d{4,20}$'
    # rule8 = r'^[A-Za-z0-9]{4,20}$'
    # rule9 = r'^\d{4,20}$'
    # rule10 = r'^\d{4,20}$'
    # # rule13 = r'^0\d{9}$'
    # rule11 = r'^[A-Za-z0-9]{4,20}$'
    # Order No. 19 digits  NumbersOnly   307******
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("MediaInternetTelecom","NumbersOnly","Order No.",RULE_DICT['mediaInternetTelecom Order No.'])
    # Refund Number  NumbersOnly     4-20 digits
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("MediaInternetTelecom","NumbersOnly","Refund Number",RULE_DICT['mediaInternetTelecom Refund Number'])
    #   Broadband number NumbersOnly 4-20 241010000000.0
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("MediaInternetTelecom","NumbersOnly","Broadband number",RULE_DICT['mediaInternetTelecom Broadband number'])
    # Wide band type    NumbersOnly 4-20 8316-555
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("MediaInternetTelecom","NumbersOnly","Wide band type",RULE_DICT['mediaInternetTelecom Wide band type'])
    # Email Address NumbersAndLetters abc@gmail.com
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = get_data("MediaInternetTelecom","NumbersAndLetters","Email Address",RULE_DICT['mediaInternetTelecom Email Address'])
    # password      LettersOnly  4-20 digits    ytrf
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = get_data("MediaInternetTelecom","LettersOnly","password",RULE_DICT['mediaInternetTelecom password1'])
    # password      NumbersOnly  4-20 digits    1923
    domain7_1, domain7_2, UtteranceType7_1, UtteranceType7_2, Category7_1, Category7_2, text7_1, text7_2 = get_data("MediaInternetTelecom","NumbersOnly","password",RULE_DICT['mediaInternetTelecom password2'])
    # password      NumbersAndLetters  4-20 digits    ytrf
    domain8_1, domain8_2, UtteranceType8_1, UtteranceType8_2, Category8_1, Category8_2, text8_1, text8_2 = get_data("MediaInternetTelecom","NumbersAndLetters","password",RULE_DICT['mediaInternetTelecom password3'])
    # Verification code      NumbersOnly  4-20 digits    192399
    domain9_1, domain9_2, UtteranceType9_1, UtteranceType9_2, Category9_1, Category9_2, text9_1, text9_2 = get_data("MediaInternetTelecom","NumbersOnly","Verification code",RULE_DICT['mediaInternetTelecom Verification code'])
    # Sales/Collection     NumbersOnly  4-20 digits
    domain10_1, domain10_2, UtteranceType10_1, UtteranceType10_2, Category10_1, Category10_2, text10_1, text10_2 = get_data("MediaInternetTelecom","NumbersOnly","Sales/Collection",RULE_DICT['mediaInternetTelecom Sales/Collection'])
    # Online account name? NumbersAndLetters    4-20 digits     as20201908
    domain11_1, domain11_2, UtteranceType11_1, UtteranceType11_2, Category11_1, Category11_2, text11_1, text11_2 = get_data("MediaInternetTelecom","NumbersAndLetters","Online account name",RULE_DICT['mediaInternetTelecom Online account name'])

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1 + domain6_1 + domain7_1 + domain8_1 + domain9_1 + domain10_1 + domain11_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2 + domain6_2 + domain7_2 + domain8_2 + domain9_2 + domain10_2 + domain11_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 + UtteranceType5_1 + UtteranceType6_1 + UtteranceType7_1 + UtteranceType8_1 \
                          + UtteranceType9_1 + UtteranceType10_1 + UtteranceType11_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 + UtteranceType5_2 + UtteranceType6_2 + UtteranceType7_2 + UtteranceType8_2 \
                          + UtteranceType9_2 + UtteranceType10_2 + UtteranceType11_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1 + Category6_1 + Category7_1 + Category8_1 + Category9_1 \
                     + Category10_1 + Category11_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2 + Category6_2 + Category7_2 + Category8_2 + Category9_2 \
                     + Category10_2 + Category11_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1 + text6_1 + text7_1 + text8_1 + text9_1 + text10_1 + text11_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2 + text6_2 + text7_2 + text8_2 + text9_2 + text10_2 + text11_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


def retail():
    # rule1 = r'^((0[1-9])|((1|2)[0-9])|30|31)(0[1-9]|1[0-2])(19\d{2}|20\d{2})\d{8}$'
    # rule2 = r'^\d{12}$'
    # rule3 = r'^[A-Z]{2}\d{3}[A-Z]{2}$'
    # rule4 = r'^[A-Z0-9]{17}$'
    # rule5 = r'^\d{8,20}$'
    # Order Number   NumbersOnly      16 digits 1122020000000000.0 格式为日、月、年+随机8位格式为日、月、年+随机8位（取决于公司或供应商，可能是17位）
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Retail","NumbersOnly","Order Number",RULE_DICT['retail Order Number'])
    # Item number?  NumbersOnly   12 digits    字母大写 204877000000.0
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Retail","NumbersOnly","Item number",RULE_DICT['retail Item number'])
    # models NumbersAndLetters   4-20 digits    CAF7230A 2个字母、3个数字和2个字母，例如：BL751CD
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Retail","NumbersAndLetters","models",RULE_DICT['retail models'])
    # VIN code        NumbersAndLetters   17 digits    LFV2A2*********
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("Retail","NumbersAndLetters","VIN code",RULE_DICT['retail VIN code'])
    # The tracking number?  NumbersOnly  12 digits
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = get_data("Retail","NumbersOnly","The tracking number",RULE_DICT['retail The tracking number'])

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 +UtteranceType5_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 +UtteranceType5_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


def travel():
    # rule1 = r'^\d{6}$'
    # rule2 = r'^\d{4,6}$'
    # rule3 = r'^[A-Z]{6}$'
    # rule4 = r'^[A-Z]{4}\d{3}$'
    # Order Number  NumbersOnly 6 digits 438906
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Travel","NumbersOnly","Order Number",RULE_DICT['travel Order Number'])
    # Room number   NumbersOnly 4-6位
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Travel","NumbersOnly","Room Number",RULE_DICT['travel Room Number'])
    # Booking number  LettersOnly  6 digits
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Travel","LettersOnly","Booking Number",RULE_DICT['travel Booking Number1'])
    # Booking number   NumbersAndLetters  7位 格式为4个字母+3个数字，随机
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("Travel","NumbersAndLetters","Booking Number",RULE_DICT['travel Booking Number2'])

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


def main():
    aviation_domain_list1, aviation_domain_list2, aviation_UtteranceType_list1, aviation_UtteranceType_list2, aviation_Category_list1, \
    aviation_Category_list2, aviation_text_list1, aviation_text_list2 = airline()
    food_domain_list1, food_domain_list2, food_UtteranceType_list1, food_UtteranceType_list2, food_Category_list1, food_Category_list2, \
    food_text_list1, food_text_list2 = fast_food()
    finance_domain_list1, finance_domain_list2, finance_UtteranceType_list1, finance_UtteranceType_list2, finance_Category_list1, \
    finance_Category_list2, finance_text_list1, finance_text_list2 = finance()
    health_domain_list1, health_domain_list2, health_UtteranceType_list1, health_UtteranceType_list2, health_Category_list1, \
    health_Category_list2, health_text_list1, health_text_list2 = healthcare()
    insurance_domain_list1, insurance_domain_list2, insurance_UtteranceType_list1, insurance_UtteranceType_list2, insurance_Category_list1, \
    insurance_Category_list2, insurance_text_list1, insurance_text_list2 = insurance()
    medial_domain_list1, medial_domain_list2, medial_UtteranceType_list1, medial_UtteranceType_list2, medial_Category_list1, \
    medial_Category_list2, medial_text_list1, medial_text_list2 = mediaInternetTelecom()
    retail_domain_list1, retail_domain_list2, retail_UtteranceType_list1, retail_UtteranceType_list2, retail_Category_list1, \
    retail_Category_list2, retail_text_list1, retail_text_list2 = retail()
    travel_domain_list1, travel_domain_list2, travel_UtteranceType_list1, travel_UtteranceType_list2, travel_Category_list1, \
    travel_Category_list2, travel_text_list1, travel_text_list2 = travel()

    domain_list1 = aviation_domain_list1 + food_domain_list1+finance_domain_list1+health_domain_list1+insurance_domain_list1+medial_domain_list1+retail_domain_list1+travel_domain_list1
    UtteranceType_list1 = aviation_UtteranceType_list1 + food_UtteranceType_list1+finance_UtteranceType_list1+health_UtteranceType_list1+insurance_UtteranceType_list1+medial_UtteranceType_list1+retail_UtteranceType_list1+travel_UtteranceType_list1
    Category_list1 = aviation_Category_list1 + food_Category_list1+finance_Category_list1+health_Category_list1+insurance_Category_list1+medial_Category_list1+retail_Category_list1+travel_Category_list1
    text_list1 = aviation_text_list1 + food_text_list1+finance_text_list1+health_text_list1+insurance_text_list1+medial_text_list1+retail_text_list1+travel_text_list1

    domain_list2 = aviation_domain_list2 + food_domain_list2+finance_domain_list2+health_domain_list2+insurance_domain_list2+medial_domain_list2+retail_domain_list2+travel_domain_list2
    UtteranceType_list2 = aviation_UtteranceType_list2 + food_UtteranceType_list2+finance_UtteranceType_list2+health_UtteranceType_list2+insurance_UtteranceType_list2+medial_UtteranceType_list2+retail_UtteranceType_list2+travel_UtteranceType_list2
    Category_list2 = aviation_Category_list2 + food_Category_list2+finance_Category_list2+health_Category_list2+insurance_Category_list2+medial_Category_list2+retail_Category_list2+travel_Category_list2
    text_list2 = aviation_text_list2 + food_text_list2+finance_text_list2+health_text_list2+insurance_text_list2+medial_text_list2+retail_text_list2+travel_text_list2
    # print(text_list2)
    df1 = pd.DataFrame(
        {'Domain': domain_list1, "UtteranceType": UtteranceType_list1, "Category": Category_list1, "Text": text_list1})
    df1.to_csv("MCE_3000_data.csv", index=False, sep=',', encoding='utf-8-sig')
    df2 = pd.DataFrame(
        {'Domain': domain_list2, "UtteranceType": UtteranceType_list2, "Category": Category_list2, "Text": text_list2})
    df2.to_csv("MCE_7000_data.csv", index=False, sep=',', encoding='utf-8-sig')


if __name__ == '__main__':
    main()
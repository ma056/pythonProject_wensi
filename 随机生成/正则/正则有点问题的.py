# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 正则有点问题的.py
@Author : wenjing
@Date : 2022/12/14 14:12
"""
import exrex
import pandas as pd


def get_data(d_type, u_type, c_type, rule):
    random_list = []
    while len(random_list) < 10000:
        # rule = r'^[A-Z]{7,10}|[A-Z]{4,5}$'
        random_str = exrex.getone(rule)
        random_list.append(random_str)
        random_list = list(set(random_list))
    return [d_type] * 3000, [d_type] * 7000, [u_type] * 3000, [u_type] * 7000, \
           [c_type] * 3000, [c_type] * 7000, random_list[0:3000], random_list[3000:10000]


# Boarding time  NumbersOnly	 4digits   W7PCYE
def airline_boarding_time():
    boarding_number = []
    # while len(boarding_number) < 10000:
    for i in range(0, 110000):
        rule = r'^[0-9]{4}$'
        num = exrex.getone(rule)
        boarding_number.append(num)
    boarding_number = list(set(boarding_number))
    number = 10000 - len(boarding_number)
    boarding_number.extend([''] * number)
    # print(boarding_number_list)
    return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, \
           ["Boarding time"] * 3000, ["Boarding time"] * 7000, boarding_number[0:3000], boarding_number[3000:10000]


def airline():
    rule1 = r'^[A-Z]{7,10}|[A-Z]{4,5}$'
    rule2 = r'^\d{4,5}|\d{7,10}$'
    rule3 = r'^[A-Z]{2}\d{4}$'
    rule4 = r'^[A-Za-z0-9]{6}$'
    # Telephone number/train number     LettersOnly     4-5 digits /7-10 digits
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Airline","LettersOnly","Telephone number/train number",rule1)
    # Telephone number/train number     NumbersOnly     4-5 digits /7-10 digits
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Airline","NumbersOnly","Telephone number/train number",rule2)
    # Flight number  NumbersAndLetters	 6 digits   格式为2个字母+4个数字
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Airline","NumbersAndLetters","Flight number",rule3)
    # order number  NumbersAndLetters	 6 digits   W7PCYE
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("Airline","NumbersAndLetters","order number",rule4)
    # Boarding time  NumbersOnly	 4digits   W7PCYE
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = airline_boarding_time()

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 + UtteranceType5_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 + UtteranceType5_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


def fast_confirmation_number():
    confirmation_number = []
    # while len(confirmation_number) < 10000:
    for i in range(0, 110000):
        rule = r'^[0-9]{4}$'
        phone_number_str = exrex.getone(rule)
        confirmation_number.append(phone_number_str)
    confirmation_number = list(set(confirmation_number))
    number = 10001 - len(confirmation_number)
    confirmation_number.extend([''] * number)
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Confirmation number"] * 3000, ["Confirmation number"] * 7000, confirmation_number[0:3000], \
           confirmation_number[3000:10000]


def fast_food():
    rule = r'^(19\d{2}|20\d{2})(0[1-9]|1[0-2])((0?[1-9])|((1|2)[0-9])|30|31)\d{8}$'
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = fast_confirmation_number()
    # order number NumbersOnly 16 digits 1.12202E+15    1122020000000000.0 格式为日、月、年+随机8位
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Fastfood","NumbersOnly","order number",rule)

    domain_list1 = domain1_1 + domain2_1
    domain_list2 = domain1_2 + domain2_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2
    Category_list1 = Category1_1 + Category2_1
    Category_list2 = Category1_2 + Category2_2
    text_list1 = text1_1 + text2_1
    text_list2 = text1_2 + text2_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Expiry date of bank card NumbersOnly   4 digits
def finance_expiry_date():
    expiry_date = []
    # while len(expiry_date) < 10000:
    for i in range(0, 10000):
        rule =r'^(19\d{2}|20\d{2})(0[1-9]|1[0-2])'
        random_str = exrex.getone(rule)
        expiry_date.append(random_str)
        expiry_date = list(set(expiry_date))
    number = 10001 - len(expiry_date)
    expiry_date.extend([''] * number)
    # print(id_number_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Expiry date of bank card"] * 3000, ["Expiry date of bank card"] * 7000, \
           expiry_date[0:3000], expiry_date[3000:10000]


def finance():
    rule1 = r'[A-Z][A-Za-z]{2,3}\d{4}$'
    rule2 = r'[A-Z]{2}\d{9}$'
    rule3 = r'\d{16}$'
    rule5 = r'[A-Z]{2}\d{2,18}$'
    rule6 = r'\d{12}$'
    # Stock number 7-8 digits  LettersOnly   Call1800 格式为3-4个字母+4个数字
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Finance","LettersOnly","Stock number",rule1)
    # Company tax Number  NumbersAndLetters     11 digits   IT12345678901 格式为2个字母+9个数字
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Finance","NumbersAndLetters","Company tax Number",rule2)
    # Bank card number NumbersOnly   16 digits  1234 1234 1234 1234
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Finance","NumbersOnly","Bank card number",rule3)
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = finance_expiry_date()
    # Contract Number  NumbersAndLetters     4-20 digits   IT302930
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = get_data("Finance","NumbersAndLetters","Contract Number",rule5)
    # Bank account number    NumbersOnly   12 digits  123456 如果后面的位数不足，则前面必须填零
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = get_data("Finance","NumbersOnly","Bank account number",rule6)

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1 + domain6_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2 + domain6_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 +UtteranceType5_1 + UtteranceType6_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 +UtteranceType5_2 + UtteranceType6_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1 + Category6_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2 + Category6_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1 + text6_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2 + text6_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


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
    while len(date_product) < 10000:
        # 出生年月日
        rule = r'^((0[1-9])|((1|2)[0-9])|30|31)'
        day = exrex.getone(rule)
        rule1 = r'^(0[1-9]|1[0-2])'
        month = exrex.getone(rule1)
        rule2 = r'^(19\d{2}|20\d{2})'
        year = exrex.getone(rule2)
        random_num = f'{day}.{month}.{year}'
        date_product.append(random_num)
        date_product = list(set(date_product))
    number = 10001 - len(date_product)
    date_product.extend([''] * number)
    # print(date_product_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Date of production"] * 3000, ["Date of production"] * 7000, date_product[0:3000], date_product[3000:10000]


def insurance():
    rule1 = r'^[A-Z]{2}\d{7}$'
    rule2 = r'^[A-Z]{2}\d{3}[A-Z]{2}$'
    rule3 = r'^[A-Z]{6}\d{2}[A-Z]{1}\d{2}[A-Z]{1}\d{3}[A-Z]{1}$'
    # Passport Number   NumbersAndLetters  9 digits YA2672719       格式为2个字母+7个数字
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Insurance","NumbersAndLetters","Passport Number",rule1)
    # License plate number   NumbersAndLetters  7 digits 2个字母+3个数字+2个字母
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Insurance","NumbersAndLetters","License plate number",rule2)
    # Personal identification number   NumbersAndLetters  16 digits RSSMRA70A01L726S 首字母（RSSMRA）出生年份（70）出生城镇（A01L）复选标记（726S）
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Insurance","NumbersAndLetters","Personal identification number",rule3)

    domain_list1 = domain1_1 + domain2_1 +domain3_1
    domain_list2 = domain1_2 + domain2_2+domain3_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1+UtteranceType3_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2+UtteranceType3_2
    Category_list1 = Category1_1 + Category2_1+Category3_1
    Category_list2 = Category1_2 + Category2_2+Category3_2
    text_list1 = text1_1 + text2_1+text3_1
    text_list2 = text1_2 + text2_2+text3_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


def mediaInternetTelecom():
    rule1 = r'^\d{19}$'
    rule2 = r'^\d{4,20}$'
    rule3 = r'^[1-9]{3,19}G$'
    rule4 = r'^\d{4,20}$'
    rule5 = r'^\d{4}-\d{1,16}$'
    rule6 = r'^[A-Za-z]{4,10}@gmail\.com$'
    rule7 = r'^[A-Za-z0-9]{4,10}@gmail\.com$'
    rule8 = r'^[a-z]{4,20}$'
    rule9 = r'^\d{4,20}$'
    rule10 = r'^[A-Za-z0-9]{4,20}$'
    rule11 = r'^\d{4,20}$'
    rule12 = r'^\d{4,20}$'
    rule13 = r'^0\d{9}$'
    rule14 = r'^[A-Za-z0-9]{4,20}$'
    # Order No. 19 digits  NumbersOnly   307******
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("MediaInternetTelecom","NumbersOnly","Order No.",rule1)
    # Refund Number  NumbersOnly     4-20 digits
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("MediaInternetTelecom","NumbersOnly","Refund Number",rule2)
    # Residual flow rate   NumbersAndLetters 4-20
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("MediaInternetTelecom","NumbersAndLetters","Residual flow rate",rule3)
    #   Broadband number NumbersOnly 4-20 241010000000.0
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("MediaInternetTelecom","NumbersOnly","Broadband number",rule4)
    # Wide band type    NumbersOnly 4-20 8316-555
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = get_data("MediaInternetTelecom","NumbersOnly","Wide band type",rule5)
    # Email Address LettersOnly abc@gmail.com
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = get_data("MediaInternetTelecom","LettersOnly","Email Address",rule6)
    # Email Address LettersOnly abc@gmail.com
    domain7_1, domain7_2, UtteranceType7_1, UtteranceType7_2, Category7_1, Category7_2, text7_1, text7_2 = get_data("MediaInternetTelecom","NumbersAndLetters","Email Address",rule7)
    # password      LettersOnly  4-20 digits    ytrf
    domain8_1, domain8_2, UtteranceType8_1, UtteranceType8_2, Category8_1, Category8_2, text8_1, text8_2 = get_data("MediaInternetTelecom","LettersOnly","password",rule8)
    # password      NumbersOnly  4-20 digits    1923
    domain9_1, domain9_2, UtteranceType9_1, UtteranceType9_2, Category9_1, Category9_2, text9_1, text9_2 = get_data("MediaInternetTelecom","NumbersOnly","password",rule9)
    # password      NumbersAndLetters  4-20 digits    ytrf
    domain10_1, domain10_2, UtteranceType10_1, UtteranceType10_2, Category10_1, Category10_2, text10_1, text10_2 = get_data("MediaInternetTelecom","NumbersAndLetters","password",rule10)
    # Verification code      NumbersOnly  4-20 digits    192399
    domain11_1, domain11_2, UtteranceType11_1, UtteranceType11_2, Category11_1, Category11_2, text11_1, text11_2 = get_data("MediaInternetTelecom","NumbersOnly","Verification code",rule11)
    # Sales/Collection     NumbersOnly  4-20 digits
    domain12_1, domain12_2, UtteranceType12_1, UtteranceType12_2, Category12_1, Category12_2, text12_1, text12_2 = get_data("MediaInternetTelecom","NumbersOnly","Sales/Collection",rule12)
    # Telephone Number  格式为0+9位     295732039       10digits
    domain13_1, domain13_2, UtteranceType13_1, UtteranceType13_2, Category13_1, Category13_2, text13_1, text13_2 = get_data("MediaInternetTelecom","NumbersOnly","Telephone Number",rule13)
    # Online account name? NumbersAndLetters    4-20 digits     as20201908
    domain14_1, domain14_2, UtteranceType14_1, UtteranceType14_2, Category14_1, Category14_2, text14_1, text14_2 = get_data("MediaInternetTelecom","NumbersAndLetters","Online account name?",rule14)

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1 + domain6_1 + domain7_1 + domain8_1 + domain9_1 + domain10_1 + domain11_1 + domain12_1 + domain13_1 + domain14_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2 + domain6_2 + domain7_2 + domain8_2 + domain9_2 + domain10_2 + domain11_2 + domain12_2 + domain13_2 + domain14_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 + UtteranceType5_1 + UtteranceType6_1 + UtteranceType7_1 + UtteranceType8_1 \
                          + UtteranceType9_1 + UtteranceType10_1 + UtteranceType11_1 + UtteranceType12_1 + UtteranceType13_1 + UtteranceType14_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 + UtteranceType5_2 + UtteranceType6_2 + UtteranceType7_2 + UtteranceType8_2 \
                          + UtteranceType9_2 + UtteranceType10_2 + UtteranceType11_2 + UtteranceType12_2 + UtteranceType13_2 + UtteranceType14_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1 + Category6_1 + Category7_1 + Category8_1 + Category9_1 \
                     + Category10_1 + Category11_1 + Category12_1 + Category13_1 + Category14_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2 + Category6_2 + Category7_2 + Category8_2 + Category9_2 \
                     + Category10_2 + Category11_2 + Category12_2 + Category13_2 + Category14_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1 + text6_1 + text7_1 + text8_1 + text9_1 + text10_1 \
                 + text11_1 + text12_1 + text13_1 + text14_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2 + text6_2 + text7_2 + text8_2 + text9_2 + text10_2 \
                 + text11_2 + text12_2 + text13_2 + text14_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Shop Number   NumbersAndLetters   4 digits    格式为1个字母+3个数字
def retail_shop_number():
    shop_number = []
    for i in range(0, 11000):
        rule = r'^[A-Za-z]{1}\d{3}$'
        random_str = exrex.getone(rule)
        shop_number.append(random_str)
    shop_number_list = list(set(shop_number))
    number = 10001 - len(shop_number_list)
    shop_number_list.extend([''] * number)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
           ["Shop Number"] * 3000, ["Shop Number"] * 7000, shop_number_list[0:3000], shop_number_list[3000:10000]


def retail():
    rule2 = r'^((0?[1-9])|((1|2)[0-9])|30|31)(0[1-9]|1[0-2])(19\d{2}|20\d{2})\d{8}'
    rule3 = r'\d{12}$'
    rule4 = r'^[A-Z0-9]{4,20}$'
    rule5 = r'^[A-Z0-9]{17}$'
    rule6 = r'\d{12}$'
    # Shop Number   NumbersAndLetters   4 digits    格式为1个字母+3个数字
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = retail_shop_number()
    # Order Number   NumbersOnly      16 digits 1122020000000000.0 格式为日、月、年+随机8位
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Retail","NumbersOnly","Order Number",rule2)
    # Item number?  NumbersOnly   12 digits    字母大写 204877000000.0
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Retail","NumbersOnly","Item number?",rule3)
    # models NumbersAndLetters   4-20 digits    CAF7230A
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("Retail","NumbersAndLetters","models",rule4)
    # VIN code        NumbersAndLetters   17 digits    LFV2A2*********
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = get_data("Retail","NumbersAndLetters","VIN code",rule5)
    # The tracking number?  NumbersOnly  12 digits
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = get_data("Retail","NumbersOnly","The tracking number?",rule6)

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1+domain6_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2+domain6_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 +UtteranceType5_1+UtteranceType6_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 +UtteranceType5_2+UtteranceType6_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1+Category6_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2+Category6_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1+text6_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2+text6_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Country of destination   LettersOnly 5-10 digits
def travel_country():
    country = []
    with open("H:/Wenjing/country.txt", 'r', encoding='utf-8') as file:
    # with open("country.txt", 'r', encoding='utf-8') as file:
        content = file.readlines()
        for i in content:
            country.append(i.replace('\n', ''))
    number = 10001 - len(country)
    country.extend([''] * number)
    # print(country)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["LettersOnly"] * 3000, ["LettersOnly"] * 7000, [
        "Country of destination"] * 3000, ["Country of destination"] * 7000, country[0:3000], country[3000:10000]


# City of Destination  LettersOnly  5-10 digits
def travel_city():
    city = []
    with open("H:/Wenjing/city.txt", 'r', encoding='utf-8') as file:
        content = file.readlines()
        for i in content:
            city.append(i.replace('\n', ''))
    number = 10001 - len(city)
    city.extend([''] * number)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["LettersOnly"] * 3000, ["LettersOnly"] * 7000, \
           ["City of Destination"] * 3000, ["City of Destination"] * 7000, city[0:3000], city[3000:10000]


# Room number   NumbersOnly 4位
def travel_room_num():
    room_num = []
    # while len(room_num) < 10000:
    for i in range(0, 11000):
        rule = r'\d{4}$'
        random_num = exrex.getone(rule)
        room_num.append(random_num)
    room_num_list = list(set(room_num))
    number = 10001 - len(room_num_list)
    room_num_list.extend([''] * number)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, \
           ["Room number"] * 3000, ["Room number"] * 7000, room_num_list[0:3000], room_num_list[3000:10000]


def travel():
    rule2 = r'\d{6}$'
    # Country of destination   LettersOnly 5-10 digits
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = travel_country()
    # Order Number  NumbersOnly 6 digits 438906
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Travel","NumbersOnly","Order Number",rule2)
    # City of Destination  LettersOnly  5-10 digits
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = travel_city()
    # Room number   NumbersOnly 4位
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = travel_room_num()

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
    df1.to_csv("3000_data.csv", index=False, sep=',', encoding='utf-8-sig')
    df2 = pd.DataFrame(
        {'Domain': domain_list2, "UtteranceType": UtteranceType_list2, "Category": Category_list2, "Text": text_list2})
    df2.to_csv("7000_data.csv", index=False, sep=',', encoding='utf-8-sig')


if __name__ == '__main__':
    main()
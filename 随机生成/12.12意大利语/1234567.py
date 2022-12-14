# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : Airline.py
@Author : wenjing
@Date : 2022/12/12 9:41
"""
import random
import string
import pandas as pd


# 航空
def airline():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = airline_tel_train_number()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = airline_tel_train_number1()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = airline_flight_number()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = airline_order_number()
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


# Telephone number/train number     LettersOnly     4-5 digits /7-10 digits
def airline_tel_train_number():
    tel_train_number = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_uppercase, 4))
        num2 = ''.join(random.sample(string.ascii_uppercase, 5))
        num3 = ''.join(random.sample(string.ascii_uppercase, 7))
        num4 = ''.join(random.sample(string.ascii_uppercase, 8))
        num5 = ''.join(random.sample(string.ascii_uppercase, 9))
        num6 = ''.join(random.sample(string.ascii_uppercase, 10))
        tel_train_number.append(num1)
        tel_train_number.append(num2)
        tel_train_number.append(num3)
        tel_train_number.append(num4)
        tel_train_number.append(num5)
        tel_train_number.append(num6)

    tel_train_number_list = list(set(tel_train_number))
    # print(order_no_list)
    return ["Airline"] * 3000, ["Airline"] * 7000, ["LettersOnly"] * 3000, ["LettersOnly"] * 7000, [
        "Telephone number/train number"] * 3000, \
           ["Telephone number/train number"] * 7000, tel_train_number_list[0:3000], tel_train_number_list[3001:10001]


# Telephone number/train number     NumbersOnly     4-5 digits /7-10 digits
def airline_tel_train_number1():
    tel_train_number1 = []
    for i in range(0, 11000):
        num1 = str(random.randint(1000, 9999))
        num2 = str(random.randint(10000, 99999))
        num3 = str(random.randint(1000000, 9999999))
        num4 = str(random.randint(10000000, 99999999))
        num5 = str(random.randint(100000000, 999999999))
        num6 = str(random.randint(1000000000, 9999999999))
        tel_train_number1.append(num1)
        tel_train_number1.append(num2)
        tel_train_number1.append(num3)
        tel_train_number1.append(num4)
        tel_train_number1.append(num5)
        tel_train_number1.append(num6)

    tel_train_number_list1 = list(set(tel_train_number1))
    # print(order_no_list)
    return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Telephone number/train number"] * 3000, ["Telephone number/train number"] * 7000, tel_train_number_list1[
         0:3000], tel_train_number_list1[3001:10001]


# Flight number  NumbersAndLetters	 6 digits   格式为2个字母+4个数字
def airline_flight_number():
    flight_number = []
    for i in range(0, 11000):
        num = ''.join(random.sample(string.ascii_uppercase, 2))
        num1 = str(random.randint(1000, 9999))
        random_num = f'{num}{num1}'
        flight_number.append(random_num)
    flight_number_list = list(set(flight_number))
    return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "Flight number"] * 3000, ["Flight number"] * 7000, flight_number_list[0:3000], flight_number_list[3001:10001]


# order number  NumbersAndLetters	 6 digits   W7PCYE
def airline_order_number():
    order_number = []
    for i in range(0, 11000):
        num1 = random.choice(string.ascii_uppercase)
        num2 = str(random.randint(0, 9))
        num3 = ''.join(random.sample(string.ascii_uppercase, 4))
        random_num = f'{num1}{num2}{num3}'
        order_number.append(random_num)
    order_number_list = list(set(order_number))
    return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "order number"] * 3000, ["order number"] * 7000, order_number_list[0:3000], order_number_list[3001:10001]


# Boarding time  NumbersOnly	 4digits   W7PCYE
def airline_boarding_time():
    boarding_number = []
    for i in range(0, 110000):
        num = str(random.randint(0, 9999)).zfill(4)
        boarding_number.append(num)
    boarding_number_list = list(set(boarding_number))
    number = 10000 - len(boarding_number_list)
    boarding_number_list.extend([''] * number)
    # print(boarding_number_list)
    return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, ["Boarding time"] * 3000,\
           ["Boarding time"] * 7000, boarding_number_list[0:3000], boarding_number_list[3000:10001]


def fast_food():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = fast_confirmation_number()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = fast_order_num()

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


# Confirmation number  NumbersOnly  4 digits
def fast_confirmation_number():
    confirmation_number = []
    for i in range(0, 110000):
        num = str(random.randint(0, 9999)).zfill(4)
        confirmation_number.append(num)

    confirmation_number_list = list(set(confirmation_number))
    number = 10000 - len(confirmation_number_list)
    confirmation_number_list.extend([''] * number)
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "Confirmation number"] * 3000, ["Confirmation number"] * 7000, confirmation_number_list[0:3000], \
           confirmation_number_list[3000:10001]


# order number NumbersOnly 16 digits 1.12202E+15    1122020000000000.0 格式为日、月、年+随机8位
def fast_order_num():
    order_num = []
    for i in range(0, 12000):
        # 出生年月日
        year = str(random.randint(1940, 2020))
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 29)).zfill(2)
        num1 = str(random.randint(10, 99))
        num2 = str(random.randint(0, 99999999)).zfill(6)
        random_num = f'{num1}{year}{month}{day}{num2}'
        order_num.append(random_num)
    order_num_list = list(set(order_num))
    # print(tel_num_list)
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "order number"] * 3000, ["order number"] * 7000, order_num_list[0:3000], order_num_list[3001:10001]


def finance():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = finance_stock_number()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = finance_company_tax_number()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = finance_bank_card()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = finance_expiry_date()
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = finance_contract_number()
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = finance_bank_account()

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


# Stock number 7-8 digits  LettersOnly   Call1800 格式为3-4个字母+4个数字
def finance_stock_number():
    stock_number = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_letters, 4))
        num1_1 = ''.join(random.sample(string.ascii_letters, 3))
        num2 = str(random.randint(0, 9999)).zfill(4)
        random_num = f'{num1}{num2}'
        random_num1 = f'{num1_1}{num2}'
        stock_number.append(random_num)
        stock_number.append(random_num1)
    stock_number_list = list(set(stock_number))
    # print(stock_number_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["LettersOnly"] * 3000, ["LettersOnly"] * 7000, [
        "Stock number"] * 3000, ["Stock number"] * 7000, stock_number_list[0:3000], stock_number_list[3001:10001]


# Company tax Number  NumbersAndLetters     11 digits   IT12345678901 格式为2个字母+9个数字
def finance_company_tax_number():
    company_tax_number = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_letters, 2))
        num2 = str(random.randint(0, 9999)).zfill(9)
        random_num = f'{num1}{num2}'
        company_tax_number.append(random_num)
    company_tax_number_list = list(set(company_tax_number))
    # print(stock_number_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, ["Company tax Number"] * 3000, \
           ["Company tax Number"] * 7000, company_tax_number_list[0:3000], company_tax_number_list[3001:10001]


# Bank card number NumbersOnly   16 digits  1234 1234 1234 1234
def finance_bank_card():
    bank_card = []
    for i in range(0, 11000):
        num = str(random.randint(1000000000000000, 9999999999999999))
        bank_card.append(num)
    bank_card_list = list(set(bank_card))
    # print(id_number_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Bank card number"] * 3000, ["Bank card number"] * 7000, bank_card_list[0:3000], bank_card_list[3001:10001]


# Expiry date of bank card NumbersOnly   4 digits
def finance_expiry_date():
    expiry_date = []
    for i in range(0, 11000):
        year = str(random.randint(0, 99)).zfill(2)
        month = str(random.randint(1, 12)).zfill(2)
        expiry_date.append(f'{month}/{year}')
    expiry_date_list = list(set(expiry_date))
    number = 10001 - len(expiry_date_list)
    expiry_date_list.extend([''] * number)
    # print(id_number_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Expiry date of bank card"] * 3000, ["Expiry date of bank card"] * 7000, \
           expiry_date_list[0:3000], expiry_date_list[3001:10001]


# Contract Number  NumbersAndLetters     4-20 digits   IT302930
def finance_contract_number():
    contract_number = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_letters, 2))
        num2 = str(random.randint(0, 9999)).zfill(4)
        num2_1 = str(random.randint(0, 9999)).zfill(5)
        num2_2 = str(random.randint(0, 9999)).zfill(6)
        num2_3 = str(random.randint(0, 9999)).zfill(7)
        random_num1 = f'{num1}{num2}'
        random_num2 = f'{num1}{num2_1}'
        random_num3 = f'{num1}{num2_2}'
        random_num4 = f'{num1}{num2_3}'
        contract_number.append(random_num1)
        contract_number.append(random_num2)
        contract_number.append(random_num3)
        contract_number.append(random_num4)
    contract_number_list = list(set(contract_number))
    # print(contract_number_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, ["Contract Number"] * 3000, \
           ["Contract Number"] * 7000, contract_number_list[0:3000], contract_number_list[3001:10001]


# Bank account number    NumbersOnly   12 digits  123456 如果后面的位数不足，则前面必须填零
def finance_bank_account():
    bank_account = []
    for i in range(0, 11000):
        num = str(random.randint(0, 999999999999)).zfill(12)
        bank_account.append(num)
    bank_account_list = list(set(bank_account))
    # print(id_number_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Bank card number"] * 3000, ["Bank card number"] * 7000, bank_account_list[0:3000], bank_account_list[3001:10001]


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
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Passport Number   NumbersAndLetters  9 digits YA2672719       格式为2个字母+7个数字
def insurance_passport_number():
    passport_number = []
    for i in range(0, 110000):
        num1 = ''.join(random.sample(string.ascii_uppercase, 2))
        num2 = str(random.randint(0, 9999999)).zfill(7)
        passport_number.append(f'{num1}{num2}')
    passport_number_list = list(set(passport_number))
    return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
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
    return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
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
    return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "Personal identification number"] * 3000, ["Personal identification number"] * 7000, personal_id_list[0:3000], \
           personal_id_list[3001:10001]


def mediaInternetTelecom():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = media_order_no()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = media_refund_num()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = media_residual_flow()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = media_broadband_num()
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = media_wide_band()
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = media_email_address()
    domain7_1, domain7_2, UtteranceType7_1, UtteranceType7_2, Category7_1, Category7_2, text7_1, text7_2 = media_email_address1()
    domain8_1, domain8_2, UtteranceType8_1, UtteranceType8_2, Category8_1, Category8_2, text8_1, text8_2 = media_psw()
    domain9_1, domain9_2, UtteranceType9_1, UtteranceType9_2, Category9_1, Category9_2, text9_1, text9_2 = media_psw1()
    domain10_1, domain10_2, UtteranceType10_1, UtteranceType10_2, Category10_1, Category10_2, text10_1, text10_2 = media_psw2()
    domain11_1, domain11_2, UtteranceType11_1, UtteranceType11_2, Category11_1, Category11_2, text11_1, text11_2 = media_ver_code()
    domain12_1, domain12_2, UtteranceType12_1, UtteranceType12_2, Category12_1, Category12_2, text12_1, text12_2 = media_sale_collect()
    domain13_1, domain13_2, UtteranceType13_1, UtteranceType13_2, Category13_1, Category13_2, text13_1, text13_2 = media_tel_number()
    domain14_1, domain14_2, UtteranceType14_1, UtteranceType14_2, Category14_1, Category14_2, text14_1, text14_2 = media_online_account()

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


# Order No. 19 digits  NumbersOnly   307******
def media_order_no():
    order_no = []
    for i in range(0, 11000):
        num = str(random.randint(1000000000000000000, 9999999999999999999))
        order_no.append(num)
    order_no_list = list(set(order_no))
    # print(stock_number_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, [
        "NumbersOnly"] * 7000, \
           ["Order No."] * 3000, ["Order No."] * 7000, order_no_list[0:3000], order_no_list[3001:10001]


# Refund Number  NumbersOnly     4-20 digits
def media_refund_num():
    refund_num = []
    for i in range(0, 11000):
        num = str(random.randint(1000, 99999999999999999999))
        refund_num.append(num)
    refund_num_list = list(set(refund_num))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, [
        "NumbersOnly"] * 7000, \
           ["Refund Number"] * 3000, ["Refund Number"] * 7000, refund_num_list[0:3000], refund_num_list[3001:10001]


# Residual flow rate   NumbersAndLetters 4-20
def media_residual_flow():
    residual_flow = []
    for i in range(0, 11000):
        random_num1 = str(random.randint(1000, 99999999999))
        random_num = f'{random_num1}G'
        residual_flow.append(random_num)
    residual_flow_list = list(set(residual_flow))
    # print(residual_flow_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersAndLetters"] * 3000, [
        "NumbersAndLetters"] * 7000, ["Residual flow rate"] * 3000, ["Residual flow rate"] * 7000, \
           residual_flow_list[0:3000], residual_flow_list[ 3001:10001]


#   Broadband number NumbersOnly 4-20 241010000000.0
def media_broadband_num():
    broadband_num = []
    for i in range(0, 11000):
        num = str(random.randint(1000, 99999999999999999999))
        broadband_num.append(num)
    broadband_num_list = list(set(broadband_num))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, \
           ["NumbersOnly"] * 7000, ["Broadband number"] * 3000, ["Broadband number"] * 7000,\
           broadband_num_list[0:3000], broadband_num_list[3001:10001]


# Wide band type    NumbersOnly 4-20 8316-555
def media_wide_band():
    wide_band = []
    for i in range(0, 11000):
        num = str(random.randint(1000, 9999))
        num1 = str(random.randint(0, 999)).zfill(3)
        wide_band.append(f'{num}-{num1}')
    wide_band_list = list(set(wide_band))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, [
        "NumbersOnly"] * 7000, \
           ["Wide band type"] * 3000, ["Wide band type"] * 7000, wide_band_list[0:3000], wide_band_list[3001:10001]


# Email Address LettersOnly abc@gmail.com
def media_email_address():
    email_address = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_letters, 4))
        num2 = ''.join(random.sample(string.ascii_letters, 6))
        num3 = ''.join(random.sample(string.ascii_letters, 10))
        email_address.append(f'{num1}@gmail.com')
        email_address.append(f'{num2}@gmail.com')
        email_address.append(f'{num3}@gmail.com')
    email_address_list = list(set(email_address))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["LettersOnly"] * 3000, [
        "LettersOnly"] * 7000, ["Email Address"] * 3000, ["Email Address"] * 7000, email_address_list[0:3000],\
           email_address_list[3001:10001]


# Email Address LettersOnly abc@gmail.com
def media_email_address1():
    email_address1 = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_letters, 4))
        num1_1 = str(random.randint(0, 9999))
        num2 = ''.join(random.sample(string.ascii_letters, 6))
        num2_1 = str(random.randint(0, 9999))
        num3 = ''.join(random.sample(string.ascii_letters, 10))
        num3_1 = str(random.randint(0, 9999))
        email_address1.append(f'{num1}{num1_1}@gmail.com')
        email_address1.append(f'{num2}{num2_1}@gmail.com')
        email_address1.append(f'{num3}{num3_1}@gmail.com')
    email_address_list1 = list(set(email_address1))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["LettersOnly"] * 3000, [
        "LettersOnly"] * 7000, \
           ["Email Address"] * 3000, ["Email Address"] * 7000, email_address_list1[0:3000], email_address_list1[
                                                                                            3001:10001]


# password      LettersOnly  4-20 digits    ytrf
def media_psw():
    psw = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_letters, 4))
        num2 = ''.join(random.sample(string.ascii_letters, 6))
        num3 = ''.join(random.sample(string.ascii_letters, 10))
        psw.append(num1)
        psw.append(num2)
        psw.append(num3)
    psw_list = list(set(psw))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["LettersOnly"] * 3000, [
        "LettersOnly"] * 7000, \
           ["password"] * 3000, ["password"] * 7000, psw_list[0:3000], psw_list[3001:10001]


# password      NumbersOnly  4-20 digits    1923
def media_psw1():
    psw1 = []
    for i in range(0, 11000):
        num1 = str(random.randint(1000, 99999999999999999999))
        psw1.append(num1)
    psw_list1 = list(set(psw1))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, [
        "NumbersOnly"] * 7000, \
           ["password"] * 3000, ["password"] * 7000, psw_list1[0:3000], psw_list1[3001:10001]


# password      NumbersAndLetters  4-20 digits    ytrf
def media_psw2():
    psw2 = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_letters, 4))
        num1_1 = str(random.randint(0, 999))
        num2 = ''.join(random.sample(string.ascii_letters, 6))
        num2_1 = str(random.randint(0, 999))
        num3 = ''.join(random.sample(string.ascii_letters, 10))
        num3_1 = str(random.randint(0, 999))
        psw2.append(f'{num1}{num1_1}')
        psw2.append(f'{num2}{num2_1}')
        psw2.append(f'{num3}{num3_1}')
    psw_list2 = list(set(psw2))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersAndLetters"] * 3000,\
         ["NumbersAndLetters"] * 7000, ["password"] * 3000, ["password"] * 7000, psw_list2[0:3000], psw_list2[3001:10001]


# Verification code      NumbersOnly  4-20 digits    192399
def media_ver_code():
    ver_code = []
    for i in range(0, 11000):
        num1 = str(random.randint(1000, 99999999999999999999))
        ver_code.append(num1)
    ver_code_list = list(set(ver_code))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000,\
           ["Verification code"] * 3000, ["Verification code"] * 7000, ver_code_list[0:3000], ver_code_list[3001:10001]


# Sales/Collection     NumbersOnly  4-20 digits
def media_sale_collect():
    sale_collect = []
    for i in range(0, 11000):
        num1 = str(random.randint(1000, 99999999999999999999))
        sale_collect.append(num1)
    sale_collect_list = list(set(sale_collect))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000,\
           ["Sales/Collection"] * 3000, ["Sales/Collection"] * 7000, sale_collect_list[0:3000], sale_collect_list[3001:10001]


# Telephone Number  格式为0+9位     295732039       10digits
def media_tel_number():
    tel_number = []
    for i in range(0, 11000):
        num1 = str(random.randint(0, 999999999)).zfill(9)
        tel_number.append(f'0{num1}')
    tel_number_list = list(set(tel_number))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000,\
           ["Telephone Number"] * 3000, ["Telephone Number"] * 7000, tel_number_list[0:3000], tel_number_list[3001:10001]


# Online account name? NumbersAndLetters    4-20 digits     as20201908
def media_online_account():
    online_account = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_letters, 2))
        num1_1 = str(random.randint(0, 999))
        num2 = ''.join(random.sample(string.ascii_letters, 6))
        num2_1 = str(random.randint(0, 999))
        num3 = ''.join(random.sample(string.ascii_letters, 3))
        num3_1 = str(random.randint(0, 999))
        online_account.append(f'{num1}{num1_1}')
        online_account.append(f'{num2}{num2_1}')
        online_account.append(f'{num3}{num3_1}')
    online_account_list = list(set(online_account))
    # print(refund_num_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersAndLetters"] * 3000, \
           ["NumbersAndLetters"] * 7000, ["Online account name?"] * 3000, ["Online account name?"] * 7000, \
           online_account_list[0:3000],online_account_list[3001:10001]

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
    # print(text_list1)
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


    domain_list1 = aviation_domain_list1 + food_domain_list1+finance_domain_list1+health_domain_list1+insurance_domain_list1+medial_domain_list1+retail_domain_list1
    UtteranceType_list1 = aviation_UtteranceType_list1 + food_UtteranceType_list1+finance_UtteranceType_list1+health_UtteranceType_list1+insurance_UtteranceType_list1+medial_UtteranceType_list1+retail_UtteranceType_list1
    Category_list1 = aviation_Category_list1 + food_Category_list1+finance_Category_list1+health_Category_list1+insurance_Category_list1+medial_Category_list1+retail_Category_list1
    text_list1 = aviation_text_list1 + food_text_list1+finance_text_list1+health_text_list1+insurance_text_list1+medial_text_list1+retail_text_list1

    domain_list2 = aviation_domain_list2 + food_domain_list2+finance_domain_list2+health_domain_list2+insurance_domain_list2+medial_domain_list2+retail_domain_list2
    UtteranceType_list2 = aviation_UtteranceType_list2 + food_UtteranceType_list2+finance_UtteranceType_list2+health_UtteranceType_list2+insurance_UtteranceType_list2+medial_UtteranceType_list2+retail_UtteranceType_list2
    Category_list2 = aviation_Category_list2 + food_Category_list2+finance_Category_list2+health_Category_list2+insurance_Category_list2+medial_Category_list2+retail_Category_list2
    text_list2 = aviation_text_list2 + food_text_list2+finance_text_list2+health_text_list2+insurance_text_list2+medial_text_list2+retail_text_list2
    df1 = pd.DataFrame(
        {'Domain': domain_list1, "UtteranceType": UtteranceType_list1, "Category": Category_list1, "Text": text_list1})
    df1.to_csv("3000_data1.csv", index=False, sep=',', encoding='utf-8-sig')
    df2 = pd.DataFrame(
        {'Domain': domain_list2, "UtteranceType": UtteranceType_list2, "Category": Category_list2, "Text": text_list2})
    df2.to_csv("7000_data1.csv", index=False, sep=',', encoding='utf-8-sig')


if __name__ == '__main__':
    main()

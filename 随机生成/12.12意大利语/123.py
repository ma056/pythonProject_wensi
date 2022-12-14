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
    print(text_list1)
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


def main():
    aviation_domain_list1, aviation_domain_list2, aviation_UtteranceType_list1, aviation_UtteranceType_list2, aviation_Category_list1, \
    aviation_Category_list2, aviation_text_list1, aviation_text_list2 = airline()
    food_domain_list1, food_domain_list2, food_UtteranceType_list1, food_UtteranceType_list2, food_Category_list1, food_Category_list2, \
    food_text_list1, food_text_list2 = fast_food()
    finance_domain_list1, finance_domain_list2, finance_UtteranceType_list1, finance_UtteranceType_list2, finance_Category_list1, \
    finance_Category_list2, finance_text_list1, finance_text_list2 = finance()

    domain_list1 = aviation_domain_list1 + food_domain_list1+finance_domain_list1
    UtteranceType_list1 = aviation_UtteranceType_list1 + food_UtteranceType_list1+finance_UtteranceType_list1
    Category_list1 = aviation_Category_list1 + food_Category_list1+finance_Category_list1
    text_list1 = aviation_text_list1 + food_text_list1+finance_text_list1

    domain_list2 = aviation_domain_list2 + food_domain_list2+finance_domain_list2
    UtteranceType_list2 = aviation_UtteranceType_list2 + food_UtteranceType_list2+finance_UtteranceType_list2
    Category_list2 = aviation_Category_list2 + food_Category_list2+finance_Category_list2
    text_list2 = aviation_text_list2 + food_text_list2+finance_text_list2
    df1 = pd.DataFrame(
        {'Domain': domain_list1, "UtteranceType": UtteranceType_list1, "Category": Category_list1, "Text": text_list1})
    df1.to_csv("3000_data.csv", index=False, sep=',', encoding='utf-8-sig')
    df2 = pd.DataFrame(
        {'Domain': domain_list2, "UtteranceType": UtteranceType_list2, "Category": Category_list2, "Text": text_list2})
    df2.to_csv("7000_data.csv", index=False, sep=',', encoding='utf-8-sig')


if __name__ == '__main__':
    main()

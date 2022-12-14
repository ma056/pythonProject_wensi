# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : finance.py
@Author : wenjing
@Date : 2022/12/12 10:52
"""
import random
from random import shuffle
import itertools
import pandas as pd
import re
import string


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
    domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2 = finance()
    # print(type_list)
    # df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    #
    # with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

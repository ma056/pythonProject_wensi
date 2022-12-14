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


def finance():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = finance_credit_code()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = finance_serial_number()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = finance_id_number()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = finance_id_number1()

    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = finance_bank_card()
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = finance_contract_no()
    domain7_1, domain7_2, UtteranceType7_1, UtteranceType7_2, Category7_1, Category7_2, text7_1, text7_2 = finance_item_no()
    domain8_1, domain8_2, UtteranceType8_1, UtteranceType8_2, Category8_1, Category8_2, text8_1, text8_2 = finance_item_no1()

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1 + domain6_1 + domain7_1+domain8_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2 + domain6_2 + domain7_2+domain8_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 +UtteranceType5_1 + UtteranceType6_1 + UtteranceType7_1 + UtteranceType8_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 +UtteranceType5_2 + UtteranceType6_2 + UtteranceType7_2 + UtteranceType8_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1 + Category6_1 + Category7_1 + Category8_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2 + Category6_2 + Category7_2 + Category8_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1 + text6_1 + text7_1 + text8_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2 + text6_2 + text7_2 + text8_2
    print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2

    # type1, number1, txt1 = finance_credit_code()
    # type2, number2, txt2 = finance_serial_number()
    # type3, number3, txt3 = finance_serial_number1()
    # type4, number4, txt4 = finance_tel_num()
    # type5, number5, txt5 = finance_bank_card()
    # type6, number6, txt6 = finance_contract_no()
    # type7, number7, txt7 = finance_item_no()
    #
    # type8, number8, txt8 = finance_security_fund()
    # type9, number9, txt9 = finance_securities_operate_income()
    # type10, number10, txt10 = finance_winning_no()
    # type11, number11, txt11 = finance_fund_price()
    # type12, number12, txt12 = finance_authorized_shares()
    # type13, number13, txt13 = finance_valid_date_of_bank_card()
    # type_list = type1 + type2 + type3 + type4 + type5 + type6 + type7+ type8 + type9 + type10 + type11 + type12 + type13
    # number_list = number1 + number2 + number3 + number4 + number5 + number6 + number7+ number8 + number9 + number10 + number11 + number12 + number13
    # txt_list = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10 + txt11 + txt12 + txt13
    # # print(type_list)
    # return type_list, number_list, txt_list
    # finance_credit_code()
    # finance_serial_number()
    # finance_serial_number1()
    # finance_tel_num()
    # finance_bank_card()
    # finance_contract_no()
    # finance_item_no()
    # finance_security_fund()
    # finance_securities_operate_income()
    # finance_winning_no()
    # finance_fund_price()
    # finance_authorized_shares()
    # finance_valid_date_of_bank_card()


# 统一社会信用代码 18位  91310000MAIFPFRF44   10000/110000固定不变，字母为大写
def finance_credit_code():
    credit_code = []
    for i in range(0, 11000):
        num1 = ''.join(random.sample(string.ascii_uppercase, 8))
        random_num = str(random.randint(100, 999))
        random_num1 = str(random.randint(10, 99))
        phone_num = f'{random_num}10000{num1}{random_num1}'
        credit_code.append(phone_num)
    order_no_list = list(set(credit_code))
    # print(order_no_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "统一社会信用代码"] * 3000, ["统一社会信用代码"] * 7000, order_no_list[0:3000], order_no_list[3001:10001]


# 证照编号 20位
def finance_serial_number():
    # '123'.zfill(5)补0操作
    serial_number = []
    for i in range(0, 11000):
        random_num = str(random.randint(10000000000000000000, 99999999999999999999))
        phone_num = f'100{random_num}'.zfill(24)
        serial_number.append(phone_num)
    serial_number_list = list(set(serial_number))
    # print(serial_number_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "证照编号"] * 3000, ["证照编号"] * 7000, serial_number_list[0:3000], serial_number_list[3001:10001]


# 身份证号 18 NumbersOnly 第1-2位：11-15，21-23，31-37，41-46，50-54，61-65；第3-4位：01-70；
# 第5-6位：01-18，21-80，81-99；第7-14位是生日的年月日，范围可设为19400101-20201231，最后一位0-9以及X
# 230802 ** ** ** ** 023X
def finance_id_number():
    id_number = []
    for i in range(0, 11000):
        num1 = random.choice(
            [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 61,
             62, 63, 64, 65])
        num2 = str(random.randint(0, 70))
        if len(num2) < 2:
            num2 = f'0{num2}'
        num3_1 = str(random.randint(0, 18))
        if len(num3_1) < 2:
            num3_1 = f'0{num3_1}'
        num3_2 = str(random.randint(21, 80))
        num3_3 = str(random.randint(81, 99))
        num3 = random.choice([num3_1, num3_2, num3_3])
        # 出生年月日
        year = str(random.randint(1940, 2020))
        month = str(random.randint(1, 12))
        if len(month) < 2:
            month = f'0{month}'
        day = str(random.randint(1, 29))
        # num4 = str(random.randint(19400101,20201231))
        num5 = str(random.randint(0, 9))
        # num5 = random.choice([num5_1, 'X'])
        phone_num = f'{num1}{num2}{num3}{year}{month}{day}023{num5}'
        id_number.append(phone_num)
    id_number_list = list(set(id_number))
    # print(id_number_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "身份证号"] * 3000, ["身份证号"] * 7000, id_number_list[0:3000], id_number_list[3001:10001]


# 身份证号 NumbersAndLetters  230802********0235  第1-2位：11-15，21-23，31-37，41-46，50-54，61-65；第3-4位：01-70；
# 第5-6位：01-18，21-80，81-99；第7-14位是生日的年月日，范围可设为19400101-20201231，最后一位0-9以及X
def finance_id_number1():
    serial_number1 = []
    for i in range(0, 11000):
        num1 = random.choice(
            [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 61,
             62, 63, 64, 65])
        num2 = str(random.randint(0, 70))
        if len(num2) < 2:
            num2 = f'0{num2}'
        num3_1 = str(random.randint(0, 18))
        if len(num3_1) < 2:
            num3_1 = f'0{num3_1}'
        num3_2 = str(random.randint(21, 80))
        num3_3 = str(random.randint(81, 99))
        num3 = random.choice([num3_1, num3_2, num3_3])
        # 出生年月日
        year = str(random.randint(1940, 2020))
        month = str(random.randint(1, 12))
        if len(month) < 2:
            month = f'0{month}'
        day = str(random.randint(1, 29))
        # num4 = str(random.randint(19400101,20201231))
        # num5_1 = str(random.randint(0, 9))
        # num5 = random.choice([num5_1, 'X'])
        phone_num = f'{num1}{num2}{num3}{year}{month}{day}023X'
        serial_number1.append(phone_num)
    id_number_list1 = list(set(serial_number1))
    # print(id_number_list1)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "身份证号"] * 3000, ["身份证号"] * 7000, id_number_list1[0:3000], id_number_list1[3001:10001]


# 银行卡/信用卡号  16-19 开头可为436742， 622280，458123，402674，622188，602969，622200，622568，548844，512431，622892
def finance_bank_card():
    start_num = [436742, 622280, 458123, 402674, 622188, 602969, 622200, 622568, 548844, 512431, 622892]
    bank_card = []
    for i in range(0, 12000):
        random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(1000000000, 9999999999999))
        phone_num = "{}{:0<8}".format(start_num[random_pn], random_num)
        bank_card.append(phone_num)
    bank_card_list = list(set(bank_card))
    # print(bank_card_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "银行卡/信用卡号"] * 3000, ["银行卡/信用卡号"] * 7000, bank_card_list[0:3000], bank_card_list[3001:10001]


# 合同编号 4位以上   GJ-WZ-LWD-B139-2013310 字母为大写，末尾需要是合理的日期，范围可设为19400101-20221231
def finance_contract_no():
    bank_card = []
    for i in range(0, 12000):
        num1 = ''.join(random.sample(string.ascii_uppercase, 2))
        num2 = ''.join(random.sample(string.ascii_uppercase, 2))
        num3 = ''.join(random.sample(string.ascii_uppercase, 3))
        num4_1 = random.choice(string.ascii_uppercase)
        num4_2 = str(random.randint(100, 999))
        year = str(random.randint(1940, 2020))
        month = str(random.randint(1, 12))
        if len(month) < 2:
            month = f'0{month}'
        day = str(random.randint(1, 29))
        num = f'{num1}-{num2}-{num3}-{num4_1}{num4_2}-{year}{month}{day}'
        bank_card.append(num)
    bank_card_list = list(set(bank_card))
    # print(bank_card_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "合同编号"] * 3000, ["合同编号"] * 7000, bank_card_list[0:3000], bank_card_list[3001:10001]


# 项目编号1 4位以上 SDTASJ2017-0910-00 2017-0910需要是合理的日期时间，范围可设为1940-0101 - 2022-1231
def finance_item_no():
    item_no = []
    for i in range(0, 12000):
        num1 = ''.join(random.sample(string.ascii_uppercase, 2))
        year = str(random.randint(1940, 2020))
        month = str(random.randint(1, 12))
        if len(month) < 2:
            month = f'0{month}'
        day = str(random.randint(1, 29))
        num2 = str(random.randint(0, 99))
        if len(num2) < 2:
            num2 = f'0{num2}'
        num = f'{num1}{year}-{month}{day}-{num2}'
        item_no.append(num)
    item_no_list = list(set(item_no))
    # print(item_no_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "项目编号"] * 3000, ["项目编号"] * 7000, item_no_list[0:3000], item_no_list[3001:10001]


# 项目编号2  4位以上 2017-0910-00  2017-0910需要是合理的日期时间，范围可设为1940-0101 - 2022-1231
def finance_item_no1():
    item_no = []
    for i in range(0, 12000):
        year = str(random.randint(1940, 2020))
        month = str(random.randint(1, 12))
        if len(month) < 2:
            month = f'0{month}'
        day = str(random.randint(1, 29))
        num2 = str(random.randint(0, 99))
        if len(num2) < 2:
            num2 = f'0{num2}'
        num = f'{year}-{month}{day}-{num2}'
        item_no.append(num)
    item_no_list = list(set(item_no))
    # print(item_no_list)
    return ["Finance"] * 3000, ["Finance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "项目编号"] * 3000, ["项目编号"] * 7000, item_no_list[0:3000], item_no_list[3001:10001]


def main():
    domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2 = finance()
    # print(type_list)
    # df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    #
    # with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

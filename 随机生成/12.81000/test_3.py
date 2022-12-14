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
    type1, number1, txt1 = finance_credit_code()
    type2, number2, txt2 = finance_serial_number()
    type3, number3, txt3 = finance_serial_number1()
    type4, number4, txt4 = finance_tel_num()
    type5, number5, txt5 = finance_bank_card()
    type6, number6, txt6 = finance_contract_no()
    type7, number7, txt7 = finance_item_no()

    type8, number8, txt8 = finance_security_fund()
    type9, number9, txt9 = finance_securities_operate_income()
    type10, number10, txt10 = finance_winning_no()
    type11, number11, txt11 = finance_fund_price()
    type12, number12, txt12 = finance_authorized_shares()
    type13, number13, txt13 = finance_valid_date_of_bank_card()
    type_list = type1 + type2 + type3 + type4 + type5 + type6 + type7+ type8 + type9 + type10 + type11 + type12 + type13
    number_list = number1 + number2 + number3 + number4 + number5 + number6 + number7+ number8 + number9 + number10 + number11 + number12 + number13
    txt_list = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10 + txt11 + txt12 + txt13
    # print(type_list)
    return type_list, number_list, txt_list
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
    for i in range(0, 1000):
        num1 = ''.join(random.sample(string.ascii_uppercase, 8))
        random_num = str(random.randint(100, 999))
        random_num1 = str(random.randint(10, 99))
        phone_num = f'{random_num}10000{num1}{random_num1}'
        credit_code.append(phone_num)
    order_no_list = list(set(credit_code))[0:1000]
    # print(order_no_list)
    return ["统一社会信用代码"] * 1000, [i for i in range(1, 1001)], order_no_list


# 证照编号 20位
def finance_serial_number():
    # '123'.zfill(5)补0操作
    serial_number = []
    for i in range(0, 1000):
        random_num = str(random.randint(10000000000000000000, 99999999999999999999))
        phone_num = f'100{random_num}'.zfill(24)
        serial_number.append(phone_num)
    serial_number_list = list(set(serial_number))[0:1000]
    # print(serial_number_list)
    return ["证照编号"] * 1000, [i for i in range(1, 1001)], serial_number_list


# 证照编号 18 第1-2位：11-15，21-23，31-37，41-46，50-54，61-65；第3-4位：01-70；
# 第5-6位：01-18，21-80，81-99；第7-14位是生日的年月日，范围可设为19400101-20201231，最后一位0-9以及X
# 230802 ** ** ** ** 023X
def finance_serial_number1():
    serial_number1 = []
    for i in range(0, 1000):
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
        num5_1 = str(random.randint(0, 9))
        num5 = random.choice([num5_1, 'X'])
        phone_num = f'{num1}{num2}{num3}{year}{month}{day}023{num5}'
        serial_number1.append(phone_num)
    serial_number_list1 = list(set(serial_number1))[0:1000]
    # print(serial_number_list1)
    return ["证照编号"] * 1000, [i for i in range(1, 1001)], serial_number_list1


# 手机号 11  开头需为133、149、153、173、177、180、181、189、190、191、193、199、130、131、132、145、155、156、166、167、171、175、176、185、186、196、135、136、137、138、139、1440、147、148、150、151、152、157、158、159、172、178、182、183、184、187、188、195、197、198、192
def finance_tel_num():
    start_num = [133, 149, 153, 173, 177, 180, 181, 189, 190, 191, 193, 199, 130, 131, 132, 145, 155, 156, 166,
                 167, 171, 175, 176, 185, 186, 196, 135, 136, 137, 138, 139, 1440, 147, 148,
                 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 195, 197, 198, 192]
    tel_num = []
    for i in range(0, 1200):
        random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(0, 99999999))
        phone_num = "{}{:0<8}".format(start_num[random_pn], random_num)
        tel_num.append(phone_num)
    tel_num_list = list(set(tel_num))[:1000]
    # print(tel_num_list)
    return ["手机号"] * 1000, [i for i in range(1, 1001)], tel_num_list


# 银行卡/信用卡号  16-19 开头可为436742， 622280，458123，402674，622188，602969，622200，622568，548844，512431，622892
def finance_bank_card():
    start_num = [436742, 622280, 458123, 402674, 622188, 602969, 622200, 622568, 548844, 512431, 622892]
    bank_card = []
    for i in range(0, 1200):
        random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(1000000000, 9999999999999))
        phone_num = "{}{:0<8}".format(start_num[random_pn], random_num)
        bank_card.append(phone_num)
    bank_card_list = list(set(bank_card))[:1000]
    # print(bank_card_list)
    return ["银行卡/信用卡号"] * 1000, [i for i in range(1, 1001)], bank_card_list


# 合同编号 4位以上   GJ-WZ-LWD-B139-2013310 字母为大写，末尾需要是合理的日期，范围可设为19400101-20221231
def finance_contract_no():
    bank_card = []
    for i in range(0, 1200):
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
    bank_card_list = list(set(bank_card))[:1000]
    # print(bank_card_list)
    return ["合同编号"] * 1000, [i for i in range(1, 1001)], bank_card_list


# 项目编号 4位以上 SDTASJ2017-0910-00 2017-0910需要是合理的日期时间，范围可设为1940-0101 - 2022-1231
def finance_item_no():
    item_no = []
    for i in range(0, 1200):
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
    item_no_list = list(set(item_no))[:1000]
    # print(item_no_list)
    return ["项目编号"] * 1000, [i for i in range(1, 1001)], item_no_list


# 证券/基金代码 6位 010123 沪A：60****；深A：00**** ，沪B：90****，深B：20****，普通三板A股: 40****；三板B股：42****；新三板：43****、83****，创业板：30****
def finance_security_fund():
    start_num = [60, 00, 90, 20, 40, 43, 83, 30]
    security_fund = []
    for i in range(0, 1200):
        random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(1000, 9999))
        phone_num = "{}{:0<4}".format(start_num[random_pn], random_num).zfill(6)
        security_fund.append(phone_num)
    security_fund_list = list(set(security_fund))[:1000]
    # print(security_fund_list)
    return ["证券/基金代码"] * 1000, [i for i in range(1, 1001)], security_fund_list


# 证券营业收入 1,772,707 四位以上
def finance_securities_operate_income():
    securities_operate_income = []
    for i in range(0, 1200):
        random_num = str(random.randint(100000, 9999999))
        random_num1 = ','.join(re.findall(r'.{3}', random_num))
        securities_operate_income.append(random_num1)
    securities_operate_income_list = list(set(securities_operate_income))[:1000]
    # print(securities_operate_income_list)
    return ["证券营业收入"] * 1000, [i for i in range(1, 1001)], securities_operate_income_list


# 中签号 923901 4位以上
def finance_winning_no():
    winning_no = []
    for i in range(0, 1200):
        random_num = str(random.randint(1000, 9999999))
        winning_no.append(random_num)
    winning_no_list = list(set(winning_no))[:1000]
    # print(winning_no_list)
    return ["中签号"] * 1000, [i for i in range(1, 1001)], winning_no_list


# 股票/基金价 46.21 4位以上
def finance_fund_price():
    fund_price = []
    for i in range(0, 1200):
        random_num = str(random.randint(1000, 999999))
        random_num1 = '.'.join(re.findall(r'.{2}', random_num))
        fund_price.append(random_num1)
    fund_price_list = list(set(fund_price))[:1000]
    # print(fund_price_list)
    return ["中签号"] * 1000, [i for i in range(1, 1001)], fund_price_list


# 发行股数 313111 4位以上
def finance_authorized_shares():
    authorized_shares = []
    for i in range(0, 1200):
        random_num = str(random.randint(1000, 9999999))
        authorized_shares.append(random_num)
    authorized_shares_list = list(set(authorized_shares))[:1000]
    # print(authorized_shares_list)
    return ["中签号"] * 1000, [i for i in range(1, 1001)], authorized_shares_list


# 银行卡有效日期   12/12（月/年） 范围可设为01-12/00-99  4位以上
def finance_valid_date_of_bank_card():
    valid_date_of_bank_card = []
    for i in range(0, 3000):
        month = str(random.randint(1, 12))
        year = str(random.randint(00, 99))
        if len(year) < 2:
            year = f'0{year}'
        if len(month) < 2:
            month = f'0{month}'
        num = f'{month}/{year}'
        valid_date_of_bank_card.append(num)
    valid_date_of_bank_card_list = list(set(valid_date_of_bank_card))
    num = 1000 - len(valid_date_of_bank_card_list)
    valid_date_of_bank_card_list.extend([''] * num)
    # print(valid_date_of_bank_card_list)
    return ["登机日期"] * 1000, [i for i in range(1, 1001)], valid_date_of_bank_card_list[0:1000]


def main():
    type_list, number_list, txt_list = finance()
    # print(type_list)
    df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})

    with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
        df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

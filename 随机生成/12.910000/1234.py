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
def aviation():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = aviation_flight_number()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = aviation_order_no()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = aviation_service_tel_num()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = aviation_ticket_no()

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2,Category_list1,Category_list2, text_list1, text_list2


# 航班号 长度5/6位 前面两位固定,字母需大写：3U,NS,8C,CA,SC,MF,EU,ZH,VD,FM,KN,MU,HU,CN,8L,PN,GS,HO,BK,G5,9C,JD
def aviation_flight_number():
    start_num = ["3U", "NS", "8C", "CA", "SC", "MF", "EU", "ZH", "VD", "FM", "KN", "MU", "HU", "CN", "8L", "PN", "GS",
                 "HO", "BK", "G5", "9C", "JD"]
    list1 = []
    for i in range(0, 13000):
        random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(100, 9999))
        phone_num = "{}{:0<3}".format(start_num[random_pn], random_num)
        list1.append(phone_num)
        # if len(phone_num) == 5:
        #     print(phone_num)
    flight_number_list = list(set(list1))
    # print(flight_number_list)
    return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "航班号"] * 3000, ["航班号"] * 7000, flight_number_list[0:3000], flight_number_list[3001:10001]


# 机票订单编号 数字	11位
def aviation_order_no():
    order_no = []
    for i in range(0, 11000):
        random_num = random.randint(1000000, 9999999)
        phone_num = f'16{random_num}91'
        order_no.append(phone_num)
    order_no_list = list(set(order_no))
    # for i1 in flight_number:
    #     if len(str(i1))<11:
    #         print(i1)
    # print(oreder_no_list)
    return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "机票订单编号"] * 3000, ["机票订单编号"] * 7000, order_no_list[0:3000], order_no_list[3001:10001]


# 客服电话 10位 开头400，021，028，010固定，还有开头三位数固定的5位数：955**，950**，开头三位数固定的5-6位可变：953**
def aviation_service_tel_num():
    start_num = ["400", "021", "028", "010", "955", "950", "953"]
    service_tel_num = []
    for i in range(0, 18000):
        random_pn = random.randrange(0, len(start_num))
        new_random_pn = start_num[random_pn]
        if new_random_pn in ["400", "021", "028", "010"]:
            random_num1 = str(random.randint(100, 999))
            random_num2 = str(random.randint(1000, 9999))
            phone_num = f"{new_random_pn}-{random_num1}-{random_num2}"  # .format(start_num[random_pn], random_num)
            service_tel_num.append(phone_num)
        elif new_random_pn in ["955", "950"]:
            random_num = str(random.randint(10, 99))
            phone_num = f"{new_random_pn}{random_num}"  # .format(start_num[random_pn], random_num)
            service_tel_num.append(phone_num)
        elif new_random_pn == '953':
            random_num = str(random.randint(10, 999))
            phone_num = f"{new_random_pn}{random_num}"
            service_tel_num.append(phone_num)
    service_tel_num_list = list(set(service_tel_num))
    res_service_tel_num_list = service_tel_num_list
    # print(res_service_tel_num_list)
    return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "客服电话"] * 3000, ["客服电话"] * 7000, res_service_tel_num_list[0:3000], res_service_tel_num_list[3001:10001]


# 机票号 13位 数字 前三位固定：东方航空781；国际航空999；南方航空784；上海航空774；
# 厦门航空731；深圳航空479；海南航空880；山东航空324；四川航空876；华夏航空883；奥凯航空866；联合航空822
def aviation_ticket_no():
    start_num = [781, 999, 784, 774, 731, 479, 880, 324, 876, 883, 866, 822]
    ticket_no = []
    for i in range(0, 12000):
        random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(1000000000, 9999999999))
        phone_num = "{}{:0<10}".format(start_num[random_pn], random_num)
        ticket_no.append(phone_num)
    ticket_no_list = list(set(ticket_no))
    # print(ticket_no_list)
    return ["Airline"] * 3000, ["Airline"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, ["机票号"] * 3000, [
        "机票号"] * 7000, ticket_no_list[0:3000], ticket_no_list[3001:10001]


def fast_food():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = fast_food_order_no()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = fast_food_tel_num()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = fast_food_waybill_no()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = fast_food_pick_code()

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


# 订单编号 数字/数字加字母 13-19位 字母位置固定大写
def fast_food_order_no():
    # num1 = random.choice(string.ascii_uppercase)
    order_no = []
    for i in range(0, 11000):
        num1 = random.choice(string.ascii_uppercase)
        random_num = str(random.randint(1000000000000, 9999999999999999999))
        phone_num = f'{num1}{random_num}'
        order_no.append(phone_num)
    order_no_list = list(set(order_no))
    # print(order_no_list)
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, ["订单编号"] * 3000, [
        "订单编号"] * 7000, order_no_list[0:3000], order_no_list[3001:10001]


# 订单编号 仅数字 13-19位
def fast_food_tel_num():
    tel_num = []
    for i in range(0, 12000):
        random_num = str(random.randint(1000000000000, 9999999999999999999))
        phone_num = "{}{:0<8}".format(187, random_num)
        tel_num.append(phone_num)
    tel_num_list = list(set(tel_num))
    # print(tel_num_list)
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "虚拟手机号码"] * 3000, ["虚拟手机号码"] * 7000, tel_num_list[0:3000], tel_num_list[3001:10001]


# 运单号 可变4位
def fast_food_waybill_no():
    waybill_no = []
    for i in range(0, 12000):
        random_num = str(random.randint(1000, 999999))
        phone_num = f'909{random_num}'
        waybill_no.append(phone_num)
    waybill_no_list = list(set(waybill_no))
    # print(waybill_no_list)
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "运单号"] * 3000, ["运单号"] * 7000, waybill_no_list[0:3000], waybill_no_list[3001:10001]


# 取件码 数字 四位以上
def fast_food_pick_code():
    pick_code = []
    for i in range(0, 11000):
        random_num = str(random.randint(1000, 999999))
        pick_code.append(random_num)
    pick_codeo_list = list(set(pick_code))
    # print(pick_codeo_list)
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "取件码"] * 3000, ["取件码"] * 7000, pick_codeo_list[0:3000], pick_codeo_list[3001:10001]

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
    # print(text_list1)
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


def healthcare():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = healthcare_national_drug_approval()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = healthcare_registration_no()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = healthcare_batch_number()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = healthcare_receipt_no()


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


# 国药准字 NumbersAndLetters  9位  Z20043804   第一个字母大写：H、Z、S、B、T、F、J
def healthcare_national_drug_approval():
    drug_approval = []
    for i in range(0, 11000):
        num1 = random.choice(["H","Z","S","B","T","F","J"])
        random_num = str(random.randint(10000000, 99999999))
        res_num = f'{num1}{random_num}'
        drug_approval.append(res_num)
    drug_approval_list = list(set(drug_approval))
    # print(drug_approval_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "国药准字"] * 3000, ["国药准字"] * 7000, drug_approval_list[0:3000], drug_approval_list[3001:10001]


# 注册证编号 NumbersOnly 11位 20168483047 前四位为年份，范围可设为1940-2022
def healthcare_registration_no():
    registration_no = []
    for i in range(0, 11000):
        year = str(random.randint(1940, 2020))
        random_num = str(random.randint(1000000, 9999999))
        res_num = f'{year}{random_num}'
        registration_no.append(res_num)
    registration_no_list = list(set(registration_no))
    # print(registration_no_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "注册证编号"] * 3000, ["注册证编号"] * 7000, registration_no_list[0:3000], registration_no_list[3001:10001]


# 生产批号 NumbersOnly 6位 140928 范围可设为00-99/01-12/01-29
def healthcare_batch_number():
    batch_number = []
    for i in range(0, 13000):
        num1 = str(random.randint(00, 99)).zfill(2)
        num2 = str(random.randint(1, 12)).zfill(2)
        num3 = str(random.randint(1, 29)).zfill(2)
        res_num = f'{num1}{num2}{num3}'
        batch_number.append(res_num)
    batch_number_list = list(set(batch_number))
    # print(batch_number_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "生产批号"] * 3000, ["生产批号"] * 7000, batch_number_list[0:3000], batch_number_list[3001:10001]


# 收据单号 NumbersOnly  7位 1147152
def healthcare_receipt_no():
    receipt_no = []
    for i in range(0, 11000):
        num = str(random.randint(1000000, 9999999)).zfill(2)
        receipt_no.append(num)
    receipt_no_list = list(set(receipt_no))
    # print(receipt_no_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "收据单号"] * 3000, ["收据单号"] * 7000, receipt_no_list[0:3000], receipt_no_list[3001:10001]


def main():
    aviation_domain_list1, aviation_domain_list2, aviation_UtteranceType_list1, aviation_UtteranceType_list2,aviation_Category_list1,\
    aviation_Category_list2, aviation_text_list1, aviation_text_list2 = aviation()
    food_domain_list1, food_domain_list2, food_UtteranceType_list1, food_UtteranceType_list2,food_Category_list1,food_Category_list2,\
    food_text_list1, food_text_list2 = fast_food()
    finance_domain_list1, finance_domain_list2, finance_UtteranceType_list1, finance_UtteranceType_list2, finance_Category_list1, \
    finance_Category_list2, finance_text_list1, finance_text_list2 = finance()
    health_domain_list1, health_domain_list2, health_UtteranceType_list1, health_UtteranceType_list2, health_Category_list1,\
    health_Category_list2, health_text_list1, health_text_list2 = healthcare()



    domain_list1 = aviation_domain_list1+food_domain_list1+finance_domain_list1+health_domain_list1
    UtteranceType_list1 = aviation_UtteranceType_list1+food_UtteranceType_list1+finance_UtteranceType_list1+health_UtteranceType_list1
    Category_list1 = aviation_Category_list1+food_Category_list1+finance_Category_list1+health_Category_list1
    text_list1 = aviation_text_list1+food_text_list1+finance_text_list1+health_text_list1

    domain_list2 = aviation_domain_list2 + food_domain_list2+finance_domain_list2+health_domain_list2
    UtteranceType_list2 = aviation_UtteranceType_list2 + food_UtteranceType_list2+finance_UtteranceType_list2+health_UtteranceType_list2
    Category_list2 = aviation_Category_list2 + food_Category_list2+finance_Category_list2+health_Category_list2
    text_list2 = aviation_text_list2 + food_text_list2+finance_text_list2+health_text_list2

    df1 = pd.DataFrame({'Domain': domain_list1, "UtteranceType": UtteranceType_list1, "Category": Category_list1, "Text":text_list1})
    df1.to_csv("3000_data.csv", index=False, sep=',',encoding='utf-8-sig')
    df2 = pd.DataFrame({'Domain': domain_list2, "UtteranceType": UtteranceType_list2, "Category": Category_list2, "Text": text_list2})
    df2.to_csv("7000_data.csv", index=False, sep=',',encoding='utf-8-sig')



if __name__ == '__main__':
    main()


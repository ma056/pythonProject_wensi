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


def insurance():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = insurance_application_form_no()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = insurance_serial_number()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = insurance_social_security_card_account()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = insurance_occupational_injury_certificate_no()
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = insurance_fax_no()

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 + UtteranceType5_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 + UtteranceType5_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2
    print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# 投保单号 NumbersOnly  4位以上  1001023*****
def insurance_application_form_no():
    application_form_no = []
    for i in range(0, 11000):
        random_num = str(random.randint(1000, 99999999))
        res_num = f'1001023{random_num}'
        application_form_no.append(res_num)
    application_form_no_list = list(set(application_form_no))
    # print(application_form_no_list)
    return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "投保单号"] * 3000, ["投保单号"] * 7000, application_form_no_list[0:3000], application_form_no_list[3001:10001]


# 流水号 NumbersOnly  4位以上 28930******************
def insurance_serial_number():
    serial_number = []
    for i in range(0, 11000):
        random_num = str(random.randint(1000, 99999999))
        res_num = f'1001023{random_num}'
        serial_number.append(res_num)
    serial_number_list = list(set(serial_number))
    # print(serial_number_list)
    return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "流水号"] * 3000, ["流水号"] * 7000, serial_number_list[0:3000], serial_number_list[3001:10001]


# 社保卡账号 NumbersOnly  10位 0007033382
def insurance_social_security_card_account():
    social_card = []
    for i in range(0, 11000):
        random_num = str(random.randint(1000000000, 9999999999))
        social_card.append(random_num)
    social_card_list = list(set(social_card))
    # print(social_card_list)
    return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "社保卡账号"] * 3000, ["社保卡账号"] * 7000, social_card_list[0:3000], social_card_list[3001:10001]


# 工伤认证号 NumbersOnly  9位 （2018）11257 需要是合理的日期，范围可设为（1940）0101/0-9-（2022）1231/0-9
def insurance_occupational_injury_certificate_no():
    injury_no = []
    for i in range(0, 11000):
        year = str(random.randint(1940, 2022))
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 29)).zfill(2)
        num = str(random.randint(0, 9))
        res_num = f'({year}) {month}{day}{num}'
        injury_no.append(res_num)
    injury_no_list = list(set(injury_no))
    # print(injury_no_list)
    return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "工伤认证号"] * 3000, ["工伤认证号"] * 7000, injury_no_list[0:3000], injury_no_list[3001:10001]


# 传真号 NumbersOnly  11位-16位 0454-6113668  “3-4位区号-8位固定电话号码-（4位分机号可有可无）”，区号的范围为：010,020-028,852,853,0固定/3-9/0-9/0-9
def insurance_fax_no():
    fax_no = []
    for i in range(0, 11000):
        num1 = ["010",'020','021','022','023','024','025','026','027','028','852','853','0309','0399']
        num = random.choice(num1)
        random_num = str(random.randint(10000000, 99999999)).zfill(11)
        fax_no.append(f'{num}-{random_num}')
    fax_no_list = list(set(fax_no))
    # print(fax_no_list)
    return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "传真号"] * 3000, ["传真号"] * 7000, fax_no_list[0:3000], fax_no_list[3001:10001]


def main():
    domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2 = insurance()
    # print(type_list)
    # df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    #
    # with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

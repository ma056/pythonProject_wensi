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


def travel():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = travel_postal_code()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = travel_reservation_no()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = travel_reservation_no1()
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


# 邮政编码 NumbersOnly  6位  http://www.xingtai.gov.cn/cycx/ybqh/200912/t20091224_272151.html
def travel_postal_code():
    postal_code = []
    for i in range(0, 11000):
        num = str(random.randint(100000,999909))
        postal_code.append(num)
    postal_code_list = list(set(postal_code))
    # print(fax_no_list)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "邮政编码"] * 3000, ["邮政编码"] * 7000, postal_code_list[0:3000], postal_code_list[3001:10001]


# 预定号 4位以上 LettersOnly  JSHT******  字母大小写皆可
def travel_reservation_no():
    reservation_no = []
    for i in range(0, 11000):
        num = ''.join(random.sample(string.ascii_letters, 4))
        num1 = ''.join(random.sample(string.ascii_letters, 5))
        reservation_no.append(num1)
        reservation_no.append(num)
    reservation_no_list = list(set(reservation_no))
    # print(fax_no_list)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["LettersOnly"] * 3000, ["LettersOnly"] * 7000, [
        "预定号"] * 3000, ["预定号"] * 7000, reservation_no_list[0:3000], reservation_no_list[3001:10001]


# 预定号 4位以上 NumbersOnly  282******
def travel_reservation_no1():
    reservation_no1 = []
    for i in range(0, 11000):
        random_num = str(random.randint(0, 9999999)).zfill(4)
        reservation_no1.append(random_num)
    reservation_no_list1 = list(set(reservation_no1))
    # print(fax_no_list)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "预定号"] * 3000, ["预定号"] * 7000, reservation_no_list1[0:3000], reservation_no_list1[3001:10001]


# 房间号   NumbersOnly 4位以上
def travel_room_num():
    room_num = []
    for i in range(0, 11000):
        random_num = str(random.randint(0, 9999999)).zfill(4)
        room_num.append(random_num)
    room_num_list = list(set(room_num))
    # print(fax_no_list)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "房间号"] * 3000, ["房间号"] * 7000, room_num_list[0:3000], room_num_list[3001:10001]

def main():
    domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2 = travel()
    # print(type_list)
    # df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    #
    # with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

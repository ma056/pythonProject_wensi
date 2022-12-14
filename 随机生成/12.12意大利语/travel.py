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
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = travel_country()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = travel_order_number()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = travel_city()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = travel_room_num()


    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2
    print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# Country of destination   LettersOnly 5-10 digits
def travel_country():
    country = []
    # with open("H:/Wenjing/country.txt", 'r') as file:
    with open("country.txt", 'r', encoding='utf-8') as file:
        content = file.readlines()
        for i in content:
            country.append(i.replace('\n', ''))
    number = 10001 - len(country)
    country.extend([''] * number)
    # print(country)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["LettersOnly"] * 3000, ["LettersOnly"] * 7000, [
        "Country of destination"] * 3000, ["Country of destination"] * 7000, country[0:3000], country[3001:10001]


# Order Number  NumbersOnly 6 digits 438906
def travel_order_number():
    order_number = []
    for i in range(0, 11000):
        random_num = str(random.randint(0, 999999)).zfill(6)
        order_number.append(random_num)
    order_number_list = list(set(order_number))
    # print(fax_no_list)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Order Number"] * 3000, ["Order Number"] * 7000, order_number_list[0:3000], order_number_list[3001:10001]


# City of Destination  LettersOnly  5-10 digits
def travel_city():
    city = []
    with open("city.txt", 'r', encoding='utf-8') as file:
        content = file.readlines()
        for i in content:
            city.append(i.replace('\n', ''))
    number = 10001 - len(city)
    city.extend([''] * number)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["LettersOnly"] * 3000, ["LettersOnly"] * 7000, [
        "City of Destination"] * 3000, ["City of Destination"] * 7000, city[0:3000], city[3001:10001]


# Room number   NumbersOnly 4位以上
def travel_room_num():
    room_num = []
    for i in range(0, 110000):
        random_num = str(random.randint(0, 9999)).zfill(4)
        room_num.append(random_num)
    room_num_list = list(set(room_num))
    # print(fax_no_list)
    return ["Travel"] * 3000, ["Travel"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Room number"] * 3000, ["Room number"] * 7000, room_num_list[0:3000], room_num_list[3000:10001]

def main():
    domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2 = travel()
    # print(type_list)
    # df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    #
    # with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : finance.py
@Author : wenjing
@Date : 2022/12/13 12:58
"""
import exrex
def get_data(d_type, u_type, c_type, rule):
    random_list = []
    while len(random_list) < 10000:
        # rule = r'^[A-Z]{7,10}|[A-Z]{4,5}$'
        random_str = exrex.getone(rule)
        random_list.append(random_str)
        random_list = list(set(random_list))
    return [d_type] * 3000, [d_type] * 7000, [u_type] * 3000, [u_type] * 7000, \
           [c_type] * 3000, [c_type] * 7000, random_list[0:3000], random_list[3000:10000]


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


finance()
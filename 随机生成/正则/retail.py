# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : retail.py
@Author : wenjing
@Date : 2022/12/13 14:11
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

# Shop Number   NumbersAndLetters   4 digits    格式为1个字母+3个数字
def retail_shop_number():
    shop_number = []
    for i in range(0, 11000):
        rule = r'^[A-Za-z]{1}\d{3}$'
        random_str = exrex.getone(rule)
        shop_number.append(random_str)
    shop_number_list = list(set(shop_number))
    number = 10001 - len(shop_number_list)
    shop_number_list.extend([''] * number)
    return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
           ["Shop Number"] * 3000, ["Shop Number"] * 7000, shop_number_list[0:3000], shop_number_list[3000:10000]


def retail():
    rule2 = r'^((0?[1-9])|((1|2)[0-9])|30|31)(0[1-9]|1[0-2])(19\d{2}|20\d{2})\d{8}'
    rule3 = r'\d{12}$'
    rule4 = r'^[A-Z0-9]{4,20}$'
    rule5 = r'^[A-Z0-9]{17}$'
    rule6 = r'\d{12}$'
    # Shop Number   NumbersAndLetters   4 digits    格式为1个字母+3个数字
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = retail_shop_number()
    # Order Number   NumbersOnly      16 digits 1122020000000000.0 格式为日、月、年+随机8位
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Retail","NumbersOnly","Order Number",rule2)
    # Item number?  NumbersOnly   12 digits    字母大写 204877000000.0
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Retail","NumbersOnly","Item number?",rule3)
    # models NumbersAndLetters   4-20 digits    CAF7230A
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("Retail","NumbersAndLetters","models",rule4)
    # VIN code        NumbersAndLetters   17 digits    LFV2A2*********
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = get_data("Retail","NumbersAndLetters","VIN code",rule5)
    # The tracking number?  NumbersOnly  12 digits
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = get_data("Retail","NumbersOnly","The tracking number?",rule6)

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1+domain6_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2+domain6_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 +UtteranceType5_1+UtteranceType6_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 +UtteranceType5_2+UtteranceType6_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1+Category6_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2+Category6_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1+text6_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2+text6_2
    print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


retail()


# # Order Number   NumbersOnly      16 digits 1122020000000000.0 格式为日、月、年+随机8位
# def retail_order_num():
#     order_num = []
#     while len(order_num) < 10000:
#     # for i in range(0, 11000):
#         year = str(random.randint(1940, 2020))
#         month = str(random.randint(1, 12)).zfill(2)
#         day = str(random.randint(1, 29)).zfill(2)
#         random_num = str(random.randint(0, 99999999)).zfill(8)
#         order_num.append(f'{day}{month}{year}{random_num}')
#         order_num = list(set(order_num))
#     # print(order_num_list)
#     return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, \
#            ["Order Number"] * 3000, ["Order Number"] * 7000, order_num[0:3000], order_num[3000:10000]
#
#
# # Item number?  NumbersOnly   12 digits    字母大写 204877000000.0
# def retail_item_number():
#     item_number = []
#     while len(item_number) < 10000:
#     # for i in range(0, 11000):
#         random_num = str(random.randint(0,999999999999)).zfill(12)
#         item_number.append(random_num)
#         item_number = list(set(item_number))
#     # print(psw_list)
#     return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, \
#            ["Item number?"] * 3000, ["Item number?"] * 7000, item_number[0:3000], item_number[3000:10000]
#
#
# # models NumbersAndLetters   4-20 digits    CAF7230A
# def retail_models_number():
#     models_number = []
#     while len(models_number) < 10000:
#     # for i in range(0, 11000):
#         random_num1 = ''.join(random.sample(string.ascii_uppercase, 3))
#         random_num2 = str(random.randint(1000, 9999999))
#         random_num3 = ''.join(random.sample(string.ascii_uppercase, 1))
#         models_number.append(f'{random_num1}{random_num2}{random_num3}')
#         models_number = list(set(models_number))
#     # print(psw_list)
#     return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
#            ["models"] * 3000, ["models"] * 7000, models_number[0:3000], models_number[3000:10000]
#
#
# # VIN code        NumbersAndLetters   17 digits    LFV2A2*********
# def retail_vin_code():
#     vin_code = []
#     while len(vin_code) < 10000:
#     # for i in range(0, 11000):
#         random_num1 = ''.join(random.sample(string.ascii_uppercase, 3))
#         random_num2 = str(random.randint(1000000, 9999999999999)).zfill(13)
#         random_num3 = ''.join(random.sample(string.ascii_uppercase, 1))
#         res_num = f'{random_num1}{random_num2}{random_num3}'
#         vin_code.append(res_num)
#         vin_code = list(set(vin_code))
#     # print(psw_list)
#     return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
#            ["VIN code"] * 3000, ["VIN code"] * 7000, vin_code[0:3000], vin_code[3000:10000]
#
#
# # The tracking number?  NumbersOnly  12 digits
# def retail_track_num():
#     track_num = []
#     while len(track_num) < 10000:
#     # for i in range(0, 11000):
#         random_num2 = str(random.randint(100000000000, 999999999999))
#         track_num.append(random_num2)
#         track_num = list(set(track_num))
#     # print(psw_list)
#     return ["Retail"] * 3000, ["Retail"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, ["The tracking number?"] * 3000,\
#            ["The tracking number?"] * 7000, track_num[0:3000], track_num[3000:10000]
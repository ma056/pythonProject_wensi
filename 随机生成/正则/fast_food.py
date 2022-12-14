# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : fast_food.py
@Author : wenjing
@Date : 2022/12/13 12:45
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


# Confirmation number  NumbersOnly  4 digits
def fast_confirmation_number():
    confirmation_number = []
    # while len(confirmation_number) < 10000:
    for i in range(0, 110000):
        rule = r'^[0-9]{4}$'
        phone_number_str = exrex.getone(rule)
        confirmation_number.append(phone_number_str)
    confirmation_number = list(set(confirmation_number))
    number = 10001 - len(confirmation_number)
    confirmation_number.extend([''] * number)
    return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "Confirmation number"] * 3000, ["Confirmation number"] * 7000, confirmation_number[0:3000], \
           confirmation_number[3000:10000]


def fast_food():
    rule = r'^(19\d{2}|20\d{2})(0[1-9]|1[0-2])((0?[1-9])|((1|2)[0-9])|30|31)\d{8}'
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = fast_confirmation_number()
    # order number NumbersOnly 16 digits 1.12202E+15    1122020000000000.0 格式为日、月、年+随机8位
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Fastfood","NumbersOnly","order number",rule)

    domain_list1 = domain1_1 + domain2_1
    domain_list2 = domain1_2 + domain2_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2
    Category_list1 = Category1_1 + Category2_1
    Category_list2 = Category1_2 + Category2_2
    text_list1 = text1_1 + text2_1
    text_list2 = text1_2 + text2_2
    print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2

fast_food()



# order number NumbersOnly 16 digits 1.12202E+15    1122020000000000.0 格式为日、月、年+随机8位
# def fast_order_num():
#     order_num = []
#     while len(order_num) < 10000:
#         rule = r'^(19\d{2}|20\d{2})(0[1-9]|1[0-2])((0?[1-9])|((1|2)[0-9])|30|31)\d{8}'
#         random_num = exrex.getone(rule)
#         order_num.append(random_num)
#         order_num = list(set(order_num))
#     # print(tel_num_list)
#     return ["Fastfood"] * 3000, ["Fastfood"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
#         "order number"] * 3000, ["order number"] * 7000, order_num[0:3000], order_num[3000:10000]
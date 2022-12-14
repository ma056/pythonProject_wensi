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


def main():
    aviation_domain_list1, aviation_domain_list2, aviation_UtteranceType_list1, aviation_UtteranceType_list2,aviation_Category_list1,\
    aviation_Category_list2, aviation_text_list1, aviation_text_list2 = aviation()
    food_domain_list1, food_domain_list2, food_UtteranceType_list1, food_UtteranceType_list2,food_Category_list1,food_Category_list2,\
    food_text_list1, food_text_list2 = fast_food()

    domain_list1 = aviation_domain_list1+food_domain_list1
    UtteranceType_list1 = aviation_UtteranceType_list1+food_UtteranceType_list1
    Category_list1 = aviation_Category_list1+food_Category_list1
    text_list1 = aviation_text_list1+food_text_list1

    domain_list2 = aviation_domain_list2 + food_domain_list2
    UtteranceType_list2 = aviation_UtteranceType_list2 + food_UtteranceType_list2
    Category_list2 = aviation_Category_list2 + food_Category_list2
    text_list2 = aviation_text_list2 + food_text_list2
    df1 = pd.DataFrame({'Domain': domain_list1, "UtteranceType": UtteranceType_list1, "Category": Category_list1, "Text":text_list1})
    df1.to_csv("3000_data.csv", index=False, sep=',',encoding='utf-8-sig')
    df2 = pd.DataFrame({'Domain': domain_list2, "UtteranceType": UtteranceType_list2, "Category": Category_list2, "Text": text_list2})
    df2.to_csv("7000_data.csv", index=False, sep=',',encoding='utf-8-sig')



if __name__ == '__main__':
    main()

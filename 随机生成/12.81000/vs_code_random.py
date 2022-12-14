# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : vs_code_random.py.py
@Author : wenjing
@Date : 2022/12/9 16:25
"""
import random
import string
import pandas as pd


# 航空
def aviation():
    type1, number1, txt1 = aviation_flight_number()
    type2, number2, txt2 = aviation_order_no()
    type3, number3, txt3 = aviation_service_tel_num()
    type4, number4, txt4 = aviation_name()
    type5, number5, txt5 = aviation_ticket_no()
    type6, number6, txt6 = aviation_board_time()
    type7, number7, txt7 = aviation_board_data()
    type_list = type1 + type2 + type3 + type4 + type5 + type6 + type7
    number_list = number1 + number2 + number3 + number4 + number5 + number6 + number7
    txt_list = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7
    # print(type_list)
    return type_list, number_list, txt_list


# 航班号 长度5/6位 前面两位固定,字母需大写：3U,NS,8C,CA,SC,MF,EU,ZH,VD,FM,KN,MU,HU,CN,8L,PN,GS,HO,BK,G5,9C,JD
def aviation_flight_number():
    start_num = ["3U", "NS", "8C", "CA", "SC", "MF", "EU", "ZH", "VD", "FM", "KN", "MU", "HU", "CN", "8L", "PN", "GS",
                 "HO", "BK", "G5", "9C", "JD"]
    list1 = []
    for i in range(0, 1300):
        random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(100, 9999))
        phone_num = "{}{:0<3}".format(start_num[random_pn], random_num)
        list1.append(phone_num)
    flight_number_list = list(set(list1))
    # print(flight_number_list)
    return ["航班号"] * 1000, [i for i in range(1, 1001)], flight_number_list[0:1000]


# 订单号 数字	11位
def aviation_order_no():
    order_no = []
    for i in range(0, 1100):
        random_num = random.randint(1000000, 9999999)
        phone_num = f'16{random_num}91'
        order_no.append(phone_num)
    order_no_list = list(set(order_no))[0:1000]
    return ["订单编号"] * 1000, [i for i in range(1, 1001)], order_no_list


# 客服电话 10位 开头400，021，028，010固定，还有开头三位数固定的5位数：955**，950**，开头三位数固定的5-6位可变：953**
def aviation_service_tel_num():
    start_num = ["400", "021", "028", "010", "955", "950", "953"]
    service_tel_num = []
    for i in range(0, 1300):
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
    res_service_tel_num_list = service_tel_num_list[0:1000]
    # print(res_service_tel_num_list)
    return ["客服电话"] * 1000, [i for i in range(1, 1001)], res_service_tel_num_list


# 目的地 4位以上 字母 地点拼写
def aviation_dest():
    pass


# 姓名 4位以上 字母 名字拼写
def aviation_name():
    aviation_name = []
    for i1 in range(1200):
        # xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        xing = ["ZHAO", "QIAN", "SUN", "LI", "ZHOU", "WU", "ZHENG", "WANG", "FENG", "CHU", "WEI", "JIANG", "SHEN",
                "HAN", "YANG", "ZHU", "QIN", "YOU", "XU", "HE", "SHI", "ZHANG", "KONG", "CAO", "YAN", "HUA", "WEI",
                "JIANG", "TAO", "MA", "CHEN"]
        # ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
        ming = ["YU", "ZHANG", "GU", "JUN", "HONG", "DOU", "XIN", "FU", "XING", "FEN", "YI", "ZHEN", "DI", "JIE",
                "HENG", "LU", "JIN", "SAN", "JIANG", "ER", "DAI", "WU", "HU", "SI", "YI"]
        X = random.choice(xing)
        M = "".join(random.choice(ming) for i in range(2))
        aviation_name.append(X + M)
    name_list = list(set(aviation_name))[0:1000]
    return ["姓名"] * 1000, [i for i in range(1, 1001)], name_list


# 机票号 13位 数字 前三位固定：东方航空781；国际航空999；南方航空784；上海航空774；
# 厦门航空731；深圳航空479；海南航空880；山东航空324；四川航空876；华夏航空883；奥凯航空866；联合航空822
def aviation_ticket_no():
    start_num = [781, 999, 784, 774, 731, 479, 880, 324, 876, 883, 866, 822]
    ticket_no = []
    for i in range(0, 1200):
        random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(1000000000, 9999999999))
        phone_num = "{}{:0<10}".format(start_num[random_pn], random_num)
        ticket_no.append(phone_num)
    ticket_no_list = list(set(ticket_no))[0:1000]
    # print(ticket_no_list)
    return ["机票号"] * 1000, [i for i in range(1, 1001)], ticket_no_list


# 登机时间 四位数字 前两位为00-23，后两位为00-59
def aviation_board_time():
    board_time = []
    for i in range(2000):
        random_num1 = str(random.randint(0, 23))
        random_num2 = str(random.randint(0, 59))
        if len(random_num1) < 2:
            random_num1 = f'0{random_num1}'
        if len(random_num2) < 2:
            random_num2 = f'0{random_num2}'
        time = f'{random_num1}{random_num2}'
        board_time.append(time)
    board_time_list = list(set(board_time))[:1000]
    # print(board_time_list)
    return ["登机时间"] * 1000, [i for i in range(1, 1001)], board_time_list


# 登机日期字母加数字 5位  最后三位是月份缩写，数字可从01至29(由于2月比较特殊，以及有的月份是30天)
def aviation_board_data():
    start_num = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    board_data = []
    for i in range(0, 1000):
        random_pn = random.randrange(0, len(start_num))
        random_num = str(random.randint(0, 29))
        if len(random_num) < 2:
            random_num = f'0{random_num}'
        phone_num = f'{random_num}{start_num[random_pn]}'
        board_data.append(phone_num)
    board_data_list = list(set(board_data))
    num = 1000 - len(board_data_list)
    board_data_list.extend([''] * num)
    # print(board_data_list)
    return ["登机日期"] * 1000, [i for i in range(1, 1001)], board_data_list

def fast_food():
    type1, number1, txt1 = fast_food_order_no()
    type2, number2, txt2 = fast_food_tel_num()
    type3, number3, txt3 = fast_food_waybill_no()
    type4, number4, txt4 = fast_food_pick_code()

    type_list = type1 + type2 + type3 + type4
    number_list = number1 + number2 + number3 + number4
    txt_list = txt1 + txt2 + txt3 + txt4
    # print(type_list)
    return type_list, number_list, txt_list

# 订单编号 数字/数字加字母 13-19位 字母位置固定大写
def fast_food_order_no():
    order_no = []
    for i in range(0, 1000):
        num1 = random.choice(string.ascii_uppercase)
        random_num = str(random.randint(1000000000000, 9999999999999999999))
        phone_num = f'{num1}{random_num}'
        order_no.append(phone_num)
    order_no_list = list(set(order_no))[0:1000]
    # print(order_no_list)
    return ["订单编号"] * 1000, [i for i in range(1, 1001)], order_no_list


# 虚拟手机号码 数字 11位
def fast_food_tel_num():
    tel_num = []
    for i in range(0, 1200):
        random_num = str(random.randint(0, 99999999))
        phone_num = "{}{:0<8}".format(187, random_num)
        tel_num.append(phone_num)
    tel_num_list = list(set(tel_num))[0:1000]
    # print(tel_num_list)
    return ["虚拟手机号码"] * 1000, [i for i in range(1, 1001)], tel_num_list


# 运单号 可变4位
def fast_food_waybill_no():
    waybill_no = []
    for i in range(0, 1100):
        random_num = str(random.randint(1000, 9999))
        phone_num = f'909{random_num}'
        waybill_no.append(phone_num)
    waybill_no_list = list(set(waybill_no))[0:1000]
    # print(waybill_no_list)
    return ["运单号"] * 1000, [i for i in range(1, 1001)], waybill_no_list


#取件码 数字 四位以上
def fast_food_pick_code():
    pick_code = []
    for i in range(0, 1100):
        random_num = str(random.randint(1000, 99999))
        pick_code.append(random_num)
    pick_codeo_list = list(set(pick_code))[0:1000]
    # print(pick_codeo_list)
    return ["取件码"] * 1000, [i for i in range(1, 1001)], pick_codeo_list


def main():
    type_list, number_list, txt_list = aviation()
    df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    fast_food_type_list, fast_food_number_list, fast_food_txt_list = fast_food()
    df2 = pd.DataFrame({'种类': fast_food_type_list, "编号": fast_food_number_list, "文本": fast_food_txt_list})

    with pd.ExcelWriter('数字字母收集.xlsx') as writer:
        df1.to_excel(writer, sheet_name='航空', index=False)
        df2.to_excel(writer, sheet_name='快餐', index=False)


if __name__ == '__main__':
    main()
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


def medial():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = medial_order_no()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = medial_refund_no()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = medial_residual_flow()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = medial_broadband_number()

    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = medial_psw()
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = medial_psw1()
    domain7_1, domain7_2, UtteranceType7_1, UtteranceType7_2, Category7_1, Category7_2, text7_1, text7_2 = medial_ver_code()
    domain8_1, domain8_2, UtteranceType8_1, UtteranceType8_2, Category8_1, Category8_2, text8_1, text8_2 = medial_email()
    domain9_1, domain9_2, UtteranceType9_1, UtteranceType9_2, Category9_1, Category9_2, text9_1, text9_2 = medial_email1()

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1 + domain6_1 + domain7_1+domain8_1+domain9_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2 + domain6_2 + domain7_2+domain8_2+domain9_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 +UtteranceType5_1 + UtteranceType6_1 + UtteranceType7_1+ UtteranceType8_1 + UtteranceType8_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 +UtteranceType5_2 + UtteranceType6_2 + UtteranceType7_2 + UtteranceType8_2 + UtteranceType8_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1 + Category6_1 + Category7_1+ Category8_1 + Category9_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2 + Category6_2 + Category7_2+ Category8_2 + Category9_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1 + text6_1 + text7_1+ text8_1 + text9_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2 + text6_2 + text7_2+ text8_2 + text9_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


# 订单编号 19位  NumbersOnly 307******
def medial_order_no():
    order_no = []
    for i in range(0, 11000):
        random_num = str(random.randint(1000000000000000, 9999999999999999))
        res_num = f'307{random_num}'
        order_no.append(res_num)
    order_no_list = list(set(order_no))
    # print(order_no_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "订单编号"] * 3000, ["订单编号"] * 7000, order_no_list[0:3000], order_no_list[3001:10001]


# 退款编号 4位以上
def medial_refund_no():
    refund_no = []
    for i in range(0, 11000):
        random_num = str(random.randint(1000, 999999))
        refund_no.append(random_num)
    refund_no_list = list(set(refund_no))
    # print(order_no_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "退款编号"] * 3000, ["退款编号"] * 7000, refund_no_list[0:3000], refund_no_list[3001:10001]


# 剩余流量 4位以上 NumbersAndLetters G.M.KB字母大写，位置固定，1TB=1024GB 1GB=1024MB 1MB=1024KB 1KB=1024B 1B=8b
def medial_residual_flow():
    residual_flow = []
    for i in range(0, 11000):
        random_num1 = str(random.randint(1, 999999))
        random_num2 = random.choice(['G','M','KB'])
        if int(random_num1)>1024 and random_num2 in ['M','KB']:
            random_num1= str(int(int(random_num1)/1024))
        random_num = f'{random_num1}{random_num2}'
        residual_flow.append(random_num)
    residual_flow_list = list(set(residual_flow))
    # print(order_no_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
           ["剩余流量"] * 3000, ["剩余流量"] * 7000, residual_flow[0:3000], residual_flow[3001:10001]


# 宽带号码 4位以上 NumbersOnly 241010107651
def medial_broadband_number():
    broadband_number = []
    for i in range(0, 11000):
        random_num = str(random.randint(1000, 999999))
        broadband_number.append(random_num)
    broadband_number_list = list(set(broadband_number))
    # print(broadband_number_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "宽带号码"] * 3000, ["宽带号码"] * 7000, broadband_number_list[0:3000], broadband_number_list[3001:10001]


#  密码 LettersOnly 4位以上 字母大小写皆可
def medial_psw():
    psw = []
    for i in range(0, 11000):
        random_num1 = ''.join(random.sample(string.ascii_letters, 4))
        random_num2 = ''.join(random.sample(string.ascii_letters, 5))
        psw.append(random_num1)
        psw.append(random_num2)
    psw_list = list(set(psw))
    # print(psw_list)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["LettersOnly"] * 3000, [
        "LettersOnly"] * 7000, ["密码"] * 3000, ["密码"] * 7000, psw_list[0:3000], psw_list[3001:10001]


#  密码 NumbersAndLetters 4位以上 字母大小写皆可
def medial_psw1():
    psw1 = []
    for i in range(0, 11000):
        num = str(random.randint(1000, 999999))
        random_num1 = ''.join(random.sample(string.ascii_letters, 4))
        # random_num2 = ''.join(random.sample(string.ascii_letters, 5))
        res = f'{num}{random_num1}'
        psw1.append(random_num1)
    psw_list1 = list(set(psw1))
    # print(psw_list1)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, [
        "NumbersOnly"] * 7000, ["密码"] * 3000, ["密码"] * 7000, psw_list1[0:3000], psw_list1[3001:10001]


#  验证码 NumbersOnly 415486，1578，03504 4位以上 0-9随机数字
def medial_ver_code():
    ver_code = []
    for i in range(0, 11000):
        num = str(random.randint(1000, 999999))
        ver_code.append(num)
    ver_code_list = list(set(ver_code))
    # print(psw_list1)
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, [
        "NumbersOnly"] * 7000, ["验证码"] * 3000, ["验证码"] * 7000, ver_code_list[0:3000], ver_code_list[3001:10001]


# 邮箱地址  @前4-10位 LettersOnly zhangsan@sina.com, wangwu@outlook.com    @sina.com, @sohu.com, @outlook.com
def medial_email():
    aviation_name = []
    for i1 in range(12000):
        # xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        xing = ["ZHAO", "QIAN", "SUN", "LI", "ZHOU", "WU", "ZHENG", "WANG", "FENG", "CHU", "WEI", "JIANG", "SHEN",
                "HAN", "YANG", "ZHU", "QIN", "YOU", "XU", "HE", "SHI", "ZHANG", "KONG", "CAO", "YAN", "HUA", "WEI",
                "JIANG", "TAO", "MA", "CHEN"]
        # ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
        ming = ["YU", "ZHANG", "GU", "JUN", "HONG", "DOU", "XIN", "FU", "XING", "FEN", "YI", "ZHEN", "DI", "JIE",
                "HENG", "LU", "JIN", "SAN", "JIANG", "ER", "DAI", "WU", "HU", "SI", "YI"]
        X = random.choice(xing)
        M = "".join(random.choice(ming) for i in range(2))
        email = random.choice(["@sina.com", "@sohu.com", "@outlook.com"])
        res_num= f'{X}{M}{email}'
        aviation_name.append(res_num)
    email_list = list(set(aviation_name))
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["LettersOnly"] * 3000, [
        "LettersOnly"] * 7000, ["邮箱地址"] * 3000, ["邮箱地址"] * 7000, email_list[0:3000], email_list[3001:10001]


# 邮箱地址  @前4-10位 NumbersAndLetters 18655402@163.com, Andy2000@sina.com, zhangsan@163.com    @sina.com, @sohu.com, @outlook.com, @qq.com, @163.com, @126.com
def medial_email1():
    aviation_name = []
    for i1 in range(12000):
        # xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        xing = ["ZHAO", "QIAN", "SUN", "LI", "ZHOU", "WU", "ZHENG", "WANG", "FENG", "CHU", "WEI", "JIANG", "SHEN",
                "HAN", "YANG", "ZHU", "QIN", "YOU", "XU", "HE", "SHI", "ZHANG", "KONG", "CAO", "YAN", "HUA", "WEI",
                "JIANG", "TAO", "MA", "CHEN"]
        # ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
        ming = ["YU", "ZHANG", "GU", "JUN", "HONG", "DOU", "XIN", "FU", "XING", "FEN", "YI", "ZHEN", "DI", "JIE",
                "HENG", "LU", "JIN", "SAN", "JIANG", "ER", "DAI", "WU", "HU", "SI", "YI"]
        X = random.choice(xing)
        M = "".join(random.choice(ming) for i in range(2))
        email = random.choice(["@sina.com", "@sohu.com", "@outlook.com", "@qq.com", "@163.com", "@126.com"])
        num = str(random.randint(10,99999))
        res_num1 = f'{num}{email}'
        res_num = f'{X}{M}{email}'
        aviation_name.append(res_num)
        aviation_name.append(res_num1)
    email_list = list(set(aviation_name))
    return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["LettersOnly"] * 3000, [
        "LettersOnly"] * 7000, ["邮箱地址"] * 3000, ["邮箱地址"] * 7000, email_list[0:3000], email_list[3001:10001]



def main():
    domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2 = medial()
    # print(type_list)
    # df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    #
    # with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

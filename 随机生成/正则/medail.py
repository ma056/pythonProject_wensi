# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : medail.py
@Author : wenjing
@Date : 2022/12/13 13:35
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


def mediaInternetTelecom():
    rule1 = r'^\d{19}$'
    rule2 = r'^\d{4,20}$'
    rule3 = r'^[1-9]{3,19}G$'
    rule4 = r'^\d{4,20}$'
    rule5 = r'^\d{4}-\d{1,16}$'
    rule6 = r'^[A-Za-z]{4,10}@gmail\.com$'
    rule7 = r'^[A-Za-z0-9]{4,10}@gmail\.com$'
    rule8 = r'^[a-z]{4,20}$'
    rule9 = r'^\d{4,20}$'
    rule10 = r'^[A-Za-z0-9]{4,20}$'
    rule11 = r'^\d{4,20}$'
    rule12 = r'^\d{4,20}$'
    rule13 = r'^0\d{9}$'
    rule14 = r'^[A-Za-z0-9]{4,20}$'
    # Order No. 19 digits  NumbersOnly   307******
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("MediaInternetTelecom","NumbersOnly","Order No.",rule1)
    # Refund Number  NumbersOnly     4-20 digits
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("MediaInternetTelecom","NumbersOnly","Refund Number",rule2)
    # Residual flow rate   NumbersAndLetters 4-20
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("MediaInternetTelecom","NumbersAndLetters","Residual flow rate",rule3)
    #   Broadband number NumbersOnly 4-20 241010000000.0
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = get_data("MediaInternetTelecom","NumbersOnly","Broadband number",rule4)
    # Wide band type    NumbersOnly 4-20 8316-555
    domain5_1, domain5_2, UtteranceType5_1, UtteranceType5_2, Category5_1, Category5_2, text5_1, text5_2 = get_data("MediaInternetTelecom","NumbersOnly","Wide band type",rule5)
    # Email Address LettersOnly abc@gmail.com
    domain6_1, domain6_2, UtteranceType6_1, UtteranceType6_2, Category6_1, Category6_2, text6_1, text6_2 = get_data("MediaInternetTelecom","LettersOnly","Email Address",rule6)
    # Email Address LettersOnly abc@gmail.com
    domain7_1, domain7_2, UtteranceType7_1, UtteranceType7_2, Category7_1, Category7_2, text7_1, text7_2 = get_data("MediaInternetTelecom","NumbersAndLetters","Email Address",rule7)
    # password      LettersOnly  4-20 digits    ytrf
    domain8_1, domain8_2, UtteranceType8_1, UtteranceType8_2, Category8_1, Category8_2, text8_1, text8_2 = get_data("MediaInternetTelecom","LettersOnly","password",rule8)
    # password      NumbersOnly  4-20 digits    1923
    domain9_1, domain9_2, UtteranceType9_1, UtteranceType9_2, Category9_1, Category9_2, text9_1, text9_2 = get_data("MediaInternetTelecom","NumbersOnly","password",rule9)
    # password      NumbersAndLetters  4-20 digits    ytrf
    domain10_1, domain10_2, UtteranceType10_1, UtteranceType10_2, Category10_1, Category10_2, text10_1, text10_2 = get_data("MediaInternetTelecom","NumbersAndLetters","password",rule10)
    # Verification code      NumbersOnly  4-20 digits    192399
    domain11_1, domain11_2, UtteranceType11_1, UtteranceType11_2, Category11_1, Category11_2, text11_1, text11_2 = get_data("MediaInternetTelecom","NumbersOnly","Verification code",rule11)
    # Sales/Collection     NumbersOnly  4-20 digits
    domain12_1, domain12_2, UtteranceType12_1, UtteranceType12_2, Category12_1, Category12_2, text12_1, text12_2 = get_data("MediaInternetTelecom","NumbersOnly","Sales/Collection",rule12)
    # Telephone Number  格式为0+9位     295732039       10digits
    domain13_1, domain13_2, UtteranceType13_1, UtteranceType13_2, Category13_1, Category13_2, text13_1, text13_2 = get_data("MediaInternetTelecom","NumbersOnly","Telephone Number",rule13)
    # Online account name? NumbersAndLetters    4-20 digits     as20201908
    domain14_1, domain14_2, UtteranceType14_1, UtteranceType14_2, Category14_1, Category14_2, text14_1, text14_2 = get_data("MediaInternetTelecom","NumbersAndLetters","Online account name?",rule14)

    domain_list1 = domain1_1 + domain2_1 + domain3_1 + domain4_1 + domain5_1 + domain6_1 + domain7_1 + domain8_1 + domain9_1 + domain10_1 + domain11_1 + domain12_1 + domain13_1 + domain14_1
    domain_list2 = domain1_2 + domain2_2 + domain3_2 + domain4_2 + domain5_2 + domain6_2 + domain7_2 + domain8_2 + domain9_2 + domain10_2 + domain11_2 + domain12_2 + domain13_2 + domain14_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1 + UtteranceType3_1 + UtteranceType4_1 + UtteranceType5_1 + UtteranceType6_1 + UtteranceType7_1 + UtteranceType8_1 \
                          + UtteranceType9_1 + UtteranceType10_1 + UtteranceType11_1 + UtteranceType12_1 + UtteranceType13_1 + UtteranceType14_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2 + UtteranceType3_2 + UtteranceType4_2 + UtteranceType5_2 + UtteranceType6_2 + UtteranceType7_2 + UtteranceType8_2 \
                          + UtteranceType9_2 + UtteranceType10_2 + UtteranceType11_2 + UtteranceType12_2 + UtteranceType13_2 + UtteranceType14_2
    Category_list1 = Category1_1 + Category2_1 + Category3_1 + Category4_1 + Category5_1 + Category6_1 + Category7_1 + Category8_1 + Category9_1 \
                     + Category10_1 + Category11_1 + Category12_1 + Category13_1 + Category14_1
    Category_list2 = Category1_2 + Category2_2 + Category3_2 + Category4_2 + Category5_2 + Category6_2 + Category7_2 + Category8_2 + Category9_2 \
                     + Category10_2 + Category11_2 + Category12_2 + Category13_2 + Category14_2
    text_list1 = text1_1 + text2_1 + text3_1 + text4_1 + text5_1 + text6_1 + text7_1 + text8_1 + text9_1 + text10_1 \
                 + text11_1 + text12_1 + text13_1 + text14_1
    text_list2 = text1_2 + text2_2 + text3_2 + text4_2 + text5_2 + text6_2 + text7_2 + text8_2 + text9_2 + text10_2 \
                 + text11_2 + text12_2 + text13_2 + text14_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2


mediaInternetTelecom()
# def media_order_no():
#     order_no = []
#     while len(order_no) < 10000:
#     # for i in range(0, 11000):
#         num = str(random.randint(1000000000000000000, 9999999999999999999))
#         order_no.append(num)
#         order_no = list(set(order_no))
#     # print(stock_number_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000,\
#            ["Order No."] * 3000, ["Order No."] * 7000, order_no[0:3000], order_no[3000:10000]
#
#
#
# def media_refund_num():
#     refund_num = []
#     while len(refund_num) < 10000:
#     # for i in range(0, 11000):
#         num = str(random.randint(1000, 99999999999999999999))
#         refund_num.append(num)
#         refund_num = list(set(refund_num))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, [
#         "NumbersOnly"] * 7000, \
#            ["Refund Number"] * 3000, ["Refund Number"] * 7000, refund_num[0:3000], refund_num[3000:10000]
#
#
#
# def media_residual_flow():
#     residual_flow = []
#     while len(residual_flow) < 10000:
#     # for i in range(0, 11000):
#         random_num1 = str(random.randint(1000, 99999999999))
#         random_num = f'{random_num1}G'
#         residual_flow.append(random_num)
#         residual_flow = list(set(residual_flow))
#     # print(residual_flow_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersAndLetters"] * 3000, [
#         "NumbersAndLetters"] * 7000, ["Residual flow rate"] * 3000, ["Residual flow rate"] * 7000, \
#            residual_flow[0:3000], residual_flow[ 3000:10000]
#
#
#
# def media_broadband_num():
#     broadband_num = []
#     while len(broadband_num) < 10000:
#     # for i in range(0, 11000):
#         num = str(random.randint(1000, 99999999999999999999))
#         broadband_num.append(num)
#         broadband_num = list(set(broadband_num))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, \
#            ["NumbersOnly"] * 7000, ["Broadband number"] * 3000, ["Broadband number"] * 7000,\
#            broadband_num[0:3000], broadband_num[3000:10000]
#
#
#
# def media_wide_band():
#     wide_band = []
#     while len(wide_band) < 10000:
#     # for i in range(0, 11000):
#         num = str(random.randint(1000, 9999))
#         num1 = str(random.randint(0, 999)).zfill(3)
#         wide_band.append(f'{num}-{num1}')
#         wide_band = list(set(wide_band))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, \
#            ["NumbersOnly"] * 7000, ["Wide band type"] * 3000, ["Wide band type"] * 7000, wide_band[0:3000], \
#            wide_band[3000:10000]
#
#
#
# def media_email_address():
#     email_address = []
#     while len(email_address) < 10000:
#     # for i in range(0, 11000):
#         num1 = ''.join(random.sample(string.ascii_letters, 4))
#         num2 = ''.join(random.sample(string.ascii_letters, 6))
#         num3 = ''.join(random.sample(string.ascii_letters, 10))
#         email_address.append(f'{num1}@gmail.com')
#         email_address.append(f'{num2}@gmail.com')
#         email_address.append(f'{num3}@gmail.com')
#         email_address = list(set(email_address))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["LettersOnly"] * 3000, [
#         "LettersOnly"] * 7000, ["Email Address"] * 3000, ["Email Address"] * 7000, email_address[0:3000],\
#            email_address[3000:10000]
#
#
#
# def media_email_address1():
#     email_address1 = []
#     while len(email_address1) < 10000:
#     # for i in range(0, 11000):
#         num1 = ''.join(random.sample(string.ascii_letters, 4))
#         num1_1 = str(random.randint(0, 9999))
#         num2 = ''.join(random.sample(string.ascii_letters, 6))
#         num2_1 = str(random.randint(0, 9999))
#         num3 = ''.join(random.sample(string.ascii_letters, 10))
#         num3_1 = str(random.randint(0, 9999))
#         email_address1.append(f'{num1}{num1_1}@gmail.com')
#         email_address1.append(f'{num2}{num2_1}@gmail.com')
#         email_address1.append(f'{num3}{num3_1}@gmail.com')
#         email_address = list(set(email_address1))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["LettersOnly"] * 3000, \
#            ["LettersOnly"] * 7000, ["Email Address"] * 3000, ["Email Address"] * 7000, email_address[0:3000],\
#            email_address[3000:10000]
#
#
#
# def media_psw():
#     psw = []
#     while len(psw) < 10000:
#     # for i in range(0, 11000):
#         num1 = ''.join(random.sample(string.ascii_letters, 4))
#         num2 = ''.join(random.sample(string.ascii_letters, 6))
#         num3 = ''.join(random.sample(string.ascii_letters, 10))
#         psw.append(num1)
#         psw.append(num2)
#         psw.append(num3)
#         psw = list(set(psw))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["LettersOnly"] * 3000, \
#            ["LettersOnly"] * 7000,["password"] * 3000, ["password"] * 7000, psw[0:3000], psw[3000:10000]
#
#
#
# def media_psw1():
#     psw1 = []
#     while len(psw1) < 10000:
#     # for i in range(0, 11000):
#         num1 = str(random.randint(1000, 99999999999999999999))
#         psw1.append(num1)
#         psw1 = list(set(psw1))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, \
#            ["NumbersOnly"] * 7000, ["password"] * 3000, ["password"] * 7000, psw1[0:3000], psw1[3000:10000]
#
#
#
# def media_psw2():
#     psw2 = []
#     while len(psw2) < 10000:
#     # for i in range(0, 11000):
#         num1 = ''.join(random.sample(string.ascii_letters, 4))
#         num1_1 = str(random.randint(0, 999))
#         num2 = ''.join(random.sample(string.ascii_letters, 6))
#         num2_1 = str(random.randint(0, 999))
#         num3 = ''.join(random.sample(string.ascii_letters, 10))
#         num3_1 = str(random.randint(0, 999))
#         psw2.append(f'{num1}{num1_1}')
#         psw2.append(f'{num2}{num2_1}')
#         psw2.append(f'{num3}{num3_1}')
#         psw2 = list(set(psw2))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersAndLetters"] * 3000,\
#          ["NumbersAndLetters"] * 7000, ["password"] * 3000, ["password"] * 7000, psw2[0:3000], psw2[3000:10000]
#
#
#
# def media_ver_code():
#     ver_code = []
#     while len(ver_code) < 10000:
#     # for i in range(0, 11000):
#         num1 = str(random.randint(1000, 99999999999999999999))
#         ver_code.append(num1)
#         ver_code = list(set(ver_code))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000,\
#            ["Verification code"] * 3000, ["Verification code"] * 7000, ver_code[0:3000], ver_code[3000:10000]
#
#
#
# def media_sale_collect():
#     sale_collect = []
#     while len(sale_collect) < 10000:
#     # for i in range(0, 11000):
#         num1 = str(random.randint(1000, 99999999999999999999))
#         sale_collect.append(num1)
#         sale_collect = list(set(sale_collect))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000,\
#            ["Sales/Collection"] * 3000, ["Sales/Collection"] * 7000, sale_collect[0:3000], sale_collect[3000:10000]
#
#
#
# def media_tel_number():
#     tel_number = []
#     while len(tel_number) < 10000:
#     # for i in range(0, 11000):
#         num1 = str(random.randint(0, 999999999)).zfill(9)
#         tel_number.append(f'0{num1}')
#         tel_number = list(set(tel_number))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000,\
#            ["Telephone Number"] * 3000, ["Telephone Number"] * 7000, tel_number[0:3000], tel_number[3000:10000]
#
#
#
# def media_online_account():
#     online_account = []
#     while len(online_account) < 10000:
#     # for i in range(0, 11000):
#         num1 = ''.join(random.sample(string.ascii_letters, 2))
#         num1_1 = str(random.randint(0, 999))
#         num2 = ''.join(random.sample(string.ascii_letters, 6))
#         num2_1 = str(random.randint(0, 999))
#         num3 = ''.join(random.sample(string.ascii_letters, 3))
#         num3_1 = str(random.randint(0, 999))
#         online_account.append(f'{num1}{num1_1}')
#         online_account.append(f'{num2}{num2_1}')
#         online_account.append(f'{num3}{num3_1}')
#         online_account = list(set(online_account))
#     # print(refund_num_list)
#     return ["MediaInternetTelecom"] * 3000, ["MediaInternetTelecom"] * 7000, ["NumbersAndLetters"] * 3000, \
#            ["NumbersAndLetters"] * 7000, ["Online account name?"] * 3000, ["Online account name?"] * 7000, \
#            online_account[0:3000],online_account[3000:10000]
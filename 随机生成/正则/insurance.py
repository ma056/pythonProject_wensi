# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : insurance.py
@Author : wenjing
@Date : 2022/12/13 13:21
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


def insurance():
    rule1 = r'^[A-Z]{2}\d{7}$'
    rule2 = r'^[A-Z]{2}\d{3}[A-Z]{2}$'
    rule3 = r'^[A-Z]{6}\d{2}[A-Z]{1}\d{2}[A-Z]{1}\d{3}[A-Z]{1}$'
    # Passport Number   NumbersAndLetters  9 digits YA2672719       格式为2个字母+7个数字
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = get_data("Insurance","NumbersAndLetters","Passport Number",rule1)
    # License plate number   NumbersAndLetters  7 digits 2个字母+3个数字+2个字母
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = get_data("Insurance","NumbersAndLetters","License plate number",rule2)
    # Personal identification number   NumbersAndLetters  16 digits RSSMRA70A01L726S 首字母（RSSMRA）出生年份（70）出生城镇（A01L）复选标记（726S）
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = get_data("Insurance","NumbersAndLetters","Personal identification number",rule3)

    domain_list1 = domain1_1 + domain2_1 +domain3_1
    domain_list2 = domain1_2 + domain2_2+domain3_2
    UtteranceType_list1 = UtteranceType1_1 + UtteranceType2_1+UtteranceType3_1
    UtteranceType_list2 = UtteranceType1_2 + UtteranceType2_2+UtteranceType3_2
    Category_list1 = Category1_1 + Category2_1+Category3_1
    Category_list2 = Category1_2 + Category2_2+Category3_2
    text_list1 = text1_1 + text2_1+text3_1
    text_list2 = text1_2 + text2_2+text3_2
    # print(text_list1)
    return domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2

insurance()

# def insurance_passport_number():
#     passport_number = []
#     # while len(passport_number) < 10000:
#     for i in range(0, 110000):
#         num1 = ''.join(random.sample(string.ascii_uppercase, 2))
#         num2 = str(random.randint(0, 9999999)).zfill(7)
#         passport_number.append(f'{num1}{num2}')
#     passport_number = list(set(passport_number))
#     return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, \
#            ["Passport Number"] * 3000, ["Passport Number"] * 7000, passport_number[0:3000], \
#            passport_number[3000:10000]
#
#
#
# def insurance_license_plate():
#     license_plate = []
#     # while len(license_plate) < 10000:
#     for i in range(0, 110000):
#         num1 = ''.join(random.sample(string.ascii_uppercase, 2))
#         num2 = str(random.randint(0, 999)).zfill(3)
#         num3 = ''.join(random.sample(string.ascii_uppercase, 2))
#         license_plate.append(f'{num1}{num2}{num3}')
#     license_plate = list(set(license_plate))
#     return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
#         "License plate number"] * 3000, ["License plate number"] * 7000, license_plate[0:3000], \
#            license_plate[3000:10000]
#
#
# # Personal identification number   NumbersAndLetters  16 digits RSSMRA70A01L726S 首字母（RSSMRA）出生年份（70）出生城镇（A01L）复选标记（726S）
# def insurance_personal_id():
#     personal_id = []
#     # while len(personal_id) < 10000:
#     for i in range(0, 110000):
#         num1 = ''.join(random.sample(string.ascii_uppercase, 6))
#         num2 = str(random.randint(0, 99)).zfill(2)
#         num3_1 = ''.join(random.sample(string.ascii_uppercase, 1))
#         num3_2 = str(random.randint(0, 99)).zfill(2)
#         num3_3 = ''.join(random.sample(string.ascii_uppercase, 1))
#         num4_1 = str(random.randint(0, 999)).zfill(3)
#         num4_2 = ''.join(random.sample(string.ascii_uppercase, 1))
#         personal_id.append(f'{num1}{num2}{num3_1}{num3_2}{num3_3}{num4_1}{num4_2}')
#     personal_id = list(set(personal_id))
#     return ["Insurance"] * 3000, ["Insurance"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
#         "Personal identification number"] * 3000, ["Personal identification number"] * 7000, personal_id[0:3000], \
#            personal_id[3000:10000]
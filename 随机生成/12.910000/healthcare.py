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


def healthcare():
    domain1_1, domain1_2, UtteranceType1_1, UtteranceType1_2, Category1_1, Category1_2, text1_1, text1_2 = healthcare_national_drug_approval()
    domain2_1, domain2_2, UtteranceType2_1, UtteranceType2_2, Category2_1, Category2_2, text2_1, text2_2 = healthcare_registration_no()
    domain3_1, domain3_2, UtteranceType3_1, UtteranceType3_2, Category3_1, Category3_2, text3_1, text3_2 = healthcare_batch_number()
    domain4_1, domain4_2, UtteranceType4_1, UtteranceType4_2, Category4_1, Category4_2, text4_1, text4_2 = healthcare_receipt_no()


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


# 国药准字 NumbersAndLetters  9位  Z20043804   第一个字母大写：H、Z、S、B、T、F、J
def healthcare_national_drug_approval():
    drug_approval = []
    for i in range(0, 11000):
        num1 = random.choice(["H","Z","S","B","T","F","J"])
        random_num = str(random.randint(10000000, 99999999))
        res_num = f'{num1}{random_num}'
        drug_approval.append(res_num)
    drug_approval_list = list(set(drug_approval))
    # print(drug_approval_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersAndLetters"] * 3000, ["NumbersAndLetters"] * 7000, [
        "国药准字"] * 3000, ["国药准字"] * 7000, drug_approval_list[0:3000], drug_approval_list[3001:10001]


# 注册证编号 NumbersOnly 11位 20168483047 前四位为年份，范围可设为1940-2022
def healthcare_registration_no():
    registration_no = []
    for i in range(0, 11000):
        year = str(random.randint(1940, 2020))
        random_num = str(random.randint(1000000, 9999999))
        res_num = f'{year}{random_num}'
        registration_no.append(res_num)
    registration_no_list = list(set(registration_no))
    # print(registration_no_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "注册证编号"] * 3000, ["注册证编号"] * 7000, registration_no_list[0:3000], registration_no_list[3001:10001]


# 生产批号 NumbersOnly 6位 140928 范围可设为00-99/01-12/01-29
def healthcare_batch_number():
    batch_number = []
    for i in range(0, 13000):
        num1 = str(random.randint(00, 99)).zfill(2)
        num2 = str(random.randint(1, 12)).zfill(2)
        num3 = str(random.randint(1, 29)).zfill(2)
        res_num = f'{num1}{num2}{num3}'
        batch_number.append(res_num)
    batch_number_list = list(set(batch_number))
    # print(batch_number_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "生产批号"] * 3000, ["生产批号"] * 7000, batch_number_list[0:3000], batch_number_list[3001:10001]


# 收据单号 NumbersOnly  7位 1147152
def healthcare_receipt_no():
    receipt_no = []
    for i in range(0, 11000):
        num = str(random.randint(1000000, 9999999)).zfill(2)
        receipt_no.append(num)
    receipt_no_list = list(set(receipt_no))
    # print(receipt_no_list)
    return ["HealthCare"] * 3000, ["HealthCare"] * 7000, ["NumbersOnly"] * 3000, ["NumbersOnly"] * 7000, [
        "收据单号"] * 3000, ["收据单号"] * 7000, receipt_no_list[0:3000], receipt_no_list[3001:10001]

def main():
    domain_list1, domain_list2, UtteranceType_list1, UtteranceType_list2, Category_list1, Category_list2, text_list1, text_list2 = healthcare()
    # print(type_list)
    # df1 = pd.DataFrame({'种类': type_list, "编号": number_list, "文本": txt_list})
    #
    # with pd.ExcelWriter('数字字母收集excel_2.xlsx') as writer:
    #     df1.to_excel(writer, sheet_name='金融', index=False)


if __name__ == '__main__':
    main()

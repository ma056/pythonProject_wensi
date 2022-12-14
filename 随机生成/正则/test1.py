# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : test1.py
@Author : wenjing
@Date : 2022/12/13 11:09
"""
import exrex

tel_train_number = []
while len(tel_train_number) < 100:
    # rule = r'^[0-9]{4}$'
    # rule1 = r'^[A-Z]{7,10}|[A-Z]{4,5}$'
    # rule = r"^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$"
    # rule = r'^(19\d{2}|20\d{2})(0[1-9]|1[0-2])((0?[1-9])|((1|2)[0-9])|30|31)\d{8}'
    # rule=r'[A-Z][A-Za-z]{2,3}\d{4}$'
    # rule =  r'^(19\d{2}|20\d{2})(0[1-9]|1[0-2])$'
    # rule = r'\d{16}$'
    # rule = r'^[A-Z]{6}\d{2}[A-Z]{1}\d{2}[A-Z]{1}\d{3}[A-Z]{1}$'
    # rule = r'^[A-Z]{6}\d{2}[J|F|M|A|S|O|N|D]((0?[1-9])|((1|2)[0-9])|30|31)[A-Z]{1}\d{3}[A-Z]{1}$'
    # rule = r'^[A-Za-z]{1}\d{3}$'
    # rule = r'^((0?[1-9])|((1|2)[0-9])|30|31)(0[1-9]|1[0-2])(19\d{2}|20\d{2})\d{8}'
    # rule = r'^[A-Za-z0-9]{4,10}(@gmail\.com|@outlook\.it|@outlook\.com|@live\.it|@hotmail\.com)$'
    # rule = r'^(19\d{2}|20\d{2})(0[1-9]|1[0-2])$'
    rule = r'^((0[1-9])|((1|2)[0-9])|30|31)(0[1-9]|1[0-2])(19\d{2}|20\d{2})\d{8}$'
    random_str = exrex.getone(rule)
    tel_train_number.append(random_str)
    # tel_train_number.append(phone_number_str1)
    tel_train_number = list(set(tel_train_number))
print(tel_train_number)
# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : test.py
@Author : wenjing
@Date : 2022/12/14 9:49
"""
import exrex


def main():
    random_list = []
    a = {}
    while len(random_list) < 10000:
        rule = r'^\d{4}$'
        random_str = exrex.getone(rule)
        random_list.append(random_str)
        random_list = list(set(random_list))
        # print(random_str)
        # print(random_list)
        if len(random_list) not in a.keys():
            a[len(random_list)] = [1]
        else:
            a[len(random_list)].append(1)
            # b = len(a[len(random_list)])
            # print(f'bbbbbbbb:{b}')
            if len(a[len(random_list)]) > 100:
                break

        # print(f'str:{random_str}-len:{len(random_list)}')
        # print(f'--------------------------------------{random_list}')
        # print(f'========================================{a}')
        # print(f'str:{random_str}---len:{len(random_list)}')
    return random_list

aq = main()
print(aq)
print(len(aq))

# def airline_boarding_time():
#     boarding_number = []
#     # while len(boarding_number) < 10000:
#     for i in range(0, 100000):
#         rule = r'^[0-9]{4}$'
#         num = exrex.getone(rule)
#         boarding_number.append(num)
#     boarding_number = list(set(boarding_number))
#     # number = 10000 - len(boarding_number)
#     # boarding_number.extend([''] * number)
#     print(boarding_number)
#     return boarding_number
# print(airline_boarding_time())

# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 最终版.py
@Author : wenjing
@Date : 2022/12/6 15:11
"""
# import json
# info_dict = {'name': 'Joe', 'age': 20, 'job': 'driver'}
# # dumps 将数据转换成字符串
# info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '))
# # 显示数据类型
# if 'age' in info_json:
#     print(111)
# else:
#     print(22)
# print(type(info_json))
num = 0
for i in range(1,10):
    num = num+i
    break
num = num+5
print(num)

# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 1.py
@Author : wenjing
@Date : 2022/11/28 16:48
"""
import pandas as pd
# a = pd.read_excel(r'C:\Users\Mawenjing\Desktop\NSS_LQA_20221122.xlsx')
# a = a.drop(0)
df_C78C3 = pd.DataFrame(pd.read_excel(r'C:\Users\Mawenjing\Downloads\NSS_LQA_20221122.xlsx',header = 1))
b = df_C78C3['Page URL'].values.tolist()
for i in b:
    # if 'https://sell.amazon.com/zh' in i:
    #     # url = f'{i.split("com/")[0]}com/en/{i.split("com/")[-1]}'
    #     # print(f'没有es{i}')
    #     print(11)
    # elif 'https://sell.amazon.com/es' in i:
    #     print(22)
    # else:
    #     url = f'{i.split("com/")[0]}com/en/{i.split("com/")[-1]}'
    #     print(url)
    print(i)
    if ('/zh' in i) or ('/es' in i):
        print(1)
    else:
        print(2)
# print(df_C78C3)

# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 最终版.py
@Author : wenjing
@Date : 2022/12/2 15:40
"""
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# 读入两个txt文件存入s1,s2字符串中
# s1 = open(r"C:\Users\Mawenjing\Downloads\file\file\txt\fi_FI _Script(drama,play)_Movies_TV shows_224_20220710.txt", 'rb').read()
# s2 = open(r"C:\Users\Mawenjing\Downloads\file\file\txt\fi_FI _Script(drama,play)_MoviesTV shows_191_20220928.txt", 'rb').read()
with open(r"C:\Users\Mawenjing\Downloads\file\file\txt\fi_FI _Script(drama,play)_Movies_TV shows_224_20220710.txt", 'rb') as f:
    a = []
    for i in f.readlines():
        a.append(i)
with open(r"C:\Users\Mawenjing\Downloads\file\file\txt\fi_FI _Script(drama,play)_MoviesTV shows_191_20220928.txt", 'rb') as f:
    b = []
    for i in f.readlines():
        b.append(i)
a = fuzz.token_set_ratio(a, b)
print(a)
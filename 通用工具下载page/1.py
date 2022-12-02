# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : draw_square.py
@Author : wenjing
@Date : 2022/11/25 15:20
"""
import html
from urllib.parse import quote
a = 'https://www.katana-land.de/en/self-defence?page=3'
print(quote(a))
print(quote(a.split('://')[1].replace('/','')))
# www.katana-land.deenself-defence%3Fpage%3D3
print(html.escape('https://www.katana-land.de/en/self-defence?page=3'.split('://')[1].replace('/','_')))

# sets = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
# for char in name:
#     if char in sets:
#         name = name.replace(char, '')
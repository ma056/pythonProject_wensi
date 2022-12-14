# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 邮政编码.py
@Author : wenjing
@Date : 2022/12/9 14:54
"""

import requests
from lxml import etree
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

}
url = 'http://www.xingtai.gov.cn/cycx/ybqh/200912/t20091224_272151.html'
res = requests.get(url, headers=headers)
tree = etree.HTML(res.content.decode())

# for prov_number in range(1, 20):
res1 = tree.xpath(f'//table/tbody/tr/td/text()')
a = []
try:
    for post in res1:
        a.append(str(post))
except Exception as e:
    print(e,post)
new_list = []
for i in a:
    if len(i) == 6:
        new_list.append(i)
print(new_list)
with open('12.910000/邮政编码.txt', 'w') as f:
    for i1 in new_list:
        aaa = i1 + '\n'
        print(i1)
        f.write(aaa)


    # res1 = tree.xpath(f'//table/tbody/tr/td/div[{prov_number}]//a')
    # for post in res1:
    #     print(post.xpath(f'//table/tbody/tr/td/div[{prov_number}]/h1/text()')[0])
    #     print(post.xpath('.//text()')[0])
    #     print(url.rstrip('/') + post.xpath('./@href')[0])



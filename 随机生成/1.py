# -- coding: utf-8 --
# 爬取全国的邮编
import requests

from lxml import etree

import csv

url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/2020/202003301019.html'

r = requests.get(url).text

html = etree.HTML(r)

c = html.xpath('//*[@id="2020年1月份县以上行政区划代码_30721"]/table/tr/td[2]//text()')

d = html.xpath('//*[@id="2020年1月份县以上行政区划代码_30721"]/table/tr/td[3]/text()')

e = zip(c,d)

for ee in e:

    with open('编码.csv', 'a+', newline='')as f:

        writer = csv.writer(f)

        writer.writerows([ee])
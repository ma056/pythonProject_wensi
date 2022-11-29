# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 饼状图.py
@Author : wenjing
@Date : 2022/11/29 10:25
"""
import matplotlib.pyplot as plt                #导入绘图包
import os
import pandas as pd

os.chdir(r'F:\公众号\6.学习python')   #设置成存放数据文件夹路径
date = pd.read_csv("股票数据.csv", encoding = 'GBK')    #读取数据

plt.rcParams['font.sans-serif'] = ['SimHei']   #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False    # 解决中文显示问题

date = date.set_index('日期')                 #把日期列设为索引
date.index = pd.to_datetime(date.index)       #把索引转为时间格式
result = date[['成交笔数']].groupby(date.index.year).sum()           #按年总计股票成交笔数
# plt.pie(result['成交笔数'], labels=result.index, autopct='%3.1f%%')  #以时间为标签，总计成交笔数为数据绘制饼图，并显示3位整数一位小数
# plt.title('股票每年成交笔数饼图')             #加标题
plt.pie(result['成交笔数'], labels=result.index, autopct='%3.1f%%', textprops={'color':'b', 'size':10, 'weight':'bold'})  #设置显示字体颜色、尺寸、加粗
plt.title('股票每年成交笔数饼图', c='b')             #加标题
plt.show()


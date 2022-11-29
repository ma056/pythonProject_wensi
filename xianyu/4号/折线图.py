# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 折线图.py
@Author : wenjing
@Date : 2022/11/29 10:02
"""
import matplotlib.pyplot as plt

# 设置默认字体，选择支持中文的字体以避免出现中文乱码情况
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

lst_temp3 = [10, 16, 17, 14, 12, 10, 12, 6, 6, 7, 8, 9, 12, 15, 15, 17, 18, 21, 16, 16, 20, 13, 15, 15, 15, 18, 20, 22,
             22, 22, 24]
lst_temp10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11,
              15, 5, 13, 17, 20, 11, 13, 12, 13, 6]
input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31]
fig, ax = plt.subplots()  # fig表示整张图片，ax表示图片中的各个图表
ax.set_title("某市2019年3月份与十月份气温变化趋势图", fontsize=20)  # 文章标题
ax.set_xlabel("日期", fontsize=14)  # 横坐标标签
ax.set_ylabel("气温/℃", fontsize=14)  # 纵坐标标签
ax.plot(input_values, lst_temp3, marker='*', label=u'三月份')  # 横坐标数据+纵坐标数据+图例
ax.plot(input_values, lst_temp10, marker='o', label=u'十月份')

plt.legend()  # 让图例生效
# 添加网格线
plt.grid(True, alpha=0.5, axis='both', linestyle=':')
plt.show()
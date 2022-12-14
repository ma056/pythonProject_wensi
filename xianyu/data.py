# -- coding: utf-8 --
from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectPercentile, chi2

import xlrd2

list1 = []


def e1(inpath):
    date = xlrd2.open_workbook(inpath, encoding_override='utf-8')
    table = date.sheets()[0]  # 选定表sheet1 或sheet2  0表示sheet1 1表示sheet2
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号
    for i in range(0, nrows):  # 第0行为表头
        alldate = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        result = alldate[0]  # 取出表中第一列数据
        list1.append(result)  # 创建


inpath = r"神经毒性物质(1).xlsx"  # excel文件所在路径
a1 = e1(inpath)
X, y = load_digits(return_X_y=True)
# print(list1)
X.shape
print(list1, 64)
X_new = SelectPercentile(chi2, percentile=20).fit_transform(X, y)
print(X_new)

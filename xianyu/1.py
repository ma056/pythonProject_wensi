# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : draw_square.py
@Author : wenjing
@Date : 2022/11/30 12:57
"""
import pandas as pd  # 获取数据#
import numpy as np

data = pd.read_excel(r"C:\Users\Mawenjing\Documents\WeChat Files\wxid_25mwm428j14h22\FileStorage\File\2022-11\数据1(1).xlsx")
print(data)
data2 = data.iloc[data['Accper'].values == '2021-12-31', [0, 2, 3, 4, 5, 6, 7, 8, 9]]

data2 = data2[data2 > 0]  # 数据清洗，去掉小于0的指标值和nan值#
data2 = data2.dropna()
print(data2)
from sklearn.preprocessing import MinMaxScaler  # 对指标数据X做标准化处理#

X = data2.iloc[:, 1:]
scaler = MinMaxScaler()
scaler.fit(X)
X = scaler.transform(X)

from sklearn.decomposition import PCA  # 对标准化后的X做主成分分析#

pca = PCA(n_components=0.95)
Y = pca.fit_transform(X)
tzxl = pca.components_
gxl = pca.explained_variance_ratio_
scaler = MinMaxScaler()
scaler.fit(Y)
Y = scaler.transform(Y)

from sklearn.cluster import KMeans

model = KMeans(n_clusters=5, random_state=0, max_iter=1000)
model.fit(Y)
c = model.labels_
center = model.cluster_centers_
center = pd.DataFrame(center)
center.columns = ['Y1', 'Y2', 'Y3']
print(center)
Fs = pd.Series(c, index=data2['Stkcd'].values)
Fs = Fs.sort_values()
Co = pd.read_excel(r"C:\Users\Mawenjing\Documents\WeChat Files\wxid_25mwm428j14h22\FileStorage\File\2022-11\上市公司信息.xlsx")
print(Co)
Co1 = pd.Series(Co['Stknme'].values, index=Co['Stkcd'].values)
for i in range(5):
    q = Co1[Fs[Fs == i].index]
    q = pd.DataFrame(q)
    q.to_excel('c' + str(i) + '.xlsx')
    Co1 = pd.Series(Co['Stknme'].values, index=Co['Stkcd'].values)
for i in range(5):
    q = Co1[Fs[Fs == i].index]
    q = pd.DataFrame(q)
    q.to_excel('c' + str(i) + '.xlsx')

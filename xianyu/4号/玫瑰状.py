import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# 设置字体格式
font = {
    'family': 'serif',
    'serif': 'Times New Roman',
    'weight': 'normal',
    'size': 10
}
plt.rc('font', **font)
plt.rc('axes.unicode_minus: False')


def plot_wind_rose():
    """绘制风速风向玫瑰图"""
    # 风速分布为16个方向
    columns = 'N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW'.split()
    # 风速分 4 段，每列数据表示各方向风速的频数统计值
    datas = {
        '0~0.2': [0.32, 0.24, 0.21, 0.38, 0.35, 0.22, 0.06, 0.28, 0.43, 0.43, 0.18, 0.16, 0.19, 0.23, 0.08, 0.18],
        '0.3~1.5': [0.32, 0.38, 0.28, 0.08, 0.12, 0.29, 0.30, 0.32, 0.31, 0.19, 0.33, 0.49, 0.30, 0.18, 0.40, 0.35],
        '1.6~3.3': [0.24, 0.18, 0.07, 0.39, 0.34, 0.17, 0.40, 0.25, 0.07, 0.24, 0.24, 0.13, 0.10, 0.28, 0.41, 0.21],
        '3.4~5.4': [0.10, 0.18, 0.42, 0.13, 0.18, 0.29, 0.22, 0.13, 0.17, 0.12, 0.23, 0.19, 0.40, 0.30, 0.09, 0.25]
    }
    df = pd.DataFrame(data=np.array(list(datas.values())), index=list(datas.keys()), columns=columns)
    # 获取 16 个方向的角度值
    degrees = np.linspace(0, 2 * np.pi, len(columns), endpoint=False)
    # 绘制扇型的宽度，可以自行调整
    width = np.pi / len(columns)
    # 开始绘图
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, projection='polar')
    for idx in df.index:
        # 每一行绘制一个扇形
        ax.bar(degrees, df.loc[idx], width=width, bottom=0.0, label=idx, tick_label=columns)
    # 设置零度方向北
    ax.set_theta_zero_location('N')
    # 逆时针方向绘图
    ax.set_theta_direction(-1)
    # plt.title('风速风向玫瑰图')
    # 将label显示出来， 并调整位置
    plt.legend(loc=4, bbox_to_anchor=(1.15, -0.07))
    plt.show()


def main():
    plot_wind_rose()


if __name__ == '__main__':
    main()

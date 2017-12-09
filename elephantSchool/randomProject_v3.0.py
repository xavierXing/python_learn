"""
    掷筛子: 科学计算

"""
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.font_manager import _rebuild
_rebuild()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    # 科学计算
    total_time = 10000
    roll_arr1 = np.random.randint(1, 7, size=total_time)
    roll_arr2 = np.random.randint(1, 7, size=total_time)
    roll_total = roll_arr1 + roll_arr2

    #数据可视化
    plt.hist(roll_total, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()

if __name__ == '__main__':
    main()
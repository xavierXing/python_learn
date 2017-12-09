"""
    掷筛子: 可视化模块
    散点图
"""

import random
import matplotlib.pyplot as plt

def roll_dice():
    roll = random.randint(1, 6)
    return roll

def main():
    total_time = 100

    result_list = [0] * 11    #该列表记录骰子每个面出现值的次数  (11个值, 因为是两个骰子)
    roll_list = range(2, 13)
    roll_dict = dict(zip(roll_list, result_list))

    roll_list1 = []
    roll_list2 = []

    while total_time > 0:
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list1.append(roll1)
        roll_list2.append(roll2)

        roll_total = roll1 + roll2
        print(roll_total)
        roll_dict[roll_total] += 1
        total_time -= 1

    for i, x in roll_dict.items():
        print("点数: {} --- 出现的次数: {} --- 出现的频率: {}".format(i, x, x/100))

    # 数据可视化
    x = range(1, 100 + 1)
    plt.scatter(x, roll_list1, alpha=0.5, c='red')
    plt.scatter(x, roll_list2, alpha=0.5, c='yellow')
    plt.show()

if __name__ == '__main__':
    main()
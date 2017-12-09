"""
    掷骰子 2.0
    模拟两个骰子, 骰出的个数
    使用元组进行记录
"""
import random

def roll_dice():
    roll = random.randint(1, 6)
    return roll

def main():
    total_time = 10

    result_list = [0] * 11    #该列表记录骰子每个面出现值的次数  (11个值, 因为是两个骰子)
    roll_list = range(2, 13)
    roll_dict = dict(zip(roll_list, result_list))

    while total_time > 0:
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_total = roll1 + roll2
        print(roll_total)
        roll_dict[roll_total] += 1
        total_time -= 1

    for i, x in roll_dict.items():
        print("点数: {} --- 出现的次数: {} --- 出现的频率: {}".format(i, x, x/10))

if __name__ == '__main__':
    main()
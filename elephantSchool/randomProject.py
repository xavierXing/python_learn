"""
    掷骰子
"""
import random

def roll_dice():
    roll = random.randint(1, 6)
    return roll

def main():
    total_time = 100000

    result_list = [0] * 6    #该列表记录骰子每个面出现值的次数
    while total_time > 0:
        roll = roll_dice()
        result_list[roll - 1] += 1
        total_time -= 1

    for i, x in enumerate(result_list):
        print("{} --- {} --- {}".format(i + 1, x, x/100000))

if __name__ == '__main__':
    main()
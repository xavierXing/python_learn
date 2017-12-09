"""
    52周存钱法则优化-封装函数
"""

import math


def math_money(total_week, money, money_week):
    money_list = []  # 存储的金额
    for i in range(total_week):
        money_list.append(money)
        saving = math.fsum(money_list)
        print("第{}周, 存{}元, 账户余额: {}元".format(i + 1, money, saving))
        money += money_week


def main():
    values = input("请输入需要存储时间(周): ,第一周存钱(人民币): ,基数(人民币): ")
    values = values.split(" ")

    try:
        total_week = values[0]
        money = values[1]
        money_week = values[2]
        math_money(int(total_week), int(money), int(money_week))
    except ValueError:
        print('程序异常')

if __name__ == '__main__':
    main()
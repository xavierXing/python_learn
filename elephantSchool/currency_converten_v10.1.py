"""
    52周存钱法
"""
import math

def main():
    week = 1                #周数
    money = 10              #每周存入的钱数
    increase = 10           #递增的钱数
    total_week = 52         #总计周数

    saving = 0              #账户累计

    money_list = []         #记录每周存款列表

    while week <= total_week:
        # saving += money
        money_list.append(money)
        saving = math.fsum(money_list)
        print('第({})周, 存入了{}元, 账户累计{}元'.format(week, money, saving))
        money += increase
        week += 1

if __name__ == '__main__':
    main()
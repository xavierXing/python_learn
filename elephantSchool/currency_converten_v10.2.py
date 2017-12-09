"""
    52周存钱法
"""
import math

def main():
    money = 10              #每周存入的钱数
    increase = 10           #递增的钱数
    total_week = 52         #总计周数
    money_list = []         #存款列表
    for i in range(total_week):
        money_list.append(money)
        saving = math.fsum(money_list)
        print('第({})周, 存入了{}元, 账户累计{}元'.format(i + 1, money, saving))
        money += increase

if __name__ == '__main__':
    main()
"""
    52周存钱法则优化-封装函数
"""

import math
import datetime

def math_money(total_week, money, money_week, num_week):
    money_list = []  # 存储的金额
    everyweek_money = []  #每周金额计算
    for i in range(total_week):
        money_list.append(money)
        saving = math.fsum(money_list)
        everyweek_money.append(saving)
        print("第{}周, 存{}元, 账户余额: {}元".format(i + 1, money, saving))

        money += money_week
    print("第{}周存储了{}元".format(num_week, everyweek_money[num_week - 1]))
def main():
    values = input("请输入需要存储时间(周): ,第一周存钱(人民币): ,基数(人民币): ")
    values = values.split(" ")
    date = input("请输入日期: (yyyy/mm/ss): ")
    input_date = datetime.datetime.strptime(date, '%Y/%m/%d')
    week_num = input_date.isocalendar()[1]
    try:
        total_week = values[0]
        money = values[1]
        money_week = values[2]
        math_money(int(total_week), int(money), int(money_week), int(week_num))
    except ValueError:
        print('程序异常')

if __name__ == '__main__':
    main()
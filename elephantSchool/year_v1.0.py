"""
    判断输入的日期是一年中的第几天
"""

from datetime import datetime

def is_leap_year(year):
    """
    判断返回是否是闰年
    true: 是
    false: 否
    :return: bool值
    """
    is_leap = False
    if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        is_leap = True
    return is_leap

def main():
    date = input("请输入日期(yyyy/mm/dd): ")
    input_date = datetime.strptime(date, "%Y/%m/%d")

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # days_year = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (is_leap_year(year)):
        days_year[1] = 29
    days = sum(days_year[: month - 1]) + day
    print("这是第{}年中的第{}天".format(year, days))

if __name__ == '__main__':
    main()
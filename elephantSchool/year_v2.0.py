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
    input_date = datetime.strptime(date,"%Y/%m/%d")

    year = input_date.year
    month = input_date.month
    day = input_date.day

    _30_sets = {4, 6, 9, 11}
    _31_sets = {1, 3, 5, 7, 8, 10, 12}

    #初始化天数 : 30
    _days = 0
    _days += day
    for _month in range(1, month):
        if _month in _30_sets:
            _days += 30
        elif _month in _31_sets:
            _days += 31
        else:
            _days += 28
    if is_leap_year(year) and month == 2:
        _days += 1

    print("第{}年中的第{}天".format(year, _days))

if __name__ == '__main__':
    main()
"""
    判断输入的日期是一年中的第几天
"""

from datetime import datetime

def main():
    date = input("请输入日期(yyyy/mm/dd): ")
    input_date = datetime.strptime(date,"%Y/%m/%d")

    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_year = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_year[: month - 1]) + day

    if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        if month > 2:
            days += 1
    print("这是第{}天".format(days))
    pass

if __name__ == '__main__':
    main()
"""
    空气质量计算
"""

def cal_liner(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
    线性缩放
    :return:
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi

def cal_pm_iaqi(pm_value):
    if 0 <= pm_value < 36:
        iaqi = cal_liner(0, 50, 0, 35, pm_value)
    elif 36 <= pm_value < 76:
        iaqi = cal_liner(50, 100, 35, 75, pm_value)
    elif 76 <= pm_value < 116:
        iaqi = cal_liner(100, 150, 75, 115, pm_value)
    else:
        pass

def cal_co_iaql(co_value):
    if 0 <= co_value < 3:
        iaqi = cal_liner(0, 50, 0, 3, co_value)
    elif 3 <= co_value < 5:
        iaqi = cal_liner(50, 100, 2, 4, co_value)
    elif 76 <= co_value < 116:
        iaqi = cal_liner(100, 150, 75, 115, co_value)
    else:
        pass

def cal_aqi(arg_list):
    """
    aqi 计算
    :param arg_list:
    :return:
    """
    pm_val = arg_list[0]
    co_val = arg_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaql(co_val)

    max_val = max(pm_iaqi, co_iaqi)

def main():

    print("请输入以下信息: ")
    input_value = input("(1)PM2.5 (2)CO: ")
    str_list = input_value.split(" ")
    pm_value = float(str_list[0])
    co_value = float(str_list[1])

    arg_list = []
    arg_list.append(pm_value)
    arg_list.append(co_value)

    aqi = cal_aqi(arg_list)
    print("空气质量指数为: {}".format(aqi))

if __name__ == '__main__':
    main()
"""
    空气质量计算
"""
def cal_pm_iaqi(pm_value):
    pass

def cal_co_iaql(co_value):
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
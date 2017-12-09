"""
    判断密码强弱
"""

def check_existStr(strings):
    for string in strings:
        if string.isalpha():
            return True
    return False


def check_numberStr(string):
    """
    判断字符串是否包含数字
    :return: bool
    """
    for number in string:
        if number.isnumeric():
            return True
    return False

def main():
    password = input("请输入密码: ")
    password_level = 0                      #密码强度

    if len(password) >= 8:                  #判断密码强度等级
        password_level += 1
    else:
        print("密码长度至少8位")

    if check_numberStr(password):           #判断密码
        password_level += 1
    else:
        print("密码需要包含数字")

    if check_existStr(password):
        password_level += 1
    else:
        print("密码需要包含字母")

    if password_level == 3:
        print("密码强度合格")
    else:
        print("密码强度不合格")


if __name__ == '__main__':
    main()
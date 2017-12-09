"""
    判断密码强弱
    优化函数
    将密码写入文件
"""
import sys

def check_existStr(strings):
    str_really = False
    for string in strings:
        if string.isalpha():
            str_really = True
            break
    return str_really


def check_numberStr(string):
    """
    判断字符串是否包含数字
    :return: bool
    """
    num_really = False
    for number in string:
        if number.isnumeric():
            num_really = True
            break
    return num_really


def main():
    try_time = 5
    while try_time > 0:
        password = input("请输入密码: ")
        password_level = 0  # 密码强度

        if len(password) >= 8:  # 判断密码强度等级
            password_level += 1
        else:
            print("密码长度至少8位")

        if check_numberStr(password):  # 判断密码
            password_level += 1
        else:
            print("密码需要包含数字")

        if check_existStr(password):
            password_level += 1
        else:
            print("密码需要包含字母")

        file = open("password.txt", "a", encoding="utf-8")
        file.write("密码是: {}, 密码强度: {}\n".format(password, password_level))
        file.close()
        if password_level == 3:
            print("密码强度合格")
            break
        else:
            print("密码强度不合格")
            try_time -= 1


if __name__ == '__main__':
    main()
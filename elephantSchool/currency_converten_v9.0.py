"""
    改进版的BMR计算器
"""
def main():

    run = input("是否退出程序(y/n)?: ")
    while run == "n":
        # gender = input("性别: ")
        # weight = float(input("体重(kg): "))
        # height = float(input("身高(cm): "))
        # age = int(input("年龄: "))
        print("请输入以下信息, 用空格分割")
        value = input("性别, 体重(kg), 身高(cm), 年龄: ")
        values = value.split(" ")

        try:
            gender = values[0]
            weight = float(values[1])
            height = float(values[2])
            age = int(values[3])

            if gender == '男':
                bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
            elif gender == '女':
                bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
            else:
                bmr = -1

            if bmr != -1:
                print('性别: {},体重({}kg),身高({}cm),年龄: {}岁'.format(gender, weight, height, age))
                print('基础代谢率是: {}大卡'.format(bmr))
            else:
                print('不支持该性别')

        except ValueError:
            print('请输入正确的信息!')
        except IndexError:
            print('输入的信息过少!')
        except:
            print('程序异常!')
        print("*****************************")
        run = input("是否退出程序(y/n)?: ")

if __name__ == '__main__':

    main()

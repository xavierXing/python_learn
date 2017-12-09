
while True:
    value = input('输入的金额: ')
    currency = value[-3:]
    # print(value,currency)
    if currency == 'USD':
        print('这是美元')
        print('换算成人民币是: ', float(value[:-3])*6.77)
    elif currency == 'CNY':
        print('这是人民币')
        print('换算成美元是: ', float(value[:-3])/6.77)
    else:
        print('您输入的货币,暂时不支持')
        exit()

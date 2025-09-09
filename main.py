# weight = input()

if weight[-2:] == 'kg':
    kg = eval(weight[0:-2])
    pd = kg * 2.2046
    print("对应的英制重量为{:.3f}磅".format(pd))
elif weight[-2:] == 'pd':
    pd = eval(weight[0:-2])
    kg = pd / 2.2046
    print("对应的公制重量为{:.3f}公斤".format(kg))
else:
    print("输入格式错误!")

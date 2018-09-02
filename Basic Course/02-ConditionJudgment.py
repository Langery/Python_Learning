# raw_input
# python3 将 raw_input 和 input 进行了整合，只保留了 input
# input() 返回的数据类型为 str 类型，不能直接和整数进行比较，必须先把 str 转换成整型，使用 int() 方法
birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')
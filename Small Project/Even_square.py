# 用列表生成式来计算值
# 定义一个函数来存放起始列表和输出结果
def square(start,end):
    result = [(num+1)**2 for num in range(start,end,2)]
    print(result)
square(1,10)
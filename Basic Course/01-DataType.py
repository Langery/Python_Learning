# coding=utf-8
# 数据类型
'''
1. Number
    int       有符号整数
    long      长整型
    float     浮点型
    complex   复数
2. Boolean
    True
    False
3. String
4. List
5. Tuple       元组
6. Dictionary  字典
'''

# 字符串
print ('I\'m fine')
print ('''line1
line2
line3''')

# Boolean
# 可以用 and or not 运算
# 只有所有都为True，and 的结果才为 True
# 只要其中有一个为True，or 的结果为 True
age = 20
if age >= 18:
    print ('adult')
else:
    print ('teenager')

# 空值 None
# 不能理解为0，0是有意义的，而 None 是一个特殊的空值
# 函数式编程
# 高阶函数

# 绝对值 abs(n)
a = int(input('输入任意整数'))
print(abs(a))

b = abs(int(input('请再次输入任意整数：')))
# 只获取最后的输入值 Num
print(b)

def add(x, y):
  return abs(x) + abs(y)

c = int(input('请输入第一个数：'))
d = int(input('请输入第二个数：'))
# e = input('请输入方法：')
print(add(c,d))

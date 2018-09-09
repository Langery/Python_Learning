# 函数参数
# 默认参数
# 平方函数
def square(a):
  return a * a

# 任意次方函数
def doubPara(a, b):
  s = 1
  while b > 0:
    b = b - 1
    s = s * a
  return s

# 用户注册函数
def login(name, age):
  print('name', name)
  print('age', age)

x = int(input('请输入基础数：'))
print('基础数的平方为:', square(x))
y = int(input('请输入次方数：'))
print('计算任意次方:', doubPara(x, y))
name = input('请输入姓名：')
age = int(input('请输入年龄：'))
# 直接打印函数，不需要print
login(name, age)
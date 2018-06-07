# 函数的参数对应

def f(a,b,c):
  return a+b+c
print(f(1,2,3))

# 关键字传递 keyword
# 关键字不用遵循位置的对应关系,但位置参数要出现在关键字参数之前
# print(f(c=3,b=2,a=1))

# 参数默认值
def g(a,b,c=10):
  return a+b+c
# c没有被赋值，将使用默认值10
print(g(3,2))
print(g(3,2,1))

# 包裹传递

# 包裹元组
def hi(*name):  # 提醒Python参数，在定义hi时需要加*，name为元组名
  print(type(name))
  print(name)
# hi构成元组(tuple)
hi(1,2,3)
hi(4,5,6,7,8)

# 包裹关键字
def keyw(**dict): # dict为字典，用于收集所有关键字，传递给函数keyw
  print(type(dict))
  print(dict)
keyw(a=1,b=9)
keyw(n=1,m=2,c=5)

# 解包裹  unpacking
def pack(a,b,c):
  print(a,b,c)
arga = (1,2,3)
pack(*arga)
# 对应的字典为 **
dict = {'a':1,'b':2,'c':3}
pack(**dict)

# 混合
# 位置 => 关键字 => 包裹位置 => 包裹关键字
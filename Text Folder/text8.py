# 循环对象

# 生成器
def gen():
  a = 100
  yield a
  a = a*8
  yield a
  yield 1000
for i in gen():
  print(i)

# 表推导
# 快速生成表的方法
L = []
for x in range(10):
  L.append(x**2)
  print(L)
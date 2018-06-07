# 函数对象

# lambda函数
func = lambda x,y: x + y
print(func(3,4))

def fund(x, y):
  return x + y
print(func(3,4))

# 函数作为参数传递
def test(f, a, b):
  print('test')
  print(f(a, b))
test(func, 3, 5)

# map()函数
re = map((lambda x: x+3),[1,3,5,6])
print(re)

# filter()函数
def fun(a):
  if a > 100:
    return True
  else:
    return False
    
print(filter(fun,[10,101,500]))

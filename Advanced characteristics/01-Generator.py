# coding=UTF-8
# 生成器
# 斐波拉契数列
def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    print(b)
    a, b = b, a + b
    n = n + 1

x = int(input('请输出数字：'))
print(fib(x))

# def fibx(max):
#   n, a, b = 0, 0, 1
#   while n < max:
#     yield b
#     a, b = b, a + b
#     n = n + 1
# y = int(input('请再次输入数字：'))
# print(fibx(y))

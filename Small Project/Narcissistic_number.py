# 水仙花数
# 所谓取模运算，就是计算两个数相除之后的余数，符号是 %
# // 整除

for num in range(100, 1000):
  low = num % 10
  mid = num // 10 % 10
  hight = num // 100
  if num == low ** 3 + mid ** 3 + hight ** 3:
    print(num)
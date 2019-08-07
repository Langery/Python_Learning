# 输出斐波那契数列前20项

a = 0
b = 1

for _ in range(20):
  a, b = b, a + b
  print(a, end=' ')
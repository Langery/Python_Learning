# 循环
# for..in 循环
i = 5
for a in [3,4.4,'life']:
  print(a)

for b in range(5):
  print(b)

for a in range(10):
  print(a**2)

while i < 10:
  print(i)
  i = i + 1

for i in range(10):
  if i == 2:
    continue #当到达指定值时跳过指定值
  print(i)

for i in range(10):
  if i == 2:
    break #当到达指定值时循环停止
  print(i)

print('==================================================>')
# while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
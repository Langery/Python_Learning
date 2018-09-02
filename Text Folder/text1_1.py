# print 命令行模式
print('Hello Python!')

# 基本数据类型
# 变量不需要声明，可以直接输出
# type() 查询数据类型

# sequence 序列
# 两种序列  tuple(定值表、元组  () )  list(表 [] )

# 运算
# 数学 + - * / ** %
# 判断 == ！= > >= < <= in
# 逻辑 and or not

# 缩进和选择
i = 1
x = 1
if i > 0:
  x = x + 1
print(x)
print('========================================>')

# 条件判断
if i > 0:
  print('positive i')
  i = i + 1
elif i == 0:
  print('i is 0')
  i = i * 10
else:
  print('negative i')
  i = i - 1
print('new i:',i)

i = 5
if i > 1:
  print('i bigger than 1')
  print('good')
  if i > 2:
    print('i bigger than 2')
    print('even better')
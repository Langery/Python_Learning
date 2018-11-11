import math
while True:
  # 用户输入
  r = input("请输入圆的半径：")
  # 判断如果是字符则重新输入
  if not r.isalpha():
    # 数据处理
    r = float(r)
    cicleArea = math.pi*r**2
    # 结果输出
    # %d 整型输出  %ld 长整型输出
    # %f 输出实数，保留小数点6位
    # %u 以十进制数输出
    print("圆的面积是：%f"%cicleArea)
    break
  else:
    print("输入错误！")
    continue

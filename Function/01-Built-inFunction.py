# 内置函数
# 0、sorted()
# a)对于一个列表的排序
# sorted([100, 20, 60, 80, 70, 5])
# >>>[5, 20, 60, 70, 80, 100]

# b)通过key参数/函数
# 按照每个元素的长度大小排序
L = [{1:5,3:4},{1:3,6:3},{1:1,2:4,5:6},{1:9}]
new_line = sorted(L,key=lambda x:len(x))
print(new_line)

# 1、map()
# 2、enumerate()
# 3、zip()
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
# 在python 3.0中zip()是可迭代对象，使用时必须将其包含在一个list中，方便一次性显示出所有结果
xyz = list(zip(x, y, z))
print(xyz)
# 4、filter()
# 过滤掉一些不符合条件的元素，从而返回符合条件的list
def obj(x):
  return x%2 == 0
# python3中filter()同样为可迭代对象
print(list(filter(obj, [1, 2, 3, 4, 5, 6, 7])))
# 5、reduce()

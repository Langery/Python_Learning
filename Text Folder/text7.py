# 循环设计

# range()
A = 'abcdefghijklmn'
for i in range(0,len(A),2):
  #       上限  下限  每次循环的步长
  print(A[i])

# enumerate()
for (index,char) in enumerate(A):
  print(index)
  print(char)

# zip()
t1 = [1,2,3]
t2 = [7,8,9]
t3 = ['a','b','c']
for (a,b,c) in zip(t1,t2,t3):
  print(a,b,c)

# cluster 
zipped = zip(t1,t2)
print(zipped)
# decompose
na, nb = zip(*zipped)
print(na, nb)
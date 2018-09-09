# 词典

# 0、dictionary 使用键值对(key-value)存储
# key不存在，dict就会报错
dict = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 901}
for key in dict:
  print(dict[key])

'''
避免key不存在的错误
1. in
eg: 'lilei' in dict
2. get
dict.get('lilei')
'''
print('================Boolean判断==================')
print('lilei' in dict)
print(dict.get('lilei'))

# 删除一个key：pop(key)

# 1、set
# 不会存储value，但是key不能重复
s = set([1, 2, 3])
print(s)
# add(key) 添加元素
# remove(key) 删除元素

# 文本文件的输入输出
# Python具有基本文本文件读写功能
# 打开文件
# f = open(文件名，模式)
# 关闭文件
# f.close()
# 'r'  只读
# 'w'  写入
# 'a'  追加
# 'r+' == r+w
# 'w+' == r+w
# 'a+' == a+r
# 写入：
# f.write('')
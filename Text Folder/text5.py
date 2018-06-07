# 模块

# 引入文件
import text3_1

for i in range(5):
  text3_1.import_to5()

# 引入模块a，并将模块a重命名为b
# import a as b
# 从模块a中引入function对象，即直接使用function
# from a import function
# 从模块a中引入所有对象
# from a import *

# 模块包
# 用于存放相似功能的模块，构成一个模块包
# import this_mod.module
# 引入this_mod文件夹中的module模块
# 该文件夹中必须包含__init__.py文件，提醒python，该文件夹为一个模块包，__init__.py可以是空文件

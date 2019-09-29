# 面向对象 扩展

# 调用类的信息
class Jay(object):
  laugh = '23333'
  def show_laugh(self):
    print(self.laugh)
  def laugh_1st(self):
    for i in range(3):
      self.show_laugh()
LL = Jay()
LL.laugh_1st()

# __init__()  special method
# 初始化
class me(Jay):
  def __init__(self,show_laugh):
    print('That is me',show_laugh)
summer = me('Langery')

class Person(object):
  def __init__(self, input_gender):
    self.gender = input_gender
  def printGender(self):
    print(self.gender)
FirPer = Person('male')
print(FirPer.gender)
FirPer.printGender()
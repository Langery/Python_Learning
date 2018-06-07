# 面向对象 OOP(Object Oriented Programming)

# 定义对象
class Bird(object):
  have_feather = True
  way_of_reproduction = 'egg'
# 获取对象属性
summer = Bird()
print(summer.way_of_reproduction)

# 动作
class Bird1(object):
  have_feather = True
  way_of_reproduction = 'egg'
  # def 定义方法
  # 方法的第一个参数必须是 self
  def move(self, dx, dy):
    position = [0,0]
    position[0] = position[0] + dx
    position[1] = position[1] + dy
    return position
summer = Bird1()
print('after move',summer.move(5,8))

# 子类
class Chicken(Bird1):
  way_of_move = 'walk'
  possible_in_KFC = True

class Oriole(Bird1):
  way_of_move = 'fly'
  possible_in_KFC = False

summer = Chicken()
print(summer.have_feather)
print(summer.move(5,8))

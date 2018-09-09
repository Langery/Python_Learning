# 时间和日期

# 格式化时间
import time

localtime = time.asctime(time.localtime(time.time()))
print('local current time :', localtime)

# 获取某月日历
import calendar

year = int(input('请输入年份: '))
mon = int(input('请输入月份: '))
cal = calendar.month(year, mon)
print('Here is the calendar:')
print(cal)


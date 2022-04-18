# From: jb51.net/article/190551.htm
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import csv
import xlrd
import xlwt
 
def handler_excel(filename=r'xxx.xlsx'):
 
  # 打开文件
  workbook = xlrd.open_workbook(filename)
  index = workbook.sheet_names()[0]
  sheet2 = workbook.sheet_by_name(index)
   
  #遍历
  nrows = sheet2.nrows
  for i in range(nrows):
    print(sheet2.row_values(i))
 
if __name__ == '__main__':
  handler_excel()
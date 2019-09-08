import csv
import xlwt
import xlrd
from xlutils.copy import copy
#创建Excel表格

path = 'D://data'
template = xlrd.open_workbook('D://data/money.xls')

print(template.sheet_names())
table = template.sheets()[0]
print(table.nrows)
title = table.cell_value(1,9)
print('_'+title+'_')
print(type(title))


path = 'D://data'
template = xlrd.open_workbook(r'C:\Users\Sean\Downloads\myMoney.xls')

print(template.sheet_names())
table = template.sheets()[0]
print(table.nrows)
title = table.cell_value(1,9)
print('_'+title+'_')
print(len(title))

a='退款-【新年狂欢节】鸭鸭2018新羽绒服女中长款大毛领长款过膝反季黑色加厚修身韩版潮'
if '退款' not in a:
    print('t')
else:
    print('f')
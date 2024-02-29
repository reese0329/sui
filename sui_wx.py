import csv

import xlrd
import xlwt
# 创建Excel表格
from classify import find
from classify import find_in
from xlutils.copy import copy

pw = False

if pw == False:
    path = 'C://Users//Administrator//Desktop//sui'
else:
    path = 'D://data'

template = xlrd.open_workbook(path + '/new.xls')
sui = copy(template)
spend = sui.get_sheet(0)
income = sui.get_sheet(1)
trans = sui.get_sheet(3)
# print(sui.sheet_names())

# 金额转换为文本格式
# 需要删除特殊的微信名

df = open(path + '//wx.csv')
read_line = csv.reader(df)
spend_i = 1
income_i = 1
trans_i = 1
m = 0

for i in read_line:
    print(i)
    if m <= 16:
        pass
    else:
        print(i)
        #print(i[2])
        if '支出' in i[4]:
            # date
            spend.write(spend_i, 9, str(i[0].replace('/', '-')))
            # sum
            spend.write(spend_i, 5, i[5])
            find(i[2], spend_i, spend)
            print(i[2])
            spend.write(spend_i, 0, i[4].replace(' ', ''))
            spend.write(spend_i, 7, i[2].replace(' ', ''))
            spend.write(spend_i, 8, i[3].replace(' ', ''))
            spend.write(spend_i, 10, i[10].replace(' ', ''))
            spend.write(spend_i, 3, i[6])
            spend_i += 1
        elif '收入' in i[4]:
            # if'退款' not in i[7]:
            #     income.write(income_i, 9, i[0].replace('/','-'))
            #     income.write(income_i, 5, float(i[5]))
            #     income.write(income_i, 7, i[2].replace(' ',''))
            #     income.write(income_i, 8, i[3].replace(' ', ''))
            #     income.write(income_i, 0, i[4].replace(' ',''))
            #     income.write(income_i, 3, '零钱通')
            #     income.write(income_i, 1, '人情往来')
            #     income.write(income_i, 2, '所收红包')
            #     # print(i[8])
            #     income_i += 1
            # else:
            #     # date
            income.write(income_i, 9, str(i[0].replace('/', '-')))
            # sum
            income.write(income_i, 5, float(i[5]))
            find_in(i[2], income_i, income)
            print(i[2])
            income.write(income_i, 0, '收入')
            income.write(income_i, 7, i[2].replace(' ', ''))
            income.write(income_i, 8, i[3].replace(' ', ''))
            income.write(income_i, 10, i[10].replace(' ', ''))
            income.write(income_i, 3, '零钱通')
            income_i += 1
        else:
            # trans.write(trans_i, 1, i[2].replace('/', '-'))
            trans.write(trans_i, 0, '转账')
            trans.write(trans_i, 3, i[6])
            trans.write(trans_i, 4, '基金账户(CNY)')
            trans.write(trans_i, 5, i[5])
            trans.write(trans_i, 7, '理财通')
            trans.write(trans_i, 8, i[1])
            trans.write(trans_i, 9, str(i[0].replace('/', '-')))
            trans.write(trans_i, 10, i[3])
            # print(float(i[9]))

            trans_i += 1
    m += 1
#
# # for i in range(8):
# #     spend.write(i, 1, i)
#
sui.save(path + '/template_wx.xls')

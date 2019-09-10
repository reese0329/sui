import csv
import xlwt
import xlrd
from xlutils.copy import copy
#创建Excel表格
from classify import find

pw = True

if pw==True:
    path = 'C://Users//Administrator//Desktop//sui'
else:
    path = 'D://data'


template = xlrd.open_workbook(path + '/template.xls')
sui = copy(template)
spend = sui.get_sheet(0)
income = sui.get_sheet(1)
trans = sui.get_sheet(2)
# print(sui.sheet_names())

df = open(path+'//alipay_record.csv',encoding='gbk')
read_line = csv.reader(df)
spend_i = 1
income_i = 1
trans_i = 1
m=0


for i in read_line:
    # print(i)
    if m<=4:
        pass
    else:
        # print(i[8])
    #time
        if '交易关闭' in i[11]:
            pass
        else:
            if '支出' in i[10]:
                #date
                spend.write(spend_i, 9, str(i[2].replace('/', '-')))
                #sum
                spend.write(spend_i, 5, float(i[9]))
                find(i[7],spend_i,spend)
                print(i[7])
                spend.write(spend_i, 7, i[7].replace(' ',''))
                spend.write(spend_i, 8, i[8].replace(' ',''))
                spend.write(spend_i, 0, i[10].replace(' ',''))
                spend.write(spend_i, 10, i[14].replace(' ',''))
                spend.write(spend_i, 3, '支付宝')
                spend_i += 1
            elif '收入' in i[10]:
                if'退款' not in i[8]:
                    income.write(income_i, 9, i[2].replace('/','-'))
                    income.write(income_i, 5, float(i[9]))
                    income.write(income_i, 7, i[7].replace(' ',''))
                    income.write(income_i, 8, i[8].replace(' ', ''))
                    income.write(income_i, 0, i[10].replace(' ',''))
                    income.write(income_i, 3, '支付宝')
                    # print(i[8])
                    income_i += 1
                else:
                    # date
                    spend.write(spend_i, 9, str(i[2].replace('/', '-')))
                    # sum
                    spend.write(spend_i, 5, -float(i[9]))
                    find(i[7], spend_i,spend)
                    # print(i[8])
                    spend.write(spend_i, 7, i[7].replace(' ', ''))
                    spend.write(spend_i, 8, i[8].replace(' ', ''))
                    spend.write(spend_i, 0, '支出')
                    spend.write(spend_i, 10, i[14].replace(' ', ''))
                    spend.write(spend_i, 3, '支付宝')
                    spend_i += 1
            else:
                trans.write(trans_i, 1, i[2].replace('/', '-'))
                trans.write(trans_i, 6, i[9])
                trans.write(trans_i, 3, '支付宝')
                trans.write(trans_i, 9, i[4].replace('/', '-'))
                # print(float(i[9]))
                trans.write(trans_i, 8, i[7].replace(' ',''))
                trans.write(trans_i, 0,i[10].replace(' ',''))
                trans.write(trans_i, 4, '支付宝')
                trans_i += 1
    m +=1
#
# # for i in range(8):
# #     spend.write(i, 1, i)
#
sui.save(path + '/pay_alipay.xls')


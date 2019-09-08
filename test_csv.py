import csv
import xlwt
import xlrd
from xlutils.copy import copy
#创建Excel表格

pw = False

if pw==True:
    path = 'C://Users//Administrator//Desktop//sui'
else:
    path = 'D://data'

template = xlrd.open_workbook(path+'/template.xls')
sui = copy(template)
spend = sui.get_sheet(0)
income = sui.get_sheet(1)
trans = sui.get_sheet(2)
# print(sui.sheet_names())

df = open(path+'//alipay_record.csv',encoding='gbk')
read_line = csv.reader(df)
spend_i = 3
income_i = 2
trans_i = 2
m=0

def find(n,spend_i):
    dic ={'张一元':{'c':'eat','e':'c'},'海底捞':{'c':'eat','e':'c'},'大麦':{'c':'sing','e':'c'}}

    for i in dic.keys():
        if i in n:
            spend.write(spend_i, 2, dic[i]['c'])
            # print(dic[i]['c'])
            spend.write(spend_i, 3, dic[i]['e'])
            # print(dic[i]['e'])
            break
        else:
            spend.write(spend_i, 2, '食品酒水')
            spend.write(spend_i, 3, '早午晚餐')


for i in read_line:
    print(i)
    if m<=6:
        pass
    else:
        print(i[10])
    #time
        if '交易关闭' in i[11]:
            pass
        else:
            if '支出' in i[10]:
                spend.write(spend_i, 1, i[4].replace('/','-'))
                spend.write(spend_i, 6, float(i[9]))
                find(i[8],spend_i)
                # print(i[8])
                spend.write(spend_i, 8, i[7])
                spend.write(spend_i, 0, i[10])
                spend_i += 1
            elif '收入' in i[10]:

                income.write(income_i, 1, i[4].replace('/','-'))
                income.write(income_i, 6, float(i[9]))
                income.write(income_i, 8, i[7])
                income.write(income_i, 0, i[10])
                income_i += 1
            else:
                trans.write(trans_i, 1, i[4].replace('/', '-'))
                trans.write(trans_i, 6, float(i[9]))
                print(type(i[9]))
                trans.write(trans_i, 8, i[7])
                trans.write(trans_i, 0, i[10])
                trans_i += 1
    m +=1
#
# # for i in range(8):
# #     spend.write(i, 1, i)
#
sui.save(path+'//template.xls')


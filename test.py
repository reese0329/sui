import csv
#
#
# # csv_file=csv.reader(open(r'C:\Users\Administrator\Desktop\sui\alipay_record_20190820_1545_1.csv','r'))
# # print(csv_file)
# # # content=[] #用来存储整个文件的数据，存成一个列表，列表的每一个元素又是一个列表，表示的是文件的某一行
# #
# # for line in csv_file:
# #     print(line) #打印文件每一行的信息
# #     print(line[0])
# # #     content.append(line)
# # # print("该文件中保存的数据为:\n",content)
#
#
# abc = "网"
#
# def find(n):
#     dic ={'全时':{'c':'eat','e':'c'},'海底捞':{'c':'eat','e':'c'},'大麦':{'c':'sing','e':'c'}}
#
#     for i in dic.keys():
#         if i in n:
#             print(dic[i]['c'])
#             print(dic[i]['e'])
#             break
#         else:
#             pass
#
# find(abc)
#
#



pw = False

if pw==True:
    path = 'C://Users//Administrator//Desktop//sui'
else:
    path = 'D://data'


# template = xlrd.open_workbook(path + '/money.xls')
# sui = copy(template)
# spend = sui.get_sheet(0)
# income = sui.get_sheet(1)
# trans = sui.get_sheet(2)
# # print(sui.sheet_names())

df = open(path+'//微信支付账单.csv')
read_line = csv.reader(df)
for i in read_line:
    print(i)
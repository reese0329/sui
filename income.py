import csv

df = open('D://data//alipay_record.csv', encoding='gbk')
read_line = csv.reader(df)

for i in read_line:
    if '支出' in i[10]:
        pass
    elif '收入' in i[10] and '退款' not in i[8]:
        print(i[10], i[8])
    else:
        pass

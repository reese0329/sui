import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Administrator/Desktop/sui/alipay_record.csv', encoding='gbk')
# print(len(df))
# print(df.loc[3:len(df)-7])
# content=[] #用来存储整个文件的数据，存成一个列表，列表的每一个元素又是一个列表，表示的是文件的某一行

for line in df.loc[3:len(df) - 7]:
    print(line)  # 打印文件每一行的信息
#     print(line[0])
#     content.append(line)
# print("该文件中保存的数据为:\n",content)

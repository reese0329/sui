import xlrd
import xlwt


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\sui\alipay_record_20190820_1545_1.csv')
    result = xlwt.Workbook()  # 创建xlsx文件
    sheet = result.add_sheet('result', cell_overwrite_ok=True)  # 表名为result
    # 获取所有sheet
    # print(workbook.sheet_names())  # [u'sheet1', u'sheet2']

    # 获取玩工作表
    table = workbook.sheets()[0]
    nrow = table.nrows
    # print(nrow)
    dict_play = {}
    for i in range(2, nrow):
        title = table.cell_value(i, 4)
        #去除没有玩的条目，即玩为"/"
        if title == "/":
            pass
        #已加入dic中的玩不再加入，去重避免修改
        elif title in dict_play.keys():
            pass
        else:
            value = table.cell_value(i, 8)
            dict_play[title] = value
            # print(value)
    print("玩dic：")
    print(dict_play)



    #练测dic
    table = workbook.sheets()[4]
    nrow = table.nrows
    # print(nrow)
    dict = {}
    for i in range(2, nrow):
        title = table.cell_value(i, 3)
        if title == "/":
            pass
        else:
            value = table.cell_value(i, 6)
            dict[title] = value
            # print(value)
    print("练测dic:")
    print(dict)




if __name__ == '__main__':
    read_excel()
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


template = xlrd.open_workbook(path + '/money.xls')
sui = copy(template)
spend = sui.get_sheet(0)
income = sui.get_sheet(1)
trans = sui.get_sheet(2)
# print(sui.sheet_names())

df = open(path+'//微信支付账单.csv')
read_line = csv.reader(df)
spend_i = 1
income_i = 1
trans_i = 1
m=0

def find(n,s):
    dic ={'小易':{'c':'食品酒水','e':'饮料'},
          '1点点':{'c':'食品酒水','e':'饮料'},
          '星巴克': {'c': '食品酒水', 'e': '饮料'},
          '50岚': {'c': '食品酒水', 'e': '饮料'},
          '便利蜂': {'c': '食品酒水', 'e': '饮料'},
          '张一元': {'c': '食品酒水', 'e': '茶'},
          '绝味': {'c': '食品酒水', 'e': '零食'},
          '哈哈镜': {'c': '食品酒水', 'e': '零食'},
          '味多美': {'c': '食品酒水', 'e': '零食'},
          '润实': {'c': '食品酒水', 'e': '水果零食'},
          '物美': {'c': '食品酒水', 'e': '早午晚餐'},
          '饿了么': {'c': '食品酒水', 'e': '早午晚餐'},
          '达美乐': {'c': '食品酒水', 'e': '早午晚餐'},
          '嘉和一品': {'c': '食品酒水', 'e': '早午晚餐'},
          '完美世界美食': {'c': '食品酒水', 'e': '早午晚餐'},
          '肯德基': {'c': '食品酒水', 'e': '早午晚餐'},
          '吉野家': {'c': '食品酒水', 'e': '早午晚餐'},
          '赛百味': {'c': '食品酒水', 'e': '早午晚餐'},
          '粉': {'c': '食品酒水', 'e': '早午晚餐'},
          '煎饼': {'c': '食品酒水', 'e': '早午晚餐'},
          '7-11': {'c': '食品酒水', 'e': '早午晚餐'},
          '汤': {'c': '食品酒水', 'e': '早午晚餐'},
          '秦唐味道': {'c': '食品酒水', 'e': '早午晚餐'},
          '麦当劳': {'c': '食品酒水', 'e': '早午晚餐'},
          '耳东小面': {'c': '食品酒水', 'e': '早午晚餐'},
          '山海蓝图': {'c': '食品酒水', 'e': '早午晚餐'},
          '蚂蚁会员': {'c': '人情往来', 'e': '慈善捐助'},
          '免费午餐': {'c': '人情往来', 'e': '慈善捐助'},
          '基金会': {'c': '人情往来', 'e': '慈善捐助'},
          '淑英': {'c': '人情往来', 'e': '孝敬父母'},
          '田申': {'c': '人情往来', 'e': '孝敬父母'},
          '青骑': {'c': '行车交通', 'e': '共享单车'},
          '舒行科技': {'c': '行车交通', 'e': '打车租车'},
          '货拉拉': {'c': '行车交通', 'e': '打车租车'},
          '轨道交通': {'c': '行车交通', 'e': '公共交通'},
          '黑狗科技': {'c': '行车交通', 'e': '公共交通'},
          '淘票票': {'c': '休闲娱乐', 'e': '电影'},
          '铁路': {'c': '出差旅游', 'e': '交通费'},
          '携程': {'c': '出差旅游', 'e': '交通费'},
          '移动': {'c': '居家生活', 'e': '电话费'},
          '德邦': {'c': '居家生活', 'e': '邮寄费'},
          '菜鸟供应链': {'c': '居家生活', 'e': '邮寄费'},
          '华为': {'c': '购物消费', 'e': '电子数码'},
          '专卖店': {'c': '购物消费', 'e': '电子数码'},
          '娇兰佳人': {'c': '购物消费', 'e': '美妆护肤'},
          '旗舰店': {'c': '购物消费', 'e': '美妆护肤'},
          '信用借还': {'c': '居家物业', 'e': '水电燃气'},
          '名创优品': {'c': '购物消费', 'e': '家居日用'},
          '幸福荣耀': {'c': '购物消费', 'e': '家居日用'},
          '京东到家': {'c': '购物消费', 'e': '家居日用'},
          '家乐福': {'c': '购物消费', 'e': '家居日用'},
          '沃尔玛': {'c': '购物消费', 'e': '家居日用'},
          '超市发': {'c': '购物消费', 'e': '家居日用'},
          '一得阁': {'c': '小乐趣', 'e': '书法'},
          '天辅': {'c': '小乐趣', 'e': '书法'},
          '优衣库': {'c': '购物消费', 'e': '衣裤鞋帽'},
          'SHINee': {'c': '小乐趣', 'e': 'SHINee'},
          'song':{'c':'eat','e':'c'},'sing':{'c':'sing','e':'c'}}
    for i in dic.keys():
        if i in n:
            spend.write(s, 1, dic[i]['c'])
            print(dic[i]['c'])
            spend.write(s, 2, dic[i]['e'])
            print(dic[i]['e'])
            break
        else:
            spend.write(s, 1, '休闲娱乐')
            spend.write(s, 2, '聚会')

for i in read_line:
    # print(i)
    if m<=16:
        pass
    else:
        # print(i[8])
    #time
        # if '交易关闭' in i[11]:
        #     pass
        # else:
            if '支出' in i[4]:
                #date
                spend.write(spend_i, 9, str(i[0].replace('/', '-')))
                #sum
                spend.write(spend_i, 5, i[5])
                find(i[2],spend_i)
                print(i[2])
                spend.write(spend_i, 0, i[4].replace(' ', ''))
                spend.write(spend_i, 7, i[2].replace(' ',''))
                spend.write(spend_i, 8, i[3].replace(' ',''))
                spend.write(spend_i, 10, i[10].replace(' ',''))
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
                    spend.write(spend_i, 9, str(i[0].replace('/', '-')))
                    # sum
                    spend.write(spend_i, 5, -float(i[5]))
                    find(i[2], spend_i)
                    print(i[2])
                    spend.write(spend_i, 0, '支出')
                    spend.write(spend_i, 7, i[2].replace(' ', ''))
                    spend.write(spend_i, 8, i[3].replace(' ', ''))
                    spend.write(spend_i, 10, i[10].replace(' ', ''))
                    spend.write(spend_i, 3, '零钱通')
                    spend_i += 1
            else:
                trans.write(trans_i, 1, i[2].replace('/', '-'))
                trans.write(trans_i, 6, i[9])
                trans.write(trans_i, 3, '支付宝')
                trans.write(trans_i, 9, i[4].replace('/', '-'))
                # print(float(i[9]))
                trans.write(trans_i, 8, i[7].replace(' ',''))
                trans.write(trans_i, 0,'转账')
                trans.write(trans_i, 4, '支付宝')
                trans_i += 1
    m +=1
#
# # for i in range(8):
# #     spend.write(i, 1, i)
#
sui.save(path + '/money1_wx.xls')


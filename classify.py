def find(n, s, m):
    dic = {'小易': {'c': '食品酒水', 'e': '饮料'},
           '在楼下科技': {'c': '食品酒水', 'e': '饮料'},
           '1点点': {'c': '食品酒水', 'e': '饮料'},
           '茶百道': {'c': '食品酒水', 'e': '饮料'},
           '蜜雪冰城': {'c': '食品酒水', 'e': '饮料'},
           '霸王茶姬': {'c': '食品酒水', 'e': '饮料'},
           '茉酸奶': {'c': '食品酒水', 'e': '饮料'},
           '星巴克': {'c': '食品酒水', 'e': '饮料'},
           '柠檬茶': {'c': '食品酒水', 'e': '饮料'},
           '大众': {'c': '食品酒水', 'e': '外出美食'},
           'luckincoffee': {'c': '食品酒水', 'e': '饮料'},
           '卓盛丽伟': {'c': '食品酒水', 'e': '饮料'},
           '50岚': {'c': '食品酒水', 'e': '饮料'},
           '宝丽可可': {'c': '食品酒水', 'e': '饮料'},
           '便利蜂': {'c': '食品酒水', 'e': '饮料'},
           '阳光人寿': {'c': '金融保险', 'e': '人身保险'},
           '省钱卡': {'c': '购物消费', 'e': '家居日用'},
           '多点': {'c': '食品酒水', 'e': '饮料'},
           '张一元': {'c': '食品酒水', 'e': '茶'},
           '绝味': {'c': '食品酒水', 'e': '零食'},
           '哈哈镜': {'c': '食品酒水', 'e': '零食'},
           '味多美': {'c': '食品酒水', 'e': '零食'},
           '润实': {'c': '食品酒水', 'e': '水果零食'},
           '物美': {'c': '食品酒水', 'e': '早午晚餐'},
           '炸鸡': {'c': '食品酒水', 'e': '早午晚餐'},
           '好邻居': {'c': '食品酒水', 'e': '早午晚餐'},
           '罗森': {'c': '食品酒水', 'e': '零食'},
           '饿了么': {'c': '食品酒水', 'e': '早午晚餐'},
           '达美乐': {'c': '食品酒水', 'e': '早午晚餐'},
           '嘉和一品': {'c': '食品酒水', 'e': '早午晚餐'},
           '完美世界（北京）软件科技发展有限公司': {'c': '食品酒水', 'e': '早午晚餐'},
           '肯德基': {'c': '食品酒水', 'e': '早午晚餐'},
           '吉野家': {'c': '食品酒水', 'e': '早午晚餐'},
           '赛百味': {'c': '食品酒水', 'e': '早午晚餐'},
           '稻香村': {'c': '食品酒水', 'e': '早午晚餐'},
           '粉': {'c': '食品酒水', 'e': '早午晚餐'},
           '煎饼': {'c': '食品酒水', 'e': '早午晚餐'},
           '7-11': {'c': '食品酒水', 'e': '早午晚餐'},
           '汤': {'c': '食品酒水', 'e': '早午晚餐'},
           '秦唐味道': {'c': '食品酒水', 'e': '早午晚餐'},
           '麦当劳': {'c': '食品酒水', 'e': '早午晚餐'},
           '耳东': {'c': '食品酒水', 'e': '早午晚餐'},
           '拉扎斯': {'c': '食品酒水', 'e': '早午晚餐'},
           '山海蓝图': {'c': '食品酒水', 'e': '早午晚餐'},
           '蚂蚁会员': {'c': '人情往来', 'e': '慈善捐助'},
           '免费午餐': {'c': '人情往来', 'e': '慈善捐助'},
           '基金会': {'c': '人情往来', 'e': '慈善捐助'},
           '淑英': {'c': '人情往来', 'e': '孝敬父母'},
           '申': {'c': '人情往来', 'e': '孝敬父母'},
           '青骑': {'c': '行车交通', 'e': '自行车'},
           '哈罗出行': {'c': '行车交通', 'e': '自行车'},
           '舒行科技': {'c': '行车交通', 'e': '打车租车'},
           '货拉拉': {'c': '行车交通', 'e': '打车租车'},
           '轨道交通': {'c': '行车交通', 'e': '公共交通'},
           '黑狗科技': {'c': '行车交通', 'e': '公共交通'},
           '淘票票': {'c': '休闲娱乐', 'e': '电影'},
           '铁路': {'c': '出差旅游', 'e': '交通费'},
           '如家': {'c': '出差旅游', 'e': '住宿费'},
           '携程': {'c': '出差旅游', 'e': '交通费'},
           '移动': {'c': '居家生活', 'e': '电话费'},
           '通信': {'c': '居家生活', 'e': '电话费'},
           '德邦': {'c': '居家生活', 'e': '邮寄费'},
           '菜鸟供应链': {'c': '居家生活', 'e': '邮寄费'},
           '华为': {'c': '购物消费', 'e': '电子数码'},
           '专卖店': {'c': '购物消费', 'e': '电子数码'},
           '娇兰佳人': {'c': '购物消费', 'e': '美妆护肤'},
           '停车': {'c': '行车交通', 'e': '停车'},
           'stayreal': {'c': '购物消费', 'e': '衣裤鞋帽'},
           '旗舰店': {'c': '购物消费', 'e': '美妆护肤'},
           '信用借还': {'c': '居家物业', 'e': '水电燃气'},
           '名创优品': {'c': '购物消费', 'e': '家居日用'},
           '浙江天猫': {'c': '购物消费', 'e': '家居日用'},
           '幸福荣耀': {'c': '购物消费', 'e': '家居日用'},
           '京东到家': {'c': '购物消费', 'e': '家居日用'},
           '家乐福': {'c': '购物消费', 'e': '家居日用'},
           '沃尔玛': {'c': '购物消费', 'e': '家居日用'},
           '超市发': {'c': '购物消费', 'e': '家居日用'},
           '一得阁': {'c': '小乐趣', 'e': '书法'},
           '天辅': {'c': '小乐趣', 'e': '书法'},
           '优衣库': {'c': '购物消费', 'e': '衣裤鞋帽'},
           '医院': {'c': '医疗保健', 'e': '门诊治疗'},
           '社区卫生': {'c': '医疗保健', 'e': '门诊治疗'},
           'SHINee': {'c': '小乐趣', 'e': 'SHINee'},
           '邮政惠民生活超市': {'c': '食品酒水', 'e': '水果零食'},
           '蚂蚁财富': {'c': '金融保险', 'e': '理财基金'},
           '超市': {'c': '小乐趣', 'e': 'SHINee'},
           'song': {'c': 'eat', 'e': 'c'},
           'sing': {'c': 'sing', 'e': 'c'},
           '公共交通': {'c': '行车交通', 'e': '公共交通'},
           '滴滴出行': {'c': '行车交通', 'e': '打车租车'},
           '青奇科技': {'c': '行车交通', 'e': '自行车'},
           '广州骑安': {'c': '行车交通', 'e': '自行车'},
           '摩拜': {'c': '行车交通', 'e': '自行车'},
           'hm': {'c': '衣服饰品', 'e': '衣服裤子'},
           '完美未来': {'c': '其他杂项', 'e': '烂账损失'},
           '魅族商城': {'c': '其他杂项', 'e': '烂账损失'},
           '华为软件': {'c': '其他杂项', 'e': '烂账损失'},
           '洪恩': {'c': '其他杂项', 'e': '烂账损失'},
           'puma': {'c': '购物消费', 'e': '衣裤鞋帽'},
           '鞋': {'c': '购物消费', 'e': '衣裤鞋帽'},
           'gu': {'c': '购物消费', 'e': '衣裤鞋帽'},
           '太平鸟': {'c': '购物消费', 'e': '衣裤鞋帽'},
           '盖璞': {'c': '购物消费', 'e': '衣裤鞋帽'},
           '燃气': {'c': '居家物业', 'e': '水电燃气'},
           '电力': {'c': '居家物业', 'e': '水电燃气'},
           '完美世界股份': {'c': '食品酒水', 'e': '早午晚餐'},
           '友饮': {'c': '食品酒水', 'e': '饮料'},
           }
    for i in dic.keys():
        if i in n:
            m.write(s, 1, dic[i]['c'])
            # print(dic[i]['c'])
            m.write(s, 2, dic[i]['e'])
            # print(dic[i]['e'])
            break
        else:
            m.write(s, 1, '休闲娱乐')
            m.write(s, 2, '聚会')

def find_in(n, s, m):
       dic = {'天弘': {'c': '职业收入', 'e': '投资收入'},
              '木子': {'c': '职业收入', 'e': '加班收入'},
              '吃饭向右嚼': {'c': '其他收入', 'e': '退款'},
              }
       for i in dic.keys():
              if i in n:
                     m.write(s, 1, dic[i]['c'])
                     # print(dic[i]['c'])
                     m.write(s, 2, dic[i]['e'])
                     # print(dic[i]['e'])
                     break
              else:
                     m.write(s, 1, '休闲娱乐')
                     m.write(s, 2, '聚会')
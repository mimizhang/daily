# # 中国广东深圳龙岗区南湾街道南岭村社区南岭商业街3栋201号 提取省份 城市
# # jieba包
# import jieba
# from pymongo import MongoClient
#
# client71 = MongoClient('117.25.133.71', 27017)
# db = client71['db_pdc']
# coll1 = db['12140_albb_detail']
# find1 = coll1.find({}, {'address': 1})
# for address in find1:
#     id_ = address["_id"]
#     seg_list = jieba.lcut(address["address"], cut_all=False)
#     province = seg_list[1]
#     city = seg_list[2]
#     coll1.update_many({'_id': id_}, {'$set': {'province': province, 'city': city}})  # 将省份和城市更新进数据库
#
# # seg_list = jieba.lcut('中国上海市浦东新区1200号', cut_all=False)
# # # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
# # print(seg_list)
# encoding=utf-8
import jieba

seg_list = jieba.cut("杭州长春药店", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(
    "那老子彭泽县懒坐衙，倦将文卷押，数十日不上马，柴门掩上咱，篱下看黄花。爱的是绿水青山，见一个白衣人来报，来报五柳庄幽静煞。【浦印亢厥令】春夏间，遍郊原桃杏繁，用尽丹青图画难。道童将驴鞴上鞍，忍不住只恁般顽，将一个酒葫芦杨柳上拴。", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))

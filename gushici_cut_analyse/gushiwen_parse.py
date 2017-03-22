# -*- coding: <utf-8> -*-
# 古诗文数据解析
# http://app.gushiwen.org/api/shiwen/view.aspx?id=70496&token=gswapi
from pymongo import MongoClient
import json

client = MongoClient('')
db = client['pdc']
coll = db['12251']
coll_target = db['gushiwen']

cursor = coll.find({'table': {'$ne': None}, 'mark': None}, {'table': 1}).limit(100)

for cursor_e in cursor:
    try:
        data_be = cursor_e['table'].replace(r'。"（', '。”（').replace(r'："', '：“')
        data = json.loads(data_be, strict=False)
        for k, v in data['tb_gushiwen'].items():
            data[k] = v
        del data['tb_gushiwen']
        coll_target.insert_one(data)
        coll.update_one({'_id': cursor_e['_id']}, {'$set': {'mark': 1}})

    except Exception as err:
        coll.update_one({'_id': cursor_e['_id']}, {'$set': {'mark': 0}})
        print(err)
        continue

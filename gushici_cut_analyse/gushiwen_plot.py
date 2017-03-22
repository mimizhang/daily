# -*- coding: <utf-8> -*-
# 古诗文数据分析 可视化数据
from pymongo import MongoClient
import pandas as pd
from bokeh.charts import Bar, show

client = MongoClient('mongodb://192.168.0.176:27017')
db = client['pdc']
coll = db['gushiwen']
coll_analyse = db['gushiwen_analyse']

# 朝代
dynasty = ['先秦', '两汉', '魏晋', '南北朝', '隋代', '唐代', '五代', '宋代', '金朝', '元代', '明代', '清代']
# 诗 词 曲 文言文
type = {'诗', '词', '曲', '文言文'}
# 作者
author = coll.distinct('author')
# dynasty
dynasty_list = []
for dynasty_e in author:
    num = coll.count({'author': dynasty_e})
    data = {
        'author': dynasty_e,
        'num': num
    }
    dynasty_list.append(data)
# dynasty_list_sort = sorted(dynasty_list, key=lambda x: x['num'], reverse=True)
dynasty_df = pd.DataFrame(dynasty_list)
dynasty_df = dynasty_df.sort_values(by='num', ascending=False).head(10)
print(dynasty_df)

p = Bar(data=dynasty_df, label='author', values='num', group='author', title="作者作品数TOP10", legend='top_right',
        plot_width=960, plot_height=540)
show(p)

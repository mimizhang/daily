# -*- coding: <utf-8> -*-
# 古诗文数据分析 分词 根据词频生成词云图
from pymongo import MongoClient
import re
import jieba.posseg as pseg
import time
from wordcloud import WordCloud

client = MongoClient('mongodb://192.168.0.176:27017')
db = client['pdc']
coll = db['gushiwen']
coll_analyse = db['gushiwen_analyse']

# 起始时间
start = time.time()
# 朝代
dynasty = {
    '先秦': 'xianqin',
    '两汉': 'han',
    '魏晋': 'weijin',
    '南北朝': 'nanbei',
    '隋代': 'sui',
    '唐代': 'tang',
    '五代': 'wudai',
    '宋代': 'song',
    '金朝': 'jin',
    '元代': 'yuan',
    '明代': 'ming',
    '清代': 'qing'
}
# 名词,动词,形容词
property = ('n', 'v', 'a')
# 实例化，通过font_path传入一个支持中文的字体
wc = WordCloud(font_path=u'hanyi120.ttf',  # 通过font_path传入一个支持中文的字体
               max_words=1000,
               width=1280,
               height=720,
               background_color='white',
               margin=5)
# 读入停用词
with open(u'stop_word_zh.txt', 'r', encoding='utf-8') as f:
    stop_words = set()
    for line in f.readlines():
        stop_words.add(line.strip())

# 循环词性
for pro_elem in property:
    try:
        # 初始化变量 词性
        words_frequency_dict_all = dict()
        words_frequency_list_all = []
        # 循环朝代
        for dynasty_k, dynasty_v in dynasty.items():
            # 初始化变量 词性_朝代
            # 词频:字典和列表
            words_frequency_dict = dict()
            words_frequency_list = []
            cursor = coll.find({'chaodai': dynasty_k}, {'cont': 1, '_id': 0}, no_cursor_timeout=True)
            for data in cursor:
                cont_cut = pseg.cut(re.sub(r'<br />|</p>|<p>', '', data['cont']))
                for word in cont_cut:
                    # 指定词性 过滤停用词
                    if (word.flag[0] == pro_elem and word.word not in stop_words):
                        words_frequency_dict[word.word] = words_frequency_dict.get(word.word, 0) + 1
                        words_frequency_dict_all[word.word] = words_frequency_dict_all.get(word.word, 0) + 1

            # 字典转 array of tuples
            for k, v in words_frequency_dict.items():
                words_frequency_list.append((k, v))
            # 排序
            words_frequency_list_sort = sorted(words_frequency_list, key=lambda x: x[1], reverse=True)[:2000]
            print(words_frequency_list_sort)
            # 保存词频数据
            coll_analyse.insert_one(
                {'chaodai': dynasty_k, 'properety': pro_elem, 'frequency': words_frequency_list_sort})
            # 制作词云图
            wc.fit_words(words_frequency_list_sort)
            # 保存词云图
            wc.to_file(dynasty_v + '_' + pro_elem + '.png')

        # 三种词性全部朝代 字典转 array of tuples
        for k, v in words_frequency_dict_all.items():
            words_frequency_list_all.append((k, v))
        # 排序
        words_frequency_list_all_sort = sorted(words_frequency_list_all, key=lambda x: x[1], reverse=True)[:2000]
        # 保存词频数据
        coll_analyse.insert_one({'chaodai': 'all', 'properety': pro_elem, 'frequency': words_frequency_list_all_sort})
        # 制作词云图
        wc.fit_words(words_frequency_list_all_sort)
        # 保存词云图
        wc.to_file('all_' + pro_elem + '.png')

    except Exception as err:
        print(err)
        continue

# 结束时间
end = time.time()
# 打印耗时
print(end - start)

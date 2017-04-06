# -*- coding: utf-8 -*-
# 2016国内马拉松业余选手成绩数据
# http://www.runchina.org.cn/portal.php?mod=score&ac=athlete&year=2016&sex=&age=&project=2
from pyquery import PyQuery as pq
from pymongo import MongoClient
import requests
import time

# 目标表
client = MongoClient('')
db = client['test']
coll = db['marathon2016']

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Referer': 'http://www.runchina.org.cn/portal.php?mod=score&ac=athlete&year=2016'
}
year = 2016
age_s = ['18-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']
map_s = {
    'project': 1,
    'shotScore': 2,
    'netScore': 3,
    'name': 4,
    'gender': 5,
    'compName': 6,
    'date': 7
}
project = '全程'

for age in age_s:
    try:
        for i in range(1, 5000):
            try:
                url = 'http://www.runchina.org.cn/portal.php?mod=score&ac=athlete&year=' + str(
                    year) + '&sex=&age=' + age + '&project=2&page=' + str(i)
                response = requests.get(url, headers=headers)
                table = pq(response.text)('.table')
                if table.text().find(project) == -1:
                    break
                for j, row in enumerate(table.items(selector='tr')):
                    data = {}
                    if j != 0:
                        for k, v in map_s.items():
                            data[k] = row('td').eq(v).text().replace(' PB', '')
                        data['age'] = age
                        coll.insert(data)
                        print(data)
            except Exception as err:
                print(err)
                continue
    except Exception as err:
        print(err)
        continue

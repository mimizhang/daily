# -*- coding: utf-8 -*-
# 固定电话区号
# http://dianhua.mapbar.com/
from pyquery import PyQuery as pq
from pymongo import MongoClient
import re

client = MongoClient('')
db = client['pdc']
coll = db['tel_area_code']

url = 'http://dianhua.mapbar.com/'

d = pq(url=url)

area_code_list = []

for pro_tag in d.items(selector='.phonenum'):
    province_bef = pro_tag('.ptitle').text().replace('电话区号', '')
    for city_tag in pro_tag.items(selector='dl'):
        data = {}
        data['city'] = city_tag('dt').text()
        data['area_code'] = city_tag('dd').text()
        if (province_bef in ['直辖市', '特别行政区']):
            data['province'] = data['city']
        else:
            data['province'] = province_bef

        print(data)
        # coll.insert_one(data)

        if (data['province'] not in ['香港', '澳门']):
            code_list = re.findall(r'\d+', data['area_code'])
            for code_list_elem in code_list:
                if (code_list_elem not in area_code_list):
                    area_code_list.append(code_list_elem)

print(area_code_list)

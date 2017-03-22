# -*- coding: utf-8 -*-
# 中国汽车燃料消耗量网站
# http://chinaafc.miit.gov.cn/n2068/index.html?searchId=scqycx
from pymongo import MongoClient
import requests
import re
import json
import time
import arrow

client = MongoClient('mongodb://192.168.0.176:27017')
db = client['pdc']
coll = db['qcrlxh']

headers = {
    'Referer': 'http://chinaafc.miit.gov.cn/n2050/index.html?searchId=tgrqcx',
    'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; 360SE)'
}

min = str(arrow.now().year) + arrow.now().format('MM')
max = str(arrow.now().year) + arrow.now().format('MM') + arrow.now().ceil('month').format('DD')

for i in range(1, 6):
    try:
        # 拖库 url
        # url = 'http://chaxun.miit.gov.cn/asopCmsSearch/searchIndex.jsp?params=%257B%2522goPage%2522%253A' + str(
        #     i) + '%252C%2522orderBy%2522%253A%255B%257B%2522orderBy%2522%253A%2522pl%2522%252C%2522reverse%2522%253Afalse%257D%255D%252C%2522pageSize%2522%253A100%252C%2522queryParam%2522%253A%255B%257B%2522shortName%2522%253A%2522allRecord%2522%252C%2522value%2522%253A%25221%2522%257D%255D%257D'
        # 新增数据 url
        url = 'http://chaxun.miit.gov.cn/asopCmsSearch/searchIndex.jsp?params=%257B%2522goPage%2522%253A' + str(
            i) + '%252C%2522orderBy%2522%253A%255B%257B%2522orderBy%2522%253A%2522pl%2522%252C%2522reverse%2522%253Afalse%257D%255D%252C%2522pageSize%2522%253A100%252C%2522queryParam%2522%253A%255B%257B%2522shortName%2522%253A%2522tgrq%2522%252C%2522type%2522%253A%2522number%2522%252C%2522min%2522%253A%2522' + min + '00000000%2522%252C%2522max%2522%253A%2522' + max + '000000%2522%257D%255D%257D'

        for i in range(1, 2):
            response = requests.get(url, headers=headers)
            if (response.status_code == 200):
                time.sleep(1)
                break

        if (response.status_code == 200):
            json_text = re.sub(r'null|\)|\(|;', '', response.text).strip()
            res_data = json.loads(json_text)
            if (res_data['resultMap']):
                for data in res_data['resultMap']:
                    if (coll.count({'baID': data['baID']}) == 0):
                        if '_id' in data:
                            del data['_id']
                        coll.insert_one(data)
                    print(data)
            else:
                break

    except Exception as err:
        print(err)
        continue

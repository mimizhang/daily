# -*- coding: gb2312 -*-
from pyquery import PyQuery as pq
from pprint import pprint

path = '/Users/zhangmimi/Git/daily/industry code/国民经济行业分GBT 4754-2011.html'
with open(path, 'rb') as f:
    html = f.read()
d = pq(html)
table = d('table')
alldata = []
data = {}
for i, elem in enumerate(table.items(selector='tr')):
    if i not in [0, 1, 1427]:
        for j in range(0, 3):
            if elem('td').eq(j).text().strip():
                data['category_' + str(j) + '_code'] = elem('td').eq(j).text().strip()
                data['category_' + str(j)] = elem('td').eq(4).text().strip()

        if elem('td').eq(3).text().strip():
            data['category_3_code'] = elem('td').eq(3).text().strip()
            data['category_3'] = elem('td').eq(4).text().strip()
            data['intro'] = elem('td').eq(5).text().strip()
            pprint(data)
            alldata.append(dict(data))

# pprint(alldata)
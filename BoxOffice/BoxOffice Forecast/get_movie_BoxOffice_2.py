# -*- coding: <utf-8> -*-
# 数据来源 艺恩电影智库app
import csv
from requests import post

'''
{
  'InsertDate': '日期',
  'BoxOffice': '票房',
  'ServicePrice': '服务费',
  'ShowCount': '场次',
  'AudienceCount': '人次',
  'BoxOfficeMoM': '票房环比'
}
'''


# 将票房数据写入csv文件
def to_csv(data):
    if data:
        fields = ['InsertDate', 'BoxOffice', 'ServicePrice', 'ShowCount', 'AudienceCount', 'BoxOfficeMoM']
        with open('box_office.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for data_elem in data:
                writer.writerow(data_elem)

# 爬取每天的票房数据
def getBoxOffice(start, end):
    url = 'http://ebotapp.entgroup.cn/Movie/TrendByWholeGrail_Json'
    data = 'sDateType=1&sDate=' + start + '&eDate=' + end + '&_ServicePrice=0&_MovieGenre=&_MovieFormat=&r=0.5936739987401416'
    headers = {
        'Host': 'ebotapp.entgroup.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://ebotapp.entgroup.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Mi-4c Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
        'Referer': 'http://ebotapp.entgroup.cn/Movie/GrailTrend',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8'
    }

    response = post(url, data=data, headers=headers)
    result = response.json()['data1']

    return result


if __name__ == '__main__':
    start = '2010-01-01'
    end = '2017-03-17'
    data = getBoxOffice(start, end)
    to_csv(data)

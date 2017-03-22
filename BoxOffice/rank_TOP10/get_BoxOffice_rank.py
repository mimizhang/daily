# -*- coding: <utf-8> -*-
# 电影票房排名
# 数据来源 艺恩电影智库app
import csv
from requests import post

'''
{
    'Irank': '排名',
    'EnMovieID': 626153,
    'MovieName': '影片名称',
    'BoxOffice': '票房',
    'ShowCount': '场次',
    'AudienceCount': '人次',
    'AvgBoxOffice': '平均票价',
    'ServicePrice': '服务费'
}
'''


# 将票房数据写入csv文件
def to_csv(data):
    if data:
        fields = ['Irank', 'EnMovieID', 'MovieName', 'BoxOffice', 'ShowCount', 'AudienceCount', 'AvgBoxOffice',
                  'ServicePrice']
        with open('/Users/zhangmimi/Git/course/daily/BoxOffice/box_office_rank.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for data_elem in data:
                writer.writerow(data_elem)


# 爬取票房排行
def getBoxOffice():
    url = 'http://ebotapp.entgroup.cn/BoxOfficeRanking/MovieSummary_Json'
    data = '_sYear=&_ServicePrice=0&_Calendar=&_CalendarText=&_MovieGenre=&_PageIndex=1&_PageSize=5190&r=0.5235029829753766'
    headers = {
        'Host': 'ebotapp.entgroup.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://ebotapp.entgroup.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Mi-4c Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
        'Referer': 'http://ebotapp.entgroup.cn/BoxOfficeRanking/Movie_Summary',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8'
    }

    response = post(url, data=data, headers=headers)
    result = response.json()['data1']

    return result


if __name__ == '__main__':
    data = getBoxOffice()
    to_csv(data)

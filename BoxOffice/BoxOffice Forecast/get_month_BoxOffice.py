# -*- coding: <utf-8> -*-
# 数据来源 艺恩电影智库app
import csv
from requests import post


# 爬取每个月的票房数据
# year 年份 str类型 如 '2010'
def getBoxOffice(monthID):
    url = 'http://ebotapp.entgroup.cn/Movie/TrendByWholeGrail_Json'
    data = 'sDateType=3&sDate=' + monthID + '&eDate=' + monthID + '&_ServicePrice=0&_MovieGenre=&_MovieFormat=&r=0.9352364118644103'
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
    result = response.json()

    return result


# 将票房数据写入csv文件
def to_csv(data, fields, f_name):
    if data:
        with open(f'/Users/zhangmimi/Git/course/daily/BoxOffice/{f_name}.csv', 'a+') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            for data_elem in data:
                writer.writerow(data_elem)


# 创建文件
def create_csv(fields, f_name):
    with open(f'/Users/zhangmimi/Git/course/daily/BoxOffice/{f_name}.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()


if __name__ == '__main__':
    start = 49
    end = 134
    # 字段
    fields_data = ['InsertDate', 'M_Year', 'Months', 'MonthID', 'BoxOffice', 'ServicePrice', 'ShowCount',
                   'AudienceCount', 'BoxOfficeMoM']
    # 创建文件
    create_csv(fields_data, 'monthTotalBoxOffice')
    # 爬取、写入csv
    for i in range(start, end + 1):
        response = getBoxOffice(str(i))
        to_csv(response['data1'], fields_data, 'monthTotalBoxOffice')

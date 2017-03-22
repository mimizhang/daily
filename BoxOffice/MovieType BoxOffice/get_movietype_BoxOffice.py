# -*- coding: <utf-8> -*-
# 数据来源 艺恩电影智库app
import csv
from requests import post


# 爬取各城市每年的数据
# year 年份 str类型 如 '2010'
def getBoxOffice(year):
    url = 'http://ebotapp.entgroup.cn/Information/MovieInvestment_Json'
    data = '&_Order=MovieCount&_OrderType=DESC&_sDate=' + year + '-01-01&_eDate=' + year + '-12-31&r=0.11431054146135544'
    headers = {
        'Host': 'ebotapp.entgroup.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://ebotapp.entgroup.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Mi-4c Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
        'Referer': 'http://ebotapp.entgroup.cn/Information/Movie_Investment',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8'
    }

    response = post(url, data=data, headers=headers)
    result = response.json()

    return result


# 加入year字段
def parse_response(year, data):
    for i in range(0, len(data['data2'])):
        data['data2'][i]['year'] = year
    return data


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
    start = 2010
    end = 2016
    # 字段
    fields_data = ['GenreID', 'GenreName', 'MovieCount', 'MovieCountPercent', 'MovieCountYoY', 'BoxOffice',
                   'BoxOfficePercent', 'BoxOfficeYoY', 'ShowCount', 'ShowCountPercent', 'ShowCountYoY', 'AudienceCount',
                   'AudienceCountPercent', 'AudienceCountYoY', 'year']
    # 创建文件
    create_csv(fields_data, 'annualMovieTypeBoxOffice')
    # 爬取、写入csv
    for i in range(start, end + 1):
        response = getBoxOffice(str(i))
        parse_data = parse_response(str(i), response)
        to_csv(parse_data['data2'], fields_data, 'annualMovieTypeBoxOffice')

# -*- coding: <utf-8> -*-
# 数据来源 艺恩电影智库app
import csv
from requests import post


# 爬取各院线每年的数据
# year 年份 str类型 如 '2010'
def getBoxOffice(year):
    url = 'http://ebotapp.entgroup.cn/Line/GetIndex_List'
    data = 'Order=201&OrderType=DESC&_ServicePrice=1&_Date=' + year + '&_DateSort=Year&_sDate=' + year + '-01-01&_eDate=' + year + '-12-31&_City=&_CityLevel=&_Index=101%2C102%2C201%2C203%2C801%2C604&r=0.8720778697660314'
    headers = {
        'Host': 'ebotapp.entgroup.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://ebotapp.entgroup.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Mi-4c Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
        'Referer': 'http://ebotapp.entgroup.cn/Line/Index',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8'
    }

    response = post(url, data=data, headers=headers)
    result = response.json()

    return result


# 加入year字段
def parse_response(year, data):
    data['data1'][0]['year'] = year
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
    fields_data1 = ['UpTime', 'sDate', 'eDate', 'SumBoxOffice', 'SumServicePrice', 'SumShowCount', 'SumOfferSeat',
                    'SumAudienceCount', 'SumAvgBoxOffice', 'SumAvgShowPeople', 'SumCinemaCount', 'SumScreen',
                    'SumCinemaSeat', 'SumAvgBoxOffice1', 'SumAvgShowPeople1', 'SumAttendance', 'year']
    fields_data2 = ['Irank', 'CinemaLineID', 'EnbaseID', 'CinemaLineName', 'BoxOffice', 'ShowCount', 'AudienceCount',
                    'ServicePrice', 'AvgShowPeople', 'year']
    # 创建文件
    create_csv(fields_data1, 'annualTotalBoxOffice')
    create_csv(fields_data2, 'annualLineBoxOffice')
    # 爬取、写入csv
    for i in range(start, end + 1):
        response = getBoxOffice(str(i))
        parse_data = parse_response(str(i), response)
        to_csv(parse_data['data1'], fields_data1, 'annualTotalBoxOffice')
        to_csv(parse_data['data2'], fields_data2, 'annualLineBoxOffice')

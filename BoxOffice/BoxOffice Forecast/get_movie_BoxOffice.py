# -*- coding: <utf-8> -*-
# 数据来源 艺恩电影智库app
from requests import post
import arrow
from pymongo import MongoClient
from multiprocessing.dummy import Pool as ThreadPool
from pprint import pprint


# 爬取每天的票房数据
# date:日期('2013-03-08'),n:重试次数(5)
def getBoxOffice(date, n):
    url = 'http://ebotapp.entgroup.cn/Movie/GetIndex_List'
    data = '_IsChart=0&_Order=201&_OrderType=DESC&_PageIndex=1&_PageSize=50&_ServicePrice=1&_Date=' + date + '&_DateSort=Day&_sDate=' + date + '&_eDate=' + date + '&_Line=&_City=&_CityLevel=&_Index=101%2C102%2C201%2C225%2C801%2C606&r=0.2807297752092923'
    headers = {
        'Host': 'ebotapp.entgroup.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://ebotapp.entgroup.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Mi-4c Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
        'Referer': 'http://ebotapp.entgroup.cn/Movie/Index',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8'
    }
    # 请求数据,重试n次
    for i in range(n):
        response = 0

        try:
            response = post(url, data=data, headers=headers)
            if response.status_code == 200:
                break
        except:
            continue

    if response and response.status_code == 200:
        result = response.json()
        result['date'] = date
        result['timestamp'] = arrow.get(date).timestamp
        result['data1'][0]['date'] = date
        result['data1'][0]['timestamp'] = arrow.get(date).timestamp
        return result
    else:
        return 0


# 插入数据库
def to_db(data):
    if data:
        client = MongoClient('')
        db = client['test']
        coll_all = db['movie_boxoffice']
        coll_boxoffice = db['boxoffice']
        coll_all.insert_one(data)
        coll_boxoffice.insert_one(data['data1'][0])
        pprint(data['data1'][0])


# 主控
def main(date):
    try:
        data = getBoxOffice(date, 5)
        to_db(data)
    except Exception as err:
        print(err)


# 日期生成器
# start:日期('2013-03-08'),day:从start开始往前多少天
def create_date(start, day):
    for i in range(day):
        date = arrow.get(start).replace(days=-i).format('YYYY-MM-DD')
        yield date


if __name__ == '__main__':
    start = '2017-03-16'
    day = 2555
    date_list = create_date(start, day)
    p = ThreadPool(8)
    s = arrow.now().timestamp
    p.map(main, date_list)
    p.close()
    p.join()
    e = arrow.now().timestamp
    print('耗时 : ' + str(e - s) + ' s')

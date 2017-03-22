# -*- coding: <utf-8> -*-
'''
{
  'InsertDate': '日期',
  'BoxOffice': '票房',
  'ServicePrice': '服务费',
  'ShowCount': '场次',
  'AudienceCount': '人次',
  'BoxOfficeMoM': '票房环比',
  'PerAudienceShow': '场均人次',
  'PerAudienceOffice': '人均票房',
  'PerShowBoxOffice': '场均票房',
}
'''
import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv('/Users/zhangmimi/Git/course/daily/BoxOffice/box_office.csv')
df['InsertDate'] = pd.to_datetime(df['InsertDate'])
df = df[df.InsertDate <= '2016-12-31']
df['PerAudienceOffice'] = df['BoxOffice'] / df['AudienceCount']
df['PerShowBoxOffice'] = df['BoxOffice'] / df['ShowCount']
df['PerShowAudience'] = df['AudienceCount'] / df['ShowCount']

def fsct(field):
    new = df.loc[:, ['InsertDate', field]].sort_values(by='InsertDate')
    # new[field] = np.log(new[field])
    plt.plot(new['InsertDate'], new[field], '--')
    plt.savefig(f'/Users/zhangmimi/Git/course/daily/BoxOffice/{field}.png', dpi=150)
    # plt.show()
    new.columns = ["ds", "y"]

    newyear = pd.DataFrame({
        'holiday': 'New Year\'s Day',
        'ds': pd.to_datetime(
            ['2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01', '2013-12-31', '2015-01-01', '2016-01-01',
             '2016-12-31']),
        'lower_window': -1,
        'upper_window': 2,
    })

    spring = pd.DataFrame({
        'holiday': 'Spring Festival',
        'ds': pd.to_datetime(
            ['2010-02-13', '2011-02-02', '2012-01-28', '2013-02-09', '2014-01-30', '2015-02-18', '2016-02-07',
             '2017-01-27']),
        'lower_window': 0,
        'upper_window': 6,
    })

    national = pd.DataFrame({
        'holiday': 'National Day',
        'ds': pd.to_datetime(
            ['2010-10-01', '2011-10-01', '2012-09-30', '2013-10-01', '2014-10-01', '2015-10-01', '2016-10-01',
             '2017-10-01']),
        'lower_window': -1,
        'upper_window': 6,
    })

    christmas = pd.DataFrame({
        'holiday': 'Christmas Eve',
        'ds': pd.to_datetime(
            ['2010-12-24', '2011-12-24', '2012-12-24', '2013-12-24', '2014-12-24', '2015-12-24', '2016-12-24',
             '2017-12-24', ]),
        'lower_window': 0,
        'upper_window': 1,
    })

    holidays = pd.concat((newyear, spring, national, christmas))

    m = Prophet(interval_width=0.8, holidays=holidays, holidays_prior_scale=20)
    m.fit(new)
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)
    # forecast.to_csv(f'/Users/zhangmimi/Git/course/daily/BoxOffice/{field}forecast.csv')
    # print(forecast.tail())
    m.plot(forecast).savefig(f'/Users/zhangmimi/Git/course/daily/BoxOffice/{field}forecast.png', dpi=150)
    m.plot_components(forecast).savefig(f'/Users/zhangmimi/Git/course/daily/BoxOffice/{field}trend.png', dpi=150)
    # return forecast

fcstData = fsct('BoxOffice')
# print(fcstData['2017-01-01'<=fcstData.ds <= '2017-02-28'].groupby('ds').sum())
# sum_ = fcstData['2017-01-01'<=fcstData.ds <= '2017-02-28']
# sum = sum_.groupby('ds').sum()
# print(sum)
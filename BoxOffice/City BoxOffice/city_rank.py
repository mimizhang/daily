# -*- coding: <utf-8> -*-
import pandas as pd
import matplotlib as mpl

mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 设置中文字体
myfont = fm.FontProperties(
    fname='/Users/zhangmimi/anaconda/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/msyh.ttf')
font_size = 8
mpl.rcParams['font.size'] = font_size  # 更改默认更新字体大小
plt.style.use('ggplot')


def get_sum_New(data, fieldName):
    total_rank = data.groupby('CityName').sum().sort_values(by=fieldName)
    result = total_rank.tail(10)

    return result

def get_mean_New(data, fieldName):
    total_rank = data.groupby('CityName').mean().sort_values(by=fieldName)
    result = total_rank.tail(10)

    return result

# def get_city_new(city,data):
#     result = data[data.CityName==city]
#
#     return result


def graph_rank(data, fieldName):
    plt.subplots()
    plt.ylabel('CityName', fontsize=8)
    plt.xlabel(fieldName, fontsize=8)
    plt.title(f'City {fieldName} Top10(2010-2016)', fontsize = 8)
    plt.yticks(range(1, 11), data.index, fontproperties=myfont, fontsize=8)
    plt.subplots_adjust(right=0.95, wspace=0.5, hspace=0.5, bottom=0.1, top=0.95)
    plt.barh(range(1, 11), data[fieldName])
    plt.savefig(f'/Users/zhangmimi/Git/course/daily/BoxOffice/City BoxOffice/City{fieldName}Top10(2010-2016).png', dpi = 150)


# def graph_change(data,field,index):
#     plt.subplots()
#     # plt.style.use('fivethirtyeight')
#     for elem in index:
#         city_new = get_city_new(elem,data)
#         plt.plot(city_new['year'], city_new[field])


if __name__ == '__main__':
    df = pd.read_csv('/Users/zhangmimi/Git/course/daily/BoxOffice/City BoxOffice/annualCityBoxOffice.csv')
    field = 'BoxOffice'
    new = get_sum_New(df, field)
    graph_rank(new, field)
    plt.show()


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
    total_rank = data.groupby('CinemaLineName').sum().sort_values(by=fieldName)
    result = total_rank.tail(10)

    return result

def get_mean_New(data, fieldName):
    total_rank = data.groupby('CinemaLineName').mean().sort_values(by=fieldName)
    result = total_rank.tail(10)

    return result


def graph_rank(data, fieldName):
    plt.ylabel('CinemaLineName', fontsize=8)
    plt.xlabel(fieldName, fontsize=8)
    plt.title(f'CinemaLine {fieldName} Top10(2010-2016)', fontsize = 8)
    plt.yticks(range(1, 11), data.index, fontproperties=myfont, fontsize=8)
    plt.subplots_adjust(left=0.19,right=0.95, wspace=0.5, hspace=0.5, bottom=0.1, top=0.95)
    plt.barh(range(1, 11), data[fieldName])
    plt.savefig(f'/Users/zhangmimi/Git/course/daily/BoxOffice/Line BoxOffice/CinemaLine{fieldName}Top10(2010-2016).png', dpi = 150)
    # plt.show()

# def graph_change(df,new):




if __name__ == '__main__':
    df = pd.read_csv('/Users/zhangmimi/Git/course/daily/BoxOffice/Line BoxOffice/annualLineBoxOffice.csv')
    field = 'AvgShowPeople'
    new = get_mean_New(df, field)
    graph_rank(new, field)
    # for elem in new.index:
    #     print(elem)


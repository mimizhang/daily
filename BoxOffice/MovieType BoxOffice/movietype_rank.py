# -*- coding: <utf-8> -*-
import better_exceptions
import numpy as np
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
    total_rank = data.groupby('GenreName').sum().sort_values(by=fieldName)
    result = total_rank.tail(10)

    return result


def get_mean_New(data, fieldName):
    total_rank = data.groupby('GenreName').mean().sort_values(by=fieldName)
    result = total_rank.tail(10)

    return result


def graph_rank(data, fieldName):
    plt.ylabel('Movie Type', fontsize=8)
    plt.xlabel(fieldName, fontsize=8)
    plt.title(f'Movie Type {fieldName} Top10(2010-2016)', fontsize = 8)
    plt.yticks(range(1, 11), data.index, fontproperties=myfont, fontsize=8)
    plt.subplots_adjust(left=0.1, right=0.95, wspace=0.5, hspace=0.5, bottom=0.1, top=0.95)
    plt.barh(range(1, 11), data[fieldName])
    plt.savefig(f'/Users/zhangmimi/Git/daily/BoxOffice/MovieType BoxOffice/MovieTypeAudienceCountTop10(2010-2016).svg', dpi = 150)
    # plt.show()


def get_type_new(GenreName, data):
    result = data[data.GenreName == GenreName]

    return result


def graph_change(data, field, index):
    plt.subplots(1, 1, figsize=(16,9))
    # plt.style.use('fivethirtyeight')
    for elem in index:
        type_new = get_type_new(elem, data)
        plt.plot(type_new['year'], type_new[field])

    plt.show()

# visdom测试
# from visdom import Visdom
# vis = Visdom()
# def test(data,fieldName):
#     win = vis.bar(
#         X=data[fieldName],
#         opts=dict(
#         rownames=list(data.index)
#         )
#     )
# def test_type_new(data,field):
#     result = data.groupby(by=['GenreName','year']).sum()[field].unstack().T
#     return result
#
# def change_test(data, field):
#     from visdom import Visdom
#     vis = Visdom()
#     vis.line(
#         Y=np.array(test_type_new(data,field)),
#         X=np.array((test_type_new(data,field).index)),
#         opts=dict(
#             legend=list((test_type_new(data,field).columns))
#         )
#     )


if __name__ == '__main__':
    df = pd.read_csv('/Users/zhangmimi/Git/daily/BoxOffice/MovieType BoxOffice/annualMovieTypeBoxOffice.csv')
    field = 'AudienceCount'
    new = get_sum_New(df, field)
    graph_rank(new, field)
    graph_change(df, field, df.GenreName)
    # change_test(df, 'BoxOffice')
    # test(new,field)

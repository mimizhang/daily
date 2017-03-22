# -*- coding: <utf-8> -*-
import pandas as pd
import matplotlib as mpl

mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 设置中文字体
myfont = fm.FontProperties(
    fname='/Users/zhangmimi/anaconda/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/msyh.ttf')

plt.style.use('ggplot')
df = pd.read_csv('/Users/zhangmimi/Git/course/daily/BoxOffice/rank_TOP10/box_office_rank.csv')
df['perShowBoxOffice'] = df['BoxOffice'] / df['ShowCount']
df['perShowAudience'] = df['AudienceCount'] / df['ShowCount']


def graph(fieldName):
    # 由于一些早期的电影数据不准确,所以只取票房总榜TOP150的进行分析
    new = df.loc[:150, ['MovieName', fieldName]].replace('inf', 0)
    new = new.sort_values(by=fieldName, ascending=True).tail(10)
    print(new)
    font_size = 8
    mpl.rcParams['font.size'] = font_size  # 更改默认更新字体大小
    plt.ylabel('MovieName', fontsize=8)
    plt.xlabel(fieldName, fontsize=8)
    plt.title(f'{fieldName}Top10', fontsize = 8)
    plt.yticks(range(1, 11), new['MovieName'], fontproperties=myfont, fontsize=8)
    plt.subplots_adjust(left=0.23, right=0.98, wspace=0.5, hspace=0.5,
                        bottom=0.1, top=0.95)
    plt.barh(range(1, 11), new[fieldName])
    plt.savefig(f'/Users/zhangmimi/Git/course/daily/BoxOffice/rank_TOP10/{fieldName}Top10.png', dpi = 150)
    # plt.show()


graph('perShowAudience')

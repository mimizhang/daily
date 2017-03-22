# -*- coding: <utf-8> -*-
import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv('/Users/zhangmimi/Git/course/daily/BoxOffice/annualCityBoxOffice.csv')

total_rank = df.groupby('CityName').sum().sort_values(by='BoxOffice')
print(total_rank.head(10))

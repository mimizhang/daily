---
title: Facebook可视化工具Visdom入门
date: 2017-03-24 15:18:04
categories:
- Python
tags:
- Facebook
- visdom
- python画图工具
---

Visdom支持Python和Torch，以下内容只涉及Python，具体内容请参照[官方文档](https://github.com/facebookresearch/visdom)。

## 1. Setup 安装 

通过`pip`安装

```bash
pip install visdom
```

## 2. Launch 启动

终端输入下面命令：

```bash
python -m visdom.server
```

在浏览器中打开http://localhost:8097，进入下面的界面：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-03-23%20%E4%B8%8A%E5%8D%8811.38.44.png)

## 3. Visualization API

目前Visdom支持以下API：

- `vis.scatter`  : 2D or 3D 点状图
- `vis.line`     : line plots 折线图
- `vis.stem`     : stem plots 杆状图
- `vis.heatmap`  : heatmap plots 热力图
- `vis.bar`      : bar graphs 条形图
- `vis.histogram`: histograms 直方图
- `vis.pie `：饼状图
- `vis.boxplot`  : boxplots 箱形图
- `vis.surf`     : surface plots 曲面图
- `vis.contour`  : contour plots 等高线图
- `vis.quiver`   : quiver plots 矢量图
- `vis.image`    : images 图片
- `vis.text`     : text box 文本
- `vis.save`     : serialize state

```python
from visdom import Visdom
import numpy as np
import math
```

### 3.1 `vis.scatter`  

```python
# scatter plots
Y = np.random.rand(30)
X = np.random.rand(30, 2)
viz.scatter(
    X=X, # 二维或者三维矩阵
    Y=(Y[Y > 0] + 1.5).astype(int), # 暂时还不知道是什么鬼
    opts=dict(
        legend=['Apples', 'Pears'], # 图标
        xtickmin=-5, # 刻度最小值
        xtickmax=5, #刻度最大值
        xtickstep=0.5, # 刻度间隔
        ytickmin=-5,
        ytickmax=5,
        ytickstep=0.5,
        markersymbol='point', # 点的样式
        markersize=10 #点大小
    )
)
```

### 3.2 `vis.line` 

插播一条Numpy广告

```python
>>> a = np.array((1,2,3))
>>> b = np.array((2,3,4))
>>> np.column_stack((a,b))
array([[1, 2],
       [2, 3],
       [3, 4]])
>>> np.row_stack((a,b))
array([[1, 2, 3],
       [2, 3, 4]])
```

`Y`是一个N×M的矩阵，对应的是y轴的值。X为与Y一一对应的X轴上的值。如果X为N×1矩阵，那么Y上所有列所对应的X轴上的值都是相同的。

```python
Y = np.linspace(-5, 5, 100)
viz.line(
    Y=np.column_stack((Y * Y, np.sqrt(Y + 5))),
    X=np.column_stack((Y, Y)),
    opts=dict(markers=False),
)
```

```python
Y = np.linspace(0, 4, 200)
win = viz.line(
    Y=np.column_stack((np.sqrt(Y), np.sqrt(Y) + 2)),
    X=np.column_stack((Y, Y)),
    opts=dict(
        fillarea=True,
        legend=False,
        width=400,
        height=400,
        xlabel='Time',
        ylabel='Volume',
        ytype='log',
        title='Stacked area plot',
        marginleft=30,
        marginright=30,
        marginbottom=80,
        margintop=30,
    ),
)
```

下面是一个在原图上再画图的例子(试试看第二个`vis.line`去掉`update`参数会发生什么？`update='append'`和是一样的`updateTrace`效果)：

```python
# line updates
win = viz.line(
    X=np.column_stack((np.arange(0, 10), np.arange(0, 10))),  
    Y=np.column_stack((np.linspace(5, 10, 10), np.linspace(5, 10, 10) + 5)),
)
viz.line(
    X=np.column_stack((np.arange(10, 20), np.arange(10, 20))),
    Y=np.column_stack((np.linspace(5, 10, 10), np.linspace(5, 10, 10) + 5)),
    win=win,
    update='append'
)
viz.updateTrace(
    X=np.arange(21, 30),
    Y=np.arange(1, 10),
    win=win,
    name='2'
)
viz.updateTrace(
    X=np.arange(1, 10),
    Y=np.arange(11, 20),
    win=win,
    name='4'
)
```

### 3.3 `vis.stem`  

参数`X`和`Y` 的设定与`vis.line`相反：`X`是一个N×M矩阵，表示`M`个时间序列数据中,每个时间序列数据`N`个时间点所对应的值。`Y`为与`X`相对应的时间点。如果`Y`是一个N×1矩阵，那么这`M`个时间序列数据所对应的时间点都是相同的。

```python
# stemplot
Y = np.linspace(0, 2 * math.pi, 70)
X = np.column_stack((np.sin(Y), np.cos(Y)))
viz.stem(
    X=X,
    Y=Y,
    opts=dict(legend=['Sine', 'Cosine'])
)
```

### 3.4 `vis.heatmap`

这里再插播一条Numpy的广告：`numpy.outer`向量外积,`numpy.inner`向量内积(点乘)。

```python
>>> a = np.ones((5,))
>>> b = np.linspace(-2, 2, 5)
>>> np.dot(a,b)
0.0
>>> np.inner(a,b)
0.0
>>> np.outer(a,b)
array([[-2., -1.,  0.,  1.,  2.],
       [-2., -1.,  0.,  1.,  2.],
       [-2., -1.,  0.,  1.,  2.],
       [-2., -1.,  0.,  1.,  2.],
       [-2., -1.,  0.,  1.,  2.]])
>>> a*b
array([-2., -1.,  0.,  1.,  2.])
```

参数`X`是一个N×M矩阵，每个点对应于热力图上的每个位置。

```python
# heatmap
viz.heatmap(
    X=np.outer(np.arange(1, 6), np.arange(1, 11)),
    opts=dict(
        columnnames=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
        rownames=['y1', 'y2', 'y3', 'y4', 'y5'],
        colormap='Electric',
    )
)
```

### 3.5 `vis.bar`

参数`X`是一个N×M矩阵，矩阵中的每个值对应的是每个柱形的高度。M对应的是变量的数量。Y是一个N×1矩阵，对应的是X轴上的取值。

参数`stacked=True`时画出的堆叠图

```python
# bar plots
viz.bar(X=np.random.rand(20))
viz.bar(
    X=np.abs(np.random.rand(5, 3)),
#    Y=np.array(['2012', '2013', '2014', '2015', '2016']),
    opts=dict(
        stacked=True,
        legend=['Facebook', 'Google', 'Twitter'],
        rownames=['2012', '2013', '2014', '2015', '2016']
    )
)
viz.bar(
    X=np.random.rand(20, 3),
    opts=dict(
        stacked=False,
        legend=['The Netherlands', 'France', 'United States']
    )
)
```

### 3.6 `vis.histogram`(貌似暂时只能支持数字)

`X`是一个N×1矩阵。

参数`numbins`指定了直方的个数。默认为30。

```python
# histogram
viz.histogram(
        X=np.random.rand(10000), 
        opts=dict(numbins=20)
)
viz.histogram(
        X=np.random.randn(10000), 
        opts=dict(numbins=30)
)
```

### 3.7 `vis.pie `

参数`X`中的每一个值对应每一个百分比

```python
# pie chart
X = np.asarray([19, 26, 55])
viz.pie(
    X=X,
    opts=dict(legend=['Residential', 'Non-Residential', 'Utility'])
)
```

### 3.8 `vis.boxplot`

参数`X`是一个N×M矩阵，M是箱子的个数。

```python
# boxplot
X = np.random.rand(100, 2)
X[:, 1] += 2
viz.boxplot(
    X=X,
    opts=dict(legend=['Men', 'Women'])
)
```

### 3.9 `vis.surf`,`vis.contour`

这里再插播一条Numpy的广告：`numpy.tile`,`numpy.transpose`,`numpy.reshape`

```python
>>> a = np.array([0, 1, 2])
>>> np.tile(a, 2)
array([0, 1, 2, 0, 1, 2])
>>> np.tile(a, (2, 2))
array([[0, 1, 2, 0, 1, 2],
       [0, 1, 2, 0, 1, 2]])
>>> np.tile(a, (2, 1, 2))
array([[[0, 1, 2, 0, 1, 2]],
       [[0, 1, 2, 0, 1, 2]]])
>>> a = np.arange(6).reshape((3, 2))
>>> a
array([[0, 1],
       [2, 3],
       [4, 5]])
>>> np.transpose(a)
array([[0, 2, 4],
       [1, 3, 5]])
```



```python
# contour
x = np.tile(np.arange(1, 101), (100, 1))
y = x.transpose()
X = np.exp((((x - 50) ** 2) + ((y - 50) ** 2)) / -(20.0 ** 2))
viz.contour(X=X, opts=dict(colormap='Viridis'))

# surface
viz.surf(X=X, opts=dict(colormap='Hot'))
```

### 3.10 `vis.quiver`   



### 3.11 `viz.text`,`viz.close()`

打印文本，关闭某个窗口

```python
>>> textwindow = viz.text('Hello World!')
>>> viz.close(win=textwindow)
''
```

## 4. `OPTS`参数


- `options.title`       : 标题
- `options.width`       : 图片宽度
- `options.height`      : 图片高度
- `options.showlegend`  : 是否显示图标 (`true` or `false`)
- `options.xtype`       : type of x-axis (`'linear'` or `'log'`)
- `options.xlabel`      : label of x-axis
- `options.xtick`       : show ticks on x-axis (`boolean`)
- `options.xtickmin`    : X轴上的第一个刻度（最小） (`number`)
- `options.xtickmax`    : X轴上的最后一个刻度（最大） (`number`)
- `options.xtickstep`   : X轴刻度间距 (`number`)
- `options.ytype`       : type of y-axis (`'linear'` or `'log'`)
- `options.ylabel`      : label of y-axis
- `options.ytick`       : show ticks on y-axis (`boolean`)
- `options.ytickmin`    : Y轴上的第一个刻度（最小） (`number`)
- `options.ytickmax`    : Y轴上的最后一个刻度（最大） (`number`)
- `options.ytickstep`   : Y轴刻度间距 (`number`)
- `options.marginleft`  : left margin (in pixels)
- `options.marginright` : right margin (in pixels)
- `options.margintop`   : top margin (in pixels)
- `options.marginbottom`: bottom margin (in pixels)
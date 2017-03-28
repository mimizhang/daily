---
title: pyocr+tesseract入门
date: 2017-03-28 11:54:30
tags:
- pyocr
- tesseract
- python
categories:
- Python
---

> 针对mac系统

tesseract项目主页：https://github.com/tesseract-ocr/tesseract

pyocr项目主页：https://github.com/jflesch/pyocr

## 1. tesseract安装

终端输入以下命令(未安装`brew`可前往[这里](https://brew.sh/index_zh-cn.html)安装)

```bash
brew install tesseract
```

## 2. tesseract语言包

- 各语言包下载地址：https://github.com/tesseract-ocr/tesseract/wiki/Data-Files
- 语言包安放路径：/usr/local/Cellar/tesseract/3.05.00/share/tessdata(3.05.00为版本号) 或：/usr/local/share/tessdata

## 3. tesseract手册

通过man或者\-\-help(-h)命令查看帮助手册

```bash
zhangmimideMacBook-Pro:3.05.00 zhangmimi$ man tesseract
zhangmimideMacBook-Pro:3.05.00 zhangmimi$ tesseract -h
```

## 4. PyOCR

### 4.1 常用API

#### 4.1.1  `pyocr.get_available_tools()`

列出可用的ocr程序(返回list)，**Pyocr**目前支持**Tesseract**和**Cuneiform**，这里我们只讨论**Tesseract**。

```python
In[35]: pyocr.get_available_tools()
Out[35]: 
[<module 'pyocr.tesseract' from '/Users/zhangmimi/anaconda/lib/python3.6/site-packages/pyocr/tesseract.py'>]
```

#### 4.1.2 `pyocr.tesseract.is_available()`

**tesseract**是否可用。这里没有安装**libtesseract**，所以返回`false`。

```python
In[36]: pyocr.tesseract.is_available()
Out[36]: 
True
In[37]: pyocr.libtesseract.is_available()
Out[37]: 
False
```

#### 4.1.3 `pyocr.tesseract.get_name()`

获取tesseract的名称

```python
In[38]: pyocr.tesseract.get_name()
Out[38]: 
'Tesseract (sh)'
```

#### 4.1.4 `pyocr.tesseract.get_version()`

版本号

```python
In[39]: pyocr.tesseract.get_version()
Out[39]: 
(3, 5, 0)
```

#### 4.1.5 `pyocr.tesseract.get_available_builders()`

可用的builder，返回的是list。

```python
In[40]: pyocr.tesseract.get_available_builders()
Out[40]: 

[pyocr.builders.LineBoxBuilder,
 pyocr.builders.TextBuilder,
 pyocr.builders.WordBoxBuilder,
 pyocr.tesseract.CharBoxBuilder,
 pyocr.builders.DigitBuilder]
```

#### 4.1.6 `pyocr.tesseract.get_available_languages()`

可用的语言，返回的是list。博主安装时默认安装的语言包只有`eng`和`osd`,其他语言包可自行添加。

```python
In[41]: pyocr.tesseract.get_available_languages()
Out[41]: 
['chi_sim', 'chi_tra', 'eng', 'equ', 'osd']
```

#### 4.1.7 `pyocr.tesseract.cleanup()`

删除某个文件（忽略不存在的文件，参数为文件名）

#### 4.1.8 `pyocr.tesseract.can_detect_orientation`

是否可以检测方向

```python
In[43]: pyocr.tesseract.can_detect_orientation()
Out[43]: 
True
```

#### 4.1.9 `pyocr.tesseract.detect_orientation`

检测图片方向，**Tesseract** 只能返回0, 90, 180, 270这四个角度。

```python
In[50]: pyocr.tesseract.detect_orientation(
            Image.open('/Users/zhangmimi/Desktop/屏幕快照 2017-03-28 下午12.15.21.png'),
            lang='eng'
        )
Out[50]: 
{'angle': 0, 'confidence': 19.53}
```

#### 4.1.10 `pyocr.tesseract.image_to_string`

图像内容转字符串

### 5. 用法

下面沿着官方文档走一遍(以img1和img2为例)：

**img1:**

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-03-28%20%E4%B8%8B%E5%8D%8812.15.21.png)

**img2：**

![](http://o7qrps1cr.bkt.clouddn.com/digit_test.png)

#### 5.1 Initialization初始化

```python
from PIL import Image
import sys

import pyocr
import pyocr.builders

# 列出可用的程序，我们这里只安装了tesseract
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    # 如果没有找到则退出程序
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'tesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))
```
#### 5.2 Image to text


参数:
    image --- 先通过PIL模块打开DISK中的图片.
    lang --- 指定语言.
    builder --- 默认的builder是TextBuilder.

返回:
    返回的类型随所指定的builder而不同。

```python
# TextBuilder用法
txt = tool.image_to_string(
    Image.open('/Users/zhangmimi/Desktop/屏幕快照 2017-03-28 下午12.15.21.png'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
print(txt)
# 输出的结果为字符串
# txt is a Python string

# WordBoxBuilder用法
word_boxes = tool.image_to_string(
    Image.open('/Users/zhangmimi/Desktop/屏幕快照 2017-03-28 下午12.15.21.png'),
    lang=lang,
    builder=pyocr.builders.WordBoxBuilder()
)
for elem in word_boxes:
    print(elem.content, elem.position)
# 返回的是一个list,list中的每个元素为box objects,box objects中存着box.content内容和每个词的位置box.position
# # list of box objects. For each box object:
# #   box.content is the word in the box
# #   box.position is its position on the page (in pixels)
# #
# # Beware that some OCR tools (Tesseract for instance)
# # may return empty boxes

# LineBoxBuilder用法
line_and_word_boxes = tool.image_to_string(
    Image.open('/Users/zhangmimi/Desktop/屏幕快照 2017-03-28 下午12.15.21.png'),
    lang=lang,
    builder=pyocr.builders.LineBoxBuilder()
)
# line_and_word_boxes也是list,list中的每个line objects有line.word_boxes(结构和box objects相同),line.content(每一行的内容)和位置line.position
print(len(line_and_word_boxes))
for line in line_and_word_boxes:
    for word in line.word_boxes:
        print(word.content, word.position)
    print(line.content, line.position)
# # list of line objects. For each line object:
# #   line.word_boxes is a list of word boxes (the individual words in the line)
# #   line.content is the whole text of the line
# #   line.position is the position of the whole line on the page (in pixels)
# #
# # Beware that some OCR tools (Tesseract for instance)
# # may return empty boxes
# 识别数字
# Digits - Only Tesseract (not 'libtesseract' yet !)
digits = tool.image_to_string(
    Image.open('/Users/zhangmimi/Desktop/digit_test.png'),
    lang=lang,
    builder=pyocr.builders.DigitBuilder(),
)

print(digits.replace(' ', ''))
# digits is a python string
```
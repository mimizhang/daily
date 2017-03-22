# -*- coding: utf-8 -*-
from newspaper import Article
from time import time
import gevent
from gevent import monkey
monkey.patch_all()
url = 'http://finance.china.com.cn/industry/medicine/20170217/4102582.shtml'

start = time()

a = Article(url, language='zh')
a.download()
a.parse()
a.nlp()
# print(a.text)
print(a.keywords)

end = time()

print(end-start)
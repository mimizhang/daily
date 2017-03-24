---
title: pip入门指南
date: 2017-03-15 20:29:10
categories:
- Python
tags: 
- python 
- pip
---

## 1. [Quickstart](https://pip.pypa.io/en/stable/quickstart/)

### 1.1 Install a package from PyPI
```bash
$ pip install SomePackage
```
### 1.2 Show what files were installed:
```bash
$ pip show --files SomePackage
```
### 1.3 List what packages are outdated:
```bash
$ pip list --outdated
```
### 1.4 Upgrade a package:
```bash
$ pip install --upgrade SomePackage
```
### 1.5 Uninstall a package:
```bash
$ pip uninstall SomePackage
```
### 1.6 Upgrading pip
```bash
pip install -U pip
```
### 1.7 安装指定版本的包
```bash
pip install elasticsearch==2.4.0
zhangmimideMacBook-Pro:~ zhangmimi$ pip install elasticsearch==2.4.0
Collecting elasticsearch==2.4.0
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/3f/be/980d79da0fbb14acc29e3c9b724287cbc24be2cb1ede47f2c0eecba60809/elasticsearch-2.4.0-py2.py3-none-any.whl (54kB)
    100% |################################| 61kB 1.1MB/s
Requirement already satisfied: urllib3<2.0,>=1.8 in ./anaconda/lib/python3.6/site-packages (from elasticsearch==2.4.0)
Installing collected packages: elasticsearch
  Found existing installation: elasticsearch 5.2.0
    Uninstalling elasticsearch-5.2.0:
      Successfully uninstalled elasticsearch-5.2.0
Successfully installed elasticsearch-2.4.0 
```
## 2. 指定pip镜像源
1. 清华: https://pypi.tuna.tsinghua.edu.cn/simple
2. 豆瓣: http://pypi.douban.com/simple/ https://pypi.doubanio.com/simple/
3. 阿里: http://mirrors.aliyun.com/pypi/simple/

> 测试表现：douban的速度最快

在 pip 命令中使用镜像源很简单，在执行 install 命令时，使用 `-i` 参数加上源地址就可以了，例如:
```
pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
```
在最新的 pip 版本(>=7)中，使用镜像源时，会提示源地址不受信任或不安全，需要像上面那样添加`--trusted-host`


但是如果我们每次安装一个包都要学那么长不觉得麻烦吗？那我们只要修改默认的镜像源，就可以一劳永逸了。像这样：
```bash
zhangmimideMacBook-Pro:~ zhangmimi$ mkdir .pip   
zhangmimideMacBook-Pro:~ zhangmimi$ vim .pip/pip.conf
```
文件里面写上：
```bash
[global]
 index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

大功告成！
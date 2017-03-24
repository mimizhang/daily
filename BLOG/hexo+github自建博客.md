---
title: hexo+github自建博客
date: 2017-03-15 15:29:10
categories:
- Other
tags: 
- hexo 
- github 
- 博客 
- mac
---

系统：MacOS

## 1. 安装

这是[Hexo](https://hexo.io/docs/)的官方文档。那么安装Hexo之前你必须安装这两样东西：

- [Node.js](http://nodejs.org/)
- [Git](http://git-scm.com/)

在MacOS上你可以使用`brew`命令，非常方便的安装这两个小家伙，像这样：

``` bash
$ brew install node
$ brew install git
```

如果你还没有安装`brew`，那么请点击这里[Homebrew](https://brew.sh/index_zh-cn.html)，安装非常简单。

Git和Node.js安装完后，你就可以安装Hexo了，在终端输入下面的命令即可：

``` bash
$ npm install -g hexo-cli
```

接下来选择你要安装的地方，比如我在`/Users/zhangmimi`路径下，安装在`mimi_blog`文件夹下，则输入一下命令：

``` bash
$ hexo init mimi_blog
$ cd mimi_blog
$ npm install
```

这样Hexo就算安装成功了。

## 2. github新建仓库`repository`

新建仓库就不用多说了吧，需要注意的是**Repository name**要写成下图中的格式，即：`your_user_name.github.io`，比如我的用户名是`mimizhang`，那么仓库名就是`mimizhang.github.io`。

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-03-15%20%E4%B8%8A%E5%8D%8811.31.34.png)

## 3. 本地博客关联到github

在刚才生成的**mimi_blog**文件夹中有个**_config.yml**文件，打开，拉到最下面，按照下图填写，`repository`是你的仓库地址，我的仓库地址是https://github.com/mimizhang/mimizhang.github.io.git。

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-03-15%20%E4%B8%8A%E5%8D%8811.42.10.png)

## 4. 部署

以上的准备工作做好之后，下面就是见证奇迹的时刻。

回到mimi_blog文件夹下，输入下面的命令：

``` bash
$ hexo generate
$ hexo deploy
```

这样就算部署成功了。你可以再输入：

``` bash
$ hexo server
```

打开http://localhost:4000/, 这样就可以在本地看到你的博客。

因为你已经部署在github上了，所以github上也可以看到你的博客，比如我的地址是https://mimizhang.github.io/, 打开你的github博客地址，就知道有多神奇了！

## 5. FAQ

### 5.1 在执行 hexo deploy 后,出现 error deployer not found:github 的错误

可能是因为还未安装 [hexo-deployer-git](https://github.com/hexojs/hexo-deployer-git)。在mimi_blog文件夹下，输入下面的命令试试：

``` bash
$ npm install hexo-deployer-git --save
```

### 5.2 `hexo server`后，http://localhost:4000 无法打开

可能是因为 [hexo-server](https://github.com/hexojs/hexo-server)还未安装

```bash
$ npm install hexo-server --save
```
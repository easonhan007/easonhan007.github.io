---
layout: post
title: "还没被玩坏的robobrowser(2)——安装及快速开始"
description: "安装和快速开始robobrowser"
category: robobrowser
tags: [robobrowser]
---
{% include JB/setup %}

### 安装robobrowser 

**注意:这里假设你知道如何使用pip安装python的库的知识，如果你不了解这一块的话，点[这里](http://www.easonhan.info/python/2013/12/07/active-python-install-selenium/)获取帮助。

强烈推荐使用pip安装。**

```
pip install robobrowser -i http://pypi.douban.com/simple/

```

这里用上了豆瓣源，原因你懂得。


### 快速开始

新建1个start.py文本文件，然后敲入下面的代码

```python
import re
from robobrowser import RoboBrowser

b = RoboBrowser(history=True)
b.open('http://itest.info/courses/2')

title = b.select('.headline h2')
print title[0].text
  
infos = b.select('h4')
  
for info in infos:
  print info.text
    
```

在命令行里运行```python start.py```，然后看一下结果,如果报错请自行耐心分析原因。

### 查看文档

robobrowser自带一点点文档，聊胜于无，凑合看吧。

在命令行里运行

```
python -m pydoc -p 1234
```
如果运行成功的话，就从浏览器中访问http://localhost:1234/robobrowser.html。主要看一下browser这个类就好了。


### 相关知识

[Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)将让你受益匪浅，强烈建议阅读。


文本版权归乙醇所有，欢迎转载，但请标明出处。

下一节：基于robobrowser的简单的爬虫

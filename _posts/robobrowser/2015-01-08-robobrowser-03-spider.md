---
layout: post
title: "还没被玩坏的robobrowser(3)——简单的spider"
description: "简单的spider"
category: robobrowser
tags: [robobrowser]
---
{% include JB/setup %}

### 背景  

做一个简单的spider用来获取[python selenium实战教程]()的一些基本信息。因为python selenium每年滚动开课，所以做这样一个爬虫随时更新最新的开课信息是很有必要的。

### 预备知识

* python语法，不会python的同学建议通过[这个视频](http://v.163.com/special/Khan/computer.html)学习；
* 安装好robobrowser，没有安装的同学参考[这里]()；

### 任务分解

这个简单的spider任务可以进行进一步的分解：

* 访问[python selenium自动化测试班](http://itest.info/courses/2)页面；
* 获取这个班的名称--**python selenium自动化测试班;**
* 获取这个班的描述--**独一无二的超低价培训-口碑之选;**
* 获取开班的时间--**第五期报名截止2015年1月17日，开课时间1月17日;**
* 获取报名方式--**课程咨询请联系QQ：12079456;**
* 获取selenium进阶群的群号--**技术交流+selenium 进阶群：189116036;**
* 获取授课老师信息--**虫师;**

### 正式开始

```python
import re
from robobrowser import RoboBrowser

# 访问python selenium自动化测试班的页面

url = 'http://itest.info/courses/2'
b = RoboBrowser(history=True)
b.open(url)

# 获取这个班的名称--python selenium自动化测试班
class_name = b.select('.headline h2')
print class_name[0].text

# 获取这个班的描述--独一无二的超低价培训-口碑之选
class_desc = b.select('.tag-box')
print class_desc[0].text

# 获取开班的时间--**第五期报名截止2015年1月17日，开课时间1月17日
class_time = b.select('h4')
print class_time[0].text

# 获取授课老师信息--虫师
teacher = b.select('.thumbnail-style h3')
print teacher[0].text

# 获取报名方式--**课程咨询请联系QQ：12079456
qq = b.find(text=re.compile('QQ'))
print qq

# 获取selenium进阶群的群号--**技术交流+selenium 进阶群：189116036
qq_group = b.find(text=re.compile('\+selenium'))
print qq_group

```

### 简单讲解

* ```b = RoboBrowser(history=True) b.open(url)```用来创建browser和打开url，没什么新意，记住就好了；
* ```b.select()```方法可以接受css选择器，返回页面上所有符合条件的元素的集合，也就是说返回的是list，可以进行迭代；
* ```b.find()```的用法在[这里](http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#find-all)，只返回1个精确的结果；
* 注意，find和select方法返回的均是Beautiful Soup的tag对象或对象集合；

如果你对上面的例子不甚理解那也没什么关系，后面几节会按照场景进行分析讲解。


文本版权归乙醇所有，欢迎转载，但请标明出处。

下一节：robobrowser抓取网页内容

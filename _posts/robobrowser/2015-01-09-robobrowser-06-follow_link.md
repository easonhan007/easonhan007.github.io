---
layout: post
title: "还没被玩坏的robobrowser(6)——follow_link"
description: "点击链接"
category: robobrowser
tags: [robobrowser]
---
{% include JB/setup %}

### 背景  

在做spider的时候，我们经常会有点击链接的需求。

考虑这样的一个简单spider：获取qq.com主页上的**今日话题**中的内容。

一般思路是先去qq.com首页上找到**今日话题**的链接，然后点击这个链接到内容页面，最后抓取里面的内容就好了。

这一节里我们就要实现这个功能。

### 预备知识

robobrowser的```follow_link```方法可以点击链接并自动完成跳转。

### 代码

``` python

#coding: utf-8
import re
from robobrowser import RoboBrowser

url = 'http://www.qq.com/'
b = RoboBrowser(history=True)
  b.open(url)

# 获取今日话题这个link
  today_top = b.find(id='todaytop').a  
  print today_top['href']

  b.follow_link(today_top)

# 这个时候已经跳转到了今日话题的具体页面了

# 打印标题
  title = b.select('.hd h1')[0]
  print '*************************************'
  print title.text
  print '*************************************'

# 打印正文内容
  print b.find(id='articleContent').text

```
### 讨论

注意一下follow_link的用法。一般来说都是用find/select/find_all方法过滤出相应的链接，然后调用```b.follow_link(link)```的方式去点击该链接。

文本版权归乙醇所有，欢迎转载，但请标明出处。

下一节: 提交表单

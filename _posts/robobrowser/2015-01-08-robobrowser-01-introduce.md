---
layout: post
title: "还没被玩坏的robobrowser(1)-简介"
description: "介绍robobrowser"
category: robobrowser
tags: [robobrowser]
---
{% include JB/setup %}

今天偶然发现了一个很有意思的python库——robobrowser。简单的看了一下，觉得这个东东作为轻量的爬虫还是很适合的。另外这个做一些简单的web测试也未尝不可。

好了，那么问题来了。

### 什么是[robobrowser](https://github.com/jmcarp/robobrowser)

官方的给出的答案是：RoboBrowser: Your friendly neighborhood web scraper。原谅我这一生不羁放纵不爱读书，真心不知道怎么用博大精深的汉语来翻译这句话，有知道的同学还请告诉一下。

简单来说robobrowser是一个浏览器，没有界面的浏览器。用纯python实现，运行在内存里。robobrowser可以打开网页，点击链接和按钮并且提交表单。嗯，听上去就弱爆了是吧。功能确实不多，但是如果是做爬虫和简单的web测试的话，这些功能实际上是够用了的。


### robobrowser能做什么呢

* 爬虫
* 简单的web测试


### robobrowser好用吗

简单的试用了一下，用起来很方便。而且由于是纯python写的，安装起来也很简单。总之是居家旅行的常备物什。

### robobrowser好学吗

语法很自然，学起来很容易。另外robobrowser其实是建立在[requests](http://docs.python-requests.org/en/latest/)和[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)之上的，站在巨人的肩膀上，robobrowser自然是容易被人们接受的。 

### requests和BeautifulSoup是做什么用的

* requests可以简单的认为是发http请求用的
* BeautifulSoup可以简单的理解为解析html文档的

本文版权属乙醇所有，欢迎转载但请标明出处。

下一节：安装robobrowser以及快速开始



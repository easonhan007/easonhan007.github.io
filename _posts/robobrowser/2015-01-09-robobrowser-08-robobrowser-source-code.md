---
layout: post
title: "还没被玩坏的robobrowser(8)——robobrowser的实现原理"
description: "点击链接"
category: robobrowser
tags: [robobrowser]
---
{% include JB/setup %}

### 背景  

学习使用工具实际上不难，不过我们应该通过阅读工具源码来提升自己的水平。

多读代码，读好代码。很不错，robobrowser的代码简单易懂，值得学习。

### 预备知识

* [源码地址](https://github.com/jmcarp/robobrowser)
* 一起其实是从[browser.py](https://github.com/jmcarp/robobrowser/blob/master/robobrowser/browser.py)开始的

### 要点

* RoboState类里，页面上内容的抓取和处理实际上委托给了BeautifulSoup。RoboState类的_parsed对象实际上就是BeautifulSoup的实例；

* RoboState类中保存了每个请求的响应内容——response.content； 

* RoboBrowser类里，发送请求的方法实际上委托给了requests类——session;

* RoboBrowser类里比较复杂就是保存每次访问的状态，以及实现back和forward功能。其主要思想是把所有的访问历史都放在内存里，然后通过游标去访问；

* 每次页面发生变化，也就是open和submit_form之后都会调用_update_state方法去更新当前状态；

### 流程梳理

* RoboBrowser()实例化的时候，会new 1个requests的session用于发送http请求,同时初始化游标为－1并且当前的status列表初始化为空;

* RoboBrowser.open(url)方法调用时，session对象会访问具体的url，然后更新游标和status列表。基本思想是往status列表里append 1个新new出来的RoboState对象；

* RoboBrowser.find()方法调用时，使用当前游标处的state对象的_parsed对象的find方法去抓取页面内容，实际上就是BeautifulSoup的find方法；

### 讨论

从robobrowser的代码里我们可以看出来，对于测试框架或者具体的业务来说，发明轮子实际上是不太可取的。用最好的第三方库去做它们最擅长的事情才是王道。robobrowser里请求的发送归requests负责，页面的解析由BeautifulSoup去管理，相得益彰。

另外RoboBrowser类中使用了委托模式，请求的发送委托给requests对象，页面解析委托给BeautifulSoup对象。

### 写在最后

新人往往纠结于读什么代码可以让自己进步。robobrowser的源码很适合新人去读，相信读过之后会很有收获。

本教程旨在抛砖引玉，错误的地方还请多多指正。

全文完。


文本版权归乙醇所有，欢迎转载，但请标明出处。


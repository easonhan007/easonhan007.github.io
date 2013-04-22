---
layout: post
title: "安装ie driver和chrome driver"
description: "安装ie driver和chrome driver"
category: webdriver
tags: [webdriver, ie, chrome]
---
{% include JB/setup %}

很多同学在使用webdriver的时候总是忘了安装ie driver和chrome driver， 因此在这里简单介绍一下这2个driver的安装方式。

IE driver
---------

在新版本的webdriver中，只有安装了ie driver使用ie进行测试工作。

ie driver的下载地址在[这里](https://code.google.com/p/selenium/downloads/list)，记得根据自己机器的操作系统版本来下载相应的driver。

下载好ie driver后，记得解压，然后把解压出来的文件放到系统的PATH里去。

一般来说，你可以把ie driver放在ruby，python或者是jdk的bin目录中。


Chrome driver
------------

chrome driver的下载地址在[这里](https://code.google.com/p/chromedriver/downloads/list)。

安装方式与ie driver相同。

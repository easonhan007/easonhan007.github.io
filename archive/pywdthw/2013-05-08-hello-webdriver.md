---
layout: post
title: "hello webdriver"
description: "hello webdriver"
category: python
tags: [python, webdriver]
---
{% include JB/setup %}
这一节的内容基本上是对上一节环境配置的检验。

查看python版本
--------------

首先你需要进入windows的命令行。一般你可以使用win + r键来调出"运行"对话框，然后输入"cmd"并按"回车"就可以了。
打开命令行后，输入下面的内容

	python --version

你应该可以看到
-------------

	Python 2.7.4

如果你无法看到上面的结果，那么也许是因为下面的原因：

*	是否输入了错误的命令，因为我们输入的是英文单词，对于使用象形文字的我们来说，单词拼写错误是最常见的;
*	是不是python没有正确安装;

如果看到的python版本跟我有所不同，那么别担心，webdriver支持python2x系列，如果你的python版本是3.x的话，那么请使用python2.x,因为暂时webdriver不支持python3。

进入python交互模式
------------------
在python的交互模式下，我们每次可以输入一行语句，然后python会自动将运行结果展示给我们。这就有点像是计算器，我们输入1+1就能得到2。
在命令行中使用下面的命令来进入python交互模式。

	python

你应该能看到
------------
	Python 2.7.4 (default, Apr  6 2013, 19:54:46) [MSC v.1500 32 bit (Intel)] on win32
	Type "help", "copyright", "credits" or "license" for more information.

hello webdriver
---------------

在python的交互模式下，我们可以使用下面的代码来启动ie浏览器

	>>> from selenium import webdriver
	>>> webdriver.Ie()

你应该能看到
------------
#### 在命令行中你应该能看到
	>>> from selenium import webdriver
	>>> webdriver.Ie()
	<selenium.webdriver.ie.webdriver.WebDriver object at 0x01A91730>
	>>>

#### 另外ie浏览器将会启动，在启动页面上会显示下面的内容
	This is the initial start page for the WebDriver server.

别担心，这就是正确启动的表现。

如果你无法看到上面的结果，那么请检查:

*	是否没有安装ie driver;
*	ie的保护模式是否正确;
*	是否是以管理员的身份打开命令行，在本书中为了避免不必要的麻烦，请一直使用管理员权限打开命令行(仅限于windows7);
*	是否存在拼写问题，这是最容易犯的错误;

---
layout: post
title: "hello webdriver"
description: "hello webdriver"
category: ruby
tags: [ruby, webdriver]
---
{% include JB/setup %}
这一节的内容基本上是对上一节环境配置的检验。

查看ruby版本
--------------

首先你需要进入windows的命令行。一般你可以使用win + r键来调出"运行"对话框，然后输入"cmd"并按"回车"就可以了。
打开命令行后，输入下面的内容

	ruby --version

你应该可以看到
-------------

	ruby 1.9.2p180 (2011-02-18) [i386-mingw32]

如果你无法看到上面的结果，那么也许是因为下面的原因：

*	是否输入了错误的命令，因为我们输入的是英文单词，对于使用象形文字的我们来说，单词拼写错误是最常见的;
*	是不是ruby没有正确安装;

如果看到的ruby版本跟我有所不同，那么别担心，我这台机器上的ruby版本已经很旧了，你最好安装ruby187之后的ruby版本，太旧的ruby版本可能对webdriver的支持不会太好。

进入ruby交互模式
------------------
在ruby的交互模式下，我们每次可以输入一行语句，然后ruby会自动将运行结果展示给我们。这就有点像是计算器，我们输入1+1就能得到2。
在命令行中使用下面的命令来进入ruby交互模式。

	irb	

你应该能看到
------------

	irb(main):001:0>

hello webdriver
---------------

在ruby的交互模式下，我们可以使用下面的代码来启动ie浏览器

	irb(main):001:0> require 'selenium-webdriver'
	irb(main):002:0> Selenium::WebDriver.for :ie

你应该能看到
------------
#### 在命令行中你应该能看到

	irb(main):001:0> require 'selenium-webdriver'
	=> true
	irb(main):002:0> Selenium::WebDriver.for :ie
	Started InternetExplorerDriver server (32-bit)
	2.28.0.0
	Listening on port 5555
	=> #<Selenium::WebDriver::Driver:0x..fcbbd48a0 browser=:internet_explorer>

如果你看到的结果有所不同，那也许是因为ie driver的版本不同的缘故，只要ie浏览器能正常打开就证明我们的代码工作正常。

#### 另外ie浏览器将会启动，在启动页面上会显示下面的内容

	This is the initial start page for the WebDriver server.

别担心，这就是正确启动的表现。

如果你无法看到上面的结果，那么请检查:

*	是否没有安装ie driver;
*	ie的保护模式是否正确;
*	是否是以管理员的身份打开命令行，在本书中为了避免不必要的麻烦，请一直使用管理员权限打开命令行(仅限于windows7);
*	是否存在拼写问题，这是最容易犯的错误;

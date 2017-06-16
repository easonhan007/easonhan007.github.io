---
layout: post
title: "关闭浏览器"
description: "关闭浏览器"
category: ruby
tags: [ruby, webdriver]
---
{% include JB/setup %}

上一节的练习中，你知道有个叫做[变量]的东西，可能你对它还不是十分熟悉。这个暂时不用担心，因为在后面的练习中你会不断的接触变量，当你对变量见怪不怪的时候，你就自然而然掌握这个知识点了。目前我们可以简单的将变量理解成是给程序中所用到的数据取个好记的名字，足矣。

关闭浏览器
----------
在前面的练习中，我们学习了如何去打开浏览器。下面的练习会教你如何去关闭浏览器。

新建文件close_browser.rb，键入下面的内容

	require 'selenium-webdriver'

	# open ie 
	driver = Selenium::WebDriver.for :ie
	puts 'browser opened'

	# close ie
	driver.quit
	puts 'browser closed'

在上面的代码中，我们定义了一个变量叫做driver，可以暂且认为webdriver把大部分神奇的功能都交给了这个变量。通过这个driver我们可以操作浏览器，定位测试对象，在后面的练习中你会一直跟这个变量打交道。

你应该可以看到
--------------
ie浏览器被打开，然后又被关闭。

在命令行中出现下面的结果

	>ruby close_browser.rb
	browser opened
	browser closed

由于selenium webdriver版本的缘故，你得到的结果可能上面的并不完全相同，但只要你能正确的打开和关闭浏览器，并且打印出上面的两行文字，那么你的代码就是没问题的。否则的话你需要仔细检查代码，看看到底是哪里有问题。

加分练习
--------
* 了解什么是变量赋值;
* 试着去打开并关闭firefox浏览器；
* 试着去打开并关闭chrome浏览器；

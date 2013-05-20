---
layout: post
title: "注释变量及打印"
description: "注释变量及打印"
category: ruby
tags: [ruby, webdriver]
---
{% include JB/setup %}

注释
----
代码里可以写注释。注释在代码被执行的时候是被忽略掉的。你可以在代码里使用注释来写小说、剧本、段子或者是诗歌，当然这是不推荐的。

一般来说注释的作用是解释代码的作用或者说明代码里的有些难懂的行为，另外在你删除代码的时候，你可以暂时的将需要移除的代码注释起来，以便日后进行恢复或重构。

在ruby中，我们使用#号来注释代码。

新建文件comment.rb
	
	# This is a comment
	# Anything after the # is ignored by ruby
	puts 'hello world' # will print hello world 

	# this line will be ignored, too
	puts 'ok'

使用```ruby comment.ruby```执行这个脚本。

你应该可以看到
--------------

	hello world
	ok

打印
----
在上面的代码里，你应该注意到```puts```这个东东。
你完全可以把puts想像成一台打印机，它会向标准输出设备打印文字。

练习下面的代码的，熟悉一下什么是打印。
新建文件print.rb
	
	puts 'something'
	puts 'I like typing this'
	puts 'I can print another line'
	puts 'this is the last line'

你应该可以看到
--------------
	ruby print.rb
	something
	I like typing this
	I can print another line
	this is the last line

变量
----
我们可以使用变量来给程序中的几乎所有东西取个好记的名字，同时在使用变量了以后，代码会看起来更容易理解。练习下面的代码,引用自[learn ruby the hard way](http://ruby.learncodethehardway.org/book/ex4.html):
新建文件variable.rb

	cars = 100
	space_in_a_car = 4.0
	drivers = 30
	passengers = 90
	cars_not_driven = cars - drivers
	cars_driven = drivers
	carpool_capacity = cars_driven * space_in_a_car
	average_passengers_per_car = passengers / cars_driven

	puts "There are #{cars} cars available."
	puts "There are only #{drivers} drivers available."
	puts "There will be #{cars_not_driven} empty cars today."
	puts "We can transport #{carpool_capacity} people today."
	puts "We have #{passengers} passengers to carpool today."
	puts "We need to put about #{average_passengers_per_car} in each car."
		
你应该可以看到
-------------
	ruby variable.rb
	There are 100 cars available.
	There are only 30 drivers available.
	There will be 70 empty cars today.
	We can transport 120.0 people today.
	We have 90 passengers to carpool today.
	We need to put about 3 in each car.
	
加分练习
--------
* 将这节里的所有代码当成简单的英语短文大声的朗读十遍，大声读出来，你会更有感觉；
* 给这一节的每一行代码添加注释；
* 如果你遇到错误，请尽量想办法独立解决问题；
* 细节很重要，如果你的结果与预期的不太一样，请静下心来逐行逐句检查代码；
* 看一看variable这个单词是什么意思，并尝试记住它；
* 试着去打印出中文，这个会比较难；



	

---
layout: post
title: "小而美的ghost driver"
description: "小而美的ghost driver"
category: phantomjs
tags: [phantomjs]
---
{% include JB/setup %}

2017年6月16日更新: 目前phantomjs已经放弃更新，大家可以选择使用chrome的[Headless](https://developers.google.com/web/updates/2017/04/headless-chrome)模式来替代。

做过selenium自动化项目的同学应该都遇到过这样的问题：测试用例太多，运行速度过慢导致团队成员怨声载道。

于是便有了selenium grid和多线程运行selenium测试用例的方法。这些方法各有利弊这里就不一一列举了。但总的来说，如果浏览器运行的速度足够快，那么多线程并发时的用例执行速度应该是可以满足实际项目需求的。

再想象一下这样的情景：如果你手头的机器是没有gui的(这是可能的，我以前的几台centos的server根本就没有ui)，如何在这样的headless的机器上运行selenium用例呢？

答案是可以用selenium自带的[HtmlUnitDriver](https://code.google.com/p/selenium/wiki/HtmlUnitDriver)。不过可惜的是HtmlUnitDriver对js的支持不是特别完美，所以该方案可行但是不完善，不是特别适合用于真实项目。

好在现在有了[phantomjs](http://phantomjs.org/)和ghostdriver，我们可以用ghostdriver来运行selenium测试用例。所有的用例都是在没有gui的浏览器里运行，运行速度可以得到极大的提升。再加上phantomjs是基于webkit的，所以ghostdriver完全可以模拟chrome和safari的行为。

在我的macbookpro上，chromedriver的表现不是特别令人满意，而我又没有安装firefox和safari driver，所以对于一般的页面(js交互不是特别多的页面)，我都是用ghost driver在调试问题，快速而简便。最主要是没有真实的浏览器弹出来，不会像chromedriver那样经常意外退出造成内存泄漏，也不会像firefox那样运行缓慢。

下面简单介绍一下ghost driver 与selenium合体的过程。

### 背景知识

下面的内容要求你已经成功的安装好python的selenim binding。如果你有pip，直接运行 ```pip install selenium```即可。如果被墙，请使用豆瓣源。

或者成功的安装好ruby的watir-webdriver。如果你有gem，直接运行 ```gem install watir-webdriver```即可。如果被墙，请使用[淘宝源](http://ruby.taobao.org)。

### 安装ghost driver

ghost driver现在已经跟phantomjs合体，所以安装好最新版本的phantomjs就等于安装好了ghostdriver。

在[这里](http://phantomjs.org/download.html)下载对应平台的phantomjs。

* 首先解压下载好的zip文件或tar文件(linux only);

* windows用户将解压过后的得到的phantomjs.exe文件加入系统的PATH中。简单点说如果你使用pyhon，就把phantomjs.exe放到python的安装目录下，ruby用户放到ruby/bin目录下；

* mac和linux用户可以把解压后得到的phantomjs建个软链到/usr/local/bin目录下。```ln -s /where/is/phantomjs /usr/local/bin/phantomjs```；

### 快速开始 

python用户新建itest.py文件然后敲入下面的内容

```python
from selenium import webdriver

dr = webdriver.PhantomJS('phantomjs')
dr.get('http://baidu.info')
print dr.title
print dr.current_url
dr.quit()
```

watir-webdriver用户新建文件itest.rb然后敲入下面的内容

```ruby
require 'watir-webdriver'

b = Watir::Browser.new :phantomjs
b.goto 'www.baidu.com'

puts b.title
puts b.url

b.close
```

### 讨论

* ghostdriver尽管对js的支持是不错的，但是如果你的页面上js交互过多的话，ghostdriver是会缴械投降的；

* 用ghostdriver+selenium的语法可以做一些不错的爬虫；

* 用java用户请使用maven下载java的ghostdriver binding；

* 当页面上有flash播放器时，phantom可能会萌萌哒的卡在那里一动不动；

* ghostdriver基于[phantomjs](http://phantomjs.org/)，phantomjs可以做爬虫，简单的性能测试，ui自动化测试和其他一些工作； 

* 由于没有ui，当测试发生错误的时候调试的工作量就会变大；

### 看不到运行的过程，心中惶恐不安怎么办

答案是截图拯救测试人员，截图拯救世界。

运行到关键的节点或步骤时截个图，即方便了调试又使你的测试拥有足够多的输出,一举两得何乐不为？

python代码

```python
from selenium import webdriver

dr = webdriver.PhantomJS('phantomjs')
dr.get('http://baidu.info')
print dr.title
print dr.current_url

dr.save_screenshot('./baidu.png')

dr.quit()

```

ruby代码

```ruby
require 'watir-webdriver'

b = Watir::Browser.new :phantomjs
b.goto 'www.baidu.com'

puts b.title
puts b.url
b.driver.save_screenshot('./baidu.jpg')

b.close
```

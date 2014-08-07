---
layout: post
title: "如何查看python selenium的api"
description: "如何在本地查看python selenium的api"
category: python
tags: [python, selenium]
---
{% include JB/setup %}

经常发现很多同学装好了python+selenium webdriver开发环境后不知道怎么去查看api文档，在这里乙醇简单介绍一下具体方法，其实非常简单。

首先打开命令行，在doc窗口输入：
    
    python -m pydoc -p 4567

简单解释一下：

* python -m pydoc表示打开pydoc模块，pydoc是查看python文档的首选工具；
* -p 4567表示在4567端口上启动server;

然后在浏览器中访问http://localhost:4567/，此时应该可以看到python中所有的Modules

按ctrl+f，输入selenium,定位到selenium文档的链接，然后点击进入到http://localhost:4567/selenium.html这个页面

这就是selenium文档所在的位置了，接下来便可以根据自己的需要进行查看了。举个例子，如果你想查看Webdriver类的基本方法，可以访问这个页面http://localhost:4567/selenium.webdriver.remote.webdriver.html

### 本文版权属于乙醇所有，欢迎转载，但请注明出处


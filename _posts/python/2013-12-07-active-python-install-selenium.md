---
layout: post
title: "最简便安装python+selenium-webdriver环境方法"
description: "使用active python安装selenium webdriver"
category: python
tags: [python]
---
{% include JB/setup %}

很多同学在windows搞不定python + selenium-webdriver的安装环境，在这里乙醇给大家提供一种极速安装的方式。

首先感谢[active-python](http://www.activestate.com/activepython/)

只需要2步就可以安装完毕。

### 安装[active-python](http://www.activestate.com/activepython/)

从[这里](http://www.activestate.com/activepython/downloads)下载active python2.7.5的windows安装版本，注意，如果是64位系统，则需要选择(64-bit, x64)版本下载。

双击打开下载的文件，直接下一步安装既可，很简单,什么都不需要更改。


### 安装selenium webdriver

打开命令行cmd，输入下面的命令

	pip install selenium

回车后，你会看到下面的提示
	
	Downloading/unpacking selenium
		Downloading selenium-2.38.1.tar.gz (2.5MB): 2.5MB downloaded
		Running setup.py egg_info for package selenium

	Installing collected packages: selenium
		Running setup.py install for selenium

	Successfully installed selenium
	Cleaning up...

现在大功告成，去喝点水庆祝一下吧!	

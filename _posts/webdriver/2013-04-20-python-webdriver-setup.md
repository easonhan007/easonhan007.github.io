---
layout: post
title: "配置python webdriver开发环境"
description: "在windows上配置python webdriver的开发环境"
category: webdriver
tags: [python, webdriver]
---
{% include JB/setup %}

在windows上配置python开发环境其实非常简单。在有网络连接的情况下，你可以通过下面的步骤来安装selenium2的python binding。

* 安装python。目前selenium的python binding只支持python2.x，所以直接去官网上下载一个2.x的稳定版本就好；

* 安装[setuptools](https://pypi.python.org/pypi/setuptools#downloads)。一定要注意安装对应python版本的setuptools;

* 安装pipy。下载pipy的压缩包，解压后运行命令```python setup.py install```；

* 进入python安装目录下的Scripts目录，在命令行中运行```pip.exe install selenium -i http://b.pypi.python.org/simple```，注意-i选项是指定了index，也就是pipy的镜像源，至于为什么要这么做，你懂的。



---
layout: post
title: "如何在本机阅读gitbook"
description: "如何在本机阅读gitbook"
category: python
tags: [python, gitbook]
---
{% include JB/setup %}

如何在本机阅读gitbook
--------------------------

本文假定你在本机安装了python，2或3都可以。

一般情况下，你都会下载到一个名为```_book.7z```文件，用7zip解压这个文件，然后

**在命令行中cd到_book文件夹**

继续在命令行中敲下面的命令行

* python2: ```python -m SimpleHTTPServer```
* python3: ```python -m http.server```

等待命令行出现下面的提示后

```
Serving HTTP on 0.0.0.0 port 8000 ...
```

在浏览器中打开[http://localhost:8000](http://localhost:8000)就可以了。

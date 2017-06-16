---
layout: post
title: "启动浏览器"
description: "如何去启动浏览器"
category: python
tags: [python, webdriver]
---
{% include JB/setup %}

上一次的练习里我们已经能够使用一些简单的代码在python的交互模式中打开ie浏览器了。在这一次的练习中，我们会试着写一点代码，然后把代码保存成python的可执行文件，通过运行文件的方式来运行代码。听起来有点绕，但实际上还是挺简单的。

新建python文件
-------------
新建一个文本文件，一般来说你可以通过在文件夹下点鼠标右键，然后在弹出菜单中的__新建(W)__菜单中选择__文本文档__。将这个文本文件重命名为start\_browser.py。注意，你需要在文件夹选项中取消掉__隐藏已知文件扩展名__的前面的勾勾，否则你无法修改文本文件的扩展名。

打开IE
--------
用notepad++打开该文件，键入下面的代码并保存：
<script src="https://gist.github.com/easonhan007/5552834.js"></script>

从命令行中cd到该文件所在目录，假设你的文件存在在e盘code目录下，你可以这么做：

	C:\Windows\system32>e:

	E:\>cd code

	E:\code>

通过下面的命令来执行你刚才编写的代码：

	python start_browser.py

你应该可以看到
--------------

Ie浏览器被正确打开并显示```This is the initial start page for the WebDriver server.```

讨论
----
可以看出后缀名为.py的文件就是我们写python代码的地方。我们可以使用```python file_name.py```命令来执行任意的文件名为file_name的python代码文件。

加分练习
-------

* 练习使用```webdriver.Chrome()```来打开Chrome浏览器；
* 练习使用```webdriver.Firefox()```来打开Firefox浏览器；


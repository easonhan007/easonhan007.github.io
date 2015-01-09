---
layout: post
title: "还没被玩坏的robobrowser(7)——表单操作"
description: "点击链接"
category: robobrowser
tags: [robobrowser]
---
{% include JB/setup %}

### 背景  

有一些站点是需要登录之后才能抓取内容的，另外做web测试的时候登录是家常便饭。

这一节里我们就以登陆testerhome为例，讲解一下robobrowser中form的操作。

### 预备知识

* ```get_form```方法用来抓取form;
* ```submit_form```方法用来提交表单;
* ```form[name].value=```方法用来给文本框赋值，也就是说往文本框里写内容;

### 代码

```python
#coding: utf-8
import re
from robobrowser import RoboBrowser

url = 'http://testerhome.com/account/sign_in/'
b = RoboBrowser(history=True)
b.open(url)

# 获取登陆表单
login_form = b.get_form(action='/account/sign_in')
print login_form

# 输入用户名和密码
login_form['user[login]'].value = 'your account'
login_form['user[password]'].value = 'your password'

# 提交表单
b.submit_form(login_form)

# 打印登陆成功的信息
print b.select('.alert.alert-success')[0].text

```


文本版权归乙醇所有，欢迎转载，但请标明出处。

下一节: 提交表单

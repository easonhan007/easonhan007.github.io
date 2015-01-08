#coding: utf-8
import re
from robobrowser import RoboBrowser

url = 'http://itest.info/courses/2'
b = RoboBrowser(history=True)
b.open(url)

# 通过tag name抓取

#<title>重定向科技</title>
title = b.find('title')  
print title.text

# 通过属性(attribute)抓取

# <img id="logo-header" src="/assets/logo-0648b8fb283a9802457da74f0c157b12.png" />
img = b.find(id='logo-header')
print img['src']

# <a href="/courses/4">android测试工具自制班</a>
print b.find(href='/courses/4').text

# <li class="active">python selenium自动化测试班</li>
print b.find(class_='active', text=re.compile('python')).text




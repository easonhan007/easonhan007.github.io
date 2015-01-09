#coding: utf-8
import re
from robobrowser import RoboBrowser

url = 'http://www.qq.com/'
b = RoboBrowser(history=True)
b.open(url)

# 获取今日话题这个link
today_top = b.find(id='todaytop').a  
print today_top['href']

b.follow_link(today_top)

# 这个时候已经跳转到了今日话题的具体页面了

# 打印标题
title = b.select('.hd h1')[0]
print '*************************************'
print title.text
print '*************************************'

# 打印正文内容
print b.find(id='articleContent').text





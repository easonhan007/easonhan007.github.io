#coding: utf-8
import re
from robobrowser import RoboBrowser

url = 'http://itest.info/courses/2'
b = RoboBrowser(history=True)
b.open(url)

#页面上所有的a
all_links = b.select('a')  
for link in all_links:
  print link.text

# 页面上所有class是container的div
divs = b.select('.container')
print len(divs)





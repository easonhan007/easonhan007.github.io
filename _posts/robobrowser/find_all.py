#coding: utf-8
import re
from robobrowser import RoboBrowser

url = 'http://itest.info/courses/2'
b = RoboBrowser(history=True)
b.open(url)

#页面上所有的a
all_links = b.find_all('a')  
for link in all_links:
  print link.text

# 页面上所有class是container的div
divs = b.find_all(class_='container')
print divs

# limit 参数控制返回的元素个数

# 页面上前2个p
first_two_p = b.find_all('p', limit=2)
print first_two_p

# 如果第1个参数是列表则返回相匹配的集合

# 页面上所有的meta和title
print b.find_all(['meta', 'img'])




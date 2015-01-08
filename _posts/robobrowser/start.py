import re
from robobrowser import RoboBrowser

b = RoboBrowser(history=True)
b.open('http://itest.info/courses/2')

'''
form = b.get_form(action='/s')
print form

form['wd'].value = 'selenium'

b.submit_form(form)

'''
title = b.select('.headline h2')
print title[0].text

infos = b.select('h4')

for info in infos:
  print info.text

body = b.select('body')
print body[0].text

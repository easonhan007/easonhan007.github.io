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





from selenium import webdriver

dr = webdriver.PhantomJS('phantomjs')
dr.get('http://www.baidu.com')
print dr.title
print dr.current_url
dr.save_screenshot('./baidu.png')
dr.close()

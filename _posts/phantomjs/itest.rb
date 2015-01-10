require 'watir-webdriver'

b = Watir::Browser.new :phantomjs

b.goto 'www.baidu.com'
puts b.title
puts b.url

b.driver.save_screenshot('./baidu.jpg')

b.close

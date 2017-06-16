require 'watir-webdriver'
ENV.delete('HTTP_PROXY')
b = Watir::Browser.new :chrome
file_path = 'file:///' + File.expand_path(File.join('.', 'full_form.html'))

b.goto file_path

# 设置单行文本框里的内容
b.text_field(:name, 'user').set 'coco'
# 打印出刚设置的内容
puts b.text_field(:name, 'user').value

# 很好用的flash方法，直接高亮要定位的元素
b.text_field(:name, 'user').flash
# 清除单行文本框中的内容
b.text_field(:name, 'user').clear

# 往多行文本框中写入内容
b.text_field(:name, 'content').set 'watir webdriver is better than selenium'

# 选择checkbox
b.checkbox(:name, 'check_me').set true
# 清除选择
b.checkbox(:name, 'check_me').set false

# 选择radio
b.radio(:name, 'man').set 
# 返回radio是否被选择
puts b.radio(:name, 'man').set? 

# 选择value为woman的选项
b.select(:name, 'sex').select 'woman'
# 返回选中的选项
puts b.select(:name, 'sex').selected_options

# 点击按钮
b.button(:name, 'btn').click

# 关闭浏览器
b.close


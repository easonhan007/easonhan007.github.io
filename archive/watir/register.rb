require 'watir-webdriver'

b = Watir::Browser.new :chrome
file_path = 'file:///' + File.expand_path(File.join('.', 'form.html'))

b.goto file_path

b.text_field(:name, 'user').set 'coco'
b.text_field(:name, 'password').set 'private'
b.text_field(:name, 'confirm_password').set 'private'
b.button(:value, 'Register').click


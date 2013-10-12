---
layout: post
title: "练习5：更多的变量和打印"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}


我们现在要键入更多的变量并且将它们打印出来，这次我们将使用一个叫「格式化字符串(format string)」的东西，每一次你使用 " 将一些文字包起来，你就建立一个字符串。字符串是程序将信息展示给人的方式。你可以打印他们，可以将它们写入文档，还可以将它们发给网站服务器等等。
字符串是很好用的东西，所以在这个练习中你将学会如何创造包含变量内容的字符串，使用专门的格式和语法将变量的内容放到字符串里，相当于来告诉 Ruby: “Hey 这是一个格式化字符串，把这些变量放到那几个位置上”

如常，即使你还不懂这些内容，只要一字不差的键入就可以了。

```sh
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

puts "Let's talk about %s." % my_name
puts "He's %d inches tall." % my_height
puts "He's %d pounds heavy." % my_weight
puts "Actually that's not too heavy."
puts "He's got %s eyes and %s hair." % [my_eyes, my_hair]
puts "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
puts "If I add %d, %d, and %d I get %d." % [
    my_age, my_height, my_weight, my_age + my_height + my_weight]
```

你应该看到的结果
----------------

```sh
$ ruby ex5.rb
Let's talk about Zed A. Shaw.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 35, 74, and 180 I get 289.
$
```

加分练习
--------

1. 修改所有的变量名称，把它们前面的 my_ 去掉，确认将每一个地方的都改掉，不只是你使用 = 赋值过的地方。 
2. 试着使用更多的格式化字符串。 
3. 在网路上搜寻所有的 Ruby 格式化字符串。 
4. 试着使用变量将英寸和磅转换成公分和公斤。不要直接键入答案，使用 Ruby 的数学计算来完成。 


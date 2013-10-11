---
layout: post
title: "习题2 注释和井号"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

程序里的注释是很重要的。它们可以用自然语言告诉你某段程序代码的功能是什么。在你想要临时移除一段程序代码时，你还可以用注释的方式将这段程序代码临时禁用。接下来的练习将让你学会注释：

```sh
# A comment, this is so you can read your program later.
# Anything after the # is ignored by Ruby.

puts "I could have code like this." # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

puts "This will run."
```

你应该看到的结果

```sh
$ ruby ex2.rb 
I could have code like this.
This will run.
$
```

加分习题

1. 弄清楚``` # ```符号的作用。而且记住它的名称。（中文为井号，英文为 octothorpe 或者 pound character)。 
2. 打开你的``` ex2.rb ```文件，从后往前逐行检查。从最后一行开始，倒着逐个单词单词检查回去。 
3. 有发现更多错误嘛？有的话就改正过来。 
4. 阅读你写的习题，把每个字符（charcter）都读出来。有没有发现更多的错误呢？有的话也一样改正过来。 

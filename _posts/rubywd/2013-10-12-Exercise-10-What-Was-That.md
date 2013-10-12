---
layout: post
title: "练习10：那是什么"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}


在练习 9 中我丢给你了一些新东西。我让你看到两种让字符串扩展到多行的方法。第一种方法是在月份中间用``` \n ```(back-slash n) 隔开。这两个字符串的作用是在该位置上放入一个「新行(new line)」字符。

使用反斜线``` \ ```(back-slash) 可以将难打印出的字符放到字符串里。针对不同的符号有很多这样的所谓「跳脱序列(escape sequences)」，但有一个特殊的跳脱序列，就是``` \ ```双反斜线( double back-slash)。这两个字符组合会打印出一个反斜线来。接下来我们做几个练习，然后你就知道这些跳脱序列的意义了。

另外一种重要的跳脱序列是用来将单引号``` ' ```和双引号``` " ```跳脱。想像你有一个用双引号括起来的字符串，你想要在字符串里的内容里再加入一组双引号进去，比如你想说``` " I "understand" joke." ```，Ruby 就认为``` "understand" ```前后的两个引号是字符串的边界，从而把字符串弄错。你需要一种方法告诉 Ruby 字符串里面的双引号不是真正的双引号。

要解决这个问题，你需要将双引号和单引号跳脱，让 Ruby 将引号也包含到字符串里面去。这里有一个例子：

```sh
1. "I am 6'2\" tall."  # escape double-quote inside string
2. 'I am 6\'2" tall.'  # escape single-quote inside string
```

第二种方法是使用文件语法(document syntax)，也就是``` <<NAME ```，你可以在键入``` NAME ```前放入\ 任意多行的文字。接下来你可以看到如何使用。

```sh
1. tabby_cat = "\tI'm tabbed in."
2. persian_cat = "I'm split\non a line."
3. backslash_cat = "I'm \\ a \\ cat."
4.
5. fat_cat = <<MY_HEREDOC
6. I'll do a list:
7. \t* Cat food
8. \t* Fishies
9. \t* Catnip\n\t* Grass
10. MY_HEREDOC
11.
12. puts tabby_cat
13. puts persian_cat
14. puts backslash_cat
15. puts fat_cat
```

你应该看到的结果

注意你打出来的 tab 字符，这节练习中的文字间隔符号对于答案的正确性是很重要的。

```sh
$ ruby ex10.rb
    I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.
I'll do a list:
    * Cat food
    * Fishies
    * Catnip
    * Grass

$
```

加分练习
--------

1. 上网搜寻一下还有哪些可用的跳脱字符。 
2. 结合跳脱序列和格式化字符串，创造一种复杂的格式。 


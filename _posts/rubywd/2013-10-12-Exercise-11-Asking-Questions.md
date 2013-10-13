---
layout: post
title: "练习11: 提问"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

我已经出过很多有关于打印的练习，让你习惯写出简单的东西，但简单的东西都有点无聊，我们现在要做的的事是把数据(data)读到你的程序里面去。这对你可能会有点难度，你可能一下子搞不明白，不过相信我，无论如何先把练习做了再说。只要做几道练习你就明白了。

一般软体做的事情主要就是下面几件：

1. 接受人的输入。 
2. 改变输入值。 
3. 打印改变了的值。 

到目前为止你只做了打印，但还不会接受或修改人的输入。你还不知道「输入(input)」是什么意思。闲话少说，我们还是开始做点练习看你能不能明白，下一道练习里面我们将会有更详细的解释。

```sh
print "How old are you? "
age = gets.chomp()
print "How tall are you? "
height = gets.chomp()
print "How much do you weigh? "
weight = gets.chomp()

puts "So, you're #{age} old, #{height} tall and #{weight} heavy."
```

> Note: 注意到我们是使用``` print ```而非``` puts ```吗？``` print ```不会自动产生新行。这样你的答案就可以跟问题在同一行了。换句话说，puts 会自动产生新行。

你应该看到的结果

```sh
$ ruby ex11.rb How old are you? 35 How tall are you? 6’2” How much do you weigh? 180lbs So, you’re ‘35’ old, ‘6'2”’ tall and ‘180lbs’ heavy. $
```

加分练习
--------

1. 上网搜寻一下 Ruby 的``` gets ```和``` chomp ```的功能是什么？ 
2. 你能找到``` gets.chomp ```别的用法吗？测试一下你上网找到的例子。 
3. 用类似的格式再写一段，把问题改成你自己的问题。 


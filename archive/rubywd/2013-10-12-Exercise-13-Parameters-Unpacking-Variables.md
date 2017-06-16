---
layout: post
title: "练习13: 参数、解包、参数"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

在这节练习中，我们将涵盖另外一种将变数传递给脚本的方法（所谓脚本，就是你写的``` .rb ```文件）。你已经知道，如果要执行``` ex13.rb ```，只要在命令列中执行``` ruby ex13.rb ```就可以了。这句命令中的``` ex13.rb ```部分就是所谓的「参数(argument)」，我们现在要做的就是写一个可以接受参数的脚本。

将下面的程序写下来，后来我将详细解释

```sh
first, second, third = ARGV

puts "The script is called: #{$0}"
puts "Your first variable is: #{first}"
puts "Your second variable is: #{second}"
puts "Your third variable is: #{third}"

```
``` ARGV ```就是「参数变数(argument variable)」，是一个非常标准的程序术语。在其他的程序语言你也可以看到它全大写的原因是因为它是一个「常数(constant)」，意思是当它 被赋值之后你就不应该去改变它了。这个变数会接收当你运行 Ruby 脚本时所传入的参数。通过后面的练习你将对它有更多的了解。 你将对它有更多的了解。

第 1 行将``` ARGV ```「解包(unpack)」，与其将所有参数放到同一个变数下面，我们将每个参数赋予一个变数名称``` first ```、``` second ```以及``` third ```。脚本本身的名称被存在一个特殊变数 $0 里，这是我们不需要解包的部份。也许看来有些诡异，但「解包」可能是最好的描述方式了。它的涵义很简单：「将``` ARGV ```中的东西解包，然后将所有的参数依次赋予左边的变数名称」。

接下来就是正常的印出了。

你应该看到的结果
----------------

用下面的方法执行你的程序：

```sh
ruby ex13.rb first 2nd 3rd
```

如果你每次使用不同的参数执行，你将看到下面的结果：

```sh
$ ruby ex13.rb first 2nd 3rd
The script is called: ex13.rb
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd

$ ruby ex13.rb cheese apples bread
The script is called: ex13.rb
Your first variable is: cheese
Your second variable is: apples
Your third variable is: bread

$ ruby ex13.rb Zed A. Shaw
The script is called: ex13.rb
Your first variable is: Zed
Your second variable is: A.
Your third variable is: Shaw
```

你其实可以将「first」、「2nd」、「3rd」替换成任意三样东西。你可以将它们换成任意你想要的东西。

```sh
ruby ex13.rb stuff I like
ruby ex13.rb anything 6 7
```
加分练习
--------

1. 传三个以下的参数给你的脚本。当有缺少参数时哪些数值会被使用到？ 
2. 再写两个脚本，其中一个接收更少的参数，另一个接收更多的参数。在参数解包时给它们取一些有意义的变数名称。 
3. 结合``` gets.chomp ```和``` ARGV ```一起使用，让你的脚本从用户手上得到更多输入。 


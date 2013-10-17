---
layout: post
title: "练习38:  阵列的操作" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

你已经学过了阵列。在你学习“` while `循环的时候，你对阵列进行过「pushed」动作，而且将阵列的内容打印了出来。另外你应该还在加分练习里研究过 Ruby 文件，看了阵列支持的其他操作。这已经是一段时间以前了，所以如果你不记得了的话，就回到本书的前面再复习一遍吧。

找到了吗？还记得吗？很好。那时候你对一个阵列执行了` push `函式。不过，你也许还没有真正明白发生的事情，所以我们再来看看我们可以对阵列进行什么样的操作。

当你看到像` mystuff.append('hello') `这样的程序时，你事实上已经在 Ruby 内部激发了一个连锁反应。以下是它的运作原理：

1. Ruby 看到你用到了` mystuff `，于是就去找到这个变量。也许它需要倒着检查看你有没有在哪里用` = `建立过这个变量，或者检查它是不是一个函式参数，或者看它是不是一个全局变量。不管哪种方式，它得先找到` mystuff `这个变量才行。 
2. 一旦它找到了` mystuff `，就轮到处理句点` .  `(period)这个操作符号，而且开始查看` mystuff `内部的一些变量了。由于` mystuff `是一个阵列，Ruby 知道` mystuff `支持一些函式。 
3. 接下来轮到了处理` push `。Ruby会将 「push」和` mystuff `支持的所有函式的名称一一对比，如果确实其中有一个叫` push `的函式，那么Ruby就会去使用这个函式。 
4. 接下来Ruby看到了括号(parenthesis)并且意识到, 「噢，原来这应该是一个函式」，到了这里，它就正常会呼叫这个函式了，不过这里的函式还要多一个参数才行。 

一下子要消化这么多可能有点难度，不过我们将做几个练习，让你头脑中有一个深刻的打印象。下面的练习将字符串和列表混在一起，看看你能不能在里边找出点乐子来：

```sh
ten_things = "Apples Oranges Crows Telephone Light Sugar"

puts "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = %w(Day Night Song Frisbee Corn Banana Girl Boy)

while stuff.length != 10
  next_one = more_stuff.pop()
  puts "Adding: #{next_one}"
  stuff.push(next_one)
  puts "There's #{stuff.length} items now."
end

puts "There we go: #{stuff}"

puts "Let's do some things with stuff."

puts stuff[1]
puts stuff[-1] # whoa! fancy
puts stuff.pop()
puts stuff.join(' ') # what? cool!
puts stuff.values_at(3,5).join('#') # super stellar!
```

你应该看到的结果
----------------

```sh
$ ruby ex39.rb 
Wait there's not 10 things in that list, let's fix that.
Adding: Boy
There's 7 items now.
Adding: Girl
There's 8 items now.
Adding: Banana
There's 9 items now.
Adding: Corn
There's 10 items now.
There we go: ["Apples", "Oranges", "Crows", "Telephone", "Light", "Sugar", "Boy", "Girl", "Banana", "Corn"]
Let's do some things with stuff.
Oranges
Corn
Corn
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
Telephone#Sugar
$
```

加分练习
---------

1. 上网阅读一些关于「物件导向程序(Object Oriented Programming)」的资料。晕了吧？嗯，我以前也是。别担心。你将从这本书学到足够用的关于物件导向程序的基础知识，而以后你还可以慢慢学到更多。 
2. something.methods 和 something的 class 有什么关系？ 
3. 如果你不知道我讲的是些什么东西，别担心。程序设计师为了显得自己聪明，于是就发明了Opject Oriented Programming，简称为OOP，然后他们就开始滥用这个东西了。如果你觉得这东西太难，你可以开始学一下「函式式程序(functional programming)」。 


---
layout: post
title: "练习29: 如果（if）"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

这里是你接下要写的作业，这段介绍了` if-statement` （if 语句）。把这段输入进去，让它能够正确执行。然后我们看看你是否有收获。

```sh
people = 20
cats = 30
dogs = 15

if people < cats
  puts "Too many cats! The world is doomed!"
end

if people > cats
  puts "Not many cats! The world is saved!"
end

if people < dogs
  puts "The world is drooled on!"
end

if people > dogs
  puts "The world is dry!"
end

dogs += 5

if people >= dogs
  puts "People are greater than or equal to dogs."
end

if people <= dogs
  puts "People are less than or equal to dogs."
end

if people == dogs
  puts "People are dogs."
end
```

你应该看到的结果
----------------

```sh
$ ruby ex29.rb 
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
$
```

加分练习
--------

猜猜「if 语句」是什么，它有什么用处。在做下一道练习前，试着用自己的话回答下面的问题:

1. 你认为 if 对于它下一行的程序码做了什么？ 
2. 把练习 29 中的其它布尔表示式放到「if 语句」中会不会也可以运行呢？试一下。 
3. 如果把变量 people、cats 和 dogs 的初始值改掉，会发生什么事情？ 


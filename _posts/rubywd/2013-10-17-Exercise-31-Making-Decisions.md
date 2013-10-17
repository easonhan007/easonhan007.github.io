---
layout: post
title: "练习31: 做出决定" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

这本书的上半部分，你打印出了一些东西，并且调用了函式，不过一切都是直线式进行的。你的脚本从最上面一行开始，一路运行到结束，但其中并没有决定程序流向的分支点。现在你已经学会了 if、else和 elsif，你就可以开始建立包含条件判断的脚本了。
上一个脚本中你写了一系列的简单提问测试。这节的脚本中，你将需要向使用者提问，依据使用者的答案来做出决定。把脚本写下来，多多捣鼓一阵子，看看他的运作原理是什么。

```sh
def prompt
  print "> "
end

puts "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

prompt; door = gets.chomp

if door == "1"
  puts "There's a giant bear here eating a cheese cake.  What do you do?"
  puts "1. Take the cake."
  puts "2. Scream at the bear."

  prompt; bear = gets.chomp

  if bear == "1"
    puts "The bear eats your face off.  Good job!"
  elsif bear == "2"
    puts "The bear eats your legs off.  Good job!"
  else
    puts "Well, doing #{bear} is probably better.  Bear runs away."
  end

elsif door == "2"
  puts "You stare into the endless abyss at Cthuhlu's retina."
  puts "1. Blueberries."
  puts "2. Yellow jacket clothespins."
  puts "3. Understanding revolvers yelling melodies."

  prompt; insanity = gets.chomp

  if insanity == "1" or insanity == "2"
    puts "Your body survives powered by a mind of jello.  Good job!"
  else
    puts "The insanity rots your eyes into a pool of muck.  Good job!"
  end

else
  puts "You stumble around and fall on a knife and die.  Good job!"
end
```

这里的重点是你可以在` if `语句中内部再放一个` if `语句。这是一个很强大的功能，可以用来建立「巢状(nested)」的决定（decision)。

你需要理解` if `语句包含` if `语句的概念。做一下加分练习，这样你会确信自己真正理解了它们。

你应该看到的结果
----------------

我在玩一个小冒险游戏。我的水准不怎么样。

```sh
$ ruby ex31.rb
You enter a dark room with two doors.  Do you go through door #1 or door #2?
> 1
There's a giant bear here eating a cheese cake.  What do you do?
1. Take the cake.
2. Scream at the bear.
> 2
The bear eats your legs off.  Good job!

$ ruby ex31.rb 
You enter a dark room with two doors.  Do you go through door #1 or door #2?
> 1
There's a giant bear here eating a cheese cake.  What do you do?
1. Take the cake.
2. Scream at the bear.
> 1
The bear eats your face off.  Good job!

$ ruby ex31.rb 
You enter a dark room with two doors.  Do you go through door #1 or door #2?
> 2
You stare into the endless abyss at Cthuhlu's retina.
1. Blueberries.
2. Yellow jacket clothespins.
3. Understanding revolvers yelling melodies.
> 1
Your body survives powered by a mind of jello.  Good job!

$ ruby ex31.rb 
You enter a dark room with two doors.  Do you go through door #1 or door #2?
> 2
You stare into the endless abyss at Cthuhlu's retina.
1. Blueberries.
2. Yellow jacket clothespins.
3. Understanding revolvers yelling melodies.
> 3
The insanity rots your eyes into a pool of muck.  Good job!

$ ruby ex31.rb
You enter a dark room with two doors.  Do you go through door #1 or door #2?
> stuff
You stumble around and fall on a knife and die.  Good job!

$ ruby ex31.rb 
You enter a dark room with two doors.  Do you go through door #1 or door #2?
> 1
There's a giant bear here eating a cheese cake.  What do you do?
1. Take the cake.
2. Scream at the bear.
> apples
Well, doing apples is probably better.  Bear runs away.
```

加分练习
---------

为游戏添加新的部分，改变玩家做决定的位置。尽自己能力扩充这个游戏，不过别把游戏弄得太诡异了。


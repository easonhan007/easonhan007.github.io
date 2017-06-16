---
layout: post
title: "练习35: 分支 (Branches) 和函式 (Functions)" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

你已经学会了 if 语句、函式、还有数组。现在你要练习扭转一下思维了。把下面的代码写下来，看你是否能弄懂它实现的是什么功能。

```sh
def prompt()
  print "> "
end

def gold_room()
  puts "This room is full of gold.  How much do you take?"

  prompt; next_move = gets.chomp
  if next_move.include? "0" or next_move.include? "1"
    how_much = next_move.to_i()
  else
    dead("Man, learn to type a number.")
  end

  if how_much < 50
    puts "Nice, you're not greedy, you win!"
    Process.exit(0)
  else
    dead("You greedy bastard!")
  end
end


def bear_room()
  puts "There is a bear here."
  puts "The bear has a bunch of honey."
  puts "The fat bear is in front of another door."
  puts "How are you going to move the bear?"
  bear_moved = false

  while true
    prompt; next_move = gets.chomp

    if next_move == "take honey"
      dead("The bear looks at you then slaps your face off.")
    elsif next_move == "taunt bear" and not bear_moved
      puts "The bear has moved from the door. You can go through it now."
      bear_moved = true
    elsif next_move == "taunt bear" and bear_moved
      dead("The bear gets pissed off and chews your leg off.")
    elsif next_move == "open door" and bear_moved
      gold_room()
    else
      puts "I got no idea what that means."
    end
  end
end

def cthulu_room()
  puts "Here you see the great evil Cthulu."
  puts "He, it, whatever stares at you and you go insane."
  puts "Do you flee for your life or eat your head?"

  prompt; next_move = gets.chomp

  if next_move.include? "flee"
    start()
  elsif next_move.include? "head"
    dead("Well that was tasty!")
  else
    cthulu_room()
  end
end

def dead(why)
  puts "#{why}  Good job!"
  Process.exit(0)
end

def start()
  puts "You are in a dark room."
  puts "There is a door to your right and left."
  puts "Which one do you take?"

  prompt; next_move = gets.chomp

  if next_move == "left"
    bear_room()
  elsif next_move == "right"
    cthulu_room()
  else
    dead("You stumble around the room until you starve.")
  end
end

start()
```

你应该看到的结果
----------------

你可以结果：

```sh
$ ruby ex35.rb
You are in a dark room.
There is a door to your right and left.
Which one do you take?
> left
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
> taunt bear
The bear has moved from the door. You can go through it now.
> open door
This room is full of gold.  How much do you take?
> asf
Man, learn to type a number. Good job!
$
```

加分练习
--------

1. 把这个游戏的地图画出来，把自己的路线也画出来。 
2. 改正你所有的错误，包括拼写错误。 
3. 为你不懂的函式写注解。记得 RDoc 中的注释吗？ 
4. 为游戏添加更多元素。通过怎样的方式可以简化并且扩充游戏的功能呢？ 
5. 这个` gold_room `游戏使用了奇怪的方式让你输入一个数字。这种方式会导致什么样的bug？你可以用比检查 0、1更好的方式判断输入是否是数字吗？` to_i() `这个函式可以给你一些头绪。 


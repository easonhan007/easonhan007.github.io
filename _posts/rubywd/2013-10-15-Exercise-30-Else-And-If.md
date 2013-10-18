---
layout: post
title: "练习30: Else 和 If" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

前一练习中你写了一些「if 语句 (if-statements)」，并且试图猜出它们是什么，以及实现的是什么功能。在你继续学习之前，我给你解释一下上一节的加分练习的答案。上一节的加分练习你做过了吧，有没有？

1. 你认为 if 对于它下一行的代码做了什么？if 语句为代码创建了一个所谓的「分支(branch)」，就跟 RPG游戏中的情节分支一样。if 语句告诉你的脚本：「如果这个布尔表示式为真，就执行接下来的代码，否则就跳过这一段。」 
2. 把练习29中的其它布尔表示式放到 if 语句中会不会也可以执行呢？试一下。可以。而且不管多复杂都可以，虽然写复杂的东西通常是一种不好的写作风格。 
3. 如果把变数 people、cats和 dogs 的初始值改掉，会发生什么事情？因为你比较的对象是数字，如果你把这些数字改掉的话，某些位置的 if 语句会被演绎为 True，而它下面的代码块将被运行。你可以试着修改这些数字，然后在头脑里假想一下那一段代码会被运行。 

把我的答案和你的答案比较一下，确认自己真正懂得代码「块(block)」的含义。这点对于你下一节的练习习很重要，因为你将会写很多的if 语句。

把这一段写下来，并让它运行起来：

```sh
people = 30
cars = 40
buses = 15

if cars > people
  puts "We should take the cars."
elsif cars < people
  puts "We should not take the cars."
else
  puts "We can't decide."
end

if buses > cars
  puts "That's too many buses."
elsif buses < cars
  puts "Maybe we could take the buses."
else
  puts "We still can't decide."
end

if people > buses
  puts "Alright, let's just take the buses."
else
  puts "Fine, let's stay home then."
end
```

你应该看到的结果
----------------

```sh
$ ruby ex30.rb
We should take the cars.
Maybe we could take the buses.
Alright, let's just take the buses.
$
```

加分练习
--------

1. 猜想一下 `elsif` 和 `else` 的功能。 
2. 将 `cars`、`people`和`buses`的数量改掉，然后追溯每一个if语句。看看最后会打印出什么来。
3. 试着写一些复杂的布尔表示式，例如 `cars > people and buses < cars`。 在每一行的上面写注解，说明这一行的功用。 


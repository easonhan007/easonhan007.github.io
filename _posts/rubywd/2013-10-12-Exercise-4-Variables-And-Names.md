---
layout: post
title: "练习4：变量和命名"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}


你已经学会了打印出东西和数学运算。下一步你要学的是「变量」。在开发程序中，变量只不过是用来代表某个东西的名称。开发人员通过使用变量名称可以 让他们的程序读起来更像英语。而且因为开发人员的记性都不怎样，变量名称可以让他们更容易记住程序的内容。如果他们没有在写程序时使用好的变量名称，在 下一次读到原来写的程序码时对他们会大为头疼的。

如果你被这章练习难住了的话，记得我们之前教过的：找到不同点、注意细节:

1. 在每一行的上面写一行注释，给自己解释一下这一行的作用。 
2. 倒着读你的``` .rb ```文档。 
3. 朗读你的``` .rb ```文档，将每个字符也朗读出来。 

```sh
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

puts "There are #{cars} cars available."
puts "There are only #{drivers} drivers available."
puts "There will be #{cars_not_driven} empty cars today."
puts "We can transport #{carpool_capacity} people today."
puts "We have #{passengers} passengers to carpool today."
puts "We need to put about #{average_passengers_per_car} in each car."
```

> Note:``` space_in_a_car ```中的``` _ ```是``` 下划线(underscore) ```符号。你要自己学会怎样打出这个符号来。这个符号在变量里通常被用作假想的空隔，用来隔开单词。

你应该看到的结果
----------------

```sh
$ ruby ex4.rb
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120.0 people today.
We have 90 passengers to carpool today.
We need to put about 3 in each car.
$
```

加分练习
--------

当我刚开始写这个程序时我犯了个错误，Ruby 告诉我这样的错误资讯：

```sh
ex4.rb:8:in `<main>': undefined local variable or method `car_pool_capacity' for main:Object (NameError)
```

用你自己的话解释一下这个错误资讯，解释时记得使用行号，而且要说明原因。

更多的加分练习
--------------

1. 解释一下为什么程序里面用了 4.0 而不是 4。 
2. 记住 4.0 是一个「浮点数」，自己研究一下这是什么意思。 
3. 在每一个变量赋值的上一行加上一行注释。 
4. 记住``` = ```的名称是等于(equal)，它的作用是为东西取名。 
5. 记住``` _ ```是下划线(underscore)。 
6. 将 IRB 作为计算机跑起来，就跟以前一样，不过这一次在计算过程中使用变量名称来做计算，常见的变量名称有``` i ```、``` x ```、``` j ```等等。 


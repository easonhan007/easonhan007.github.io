---
layout: post
title: "练习3 数字和数学表达式"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}


每一种程序语言都包含处理数字和进行数学表达式的方法。不必担心，程序员经常撒谎说他们是多们厉害的数学天才，其实他们根本不是。如果他们真是数学天才，他们早就去从事数学相关的行业了，而不是写写广告程序和社交网路游戏，从人们身上偷赚点小钱而已。

这章练习里有很多的数学运算符号。我们来看一遍它们都叫什么。你要一边写一边念出它们的名称来。直到你念烦了为止。名称如下：

```sh
+ 加号
- 减号
/ 除号
* 乘号
% 百分比符号
< 小于符号
> 大于符号
<= 小于等于符号
>= 大于等于号
```

有没有注意到以上只是些符号，没有运算操作呢？写完下面的练习程序代码后，再回到上面的列表，写出每个符号的作用。例如``` + ```是用来做加法运算的。

```sh
puts "I will now count my chickens:"

puts "Hens", 25 + 30 / 6
puts "Roosters", 100 - 25 * 3 % 4

puts "Now I will count the eggs:"

puts 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

puts "Is it true that 3 + 2 < 5 - 7?"

puts 3 + 2 < 5 - 7

puts "What is 3 + 2?", 3 + 2
puts "What is 5 - 7?", 5 - 7

puts "Oh, that's why it's false."

puts "How about some more."

puts "Is it greater?", 5 > -2
puts "Is it greater or equal?", 5 >= -2
puts "Is it less or equal?", 5 <= -2
```

你应该看到的结果
----------------

```sh
$ ruby ex3.rb 
I will now count my chickens:
Hens 
30
Roosters 
97
Now I will count the eggs: 
7
Is it true that 3 + 2 < 5 - 7?
false
What is 3 + 2? 
5
What is 5 - 7? 
-2
Oh, that's why it's false. 
How about some more.
Is it greater? 
true
Is it greater or equal? 
true
Is it less or equal? 
false
$
```

加分练习
---------
1. 使用``` # ```在程序代码每一行的前一行为自己写一个注解，说明一下这一行的作用。 
2. 记得最开始时的 的 IRB 吧？再次打开 IRB，然后使用刚才学到的运算符号，把Ruby 当做计算机玩玩。 
3. 自己找个想要计算的东西，写一个``` .rb ```文件把它计算出来。 
4. 有没有发现计算结果是「错」的呢？计算结果只有整数，没有小数部分。研究一下这是为什么，搜寻一下「浮点数(floating point number)」是什么东西。 
5. 使用浮点数重写一遍``` ex3.rb ```，让它的计算结果更准确(提示: 20.0 是一个浮点数)。 


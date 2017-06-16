---
layout: post
title: "练习6：字符串和文字"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}


虽然你已经在程序中写过字符串了，你还没学过它们的用处。在这章练习中我们将使用复杂的字符串来建立一系列的变量，从中你将学到它们的用途。首先我们解释一下字符串是什么东西。

字符串通常是指你想要展示给别人的，或者是你想要从程序里「导出」的一小段字符。Ruby 可以通过文字里的双引号``` " ```或者是单引号``` ' ```识别出字符串来。这在你以前的``` puts ```练习中你已经见过很多次了。如果你把单引号或者双引号括起来的文字放到``` puts ```后面，他们就会被 Ruby 打印出来。

字符串可以包含你目前学过的格式化字符串。你只要将格式化的变量放到字符串中，跟着一个百分比符号``` % ```(percent)，再紧跟着变量名称即可。唯一要注意的地方，是如果你想要在字符串中通过格式化字符串放入多个变量的结果，你需要将变量放到``` [] ```中括号(brackets) 中，而且变量之间用``` , ```逗号(comma)隔开。就像你逛商店时说「我要买牛奶、面包、鸡蛋、汤」一样，只不过程序设计师说的是”[milk, eggs, bread, soup]”。

另一种方式是使用字符串插值 (string interpolation) 这种技巧，将变量注入到你的字符串中。方法是使用``` #{} ```井号和大括号(pound and curly brace)。与其使用这种格式化字符串

```sh
name1 = "Joe"
name2 = "Mary"
puts "Hello %s, where is %s?" % [name1, name2]
```

我们可以输入：

```sh
name1 = "Joe"
name2 = "Mary"
puts "Hello #{name1}, where is #{name2}?"
```

我们将输入大量的字符串、变量和格式化字符串，并且将它们打印出来。我们还将练习使用简写的变量名称。程序设计师喜欢使用恼人的隐晦简写来节省打字时间，所以我们现在就将提早学会这件事，这样你就能读懂并写出这些东西了。

```sh
x = "There are #{10} types of people."
binary = "binary"
do_not = "don't"
y = "Those who know #{binary} and those who #{do_not}."

puts x
puts y

puts "I said: #{x}."
puts "I also said: '#{y}'."

hilarious = false
joke_evaluation = "Isn't that joke so funny?! #{hilarious}"

puts joke_evaluation

w = "This is the left side of..."
e = "a string with a right side."

puts w + e
```

你应该看到的结果

```sh
There are 10 types of people.
Those who know binary and those who don't.
I said: There are 10 types of people..
I also said: 'Those who know binary and those who don't.'.
Isn't that joke so funny?! false
This is the left side of...a string with a right side.
```

加分练习
--------

1. 遍历程序，在每一行的上面写一行注释，给自己解释这一行的作用。 
2. 找到所有的「字符串包含字符串」的位置，总共有四个位置。 
3. 你确定只有四个位置吗？你怎么知道的？说不定我在骗你呢。 
4. 解释一下为什么``` w ```和``` e ```用``` + ```连起来就可以生成一个更长的字符串。 


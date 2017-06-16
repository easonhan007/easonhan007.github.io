---
layout: post
title: "练习19: 函式和变量"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

函式这个概念也许承载了太多的数据量。不过别担心，只要坚持做这些练习，对照上个练习中的检查清单检查这次练习的关联，你最终会明白这些内容的。
有一个你可能没有注意到的细节，我们现在强调一下，函式里面的变量和脚本里面的变量之间是没有连接的。下面的这个练习可以让你对这一点有更多的思考：

```sh
def cheese_and_crackers(cheese_count, boxes_of_crackers)
  puts "You have #{cheese_count} cheeses!"
  puts "You have #{boxes_of_crackers} boxes of crackers!"
  puts "Man that's enough for a party!"
  puts "Get a blanket."
  puts # a blank line
end

puts "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

puts "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

puts "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

puts "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
```

通过这个练习，你看到我们给我们的函式``` cheese_and_crackers ```很多的参数，然后在函式里把他们打印出来。我们可以填数字、填变量进去函式，我们甚至可以将变量和数学运算结合在一起。

从一方面来说，函式的参数和我们生成变量时用的``` = ```赋值符号类似。事实上，如果一个物件你可以用``` = ```将其命名，你通常也可以将其作为参数传给一个函式。

你应该看到的结果
----------------

你应该研究一下脚本的输出，和你想像的结果对比一下看有什么不同。

```sh
$ ruby ex19.rb
We can just give the function numbers directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR, we can use variables from our script:
You have 10 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do math inside too:
You have 30 cheeses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two, variables and math:
You have 110 cheeses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.
$
```

加分练习
--------

1. 倒着将脚本读完，在每一行上面添加一行注解，说明这行程式的作用。 
2. 从最后一行开始，倒着阅读每一行，读出所有重要的符号来。 
3. 自己边写出至少一个函式出来，然后用十种方法运行这个函式。 


---
layout: post
title: "练习24: 更多练习"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

你离这本书第一部分的结尾已经不远了，你应该已经具备了足够的 Ruby 基础知识，可以继续学习一些程序的原理了，但你应该做更多的练习。这个练习的内容比较长，它的目的是锻炼你的毅力，下一个练习也差不多是这样的，好好完成它们，做到完全正确，记得仔细检查。

```sh
puts "Let's practice everything."
puts "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = <<MULTI_LINE_STRING

\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.

MULTI_LINE_STRING

puts "--------------"
puts poem
puts "--------------"

five = 10 - 2 + 3 - 6
puts "This should be five: #{five}"

def secret_formula(started)
  jelly_beans = started * 500
  jars = jelly_beans / 1000
  crates = jars / 100
  return jelly_beans, jars, crates
end

start_point = 10000
beans, jars, crates = secret_formula(start_point)

puts "With a starting point of: #{start_point}"
puts "We'd have #{beans} beans, #{jars} jars, and #{crates} crates."

start_point = start_point / 10

puts "We can also do that this way:"
puts "We'd have %s beans, %s jars, and %s crates." % secret_formula(start_point)
```

你应该看到的结果
----------------

```sh
$ ruby ex24.rb
Let's practice everything.
You'd need to know 'bout escapes with \ that do 
 newlines and    tabs.
--------------

    The lovely world
with logic so firmly planted
cannot discern 
 the needs of love
nor comprehend passion from intuition
and requires an explanation

        where there is none.

--------------
This should be five: 5
With a starting point of: 10000
We'd have 5000000 beans, 5000 jars, and 50 crates.
We can also do that this way:
We'd have 500000 beans, 500 jars, and 5 crates.
$
```

加分练习
--------

1. 记得仔细检查结果，从后往前倒着检查，把程序代码朗读出来，在不清楚的位置加上注释。 
2. 故意将程序码改烂，执行并检查会发生什么样的错误，并且确认你有能力改正这些错误。 


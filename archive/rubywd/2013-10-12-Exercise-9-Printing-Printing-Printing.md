---
layout: post
title: "练习9：打印，打印，还是打印"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

```sh
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

puts "Here are the days: ", days
puts "Here are the months: ", months

puts <<PARAGRAPH
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
PARAGRAPH
```

你应该看到的结果

```sh
$ ruby ex9.rb
Here are the days:  
Mon Tue Wed Thu Fri Sat Sun
Here are the months:
Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
```

加分练习
--------

1. 自己检查结果，记录你犯过的错误，并且在下个练习中尽量不犯相同的错误。 


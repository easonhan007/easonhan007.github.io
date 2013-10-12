---
layout: post
title: "练习9：打印，打印，还是打印"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

```sh
1. # Here's some new strange stuff, remember type it exactly.

2. days = "Mon Tue Wed Thu Fri Sat Sun"
3. months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

4. puts "Here are the days: ", days
5. puts "Here are the months: ", months

6. puts <<PARAGRAPH
7. There's something going on here.
8. With the three double-quotes.
9. We'll be able to type as much as we like.
10. Even 4 lines if we want, or 5, or 6.
11. PARAGRAPH
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


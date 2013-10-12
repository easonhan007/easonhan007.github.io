---
layout: post
title: "练习8：打印，打印"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

```sh
formatter = "%s %s %s %s"

puts formatter % [1, 2, 3, 4]
puts formatter % ["one", "two", "three", "four"]
puts formatter % [true, false, false, true]
puts formatter % [formatter, formatter, formatter, formatter]
puts formatter % [
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
]
```

你应该看到的结果

```sh
$ ruby ex8.rb
1 2 3 4
one two three four
true false false true
%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s
I had this thing. That you could type up right. But it didn't sing. So I said goodnight.
$
```

加分练习
--------

1. 自己检查结果，记录你犯过的错误，并且在下个练习中尽量不犯相同的错误。 


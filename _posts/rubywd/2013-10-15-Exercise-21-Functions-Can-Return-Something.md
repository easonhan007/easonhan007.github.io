---
layout: post
title: "练习21: 函式的返回值"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

你已经学过使用``` = ```给变量命名，以及将变量定义为某个数字换字符串。接下来我们将让你见证更多奇迹。我们要示范给你的是如何使用``` = ```来将变量设置为「一个函式的值」。有一件事你需要特别注意，但待会再说，先输入下面的脚本吧：

```sh
def add(a, b)
  puts "ADDING #{a} + #{b}"
  a + b
end

def subtract(a, b)
  puts "SUBTRACTING #{a} - #{b}"
  a - b
end

def multiply(a, b)
  puts "MULTIPLYING #{a} * #{b}"
  a * b
end

def divide(a, b)
  puts "DIVIDING #{a} / #{b}"
  a / b
end

puts "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78,4)
weight = multiply(90, 2)
iq = divide(100, 2)

puts "Age: #{age}, Height: #{height}, Weight: #{weight}, IQ: #{iq}"

# A puzzle for the extra credit, type it in anyway.
puts "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

puts "That becomes: #{what} Can you do it by hand?"
```

现在我们创造了我们自己的加减乘除数学函式：``` add ```、``` subtract ```、``` multiply ```以及``` divide ```。最重要的是函式的最后一行，例如``` add ```的最后一行是``` return a + b ```，它实现的功能是这样的：

1. 我们调用函式时使用了两个参数：``` a ```和``` b ```。 
2. 我们打印出这个函式的功能，这里就是计算加法（ADDING)。 
3. 接下来我们告诉 Ruby 让他做某个回传的动作：我们将``` a+b ```的值返回 (return)。或者你可以这么说：「我将 a 和 b 加起来，再把结果返回。」 
4. Ruby 将两个数字相加，然后当函式结束时，它就可以将 a + b 的结果赋予给一个变量。 

和本书里的很多其他东西一样，你要慢慢消化这些内容，一步一步执行下去，追踪一下究竟发生了什么。为了帮助你理解，本节的加分练习将让你解决一个谜题，并且让你学到点比较酷的东西。

你应该看到的结果
----------------

```sh
$ ruby ex21.rb
Let's do some math with just functions!
ADDING 30 + 5
SUBTRACTING 78 - 4
MULTIPLYING 90 * 2
DIVIDING 100 / 2
Age: 35, Height: 74, Weight: 180, IQ: 50
Here is a puzzle.
DIVIDING 50 / 2
MULTIPLYING 180 * 25
SUBTRACTING 74 - 4500
ADDING 35 + -4426
That becomes:  -4391 Can you do it by hand?
$
```

加分练习
--------

1. 如果你不是很确定 return 回来的值，试着自己写几个函式出来，让它们返回一些值。你可以将任何可以放在``` = ```右边的东西作为一个函式的返回值。
2. 这个脚本的结尾是一个谜题。我将一个函式的返回值当作了另外一个函式的参数。我将它们链接到了一起，接跟写数学等式一样。这样可能有些难读，不过执行一下你就知道结果了。接下来，你需要试试看能不能用正常的方法实现和这个方程式一样的功能。
3. 一旦你解决了这个谜题，试着修改一下函式里的某些部分，然后看会有什么样的结果。你可以有目的地修改它，让它输出另外一个值。
4. 最后，倒过来做一次。写一个简单的等式，使用一样的函式来计算它。

这个练习可能会让你有些头大，不过还是慢慢来，把它当做一个游戏，解决这样的谜题正是写程式的乐趣之一。后面你还会看到类似的小谜题。


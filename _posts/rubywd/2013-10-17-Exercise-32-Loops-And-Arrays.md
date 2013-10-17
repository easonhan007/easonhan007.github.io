---
layout: post
title: "练习32: 循环和数组" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

现在你应该有能力写更有趣的程序出来了。如果你能够一直跟得上，你应该已意识到你能将之前学到的将` if `语句 和 「布尔表示式」这些东西结合起来，让程序做出一些聪明的事了。

然而，我们的城市还需要能很快地完成重复的事情。这节练习中我们将使用` for-loop `(for 循环) 来建立和打印出各式的数组。在做练习的过程中，你将会逐渐搞懂它们是怎么回事。现在我不会告诉你，你需要自己找到答案。

在你开始使用 for 循环之前，你需要在某个位置存放循环的结果。最后的方法是使用数组` array `。一个数组，就是一个按照顺序存放东西的容器。数组并不复杂，你只是要学习一点新的语法。首先我们来看看如何建立一个数组：

```sh
hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]
```

你要做的是以` [ `左中括号开头「打开」数组，然后写下你要放入数组的东西、用逗号` , `隔开，就跟函式的参数一样，最后你需要用` ] `右中括号结束数组的定义。然后 Ruby 接收这个数组以及里面所有的内容，将其赋予给一个变数。

> Warning: 对于不会写程序的人来说这是一个困难点。习惯性思维告诉你的大脑大地是平的。记得上一个练习中的巢状 if 语句吧，你可能觉得要理解它有些难度，因为生活中一般人不会去想这样的问题，但这样的问题在程序中几乎到处都是。你会看到一个函式调用用另外一个包含 if 语句的函式，其中又有巢状数组的数组。如果你看到这样的东西一时无法弄懂，就用纸笔记下来，手动分割下去，直到弄懂为止。

现在我们将使用循环建立一些数组，然后将它们打印出来：

```sh
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through an array
for number in the_count
  puts "This is count #{number}"
end

# same as above, but using a block instead
fruits.each do |fruit|
  puts "A fruit of type: #{fruit}"
end

# also we can go through mixed arrays too
for i in change
  puts "I got #{i}"
end

# we can also build arrays, first start with an empty one
elements = []

# then use a range object to do 0 to 5 counts
for i in (0..5)
  puts "Adding #{i} to the list."
  # push is a function that arrays understand
  elements.push(i)
end

# now we can puts them out too
for i in elements
  puts "Element was: #{i}"
end
```

你应该看到的结果
----------------

```sh
$ ruby ex32.rb
This is count 1
This is count 2
This is count 3
This is count 4
This is count 5
A fruit of type: apples
A fruit of type: oranges
A fruit of type: pears
A fruit of type: apricots
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5
$
```

加分练习
----------

1. 注意一下` range (0..5) `。查一下` Range ` class (类别) 并弄懂它。 
2. 在第 24 行，你可以直接将` elements `赋值为` (0..5) `，而不需使用 for 循环吗？ 
3. 在 Ruby 文件中可以找到关于数组的内容，仔细阅读一下，除了` push `以外，数组还支持那些操作？ 


---
layout: post
title: "理解ruby Enumerable并实现之"
description: "理解ruby Enumerable并实现之"
category: ruby 
tags: [ruby]
---
{% include JB/setup %}

[原文地址](http://mauricio.github.io/2015/01/12/implementing-enumerable-in-ruby.html)

Ruby的Enumerable module是实现module的绝好例子。该module提供了很多有用的方法，而你要做的只是实现1个```each```方法。因此任何的类都可以拥有集合类的行为，只要其实现了```each```方法和include Enumerable.

实现Enumerable module的主要方法是理解该module的不错的方式。

首先我们需要include了CustomEnumerable的类。下面是其定义：

```ruby
class ArrayWrapper

  include CustomEnumerable

  def initialize(*items)
    @items = items.flatten
  end

  def each(&block)
    @items.each(&block)
    self
  end

  def ==(other)
    @items == other
  end

end
```
这里没什么特别的，主要是实现==方法是为了能够使用Rspec的eq matcher.该方法并不是Enumerable类的所必需要求实现的方法。

### map

```map```的文档里这样是这样说的

> Returns a new array with the results of running block once for every element in enum.

因此我们的代码块必须遍历每个item然后构建出一个需要返回的数组。实现如下：

```ruby
```

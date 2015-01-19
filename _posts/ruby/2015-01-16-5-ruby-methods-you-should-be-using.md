---
layout: post
title: "你应该学会使用的5个ruby方法"
description: "你应该学会使用的5个ruby方法"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

今天看到了这篇文章--[Five Ruby Methods You Should Be Using](https://blog.engineyard.com/2015/five-ruby-methods-you-should-be-using),感觉收获颇丰，先简单翻译一下先。

作者写这篇文章的契机是在[Exercism](http://exercism.io/)上看到了很多ruby代码可以用更好的方式去重构，因此他分享了一些冷门的但是非常有用的ruby方法。

### Object#tap

你是否曾发现在某个对象上调用方法时返回值不是你所预期？你想返回这个对象，但是返回的时候又想对这个对象进行一些修改。比方说，你想给hash对象增加1个key value，这时候你需要调用Hash.[]方法，但是你想返回的是整个hash对象，而不是具体的某个value值，因此你需要显示的返回该对象。

```ruby
def update_params(params)
  params[:foo] = 'bar'
  params
end
```
最后一行的那个params显得有些多余了。

我们可以用```Object#tap```方法来优化这个方案。

[tap](http://www.ruby-doc.org/core-2.1.5/Object.html#method-i-tap)方法用起来非常简单,直接在某个对象上调用tap方法，然后就可以在代码块里yielded这个对象，最后这个对象本身会被返回。下面的代码演示了如何使用tap方法来重构刚才的实现。

```ruby
def update_params(params)
  params.tap {|p| p[:foo] = 'bar' }
end
```

有很多地方都可以使用到```Object#tap```方法，一般的规律是对那些在对象上调用，希望返回对象，但是却没返回该对象本身的方法都适用。


### Array#bsearch

我不清楚你的情况，但我经常在数组里去查找数据。ruby的enumerable模块提供了很多简单好用的方法```select, reject, find ```。不过当数据源很庞大的时候，我开始对这些查找的性能表示忧桑。

如果你正在使用ActiveRecord和非NO SQL的数据库，查询的算法复杂度是经过优化了的。但是有时候你需要从数据库里把所有的数据拉出来进行处理，比方说如果你加密了数据库，那就不能好好的写sql做查询了。

这时候我会冥思苦想以找到一个最小的算法复杂度来筛选数据。如果你不了解算法复杂度，也就是这个O，请阅读[ Big-O Notation Explained By A Self-Taught Programmer](https://justin.abrah.ms/computer-science/big-o-notation-explained.html)或［Big-O Complexity Cheat Sheet](http://bigocheatsheet.com/)。

一般来说，算法复杂度越低，程序运行的速度就越快。``` O(1), O(log n), O(n), O(n log(n)), O(n^2), O(2^n), O(n!)```，在这个例子里，越往右算法复杂度是越高的。所以我们要让我们的算法接近左边的复杂度。

当我们搜索数组的时候，一般第一个想到的方法便是```Enumerable#find```,也就是select方法。不过这个方法会搜索整个数组直到找到预期的结果。如果要找的元素在数组的开始部分，那么搜索的效率倒不会太低，但如果是在数据的末尾，那么搜索时间将是很可观的。find方法的算法复杂度是O(n)。

更好的办法是使用(Array#bsearch)[http://www.ruby-doc.org/core-2.1.5/Array.html#method-i-bsearch]方法。该方法的算法复杂度是O(log n)。你可以查看[Building A Binary Search](http://fluxusfrequency.github.io/blog/2014/01/31/building-a-binary-search/)这篇文章来该算法的原理。

下面的代码显示了搜索50000000个数字时不同算法之间的性能差异。

```
require 'benchmark'

data = (0..50_000_000)

Benchmark.bm do |x|
  x.report(:find) { data.find {|number| number > 40_000_000 } }
  x.report(:bsearch) { data.bsearch {|number| number > 40_000_000 } }
end

         user       system     total       real
find     3.020000   0.010000   3.030000   (3.028417)
bsearch  0.000000   0.000000   0.000000   (0.000006)
```

如你所见，```bsearch```要快的多。不过要注意的是bsearch要求搜索的数组是排序过的。尽管这个限制bsearch的使用场景，bsearch在显示生活中确实是有用武之地的。比如通过```created_at```字段来查找从数据库中取出的数据。

### Enumerable#flat_map

考虑这种情况，你有个blog应用，你希望找到上个月有过评论的所有作者，你可以会这样做：

```ruby
module CommentFinder
  def self.find_for_users(user_ids)
    users = User.where(id: user_ids)
    user.posts.map do |post|
      post.comments.map |comment|
        comment.author.username
      end
    end
  end
end
```

得到的结果看起来会是这样的

```ruby
[[['Ben', 'Sam', 'David'], ['Keith']], [[], [nil]], [['Chris'], []]]
```

不过你想得到的是所有作者，这时候你大概会使用```flatten```方法。

```ruby
module CommentFinder
  def self.find_for_users(user_ids)
    users = User.where(id: user_ids)
    user.posts.map { |post|
      post.comments.map { |comment|
        comment.author.username
      }.flatten
    }.flatten
  end
end
```

另一个选择是使用```flat_map```方法。

```ruby
module CommentFinder
  def self.find_for_users(user_ids)
    users = User.where(id: user_ids)
    user.posts.flat_map { |post|
      post.comments.flat_map { |comment|
        comment.author.username
      }
    }
  end
end
```
这跟使用flatten方法没什么太大的不同，不过看起来会优雅一点，毕竟不需要反复调用flatten了。


### Array.new with a Block

想当年我在一个技术训练营，我们的导师Jeff Casimir同志([Turing School](http://turing.io/)的创始人)让我们在一小时内写个Battleship游戏。这是极好的进行面向对象编程的练习，我们需要Rules，Players, Games和Boards类。

创建代表Board的数据结构是一件非常有意思的事情。经过几次迭代我发现下面的方法是初始化8x8格子的最好方式：

```ruby
class Board
  def board
    @board ||= Array.new(8) { Array.new(8) { '0' } }
  end
end
```

上面的代码是什么意思？当我们调用```Array.new```并传入了参数length，1个长度为length的数组将会被创建。

```ruby
Array.new(8)
#=> [nil, nil, nil, nil, nil, nil, nil, nil]
```

当你传入一个block，这时候block的返回值会被当成是数组的每个元素。

```ruby
Array.new(8) { 'O' }
#=> ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
```

因此，当你向block传入1个具有8个元素的数组时，你会得到8x8个元素的嵌套数组了。

用Array#new加block的方式可以创建很多有趣和任意嵌套层级的数组。


### <=>

这个方法就很常见了。简单来说这方法是判断左值和右值的关系的。如果左值大于右值返回1，相等返回0，否则返回－1。

实际上```Enumerable#sort, Enumerable#max```方法都是基于<=>的。另外如果你定义了<=>，然后再include Comparable，你将免费得到<=, <, >=, >以及between方法。

这是作者的在现实生活中所用到的例子：

```ruby
def fix_minutes
  until (0...60).member? minutes
    @hours -= 60 <=> minutes
    @minutes += 60 * (60 <=> minutes)
  end
  @hours %= 24
  self
end
```
这个方法不是很好理解，大概的意思就是如果minutes超过60的话，小时数+1,等于60小时数不变，否则－1。

### 讨论

会的方法越多写出来的代码可能会更有表现力，边写代码边改进,另外多读rubydoc。








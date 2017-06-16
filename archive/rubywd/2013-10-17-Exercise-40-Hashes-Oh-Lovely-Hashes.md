---
layout: post
title: "练习40:  Hash, 可爱的 Hash" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

接下来我要教你另外一种让你伤脑筋的容器型资料结构，因为一旦你学会这种资料结构，你将拥有超酷的能力。这是最有用的容器：Hash。

Ruby 将这种资料类型叫做「Hash」，有的语言里它的名称是「dictionaries」。这两种名字我都会用到，不过这并不重要，重要的是它们和数组的区别。你看，针对数组你可以做这样的事情：

```sh
ruby-1.9.2-p180 :015 > things = ['a','b','c','d']
 => ["a", "b", "c", "d"]
ruby-1.9.2-p180 :016 > print things[1]
b => nil
ruby-1.9.2-p180 :017 > things[1] = 'z'
 => "z"
ruby-1.9.2-p180 :018 > print things[1]
z => nil
ruby-1.9.2-p180 :019 > print things
["a", "z", "c", "d"] => nil
ruby-1.9.2-p180 :020 >
```

你可以使用数字作为数组的「索引」，也就是你可以通过数字找到数组中的元素。而 Hash 所作的，是让你可以通过任何东西找到元素，不只是数字。是的，Hash 可以将一个物件和另外一个东西关联，不管它们的类型是什么，我们来看看：

```sh
ruby-1.9.2-p180 :001 > stuff = {:name => "Rob", :age => 30, :height => 5*12+10}
 => {:name=>"Rob", :age=>30, :height=>70}
ruby-1.9.2-p180 :002 > puts stuff[:name]
Rob
 => nil
ruby-1.9.2-p180 :003 > puts stuff[:age]
30
 => nil
ruby-1.9.2-p180 :004 > puts stuff[:height]
70
 => nil
ruby-1.9.2-p180 :005 > stuff[:city] = "New York"
 => "New York"
ruby-1.9.2-p180 :006 > puts stuff[:city]
New York
 => nil
ruby-1.9.2-p180 :007 >
```

你将看到除了通过数字以外，我们在 Ruby 还可以用字串来从 Hash 中获取` stuff `，我们还可以用字串来往 Hash 中添加元素。当然它支持的不只有字串，我们还可以做这样的事情：

```sh
ruby-1.9.2-p180 :004 > stuff[1] = "Wow"
 => "Wow"
ruby-1.9.2-p180 :005 > stuff[2] = "Neato"
 => "Neato"
ruby-1.9.2-p180 :006 > puts stuff[1]
Wow
 => nil
ruby-1.9.2-p180 :007 > puts stuff[2]
Neato
 => nil
ruby-1.9.2-p180 :008 > puts stuff
{:name=>"Rob", :age=>30, :height=>70, :city=>"New York", 1=>"Wow", 2=>"Neato"}
 => nil
ruby-1.9.2-p180 :009 >
```

在这里我使用了数字。其实我可以使用任何东西，不过这么说并不准确，不过你先这么理解就行了。

当然了，一个只能放东西进去的 Hash是没啥意思的，所以我们还要有删除物件的方法，也就是使用` delete `这个关键字：

```sh
ruby-1.9.2-p180 :009 > stuff.delete(:city)
 => "New York"
ruby-1.9.2-p180 :010 > stuff.delete(1)
 => "Wow"
ruby-1.9.2-p180 :011 > stuff.delete(2)
 => "Neato"
ruby-1.9.2-p180 :012 > stuff
 => {:name=>"Rob", :age=>30, :height=>70}
ruby-1.9.2-p180 :013 >
```

接下来我们要做一个练习，你必须「非常」仔细，我要求你将这个练习写下来，然后试着弄懂它做了些什么。这个练习很有趣，做完以后你可能会有豁然开朗的感觉。

```sh
cities = {'CA' => 'San Francisco',
  'MI' => 'Detroit',
  'FL' => 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(map, state)
  if map.include? state
    return map[state]
  else
    return "Not found."
  end
end

# ok pay attention!
cities[:find] = method(:find_city)

while true
  print "State? (ENTER to quit) "
  state = gets.chomp

  break if state.empty?

  # this line is the most important ever! study!
  puts cities[:find].call(cities, state)
end
```

你应该看到的结果
----------------

```sh
$ ruby ex40.rb 
State? (ENTER to quit) > CA
San Francisco
State? (ENTER to quit) > FL
Jacksonville
State? (ENTER to quit) > O
Not found.
State? (ENTER to quit) > OR
Portland
State? (ENTER to quit) > VT
Not found.
State? (ENTER to quit) >
```

加分练习
---------

1. 在 Ruby 文件中找到 Hash 相关的内容，学着对 Hash 做更多的操作。 
2. 找出一些 Hash 无法做到的事情。例如比较重要的一个就是 Hash 的内容是无序的，你可以检查一下看看是否真是这样。 
3. 试着把` for `循环执行到 Hash 上面，然后试着在` for `循环中使用 Hash 的 each 函式，看看会有什么样的结果。 


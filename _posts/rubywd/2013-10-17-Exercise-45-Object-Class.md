---
layout: post
title: "练习45:  对象，类和从属关系" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

有一个重要的概念你需要弄明白，那就是` Class `「类」和` Object `「对象」的区别。问题在于，class 和 object 并没有真正的不同。它们其实是同样的东西，只是在不同的时间名字不同罢了。我用禅语来解释一下吧：

` 鱼(Fish)和鲑鱼(Salmon)有什么区别？ `

这个问题有没有让你有点晕呢？说真的，坐下来想一分钟。我的意思是说，鱼和鲑鱼是不一样，不过它们其实也是一样的是不是？泥鳅是鱼的一种，所以说没什么不同，不过泥鳅又有些特别，它和别的种类的鱼的确不一样，比如鲑鱼和比目鱼就不一样。所以鲑鱼和鱼既相同又不同。怪了。

这个问题让人晕的原因是大部分人不会这样去思考问题，其实每个人都懂这一点，你无须去思考鱼和鲑鱼的区别，因为你知道它们之间的关系。你知道鲑鱼是鱼的一种，而且鱼还有别的种类，根本就没必要去思考这类问题。

让我们更进一步，假设你有一只水桶，里边有三条鲑鱼。假设你的好人卡多到没地方用，于是你给它们分别取名叫Frank，Joe，Mary。现在想想这个问题：

` Mary 和鲑鱼有什么区别？ `

这个问题一样的奇怪，但比起鱼和鲑鱼的问题来还好点。你知道 Mary是一条鲑鱼，所以他并没什么不同，他只是鲑鱼的一个「实例(instance)」。Joe 和Frank 一样也是鲑鱼的实例。我的意思是说，它们是由鲑鱼创建出来的，而且代表着和鲑鱼一样的属性。

所以我们的思维方式是（你可能会有点不习惯）：鱼是一个「类(class)」，鲑鱼是一个「类(class)」，而 Mary 是一个「对象(object)」。仔细想想，然后我再一点一点慢慢解释给你。

鱼是一个「类」，表示它不是一个真正的东西，而是一个用来描述具有同类属性的实例的概括性词汇。你有鳍？你有鳔？你住在水里？好吧那你就是一条鱼。

后来一个博士路过，看到你的水桶，于是告诉你：「小伙子，你这些鱼是鲑鱼。」 专家一出，真相即现。并且专家还定义了一个新的叫做「鲑鱼」的「类」，而这个「类」又有它特定的属性。长鼻子？红肉？体型大？住在海里或是干净新鲜的 水里？吃起来味道不错？那你就是一条鲑鱼。

最后一个厨师过来了，他跟博士说：「非也非也，你看到的是鲑鱼，我看到的是Mary，而且我要把 Mary 淋上美味酱料做一道小菜。 」于是你就有了一只叫做Mary 的鲑鱼的「实例(instance)」（鲑鱼也是鱼的一个「实例」），并且你使用了它（把它塞到你的胃里了），这样它就是一「对象 (object)」。

这会你应该了解了：Mary 是鲑鱼的成员，而鲑鱼又是鱼的成员。这里的关系式：对象属于某个类，而某个类又属于另一个类。

写完后的代码是什么样子
-------------------

这个概念有点诡异，不过实话说，你只要在建立和使用class的时候操心一下就可以了。我来给你两个区分` Class `和` Object `的小技巧。

首先针对类和对象，你需要学会两个说法，「is-a(是啥)」和「has-a(有啥)」。「是啥」要用在谈论「两者以类的关系互相关联」的时候，而「有啥」要用在「两者无共同点，仅是互为参照」的时候。

接下来，通读这段代码，将每一个注解为` ##?? `的位置标明他是「is-a」还是「has-a」的关系，并讲明白这个关系是什么。在代码的开始我还举了几个例子，所以你只要写剩下的就可以了。

记住，「是啥」指的是鱼和鲑鱼的关系，而「有啥」指的是鲑鱼和烤肉架的关系。

```sh
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal

end

## ??
class Dog < Animal

  def initialize(name)
    ## ??
    @name = name
  end

end

## ??
class Cat < Animal

  def initialize(name)
    ## ??
    @name = name
  end

end

## ??
class Person

  attr_accessor :pet

  def initialize(name)
    ## ??
    @name = name

    ## Person has-a pet of some kind
    @pet = nil
  end

end
## ??
class Employee < Person

  def initialize(name, salary)
    ## ?? hmm what is this strange magic?
    super(name)
    ## ??
    @salary = salary
  end

end

## ??
class Fish

end

## ??
class Salmon < Fish

end

## ??
class Halibut < Fish

end

## rover is-a Dog
rover = Dog.new("Rover")

## ??
satan = Cat.new("Satan")

## ??
mary = Person.new("Mary")

## ??
mary.pet = satan

## ??
frank = Employee.new("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish.new

## ??
crouse = Salmon.new

## ??
harry = Halibut.new
```

加分练习
--------
1. 有没有办法把` Class `当作` Object `使用呢？ 
2. 在练习中为 animals、fish、还有people 添加一些函数，让它们做一些事情。看看当函数在 Animal 这样的「基类(base class)」里和在 Dog 里有什么区别。 
3. 找些别人的代码，理清里边的「是啥」和「有啥」的关系。 
4. 使用 Array 和 Hash 建立一些新的一对应多的「has-many」的关系。 
5. 你认为会有一种「has-many」的关系吗？阅读一下关于「多重继承(multiple inheritance)」的资料，然后尽量避免这种用法。 


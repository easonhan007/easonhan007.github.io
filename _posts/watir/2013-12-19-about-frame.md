---
layout: post
title: "爱在watir(6)————关于frame的那些事情"
description: "如何定位iframe中的元素"
category: watir
tags: [watir]
---
{% include JB/setup %}

fred对于tom暴力抗拒加班的行为非常生气。他化愤怒为食欲，早餐多吃了2个肉包。

但是对于tom他却也无话可说。tom那天确实是提前完成了工作，而且做的很好，fred也挑不出什么毛病来。fred只是在第二天很客气的对tom说:"小伙子动作很麻利，手脚很快。不过你也要多注意点teamwork，有了teamwork才能带领团队更好的工作"。

fred很郁闷，他现在已经在盘算着如何找个茬把tom给开掉了。因为对于fred来说，听话的下属比会干活的下属更有价值。当然了，不仅是fred，很多失去了动力的基层leader都是如此认为。

tom不知道也不在乎fred的小肚鸡肠。因为coco最近进步很快，经常向tom请教一些实际问题了。coco已经不局限于示例代码，她开始自己写脚本去替代手工操作，开始释放自己，越来越多的在代码中寻求自己的价值。

其实对于watir以及其他的一些自动化测试工具来说，最麻烦的事情无非就是定位元素。也就是把页面上的需要操作的东西找到。为了找这些东西，每个工具都有自己的一套语言或规则，这些语法和规则可以称之为DSL。

一般来说，这些规则都是简单和容易理解的，如何熟练而灵活的运用这些规则反倒是一件非常费时的事情。这需要经验和反复实践。

coco也遇到了对象无法定位的问题。她用id去定位一个链接，却发现无论如何都定位不到。

tom告诉coco，这是因为这个链接在iframe里，需要先定位到iframe，然后再定位链接。这个可以说是watir的一个规则，直接记住就好了。

所谓的frame就是类似于<frame></frame>或<iframe></iframe>之类的标签，看到这个标签你就应该条件反射的想到这里有一个frame。如果需要定位frame中的一些元素，那么第一步就是定位这个frame，在watir中处理frame是优雅的。

tom给出了下面的演示代码

```ruby
b.frame(:id => "content_ifr").send_keys "hello world"
```

可以看出来，在watir中定位frame和定位其他的元素没什么不同。

定位frame中的元素如下例所示，也很自然。

```ruby
b.frame(:name => "ifrmae").link(:id => 'click').click
```

coco问道:"如果页面上的iframe没有id,name之类的属性怎么办呢？"

tom想了想给出了答案。

一般来说，如果frame没有属性的话可以让开发帮忙加一个，这个对于开发人员来说是没有负面影响的事情，好好沟通一般都会成功。

如果开发实在是没办法加，因为有些js框架自动生成的frame是不好加属性的，那么你就可以用下面的代码去尝试。

```ruby
# 先找出所有的frame，然后选择自己想要的那个
# 这个例子里找的是第1个frame
browser.frames.first.link(:id => 'click').click
```

在watir和selenium webdriver中，如果元素没有特殊的好定位的属性的话，都可以用上面的方法，先找到全部的某种元素，然后定位到其中的一个。

coco听完若有所思，tom继续矛盾，因为他知道coco会的越多就会离他越远。




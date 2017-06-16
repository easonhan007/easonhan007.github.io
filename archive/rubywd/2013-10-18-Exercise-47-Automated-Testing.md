---
layout: post
title: "练习47:  自动化测试" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

为了确认游戏的功能是否正常，你需要一遍一遍地在你的游戏中输入命令。这个过程是很枯燥无 味的。如果能写一小段代码用来测试你的代码岂不是更好？然后只要你对程序做了任何修改，或者添加了什么新东西，你只要「跑一下你的测试」，而这些测试 能确认程序依然能正确运行。这些自动测试不会抓到所有的bug，但可以让你无需重复输入命令运行你的代码，从而为你节约很多时间。

从这一章开始，以后的练习将不会有「你应该看到的结果」这一节，取而代之的是一个「你应该测试的东西」一节。从现在开始，你需要为自己写的所有代码写自动化测试，而这将让你成为一个更好的程序员。

我不会试图解释为什么你需要写自动化测试。我要告诉你的是，你想要成为一个开发人员，而程序的作用是让无聊冗繁的工作自动化，测试软件毫无疑问是无聊冗繁的，所以你还是写点代码让它为你测试的更好。

这应该是你需要的所有的解释了。因为你写单元测试的原因是让你的大脑更加强健。你读了这本书，写了很多代码让它们实现一些事情。现在你将更进一 步，写出懂得你写的其他代码的代码。这个写代码测试你写的其他代码的过程将强迫你清楚的理解你之前写的代码。这会让你更清晰地了解你写的代码 实现的功能及其原理，而且让你对细节的注意更上一个台阶。

撰写 Test Case
---------------

我们将拿一段非常简单的代码为例，写一个简单的测试，这个测试将建立在上节我们创建的项目骨架上面。

首先从你的项目骨架创建一个叫做` ex47 `的项目。确认该改名称的地方都有改过，尤其是` tests/ex47_tests.rb `这处不要写错。

接下来建立一个简单的` ex47/lib/game.rb `文件，里边放一些用来被测试的代码。我们现在放一个傻乎乎的小 class 进去，用来作为我们的测试对象：

```sh
class Room

  attr_accessor :name, :description, :paths

  def initialize(name, description)
    @name = name
    @description = description
    @paths = {}
  end

  def go(direction)
    @paths[direction]
  end

  def add_paths(paths)
    @paths.update(paths)
  end

end
```

一旦你有了这个文件，修改你的 unit test 骨架变成这样：

```sh
require 'test/unit'
require_relative '../lib/ex47'

class MyUnitTests < Test::Unit::TestCase

  def test_room()
    gold = Room.new("GoldRoom",
                    """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
  end

  def test_room_paths()
    center = Room.new("Center", "Test room in the center.")
    north = Room.new("North", "Test room in the north.")
    south = Room.new("South", "Test room in the south.")

    center.add_paths({:north => north, :south => south})
    assert_equal(center.go(:north), north)
    assert_equal(center.go(:south), south)
  end

  def test_map()
    start = Room.new("Start", "You can go west and down a hole.")
    west = Room.new("Trees", "There are trees here, you can go east.")
    down = Room.new("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({:west => west, :down => down})
    west.add_paths({:east => start})
    down.add_paths({:up => start})

    assert_equal(start.go(:west), west)
    assert_equal(start.go(:west).go(:east), start)
    assert_equal(start.go(:down).go(:up), start)
  end

end
```

这个文件 require 了你在` lib/ex47.rb `里建立的` Room `这个类，接下来我们要做的就是测试它。于是我们看到一系列的以` test_ `开头的测试函数，它们就是所谓的「Test Case」，每一个Test Case里面都有一小段代码，它们会建立一个或者一些房间，然后去确认房间的功能和你期望的是否一样。它测试了基本的房间功能，然后测试了路径，最后测试了整个地图。

这里最重要的函数时` assert_equal `，它保证了你设置的变量，以及你在Room 里设置的路径和你的期望相符。如果你得到错误的结果的话，Ruby 的` Test::Unit `模块将会印出一个错误信息，这样你就可以找到出错的地方并且修正过来。

测试指南
---------

在写测试代码时，你可以照着下面这些不是很严格的指南来做：

1. 测试脚本要放到` tests/ `目录下，并且命名为` test_NAME.rb `。这样做还有一个好处就是防止测试代码和别的代码互相混淆。 
2. 为你的每一个模块写一个测试。 
3. Test Cast 函数保持简短，但如果看上去不怎么整洁也没关系，Test Cast一般都有点乱。 
4. 就算Test Cast有些乱，也要试着让他们保持整洁，把里边重复的代码删掉。建立一些辅助函数来避免重复的代码。当你下次在改完代码需要改测试的时候，你会感谢我这一条建议的。重复的代码会让修改测试变得很难操作。 
5. 最后一条是别太把测试当做一回事。有时候，更好的方法是把代码和测试全部删掉，然后重新设计代码。 

你应该看到的结果
----------------

```sh
$ ruby test_ex47.rb 
Loaded suite test_ex47
Started
...
Finished in 0.000353 seconds.

3 tests, 7 assertions, 0 failures, 0 errors, 0 skips

Test run options: --seed 63537
That’s what you should see if everything is working right. Try causing an error to see what that looks like and then fix it.
```

加分练习
---------

1. 仔细阅读` Test::Unit `相关的文件，再去了解一下其他的替代方案。 
2. 了解一下` Rspec `，看看它是否可以干得更出色。 
3. 改进你游戏里的 Room，然后用它重建你的游戏。这次重写，你需要一边写代码，一般把单元测试写出来。 


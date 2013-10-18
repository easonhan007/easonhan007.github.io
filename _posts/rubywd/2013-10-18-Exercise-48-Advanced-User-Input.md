---
layout: post
title: "练习48:  更进阶的使用者输入" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

你的游戏可能一路跑得很爽，不过你处理使用者输入的方式肯定让你不胜其烦了。每一个房间都需要一套自己的语句，而且只有使用者完全输入正确后才能执行。你需要一个设备，它可以允许使用者以各种方式输入语汇。例如下面的几种表述都应该被支援才对：

* open door 
* open the door 
* go THROUGH the door 
* punch bear 
* Punch The Bear in the FACE 

也就是说，如果使用者的输入和常用英语很接近也应该是可以的，而你的游戏要识别出它们的意思。为了达到这个目的，我们将写一个模块专门做这件事情。这个模块里边会有若干个类，它们互相配合，接受使用者输入，并且将使用者输入转换成你的游戏可以识别的命令。

英语的简单格式是这个样子的：

* 单词由空格隔开。 
* 句子由单词组成。 
* 语法控制句子的含义。 

所以最好的开始方式是先搞定如何得到使用者输入的词汇，并且判断出它们是什么。

我们的游戏语汇
---------------

我在游戏里建立了下面这些语汇：

* 表示方向: north, south, east, west, down, up, left, right, back. 
* 动词: go, stop, kill, eat. 
* 修饰词: the, in, of, from, at, it 
* 名词: door, bear, princess, cabinet. 
* 数字词: 由 0-9 构成的数字。 

说到名词，我们会碰到一个小问题，那就是不一样的房间会用到不一样的一组名词，不过让我们先挑一小组出来写程式，以后再做改进吧。

如何断句
--------

我们已经有了词汇表，为了分析句子的意思，接下来我们需要找到一个断句的方法。我们对于句子的定义是「空格隔开的单词」，所以只要这样就可以了：

```sh
stuff = gets.chomp()
words = stuff.split()
```

目前做到这样就可以了，不过这招在相当一段时间内都不会有问题。

语汇结构
--------

一旦我们知道了如何将句子转化成词汇列表，剩下的就是逐一检查这些词汇，看它们是什么类型。为了达到这个目的，我们将用到一个非常便利的 Ruby 资料结构「struct」。「struct」其实就是一个可以把一串的 attrbutes 绑在一起的方式，使用 accessor 函数，但不需要写一个复杂的 class。它的建立方式就像这样：

```sh
Pair = Struct.new(:token, :word)
first_word = Pair.new("direction", "north")
second_word = Pair.new("verb", "go")
sentence = [first_word, second_word]
```

这建立了一对 (TOKEN, WORD) 可以让你看到 word 和在里面做事。

这只是一个例子，不过最后做出来的样子也差不多。你接受使用者输入，用split 将其分隔成单词列表，然后分析这些单词，识别它们的类型，最后重新组成一个句子。

扫描输入资料
-------------

现在你要写的是词汇扫描器。这个扫描器会将使用者的输入字符串当做参数，然后返回由多个(TOKEN, WORD) struct 组成的列表，这个列表实现类似句子的功能。如果一个单词不在预定的词汇表中，那它返回时 WORD 应该还在，但TOKEN 应该设置成一个专门的错误标记。这个错误标记将告诉使用者哪里出错了。

有趣的地方来了。我不会告诉你这些该怎样做，但我会写一个「单元测试(unit test)」，而你要把扫描器写出来，并保证单元测试能够正常通过。

Exceptions And Numbers
-------------------------

有一件小事情我会先帮帮你，那就是数字转换。为了做到这一点，我们会作一点弊，使用「异常(exceptions)」来做。「异常」指的是你运行某 个函数时得到的错误。你的函数在碰到错误时，就会「提出(raise)」一个「异常」，然后你就要去处理(handle)这个异常。假如你在 IRB 里写了这些东西：

```sh
ruby-1.9.2-p180 :001 > Integer("hell")
ArgumentError: invalid value for Integer(): "hell"
    from (irb):1:in `Integer'
    from (irb):1
    from /home/rob/.rvm/rubies/ruby-1.9.2-p180/bin/irb:16:in `<main>'
```

这个 ArgumentError 就是 Integer() 函数抛出的一个异常。因为你给Integer() 的参数不是一个数字。Integer()函数其实也可以传回一个值来告诉你它碰到了错误，不过由于它只能传回整数值，所以很难做到这一点。它不能返回-1，因为这也是一个数字。 Integer()没有纠结在它「究竟应该返回什么」上面，而是提出了一个叫做TypeError的异常，然后你只要处理这个异常就可以了。

处理异常的方法是使用 begin 和 rescue 这两个关键字：

```sh
def convert_number(s)
  begin
    Integer(s)
  rescue ArgumentError
    nil
  end
end
```

你把要试着运行的程式码放到「begin」的区段里，再将出错后要运行的程式码放到「except」区段里。在这里，我们要试着呼叫 Integer() 去处理某个可能是数字的东西，如果中间出了错，我们就「rescue」这个错误，然后返回 「nil」。

在你写的扫描器里面，你应该使用这个函数来测试某个东西是不是数字。做完这个检查，你就可以声明这个单词是一个错误单词了。

What You Should Test
---------------------

这里是你应该使用的测试文件 test/test_lexicon.rb:

```sh
require 'test/unit'
require_relative "../lib/lexicon"

class LexiconTests < Test::Unit::TestCase

  Pair = Lexicon::Pair
  @@lexicon = Lexicon.new()

  def test_directions()
    assert_equal([Pair.new(:direction, 'north')], @@lexicon.scan("north"))
    result = @@lexicon.scan("north south east")
    assert_equal(result, [Pair.new(:direction, 'north'),
                 Pair.new(:direction, 'south'),
                 Pair.new(:direction, 'east')])
  end

  def test_verbs()
    assert_equal(@@lexicon.scan("go"), [Pair.new(:verb, 'go')])
    result = @@lexicon.scan("go kill eat")
    assert_equal(result, [Pair.new(:verb, 'go'),
                 Pair.new(:verb, 'kill'),
                 Pair.new(:verb, 'eat')])
  end

  def test_stops()
    assert_equal(@@lexicon.scan("the"), [Pair.new(:stop, 'the')])
    result = @@lexicon.scan("the in of")
    assert_equal(result, [Pair.new(:stop, 'the'),
                 Pair.new(:stop, 'in'),
                 Pair.new(:stop, 'of')])
  end

  def test_nouns()
    assert_equal(@@lexicon.scan("bear"), [Pair.new(:noun, 'bear')])
    result = @@lexicon.scan("bear princess")
    assert_equal(result, [Pair.new(:noun, 'bear'),
                 Pair.new(:noun, 'princess')])
  end

  def test_numbers()
    assert_equal(@@lexicon.scan("1234"), [Pair.new(:number, 1234)])
    result = @@lexicon.scan("3 91234")
    assert_equal(result, [Pair.new(:number, 3),
                 Pair.new(:number, 91234)])
  end

  def test_errors()
    assert_equal(@@lexicon.scan("ASDFADFASDF"), [Pair.new(:error, 'ASDFADFASDF')])
    result = @@lexicon.scan("bear IAS princess")
    assert_equal(result, [Pair.new(:noun, 'bear'),
                 Pair.new(:error, 'IAS'),
                 Pair.new(:noun, 'princess')])
  end

end
```

记住你要使用你的项目骨架来建立新项目项目，将这个 Test Case 写下来（不许复制贴上！），然后编写你的扫描器，直至所有的测试都能通过。注意细节并确认结果一切工作良好。

设计提示
----------

集中一次实现一个测试，尽量保持简单，只要把你的 lexicon.rb 词汇表中所有的单词放那里就可以了。不要修改输入的单词表，不过你需要建立自己的新列表，里边包含你的语汇元组。另外，记得使用 include? 函数来检查这些语汇阵列，以确认某个单词是否在你的语汇表中。

加分练习
--------

1. 改进单元测试，让它复盖到更多的语汇。 
2. 向语汇列表添加更多的语汇，并且更新单元测试程式码。 
3. 让你的扫描器能够识别任意大小写的词汇。更新你的单元测试以确认其功能。 
4. 找出另外一种转换为数字的方法。 
5. 我的解决方案用了37 行程式码，你的是更长还是更短呢？ 


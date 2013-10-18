---
layout: post
title: "练习25: 更多更多的练习"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

我们将做一些关于函式和变量的练习，以确认你真正掌握了这些知识。这节练习对你来说可以说是一本道：写程序，逐行研究，弄懂它。
不过这节练习还是有些不同，你不需要执行它，取而代之，你需要将它导入到 Ruby 通过自己执行函式的方式运行。

```sh
module Ex25
  def self.break_words(stuff)
    # This function will break up words for us.
    words = stuff.split(' ')
    words
  end

  def self.sort_words(words)
    # Sorts the words.
    words.sort()
  end

  def self.print_first_word(words)
    # Prints the first word and shifts the others down by one.
    word = words.shift()
    puts word
  end

  def self.print_last_word(words)
    # Prints the last word after popping it off the end.
    word = words.pop()
    puts word
  end

  def self.sort_sentence(sentence)
    # Takes in a full sentence and returns the sorted words.
    words = break_words(sentence)
    sort_words(words)
  end

  def self.print_first_and_last(sentence)
    # Prints the first and last words of the sentence.
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
  end

  def self.print_first_and_last_sorted(sentence)
    # Sorts the words then prints the first and last one.
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
  end
end
```

首先以正常的方式``` ruby ex25.rb ```运行，找出里面的错误，并把它们都改正过来。然后你需要接着下面的答案章节完成这节练习。

你应该看到的结果
----------------

这节练习我们将在你之前用来做算术的 Ruby 编译器(IRB)里，用交互的方式和你的.rb 作交流。

这是我做出来的样子：

```sh
$ irb
irb(main):001:0> require './ex25'
=> true
irb(main):002:0> sentence = "All good things come to those who wait."
=> "All good things come to those who wait."
irb(main):003:0> words = Ex25.break_words(sentence)
=> ["All", "good", "things", "come", "to", "those", "who", "wait."]
irb(main):004:0> sorted_words = Ex25.sort_words(words)
=> ["All", "come", "good", "things", "those", "to", "wait.", "who"]
irb(main):005:0> Ex25.print_first_word(words)
All
=> nil
irb(main):006:0> Ex25.print_last_word(words)
wait.
=> nil
irb(main):007:0> Ex25.wrods
NoMethodError: undefined method `wrods' for Ex25:Module
        from (irb):6
irb(main):008:0> words
=> ["good", "things", "come", "to", "those", "who"]
irb(main):009:0> Ex25.print_first_word(sorted_words)
All
=> nil
irb(main):010:0> Ex25.print_last_word(sorted_words)
who
=> nil
irb(main):011:0> sorted_words
=> ["come", "good", "things", "those", "to", "wait."]
irb(main):012:0> Ex25.sort_sentence(sentence)
=> ["All", "come", "good", "things", "those", "to", "wait.", "who"]
irb(main):013:0> Ex25.print_first_and_last(sentence)
All
wait.
=> nil
irb(main):014:0> Ex25.print_first_and_last_sorted(sentence)
All
who
=> nil
irb(main):015:0> ^D
$
```

我们来逐行分析一下每一步实现的是什么：

1. 在第 2 行你 require 了自己的``` ./ex25.rb Ruby ```文件，和你做过的其他 require 一样＄。在 require 的时候你不需要加``` .rb ```后缀。这个过程里，你将这个文件当做了一个``` module ```(模块)来使用，你在这个模块里定义的函式也可以直接引用出来。 
2. 第 4 行你创造了一个用来处理的``` sentence ```(句子)。 
3. 第 6 行你使用了``` Ex25 ```模块引用了你的第一个函式``` Ex25.break_words ```。其中的 . (dot, period) 符号可以告诉 Ruby：「Hi，我要执行``` Ex25 ```里的那个叫``` break_word ```的函式！」 
4. 第 8 行我们只是输入``` Ex25.sort_words ```来得到一个排序过的句子。 
5. 10-15 行我们使用``` Ex25.print_first_word ```和``` Ex25.print_last_word ```将第一个和最后一个词打印出来。 
6. 第 16 行比较有趣。我把``` words ```变量写错成了``` wrods ```，所以 Ruby 在 17-18 行给了一个错误信息。 
7. 第 19-20 行我们打印出了修改过后的词汇列表。第一个和最后一个词我们已经打印过了，所以在这里没有再打印出来。 
8. 剩下的行你需要自己分析一下，就留作你的加分练习了。 

加分练习
---------
1. 研究答案中没有分析过的行，找出它们的来龙去脉。确认自己明白了自己使用的是模块 Ex25 中定义的函式。 
2. 我们将我们的函式放在一个``` module ```里式因为他们拥有自己的 命名空间 (namespace)。这样如果有其他人写了一个函式也叫``` break_words ```，这样就不会发生碰创。无论如何，输入``` Ex25 ```. 是一件很烦人的事。有一个比较方便的作法，你可以输入``` include Ex25 ```，这相当于说：「我要将所有 Ex25 这个 mudle 里的所有东西 include 到我现在的 module 里。」 
3. 试着在你正在使用 IRB 时，弄烂文件会发生什么事。你可能要执行 CTRL-D ( Windows下是CTRL-Z ) 才能把 IRB 关掉 reload 一次。 


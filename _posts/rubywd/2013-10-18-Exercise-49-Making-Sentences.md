---
layout: post
title: "练习49:  创造句子" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

从我们这个小游戏的词汇扫描器中，我们应该可以得到类似下面的列表（你的看起来可能格式会不太一样）：

```sh
ruby-1.9.2-p180 :003 > print Lexicon.scan("go north")
[#<struct Lexicon::Pair token=:verb, word="go">,
    #<struct Lexicon::Pair token=:direction, word="north">] => nil 
ruby-1.9.2-p180 :004 > print Lexicon.scan("kill the princess")
[#<struct Lexicon::Pair token=:verb, word="kill">,
    #<struct Lexicon::Pair token=:stop, word="the">,
    #<struct Lexicon::Pair token=:noun, word="princess">] => nil
ruby-1.9.2-p180 :005 > print Lexicon.scan("eat the bear")
[#<struct Lexicon::Pair token=:verb, word="eat">,
    #<struct Lexicon::Pair token=:stop, word="the">,
    #<struct Lexicon::Pair token=:noun, word="bear">] => nil 
ruby-1.9.2-p180 :006 > print Lexicon.scan("open the door and smack the bear in the nose")
[#<struct Lexicon::Pair token=:error, word="open">,
    #<struct Lexicon::Pair token=:stop, word="the">, 
    #<struct Lexicon::Pair token=:noun, word="door">, 
    #<struct Lexicon::Pair token=:error, word="and">, 
    #<struct Lexicon::Pair token=:error, word="smack">, 
    #<struct Lexicon::Pair token=:stop, word="the">, 
    #<struct Lexicon::Pair token=:noun, word="bear">, 
    #<struct Lexicon::Pair token=:stop, word="in">, 
    #<struct Lexicon::Pair token=:stop, word="the">, 
    #<struct Lexicon::Pair token=:error, word="nose">] => nil 
ruby-1.9.2-p180 :007 >
```

现在让我们把它转化成游戏可以使用的东西，也就是一个 Sentence 类。

如果你还记得学校学过的东西的话，一个句子是由这样的结构组成的：

> 主语(Subject) + 谓语(动词Verb) + 宾语(Object)

很显然实际的句子可能会比这复杂，而你可能已经在英语的语法课上面被折腾得够呛了。我们的目的，是将上面的 struct 列表转换为一个 Sentence 对象，而这个对象又包含主谓宾各个成员。

匹配(Match) And 窥视(Peek)
----------------------------

为了达到这个效果，你需要四样工具：

1. 一个循环存取 struct 列表的方法，这挺简单的。 
2. 「匹配」我们的主谓宾设置中不同种类 struct 的方法。 
3. 一个「窥视」潜在struct的方法，以便做决定时用到。 
4. 「跳过(skip)」我们不在乎的内容的方法，例如形容词、冠词等没有用处的词汇。 
5. 我们使用 peek 函数查看 struct 列表中的下一个成员，做匹配以后再对它做下一步动作。让我们先看看这个 peek 函数： 

```sh
def peek(word_list)
  begin
    word_list.first.token
  rescue
    nil
  end
end
```

很简单。再看看 match 函数：

```sh
def match(word_list, expecting)
  begin
    word = word_list.shift
    if word.token == expecting
      word
    else
      nil
    end
  rescue
    nil
  end
end
```

还是很简单，最后我们看看 skip 函数:

```sh
def skip(word_list, word_type)
  while peek(word_list) == word_type
    match(word_list, word_type)
  end
end
```

以你现在的水准，你应该可以看出它们的功能来。确认自己真的弄懂了它们。

句子的语法
----------

有了工具，我们现在可以从 struct 列表来构建句子(Sentence)对象了。我们的处理流程如下：

1. 使用` peek `识别下一个单词。 
2. 如果这个单词和我们的语法匹配，我们就调用一个函数来处理这部分语法。假设函数的名字叫` parse_subject `好了。 
3. 如果语法不匹配，我们就` raise `一个错误，接下来你会学到这方面的内容。 
4. 全部分析完以后，我们应该能得到一个 Sentence 对象，然后可以将其应用在我们的游戏中。 

演示这个过程最简单的方法是把代码展示给你让你阅读，不过这节练习有个不一样的要求，前面是我给你测试代码，你照着写出代码来，而这次是我给你的程序，而你要为它写出测试代码来。

以下就是我写的用来解析简单句子的代码，它使用了` ex48 `这个 Lexicon class。

```sh
class ParserError < Exception

end

class Sentence

  def initialize(subject, verb, object)
    # remember we take Pair.new(:noun, "princess") structs and convert them
    @subject = subject.word
    @verb = verb.word
    @object = object.word
  end

end

def peek(word_list)
  begin
    word_list.first.token
  rescue
    nil
  end
end

def match(word_list, expecting)
  begin
    word = word_list.shift
    if word.token == expecting
      word
    else
      nil
    end
  rescue
    nil
  end
end

def skip(word_list, token)
  while peek(word_list) == token
    match(word_list, token)
  end
end

def parse_verb(word_list)
  skip(word_list, :stop)

  if peek(word_list) == :verb
    return match(word_list, :verb)
  else
    raise ParserError.new("Expected a verb next.")
  end
end

def parse_object(word_list)
  skip(word_list, :stop)
  next_word = peek(word_list)

  if next_word == :noun
    return match(word_list, :noun)
  end
  if next_word == :direction
    return match(word_list, :direction)
  else
    raise ParserError.new("Expected a noun or direction next.")
  end
end

def parse_subject(word_list, subj)
  verb = parse_verb(word_list)
  obj = parse_object(word_list)

  return Sentence.new(subj, verb, obj)
end

def parse_sentence(word_list)
  skip(word_list, :stop)

  start = peek(word_list)

  if start == :noun
    subj = match(word_list, :noun)
    return parse_subject(word_list, subj)
  elsif start == :verb
    # assume the subject is the player then
    return parse_subject(word_list, Pair.new(:noun, "player"))
  else
    raise ParserError.new("Must start with subject, object, or verb not: #{start}")
  end
end
```

关于异常(Exception)
--------------------

你已经简单学过关于异常的一些东西，但还没学过怎样抛出(raise)它们。这节的代码示范了如何 raise。首先在最前面，你要定义好` ParserException `这个类，而它又是` Exception `的一种。另外要注意我们是怎样使用` raise `这个关键字来抛出异常的。

你的测试代码应该也要测试到这些异常，这个我也会示范给你如何实现。

你应该测试的东西
------------------

为《练习49》写一个完整的测试方案，确认代码中所有的东西都能正常工作，其中异常的测试——输入一个错误的句子它会抛出一个异常来。

使用` assert_raises `这个函数来检查异常，在 Test::Unit 的文件里查看相关的内容，学着使用它写针对「执行失败」的测试，这也是测试很重要的一个方面。从文件中学会使用` assert_raises `，以及一些别的函数。

写完测试以后，你应该就明白了这段代码的运作原理，而且也学会了如何为别人的代码写测试代码。相信我，这是一个非常有用的技能。

加分练习
-----------

1. `修改 parse_ method `，将它们放到一个类里边，而不仅仅是独立的方法函数。这两种设计你喜欢哪一种呢？ 
2. 提高parser 对于错误输入的抵御能力，这样即使使用者输入了你预定义语汇之外的词语，你的代码也能正常运行下去。 
3. 改进语法，让它可以处理更多的东西，例如数字。 
4. 想想在游戏里你的 Sentence 类可以对使用者输入做哪些有趣的事情。 


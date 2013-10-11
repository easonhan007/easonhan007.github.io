---
layout: post
title: "习题1 第一个程序"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}


你应该在习题 0 中花了不少的时间，学会了如何安装文字编辑器、执行文字编辑器、以及如何运行 Terminal，如果你还没这么做的话，请别继续往前走，之后会有很多苦头的。请不要跳过前一个习题的内容继续前进，这也是本书唯一的一次在习题开头就做这样的警告。

```sh
puts "Hello World!"
puts "Hello Again"
puts "I like typing this."
puts "This is fun."
puts 'Yay! Printing.'
puts "I'd much rather you 'not'."
puts 'I "said" do not touch this.'
```

将上面的内容写到一个档案中，取名为``` ex1.rb ```。注意这样的命名方式，Ruby 文件最好以``` .rb ```结尾。

然后你需要在 Terminal 中输入以下内容来执行这段程序：
```sh
ruby ex1.rb
```

如果你写对了的话，你应该看到和下面一样的内容。如果不一样，那就是你弄错了什么东西。不是电脑有问题，电脑没问题。

你应该看到的内容
----------------
```sh
$ ruby ex1.rb
Hello World!
Hello Again
I like typing this.
This is fun.
Yay! Printing.
"'d much rather you 'not'."
I "said" do not touch this.
$ 
```

你也许会看到 $ 前面会显示你所在的目录的名称，这部是问题，但如果你的输出不一样的话，你需要找出为什么会不一样，然后把你的程序改对。
如果你看到类似如下的错误信息:

```sh
ruby ex1.rb
ex1.rb:4: syntax error, unexpected tCONSTANT, expecting $end
puts "This is fun."
          ^
```

看懂这些内容对你来说是很重要的。因为你以后还会犯类似的错误。就是我现在也会犯这样的错误。让我们一行一行来看。

1. 首先我们在 Terminal 输入命令来执行``` ex1.rb ```脚本。 
2. Ruby 告诉我们``` ex1.rb ```档案的第 4 行有一个错误。 
3. 然后这一行的内容被打印了出来。 
4. 然后 Ruby 打印出了一个``` ^ ```(插入符号，caret) 符号，用来指示错误的位置。 
5. 最后，它打印出了一行「语法错误(SyntaxError)」告诉你究竟是发生了怎么样的错误。通常这些错误资讯都非常的难懂，不过你可以把错误资讯的内容复制到搜寻引擎里，然后你就能看到别人也遇到过这样的错误，而且你也许能搞清楚怎样解决这个问题。 

加分习题
--------

你还会有加分习题需要完成。加分习题里面的内容是供你尝试的。如果你觉得做不出来，你可以暂时跳过， 过段时间再回来做。

在这个练习中，试试这些东西：

1. 让你的脚本再多打印一行。 
2. 让你的脚本只打印其中的一行。 
3. 在一行的开始位置放置一个 # (octothorpe) 符号。它的作用是什么？自己研究一下。 
4. 从现在开始，除非特别情况，我将不再解释每个习题的运作原理了。 

> Note: 井号有很多的英文代称，例如「octothorpe ( 八角帽 )」」、「pound( 英镑符号 )」、「hash( 电话的 # 键 )」、「mesh ( 网 )」。


---
layout: post
title: "练习15: 读取文件"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

你已经学过了``` STDIN.gets ```和``` ARGV ```，这些是你开始学习读取文件的必备基础。你可能需要多多实验才能明白它的运作原理，所以你要细心练习，并且仔细检查结果。处理文件需要非常仔细，如果不仔细的话，你可能会把有用的文件弄坏或者清空。导致前功尽弃。

这节练习涉及到写两个文件。一个正常的``` ex15.rb ```文件，另外一个是``` ex15_sample.txt ```，第二个文件并不是脚本，而是供你的脚本读取的文字文件。以下是后者的内容：

```sh
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
```

我们要做的是把该文件用我们的脚本「打开(open)」，然后打印出来。然而把文件名``` ex15_sample.txt ```「写死(Hard Coding」在程序代码不是一个好主意，这些数据应该是使用者输入的才对。如果我们碰到其他文件要处理，写死的文件名就会给你带来麻烦了。解决方案是使用``` ARGV ```和``` STDIN.gets ```来从使用者端获取数据，从而知道哪些文件该被处理。

```sh
filename = ARGV.first

prompt = "> "
txt = File.open(filename)

puts "Here's your file: #{filename}"
puts txt.read()

puts "Type the filename again:"
print prompt
file_again = STDIN.gets.chomp()

txt_again = File.open(file_again)

puts txt_again.read()
```

这个脚本中有一些新奇的玩意，我们来快速地过一遍：

程序代码的 1-3 行使用``` ARGV ```来获取文件名，这个你已经熟悉了。接下来第 4 行我们使用一个新的命令 File.open。现在请在命令列执行``` ri File.open ```来读读它的说明。注意到这多像你的脚本，它接收一个参数，并且传回一个值，你可以将这个值赋予一个变数。这就是你打开文件的过程。

第 6 行我们打印出了一小行，但在第 7 行我们看到了新奇的东西。我们在``` txt ```上引入了一个函式。你从``` open ```获得的东西是一个``` file ```（文件），文件本身也支援一些命令。它接受命令的方式是使用句点 . (dot or period)，紧跟着你的命令，然后参数。就像``` File.open ```做的事一样。差别是：当你说``` txt.read() ```时，你的意思其实是：「嘿 txt！执行你的 read 命令，无需任何参数！」

脚本剩下的部份基本差不多，不过我就把剩下的分析作为加分练习留给你自己了。

你应该看到的结果
----------------

我的脚本叫 “ex15_sample.txt”，以下是执行结果：

```sh
$ ruby ex15.rb ex15_sample.txt 
Here's your file 'ex15_sample.txt':
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

I'll also ask you to type it again:
> ex15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

$
```

加分练习
--------

这节的难度跨越有点大，所以你要尽量做好这节加分练习，然后再继续后面的章节。
1. 在每一行的上面用注释说明这一行的用途。 
2. 如果你不确定答案，就问别人，或者是上网搜寻。大部分时候，只要搜寻「ruby 你要搜寻的东西」，就能得到你要的答案。比如搜寻一下「ruby file.open」。 
3. 我使用了「命令」这个词，不过实际上他们的名字是「函式(function)」和「方法(method)」。上网搜寻一下这两者的意义和区别。看不懂也没关系，迷失在其他程式设计师的知识海洋里是很正常的一件事。 
4. 删掉 9-15 行使用到``` STDIN.gets ```的部份，再执行一次脚本。 
5. 只用``` STDIN.gets ```撰写这个脚本，想想哪种得到文件名的方法更好，以及为什么。 
6. 执行``` ri File ```然后往下卷动直到看见``` read() ```命令（函式/方法）。看到很多其他的命令了吧。你可以玩其他试试。 
7. 再次启动 IRB，然后在里面使用``` File.open ```打开一个文件，这种 open 和 read 的方法也值得一学。 
8. 让你的脚本针对``` txt ```和``` txt_again ```变数执行一下``` close() ```，处理完文件后你需要将其关闭，这是很重要的一点。 


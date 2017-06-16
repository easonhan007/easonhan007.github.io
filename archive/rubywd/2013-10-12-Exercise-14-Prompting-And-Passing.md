---
layout: post
title: "练习14: 提示和传递"
description: "笨方法学ruby"
category: ruby
tags: ruby[]
---
{% include JB/setup %}

让我们使用``` ARGV ```和``` gets.chomp ```一起来向使用者提一些特别的问题。下一节练习你将会学习到如何读写文件，这节练习是下节的基础。在这道练习里我们将用一个简单的``` > ```作为提示符号。这和一些游戏中的方法类似，例如 Zork 或者 Adventure 这两款游戏。

```sh
user = ARGV.first
prompt = '> '

puts "Hi #{user}, I'm the #{$0} script."
puts "I'd like to ask you a few questions."
puts "Do you like me #{user}?"
print prompt
likes = STDIN.gets.chomp()

puts "Where do you live #{user}?"
print prompt
lives = STDIN.gets.chomp()

puts "What kind of computer do you have?"
print prompt
computer = STDIN.gets.chomp()

puts <<MESSAGE
Alright, so you said #{likes} about liking me.
You live in #{lives}.  Not sure where that is.
And you have a #{computer} computer.  Nice.
MESSAGE
```

注意到我们将用户提示符号设置为``` prompt ```，这样我们就不用每次都要重打一遍了。如果你要将提示符号和修改成别的字串，你只要改一个地方就可以了。

非常顺手吧。

> Important: 同时必须注意的是，我们也用了``` STDIN.gets ```取代了``` gets ```。这是因为如果有东西在``` ARGV ```里，标准的 ```gets ```会认为将第一个参数当成文件而尝试从里面读东西。在要从使用者的输入（如``` stdin ```）读取资料的情况下我们必须明确地使用``` STDIN.gets ```。

你应该看到的结果
----------------

当你执行这个脚本时，记住你需要把你的名字传给这个脚本，让``` ARGV ```可以接收到。

```sh
$ ruby ex14.rb Zed
Hi Zed, I'm the ex14.rb script.
I'd like to ask you a few questions.
Do you like me Zed?
> yes
Where do you live Zed?
> America
What kind of computer do you have?
> Tandy

Alright, so you said 'yes' about liking me.
You live in 'America'.  Not sure where that is.
And you have a 'Tandy' computer.  Nice.
```

加分练习
---------

1. 查一下 Zork 和 Adventure 是两个怎样的游戏。看能不能抓到，然后玩玩看。 
2. 将``` prompt ```变数改为完全不同的内容再执行一遍。 
3. 给你的脚本再新增一个参数，让你的程式用到这个参数。 
4. 确认你弄懂了我如何结合``` <<SOMETHING ```形式的多行字串与``` #{} ```字串注入做的打印。 


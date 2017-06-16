---
layout: post
title: "练习16: 读写文件"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

如果你做了上一个练习的加分练习，你应该已经了解了个种文件相关的命令（方法/函式）。你应该记住的命令如下：

* close – 关闭文件。跟你编辑器的``` 文件->储存.. ```是一样的意思。 
* read – 读取文件内容。你可以把结果赋给一个变量。 
* readline – 读取文件文字中的一行。 
* truncate – 清空文件，请小心使用该命令。 
* write(stuff) – 将 stuff 写入文件。 

这是你现在应该知道的重要命令。有些命令需要接收参数，但这对我们并不重要。你只要记住 write 的用法就可以了。``` write ```需要接收一个字符串作为参数，从而将该字符串写入文件。

让我们来使用这些命令做一个简单的文字编辑器吧：

```sh
filename = ARGV.first
script = $0

puts "We're going to erase #{filename}."
puts "If you don't want that, hit CTRL-C (^C)."
puts "If you do want that, hit RETURN."

print "? "
STDIN.gets

puts "Opening the file..."
target = File.open(filename, 'w')

puts "Truncating the file.  Goodbye!"
target.truncate(target.size)

puts "Now I'm going to ask you for three lines."

print "line 1: "; line1 = STDIN.gets.chomp()
print "line 2: "; line2 = STDIN.gets.chomp()
print "line 3: "; line3 = STDIN.gets.chomp()

puts "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

puts "And finally, we close it."
target.close()
```

这是一个大文件，大概是你输入过的最大的文件。所以慢慢来，仔细检查，让它能够跑起来。有一个小技巧就是你可以让你的脚本一部分一部分地跑起来。先写 1-8 行，让它能跑起来，再多做 5 行，再接着几行，以此类推，直到整个脚本都可以跑起来为止。

你应该看到的结果
----------------

你将看到两样东西，一样是你新脚本的输出：

```sh
$ ruby ex16.rb test.txt
We're going to erase 'test.txt'.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
?
Opening the file...
Truncating the file.  Goodbye!
Now I'm going to ask you for three lines.
line 1: To all the people out there.
line 2: I say I don't like my hair.
line 3: I need to shave it off.
I'm going to write these to the file.
And finally, we close it.
$
```

这是一个大文件，大概是你输入过的最大的文件。所以慢慢来，仔细检查，让它能够跑起来。有一个小技巧就是你可以让你的脚本一部分一部分地跑起来。先写 1-8 行，让它能跑起来，再多做 5 行，再接着几行，以此类推，直到整个脚本都可以跑起来为止。

加分练习
--------

1. 如果你觉得自己没有弄懂的话，用我们的老方法，在每一行之前加上注释，为自己理清思路。就算不能理清思路，你也可以知道自己究竟具体哪里没弄清楚。 
2. 写一个和上一个练习类似的脚本，使用``` read ```和``` ARGV ``` 读取你刚才新建立的文件。 
3. 文件中重复的地方太多了。试着用一个``` target.write() ```将``` line1 ```，``` line2 ```，``` line3 ```印出来，你可以使用字符串、格式化字符串以及跳脱字符串。 
4. 找出为什么我们打开文件时要使用 w 模式，而你真的需要``` target.truncate() ```吗？去看 Ruby 的``` File.open ```函式找答案吧。 


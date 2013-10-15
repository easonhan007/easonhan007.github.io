---
layout: post
title: "练习17: 更多文件操作"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

现在让我们再学习几种文件操作。我们将编写一个 Ruby 脚本，将一个文件中的内容拷贝到另一个文件中。这个脚本很短，不过它会让你对于文件操作有更多的了解。

```sh
from_file, to_file = ARGV
script = $0

puts "Copying from #{from_file} to #{to_file}"

# we could do these two on one line too, how?
input = File.open(from_file)
indata = input.read()

puts "The input file is #{indata.length} bytes long"

puts "Does the output file exist? #{File.exists? to_file}"
puts "Ready, hit RETURN to continue, CTRL-C to abort."
STDIN.gets

output = File.open(to_file, 'w')
output.write(indata)

puts "Alright, all done."

output.close()
input.close()
```

你应该注意到了我们使用了一个很好用的函式``` File.exists? ```。运作原理是将文件名字符串当做一个参数传入，如果文件存在的话，它会传回``` true ```，如果不存在的话就传回``` false ```。之后在这本书中，我们将会使用这个函式做更多的事情。

你应该看到的结果
----------------

如同你前面所写的脚本，运行该脚本需要两个参数，一个是待拷贝的文件位置，一个是要拷贝至的文件位置。如果我们使用以前的``` test.txt ```我们将看到如下的结果：

```sh
$ ruby ex17.rb test.txt copied.txt
Copying from test.txt to copied.txt
The input file is 81 bytes long
Does the output file exist? False
Ready, hit RETURN to continue, CTRL-C to abort.

Alright, all done.

$ cat copied.txt
To all the people out there.
I say I don't like my hair.
I need to shave it off.
$
```

该命令对于任何文件应该都是有效的。试试操作一些别的文件看看结果。不过当心别把你的重要文件给弄坏了。

> Warning: 你看到我用``` cat ```这个指令了吧？它只能在 Linux 和 OX 下使用，Windows 用户可以使用``` type ```做到相同效果。

加分练习
--------

1. 再多读读和``` require ```相关的资料，然后将 IRB 跑起来，试试 require 一些东西看能不能摸出门到。当然，即使搞不清楚也没关系。 
2. 这个脚本实在有点烦人。没必要再拷贝之前都问一遍吧，没必要在屏幕上输出那么多东西。试着删掉脚本的一些功能，使它用起来更友善。 
3. 看看你能把这个脚本改到多短，我可以把它写成一行。 
4. 我使用了一个叫``` cat ```的东西，这个古老的命令用处是将两个文件「连接(concatenate）」在一起，不过实际上它最大的用处是印出打文件内容到屏幕是。你可以通过``` man cat ```命令了解到更多资讯。 
5. 使用 Windows 的人，你们可以给自己找一个``` cat ```的替代品。关于``` man ```的东西就别想太多了。Windows 下没这个指令。 
6. 找出为什么需要在程式码中写``` output.close() ```的原因。 


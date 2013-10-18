---
layout: post
title: "练习20: 函式和文件"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

回忆一下函式的要点，然后一边做这节练习，一边注意一下函式和文件是如何一起协作发挥作用的。

```sh
input_file = ARGV[0]

def print_all(f)
  puts f.read()
end

def rewind(f)
  f.seek(0, IO::SEEK_SET)
end

def print_a_line(line_count, f)
  puts "#{line_count} #{f.readline()}"
end

current_file = File.open(input_file)

puts "First let's print the whole file:"
puts # a blank line

print_all(current_file)

puts "Now let's rewind, kind of like a tape."

rewind(current_file)

puts "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
```

特别注意一下，每次运行``` print_a_line ```时，我们是怎样传递当前的行号数据的。

你应该看到的结果
----------------

```sh
$ ruby ex20.rb test.txt
First let's print the whole file:

To all the people out there.
I say I don't like my hair.
I need to shave it off.

Now let's rewind, kind of like a tape.
Let's print three lines:
1 To all the people out there.
2 I say I don't like my hair.
3 I need to shave it off.

$
```

加分练习
--------

1. 通读脚本，在每行之前加上注解，以理解脚本里发生的事情。 
2. 每次``` print_a_line ```运行时，你都传递了一个叫``` current_line ```的变量。在每次调用函数时，打印出``` current_line ```的值，跟踪一下它在``` print_a_line ```中是怎样变成``` line_count ```的。 
3. 找出脚本中每一个用到函式的地方。检查``` def ```一行，确认参数没有用错。 
4. 上网研究一下 file 中的``` seek ```函数是做什么用的。试着运行``` ri file ```看看能不能从``` rdoc ```中学到更多。 
5. 研究一下``` += ```这个简写操作符号的作用，写一个脚本，把这个操作符号用在里边试一下。 


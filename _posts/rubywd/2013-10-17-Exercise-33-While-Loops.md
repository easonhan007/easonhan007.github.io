---
layout: post
title: "练习33: While 循环" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

接下来是一个更在你意料之外的概念：` while-loop `(while循环)。` while `循环会一直执行它下面的代码块，直到它对应的布尔表示式为` false `才会停下来。

等等，你还能跟的上这些术语吧？如果我们写了这样一个语句：` if items > 5 `或者是` for fruit in fruits `，那就是在开始一个代码块 (code block)，新的代码块是需要被缩排的，最后再以 end 语句结尾。只有将代码用这样的方式格式化，Ruby 才能知道你的目的。如果你不太明白这一点，就回去看看 「if 语句」、「函式」和「for 循环」章节，直到你明白为止。

接下来的练习将训练你的大脑去阅读这些结构化的与集，这和我们将布尔表示式刻录到你的大脑中的过程有点类似。

回到` while `循环，它所作的和` if `语句类似，也是去检查一个布尔表示式的真假，不一样的是它下面的代码块不是只被执行一次，而是执行完后再次回到` while `所在的位置，如此重复进行，直到 while 表示式为 false 为止。

` while `循环有一个问题：那就是有时它会永不结束。如果你的目的是循环到宇宙毁灭为止，那这样也挺好的，不过其他的情况下你的回总需要有一个结束点。

为了避免这样的问题，你需要遵循下面的规定：

1. 尽量少用` while `循环，大部分时候` for `循环是更好的选择。 
2. 重复检查你的` while `语句，确定你测试的布尔表示式最终会变成 false。 
3. 如果不确定，就在` while `循环的结尾印出你要测试的值。看看它的变化。 

在这节练习中，你将通过上面的三样事情学会 while 循环：

```sh
i = 0
numbers = []

while i < 6
  puts "At the top i is #{i}"
  numbers.push(i)

  i = i + 1
  puts "Numbers now: #{numbers}"
  puts "At the bottom i is #{i}"
end

puts "The numbers: "

for num in numbers
  puts num
end
```

你应该看到的结果
----------------

```sh
$ ruby ex33.rb
At the top i is 0
Numbers now:  [0]
At the bottom i is 1
At the top i is 1
Numbers now:  [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now:  [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now:  [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now:  [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now:  [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers: 
0
1
2
3
4
5
```

加分练习
--------

1. 将这个 while 循环改成一个函式，将测试条件` (i < 6) `中的 6 换成一个变量。 
2. 使用这个函式重写你的脚本，并使用不同的数字进行测试。 
3. 为函式添加另一个参数，这个参数用来定义第 8 行的` +1 `，这样你就可以让它任意加值了。 
4. 再使用该函式重写一遍这个脚本。看看效果如何。 
5. 接下来使用` for `循环和 range 把这个脚本再写一遍。你还需要中间的加值操作吗？如果你不去掉它，会有什么样的结果？ 

有可能你会碰到程序跑着停不下来了，这时你只要按着 CTRL 再敲 c (CTRL-c)，这样程式就会中断下来了。


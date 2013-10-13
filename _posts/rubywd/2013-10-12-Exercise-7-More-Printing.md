---
layout: post
title: "练习7：更多的打印"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}


现在我们将做一批练习，在练习的过程中你需要输入程式代码，并且让它们运行起来，我不会解释太多，因为这节的内容都是以前熟悉的。这节练习的目的是巩固你学到的东西，我们几轮练习后再见。不要跳过这些练习，不要复制贴上！

```sh
puts "Mary had a little lamb."
puts "Its fleece was white as %s." % 'snow'
puts "And everywhere that Mary went."
puts "." * 10  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# notice how we are using print instead of puts here. change it to puts
# and see what happens.
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12

# this just is polite use of the terminal, try removing it
puts
```

你应该看到的结果

```sh
$ ruby ex7.rb
Mary had a little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
CheeseBurger
$
```

加分练习
--------
接下来几节的加分练习是一样的。

1. 逆向阅读，在每一行的上面加一行注释。 
2. 倒着阅读出来，找出自己的错误。 
3. 从现在开始，把你的错误记录下来，写在一张纸上。 
4. 在开始下一节练习时，阅读一遍你记录下来的错误。并且尽量避免在下个练习中再犯相同的错误。 
5. 记住，每个人都会犯错。程式设计师和魔术师一样，他们希望大家认为他们从不犯错，不过这只是表象而已，他们每时每刻都在犯错。 


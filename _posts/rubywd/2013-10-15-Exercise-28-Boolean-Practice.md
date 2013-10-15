---
layout: post
title: "练习28: 布尔（Boolean）表示式练习"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

上一节你学到的逻辑组合的正式名称是「布尔逻辑表示式(boolean logic expression)」。在程序中，布尔逻辑可以说是无处不在。它们是电脑运算的基础和重要组成部分，掌握它们就跟学音乐掌握音阶一样重要。

在这节练习中，你将在 IRB 里使用到上节学到的逻辑表示式。先为下面的每一个逻辑问题写出你认为的答案，每一题的答案要嘛为 True 要嘛为 False。写完以后，你需要将 IRB 运行起来，把这些逻辑语句输入进去，确认你写的答案是否正确。

```sh
true and true
false and true
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
true and 1 == 1
false and 0 != 0
true or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (true and false)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and not ("testing" == 1 or 1 == 0)
"chunky" == "bacon" and not (3 == 4 or 3 == 3)
3 == 3 and not ("testing" == "testing" or "Ruby" == "Fun")
```

在本节结尾的地方我会给你一个理清复杂逻辑的技巧。

所有的布尔逻辑式都可以用下面的简单流程得到结果：

1. 找到相等判断的部分 (== or !=)，将其改写为其最终值(True 或False)。 
2. 找到括号里的 and/or，先算出它们的值。 
3. 找到每一个 not，算出他们反过来的值。 
4. 找到剩下的 and/or，解出它们的值。 
5. 等你都做完后，剩下的结果应该就是 True 或者 False 了。 

下面我们以 #20 逻辑式示范一下：

`3 != 4 and not ("testing" != "test" or "Ruby" == "Ruby")`

接下来你将看到这个复杂表达式是如何逐级解析为一个单独结果的：

1. 出每一个等值判断: 

* `3 != 4 为 True: true and not ("testing" != "test" or "Ruby" == "Ruby")` 
* `"testing" != "test" 为 True: true and not (true or "Ruby" == "Ruby")` 
* `"Ruby" == "Ruby": true and not (true or true)`
 
2. 找到 () 中的每一个 and/or : 

* `(true or true) is True: true and not (true)`

3. 找到每一个not 并将其逆转: 

* `not (true) is False: true and false`
 
4. 找到剩下的and/or，解出它们的值: 

* `true and false is False`
 
这样我们就解出了它最终的值为 False .

>布尔（Boolean）表示式练习 Warning: 杂的逻辑表达式一开始看上去可能会让你觉得很难。而且你也许已经碰壁过了，不过别灰心，这些「逻辑体操」式的训练只是让你逐渐习惯起来，这样后面你可以轻 易应对程序里边更酷的一些东西。只要你坚持下去，不放过自己做错的地方就行了。如果你暂时不太能理解也没关系，弄懂的时候总会到来的。

你应该看到的结果
----------------

以下内容是在你自己猜测结果以后，通过和 IRB 对话得到的结果：

```sh
$ irb
ruby-1.9.2-p180 :001 > true and true
 => true 
ruby-1.9.2-p180 :002 > 1 == 1 and 2 == 2
 => true
```
 
加分练习
--------

1. Ruby 里还有很多和 `!=`、`==`类似的操作符号。试着尽可能多的列出 Ruby 中的「等价运算符号」。例如 `<` 或是 `<=`。 
2. 写出每一个等价运算符号的名称。例如 `!=` 叫「not equal（不等于」。 
3. 在 IRB 里测试新的布尔逻辑式。在敲 Enter 前你需要喊出它的结果。不要思考，凭自己的第一直觉就可以了。把表达式和结果用笔写下来再敲 Enter，最后看自己做对多少，做错多少。 
4. 把练习 3 那张纸丢掉，以后你不再需要查询它了。

---
layout: post
title: "练习0 准备工作"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}


这道练习并没有程序代码。它的主要目的是让你在电脑上安装好 Ruby，你应该尽量照着指示操作。

这份教学已经预设你将使用 Ruby 1.9.2

你的系统里面可能已经装好了 Ruby。打开 console 并尝试运行:

```sh
$ ruby -v
ruby 1.9.2
```

如果你的系统内并没有 Ruby，不论你使用的是哪一套操作系统，我都强烈建议你使用 [Ruby Version Manager (RVM)](https://rvm.beginrescueend.com/) 安装 Ruby。

Mac OSX
-------

你需要做下列任务来完成这个练习：

1. 用浏览器打开 [http://learnpythonthehardway.org/wiki/ExerciseZero](http://learnpythonthehardway.org/exercise0.html) 下载并安装 ``` gedit ``` 文字编辑器。 
2. 把 ``` gedit ``` 放到桌面或者快速启动列，这样以后你就可以方便使用它了。这两个选项在安装时可以看到。 
a. 执行 gedit （也就是你的编辑器），我们要先改掉一些愚蠢的预设值。 
b. 从 ``` gedit menu ```中打开 ``` Preferences ```，选择``` Editor ```页面。 
c. 将``` Tab width: ```改为 2。 
d. 选择(确认有勾选到该选项)``` Insert spaces instead of tabs ```。 
e. 然后打开 「Automatic indentation」 选项。 
f. 转到``` View ```页面，打开 「Display line numbers」 选项。 
3. 找到 「Terminal」 程序。它的名字是``` Command Promot ```，或者你可以直接执行``` cmd ```。 
4. 为它建立一个捷径，放到桌面或者是快速启动列中以方便使用。 
5. 执行 Terminal，这个程序看上去不怎么地。 
6. 在 Termnal 程序里执行``` irb ```。在 Terminal 中执行程序的方式是输入程序的名称然后再敲一下 Return (Enter)。 
a. 如果你执行``` irb ```但发现不存在(不认得``` irb ```这个指令)。请用 [Ruby Version Manager (RVM)](https://rvm.beginrescueend.com/) 安装 Ruby。 
7. 敲击 CTRL-Z (Z) 退出``` irb ```。 
8. 这样你就应该能回到敲``` irb ```前的提示介面了。如果没有的话自己研究一下为什么。 
9. 学着使用 Terminal 创造一个目录，你可以上网搜寻怎么做。 
10. 学着使用 Terminal 进入一个目录，同样你可以上网搜寻。 
11. 使用你的编辑器在你进入的目录下建立一个档案。你将建立一个档案。使用 「Save」 或者 「Save As…」 选项，然后选择这个目录。 
12. 使用键盘切回到 Terminal  视图，如果不知道怎样使用键盘切换，你一样可以上网搜寻。 
13. 回到 Terminal，看看你能不能使用命令列列出你在目录里新建立的档案，在网路上搜寻怎么列出档案夹里的资料。 
> Note: 如果你在使用 gedit 上有问题，很有可能这是 non-English keyboards layout 造成的，那么我会建议你改使用 [http://www.barebones.com/products/textwrangler/](http://www.barebones.com/products/textwrangler/)。

OSX: 你应该看到的结果
---------------------

以下是我在自己电脑的 Terminal 中练习上述练习时看到的内容。可能会跟你在自己电脑中看的到结果有些不同，所以看看你能不能搞清楚两者的差异。

```sh
Last login: Sat Apr 24 00:56:54 on ttys001
~ $ irb
ruby-1.9.2-p180 :001 >
ruby-1.9.2-p180 :002 > ^D
~ $ mkdir mystuff
~ $ cd mystuff
mystuff $ ls
# ... Use Gedit here to edit test.txt....
mystuff $ ls
test.txt
mystuff $
```

Windows
-------

> Note: Contributed by zhmark.

1. 用浏览器打开 [http://learnpythonthehardway.org/wiki/ExerciseZero](http://learnpythonthehardway.org/exercise0.html) 下载并安装``` gedit ```文字编辑器。 
2. 把``` gedit ```放到桌面或者快速启动列，这样以后你就可以方便使用它了。这两个选项在安装时可以看到。 a. 执行 gedit （也就是你的编辑器），我们要先改掉一些愚蠢的预设值。 b. 从``` gedit menu ```中打开``` Preferences ```，选择``` Editor ```页面。 c. 将``` Tab width: ```改为 2。 d. 选择(确认有勾选到该选项)``` Insert spaces instead of tabs ```。 e. 然后打开 「Automatic indentation」 选项。 f. 转到``` View ```页面，打开 「Display line numbers」 选项。 
3. 找到 「Terminal」 程序。它的名字是``` Command Promot ```，或者你可以直接执行 cmd 。 
4. 为它建立一个捷径，放到桌面或者是快速启动列中以方便使用。 
5. 执行 Terminal，这个程序看上去不怎么地。 
6. 在 Termnal 程序里执行``` irb ```。在 Terminal 中执行程序的方式是输入程序的名称然后再敲一下 Return (Enter)。 
a. 如果你执行``` irb ```但发现不存在(不认得``` irb ```这个指令)。请用 Ruby Version Manager (RVM) 安装 Ruby。 
7. 敲击 CTRL-Z (Z) 退出``` irb ```。 
8. 这样你就应该能回到敲``` irb ```前的提示介面了。如果没有的话自己研究一下为什么。 .. _Ruby Version Manager (RVM): https://rvm.beginrescueend.com/ 
9. 学着使用 Terminal 创造一个目录，你可以上网搜寻怎么做。 
10. 学着使用 Terminal 进入一个目录，同样你可以上网搜寻。 
11. 使用你的编辑器在你进入的目录下建立一个档案。你将建立一个档案。使用 「Save」 或者 「Save As…」 选项，然后选择这个目录。 
12. 使用键盘切回到 Terminal  视图，如果不知道怎样使用键盘切换，你一样可以上网搜寻。 
13. 回到 Terminal，看看你能不能使用命令列列出你在目录里新建立的档案，在网路上搜寻怎么列出档案夹里的资料。 
> Warning: 对于 Ruby 来说 Windows 是个大问题。有时候你在一台电脑上装得好好的，但在另外一台电脑上却会漏掉一堆重要功能。如果遇到问题的话，你可以访问： http://rubyinstaller.org/。

Windows: 你应该看到的结果
-------------------------
```sh
C:\Documents and Settings\you>irb
ruby-1.9.2-p180 :001 >
ruby-1.9.2-p180 :001 > ^Z

C:\Documents and Settings\you>mkdir mystuff

C:\Documents and Settings\you>cd mystuff

... Here you would use gedit to make test.txt in mystuff ...

C:\Documents and Settings\you\mystuff>
   <bunch of unimportant errors if you istalled it as non-admin - ignore them - hit Enter>
C:\Documents and Settings\you\mystuff>dir
 Volume in drive C is
 Volume Serial Number is 085C-7E02

 Directory of C:\Documents and Settings\you\mystuff

04.05.2010  23:32    <DIR>          .
04.05.2010  23:32    <DIR>          ..
04.05.2010  23:32                 6 test.txt
               1 File(s)              6 bytes
               2 Dir(s)  14 804 623 360 bytes free

C:\Documents and Settings\you\mystuff>
```

你会看到的提示介面、Ruby 资讯，以及一些其他东西可能非常不一样，不过应该大致上不会差多少。如果你的系统差太多的话，反映给我们，我们会修正过来。

Linux
-----

Linux 系统可谓五花八门，安装软体的方式也个有不同。我们假设作为 Linux 使用者的你应该知道如何安装软体了，以下是给你的操作指示：

1. 用浏览器打开 http://learnpythonthehardway.org/wiki/ExerciseZero 下载并安装``` gedit ```文字编辑器。 
2. 把``` gedit ```放到 Window Manager 明显的位置，以方便之后使用。 
a. 执行 gedit （也就是你的编辑器），我们要先改掉一些愚蠢的预设值。 
b. 从``` gedit menu ```中打开``` Preferences ```，选择 Editor 页面。 
c. 将``` Tab width: ```改为 2。 
d. 选择(确认有勾选到该选项)``` Insert spaces instead of tabs ```。 
e. 然后打开 「Automatic indentation」 选项。 
f. 转到``` View ```页面，打开 「Display line numbers」 选项。 
3. 找到 「Terminal」 程序。它的名字可能是``` GNOME Terminal ```\、\``` Konsole ```\、或者``` xterm ```\。 
4. 把 Terminal 也放到 Dock 上。 
5. 执行 Terminal，这个程序看上去不怎么地。 
6. 在 Termnal 程序里执行``` irb ```。在 Terminal 中执行程序的方式是输入程序的名称然后再敲一下 Return (Enter)。 
a. 如果你执行``` irb ```但发现不存在(不认得``` irb ```这个指令)。请用 [Ruby Version Manager (RVM)](https://rvm.beginrescueend.com/) 安装 Ruby。 
7. 敲击 CTRL-D (D) 退出``` irb ```。 
8. 这样你就应该能回到敲``` irb ```前的提示介面了。如果没有的话自己研究一下为什么。 
9. 学着使用 Terminal 创造一个目录，你可以上网搜寻怎么做。 
10. 学着使用 Terminal 进入一个目录，同样你可以上网搜寻。 
11. 使用你的编辑器在你进入的目录下建立一个档案。你将建立一个档案。使用 「Save」 或者 「Save As…」 选项，然后选择这个目录。 
12. 使用键盘切回到 Terminal  视图，如果不知道怎样使用键盘切换，你一样可以上网搜寻。 
13. 回到 Terminal，看看你能不能使用命令列列出你在目录里新建立的档案，在网路上搜寻怎么列出档案夹里的资料。 

Linux: 你应该看到的结果
-----------------------
```sh
$ irb
ruby-1.9.2-p180 :001 > 
ruby-1.9.2-p180 :002 > ^D
$ mkdir mystuff
$ cd mystuff
# ... Use gedit here to edit test.txt ...
$ ls
test.txt
$
```

你会看到的提示介面、Ruby 资讯，以及一些其他东西可能非常不一样，不过应该大致上不会差多少。如果你的系统差太多的话，反映给我们，我们会修正过来。

给新手的告诫
------------

你已经完成了这节练习，取决于你对电脑的熟悉程度，这个练习对你而言可能会有些难。如果你觉得有难度的话，你要自己克服困难，多花点时间学习一下。因为如果你不会这些基础操作的话，写程序对你来说将会是相当艰难的一件事。

如果有程序员叫你去使用``` vim ```或者``` emacs ```，你应该拒绝他们。当你成为一个更好的程序员的时候，这些编辑器才会适合你使用。你现在需要的一个可以编辑文字的编辑器。我们使用``` gedit ```是因为它很简单，而且在不同的系统上面使用起来也是一样的。就连专业程序员也用``` gedit ```，所以对于初学者而言它已经够用了。

总有一天你会听到有程序员建议你使用 Mac OSX 或者 Linux。如果他喜欢字体美观，他会叫你弄台 Mac OSX 电脑，如果他们喜欢操作控制而且留了一把大胡子，他会叫你安装 Linux。这里再度向你说明，只要是一台手上能用的电脑就够了。你需要的只有三样东西``` gedit ```、一个 Terminal、还有``` IRB ```。

Finally the purpose of this setup is so you can do three things very reliably while you work on the exercises:

最后要说的是这节练习的准备工作的目的，也就是让你可以在以后的练习中顺利做到下面的这些事情：

1. 使用``` gedit ```编写程序代码。 
2. 执行你写的练习答案。 
3. 修改错误的练习答案。 
4. 重复上述步骤。 

其他的事情只会让你更困惑，所以还是坚持照着这个计画进行吧。


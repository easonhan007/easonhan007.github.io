---
layout: post
title: "练习27: 记住逻辑关系"
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

到此为止你已经学会了读写文件，命令行处理，以及很多 Ruby 数学运算功能。

今天，你将要开始学习逻辑了。你要学习的不是研究院里的高深逻辑理论，只是程序员每天都用到的让程序跑起来的基础逻辑知识。

学习逻辑之前你需要先记住一些东西。这个练习我要求你一个星期完成，不要擅自修改 schedule，就算你烦得不得了，也要坚持下去。这个练习会让你背下来一系列的逻辑表格，这会让你更容易地完成后面的练习。

需要事先警告你的是：这件事情一开始一点乐趣都没有，你会一开始就觉得它很无聊乏味，但它的目的是教你程序员必须的一个重要技能 — 一些重要的概念是必须记住的，一旦你明白了这些概念，你会获得相当的成就感，但是一开始你会觉得它们很难掌握，就跟和乌贼摔跤一样，而等到某一天，你会刷的一下豁然开朗。你会从这些基础的记忆学习中得到丰厚的回报。

这里告诉你一个记住某样东西，而不让自己抓狂的方法：在一整天里，每次记忆一小部分，把你最需要加强的部分标记起来。不要想着在两小时内连续不停地背诵，这不会有什么好的结果。不管你花多长时间，你的大脑也只会留住你在前15 或者30 分钟内看过的东西。

取而代之，你需要做的是创建一些索引卡片，卡片有两列内容，正面写下逻辑关系，反面写下答案。你需要做到的结果是：拿出一张卡片来，看到正面的表达式，例如「True or False」，你可以立即说出背面的结果是「True」！坚持练习，直到你能做到这一点为止。

一旦你能做到这一点了，接下来你需要每天晚上自己在笔记本上写一份真值表出来。不要只是抄写它们，试着默写真值表，如果发现哪里没记住的话，就飞快地撇一眼这里的答案。这样将训练你的大脑让它记住整个真值表。

不要在这上面花超过一周的时间，因为你在后面的应用过程中还会继续学习它们。

逻辑术语
--------

在 Ruby 中我们会用到下面的术语（符号或者词汇）来定义事物的真(True)或者假(False)。电脑的逻辑就是在程序的某个位置检查这些符号或者变数组合在一起表达的结果是真是假。

* and 和 
* or 或 
* not 非 
* != (not equal) 不等于 
* == (equal) 等于 
* >= (greater-than-equal) 大于等于 
* <= (less-than-equal) 小于等于 
* true 真 
* false 假 

其实你已经见过这些符号了，但这些词汇你可能还没见过。这些词汇(and, or, not)和你期望的效果其实是一样的，跟英语里的意思一模一样。

真值表
------

我们将使用这些符号来创建你需要记住的真值表。
<table>
  <tr>
    <th>NOT</th>
    <th>True?</th>
  </tr>
  <tr>
    <td>not False</td>
    <td></td>
    <td>True</td>
  </tr>
  <tr>
    <td>not True</td>
    <td></td>
    <td>False</td>
  </tr>
</table>

<table>
  <tr>
    <th>OR</th>
    <th>True?</th>
  </tr>
  <tr>
    <td>True or False</td>
    <td></td>
    <td>True</td>
  </tr>
  <tr>
    <td>True or True</td>
    <td></td>
    <td>True</td>
  </tr>
  <tr>
    <td>False or True</td>
    <td></td>
    <td>True</td>
  </tr>
  <tr>
    <td>False or False</td>
    <td></td>
    <td>False</td>
  </tr>
</table>

<table>
  <tr>
    <th>AND</th>
    <th>True?</th>
  </tr>
  <tr>
    <td>True and False</td>
    <td></td>
    <td>False</td>
  </tr>
  <tr>
    <td>True and True</td>
    <td></td>   
    <td>True</td>
  </tr>
  <tr>
    <td>False and True</td>
    <td></td>
    <td>False</td>
  </tr>
  <tr>
    <td>False and False</td>
    <td></td> 
    <td>False</td>
  </tr>
</table>

<table>
  <tr>
    <th>NOT OR</th>
    <th>True?</th>
  </tr>
  <tr>
    <td>not (True or False)</td>
    <td></td>
    <td>False</td>
  </tr>
  <tr>
    <td>not (True or True)</td>
    <td></td>
    <td>False</td>
  </tr>
  <tr>
    <td>not (False or True)</td>
    <td></td>
    <td>False</td>
  </tr>
  <tr>
    <td>not (False or False)</td>
    <td></td>
    <td>True</td>
  </tr>
</table>

<table>
  <tr>
    <th>NOT AND</th>
    <th>True?</th>
  </tr>
  <tr>
    <td>not (True and False)</td>
    <td></td>
    <td>True</td>
  </tr>
  <tr>
    <td>not (True and True)</td>
    <td></td>
    <td>False</td>
  </tr>
  <tr>
    <td>not (False and True)</td>
    <td></td>
    <td>True</td>
  </tr>
  <tr>
    <td>not (False and False)</td>
    <td></td>
    <td>True</td>
  </tr>
</table>

<table>
  <tr>
    <th>!=</th>
    <th>True?</th>
  </tr>
  <tr>
    <td>1 != 0</td>
    <td></td>
    <td>True</td>
  </tr>
  <tr>
    <td>1 != 1</td>
    <td></td>
    <td>False</td>
  </tr>
  <tr>
    <td>0 != 1</td>
    <td></td>
    <td>True</td>
  </tr>
  <tr>
    <td>0 != 0</td>
    <td></td>
    <td>False</td>
  </tr>
</table>

<table>
  <tr>
    <th>==</th>
    <th>True?</th>
  </tr>
  <tr>
    <td>1 == 0</td>
    <td></td>
    <td>False</td>
  </tr>
  <tr>
    <td>1 == 1</td>
    <td></td>
    <td>True</td>
  </tr>
  <tr>
    <td>0 == 1</td>
    <td></td>
    <td>False</td>
  </tr>
  <tr>
    <td>0 == 0</td>
    <td></td>
    <td>True</td>
  </tr>
</table>

现在使用这些表格创建你自己的卡片，再花一个星期慢慢记住它们。记住一点，这本书不会要求你成功或者失败，只要每天尽力去学，在尽力的基础上多花一点功夫就可以了。


---
layout: post
title: "ror零基础训练营0：环境篇"
description: "ror零基础训练营0：环境篇"
category: ror_traning
tags: [ror_traning]
---
{% include JB/setup %}

### 第一条规则：千万不要在windows上开发

我在windows上用watir用了5年，除了watir，windows确实是不适合初学者来学习和使用ruby的，特别是ruby on rails，有些gem无法装上（可以装，但是很麻烦），为了简单起见，还是不在windows折腾为好。

下面推荐一些环境配置，大家自行选择：

* vituralbox + ubuntu：在windows上安装ubuntu虚拟机，这个对新手比较友好；以后就在虚拟机里工作，ubuntu装桌面版；

* ubuntu：双系统和单系统均可，要桌面版；

* osx：macbook pro， macbook air, mac mini等均可；

### 安装并学习ruby

ubuntu和osx自带ruby，但是不要用，参考[这个链接](https://ruby-china.org/wiki/rbenv-guide)自行安装ruby。注意，这篇文章提到了gemset这个概念，不用去理解，那一节也不用看。**强烈注意，rbenv依赖git，因此在安装前要学习git的初级使用技巧，戳[这里](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)**。如果你看不懂一整篇英文，那么你只要配置下面的东西就好了


```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com

```

安装好ruby后，如果你纠结使用什么ide或编辑器，请戳[这里](https://ruby-china.org/wiki/tools)

如果你想买本参考书的话，没问题，看[这里](https://ruby-china.org/wiki/books)

对于我们来说，学习ruby的入门教程应该是[这个](http://www.easonhan.info/learn_ruby_the_hard_way.html)，2天敲完，每天8小时左右。极速提升自己的代码量。

再多说一句，ror不要求你的ruby基础有多好，ror自己的dsl和套路够多，因为ruby只要学个一般就可以学习使用ror了。

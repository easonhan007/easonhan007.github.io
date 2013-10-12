---
layout: post
title: "练习12: 模组 (Module)"
description: ""
category: 
tags: []
---
{% include JB/setup %}

看看这段 code

```sh
require 'open-uri'

open("http://www.ruby-lang.org/en") do |f|
  f.each_line {|line| p line}
  puts f.base_uri         # <URI::HTTP:0x40e6ef2 URL:http://www.ruby-lang.org/en/>
  puts f.content_type     # "text/html"
  puts f.charset          # "iso-8859-1"
  puts f.content_encoding # []
  puts f.last_modified    # Thu Dec 05 02:45:02 UTC 2002
end
```

在第一行是 require。这是一个 Ruby 中在你所写的脚本中加入其他来源（如：Ruby Gems 或者是你写的其他东西）的功能(features) 的方法。与其一次给你所有功能，Ruby 会问你你打算使用什么。这可使你的程序保持轻薄，又可当做之后其他程序设计师阅读你的程序时的参考。

等一下！功能 (Features) 还有另外一个名字
----------------------------------------

我在这里称呼他们为「功能(features)」。但实际上没人这样称呼。我这样做只是取了点巧，使你在学习时先不用理解「行话」。在继续进行之前你得先知道它们的真名``` modules ```（模组）。

从现在开始我们将把这些我们 require 进来的功能称作``` modules ```（模组）。我会这样说：「你想要 require``` open-uri ```module。」也有人给它另外一个称呼：「函式库(libraries)」。但在这里我们还是先叫它们``` modules ```（模组）吧。

加分练习
--------

1. 上网搜寻 require 与 include 的差异点。它们有什么不同？ 
2. 你能 require 一段没有特别包含 module 的脚本吗？ 
3. 搞懂 Ruby 会去系统的哪里找你 require 的 modules。 

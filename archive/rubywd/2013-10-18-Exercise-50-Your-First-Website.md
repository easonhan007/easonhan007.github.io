---
layout: post
title: "练习50:  你的第一个网站" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

这节以及后面的练习中，你的任务是把前面建立的游戏做成网页版。这是本书的最后三个章节，这些内容对你来说难度会相当大，你要在上面花些时间才能做出来。在你开始这节练习以前，你必须已经成功地完成过了《练习46》的内容，正确安装了 RubyGems，而且学会了如何安装软件包件以及如何建立项目骨架。如果你不记得这些内容，就回到《练习46》重新复习一遍。

安装 Sinatra
-------------

在建立你的第一个网页应用程序之前，你需要安装一个「Web框架」，它的名字叫 Sinatra。所谓的「框架」通常是指「让某件事情做起来更容易的软件包件」。在网页应用的世界里，人们建立了各种各样的「网页框架」，用来解决他们在建立网站时碰到的问题，然后把这些解决方案用软件包件的方式发布出来，这样你就可以利用它们引导建立你自己的项目了。

可选的框架类型有很多很多，不过在这里我们将使用 Sinatra 框架。你可以先学会它，等到差不多的时候再去接触其它的框架，不过 Sinatra 本身挺不错的，所以就算你一直使用也没关系。

使用` gem `安装 Sinatra:

```sh
$ gem install sinatra
Fetching: tilt-1.3.2.gem (100%)
Fetching: sinatra-1.2.6.gem (100%)
Successfully installed tilt-1.3.2
Successfully installed sinatra-1.2.6
2 gems installed
Installing ri documentation for tilt-1.3.2...
Installing ri documentation for sinatra-1.2.6...
Installing RDoc documentation for tilt-1.3.2...
Installing RDoc documentation for sinatra-1.2.6...
```

写一个简单的「Hello World」项目

现在你将做一个非常简单的「Hello World」项目出来，首先你要建立一个项目目录：

```sh
$ cd projects
$ bundle gem gothonweb
```

你最终的目的是把《练习42》中的游戏做成一个 web 应用，所以你的项目名称叫做i` gothonweb `，不过在此之前，你需要建立一个最基本的 Sinatra应用，将下面的代码放到` lib/gothonweb.rb `中：

```sh
require_relative "gothonweb/version"
require "sinatra"

module Gothonweb
  get '/' do
    greeting = "Hello, World!"
    return greeting
  end
end
```

然后使用下面的方法来运行这个 web 程序：

```sh
$ ruby lib/gothonweb.rb
== Sinatra/1.2.6 has taken the stage on 4567 for development with backup from WEBrick
[2011-07-18 11:27:07] INFO  WEBrick 1.3.1
[2011-07-18 11:27:07] INFO  ruby 1.9.2 (2011-02-18) [x86_64-linux]
[2011-07-18 11:27:07] INFO  WEBrick::HTTPServer#start: pid=6599 port=4567
```
最后，使用你的网页浏览器，打开 URL` http://localhost:4567/ `，你应该看到两样东西，首先是浏览器里显示了` Hello, world! `，然后是你的命令行终端显示了如下的输出：

```sh
127.0.0.1 - - [18/Jul/2011 11:29:10] "GET / HTTP/1.1" 200 12 0.0015
localhost - - [18/Jul/2011:11:29:10 EDT] "GET / HTTP/1.1" 200 12
- -> /
127.0.0.1 - - [18/Jul/2011 11:29:10] "GET /favicon.ico HTTP/1.1" 404 447 0.0008
localhost - - [18/Jul/2011:11:29:10 EDT] "GET /favicon.ico HTTP/1.1" 404 447
- -> /favicon.ico
```

这些是 Sinatra 打印出的 log 信息，从这些信息你可以看出服务器有在运行，而且能了解到程序在浏览器背后做了些什么事情。这些信息还有助于你发现程序的问题。例如在最后一行它告诉你浏览器试图存取` /favicon.ico `，但是这个文件并不存在，因此它返回的状态码是` 404 Not Found `。

到这里，我还没有讲到任何 web 相关的工作原理，因为首先你需要完成准备工作，以便后面的学习能顺利进行，接下来的两节练习中会有详细的解释。我会要求你用各种方法把你的 Sinatra 应用程序弄坏，然后再将其重新构建起来：这样做的目的是让你明白运行 Sinatra 程序需要准备好哪些东西。

发生了什么事情？
----------------

在浏览器访问到你的网页应用程序时，发生了下面一些事情：

1. 浏览器通过网路连接到你自己的电脑，它的名字叫做` localhost `，这是一个标准称呼，表示的谁就是网路中你自己的这台电脑，不管它实际名字是什么，你都可以使用` localhost `来访问。它使用到port 4567。 
2. 连接成功以后，浏览器对 lib/gothonweb.rb` 这个应用程序发出了HTTP请求(request)，要求访问URL/ `，这通常是一个网站的第一个URL。 
3. 在` lib/gothonweb.rb ` 里，我们有一个代码块，里面包含了 URL 的匹配关系。我们这里只定义了一组匹配，那就是「/」。它的含义是：如果有人使用浏览器访问 / 这一级目录，Sinatra 将找到它，从而用它处理这个浏览器请求。 
4. Sinatra 调用匹配到的代码块，这段代码只简单的回传了一个字串传回给浏览器。 
5. 最后 Sinatra 完成了对于浏览器请求的处理将响应(response)回传给浏览器，于是你就看到了现在的页面。 

确定你真的弄懂了这些，你需要画一个示意图，来理清信息是如何从浏览器传递到 Sinata，再到 / 区段，再回到你的浏览器的。

修正错误
-----------

第一步，把第 6 行的` greeting `变量删掉，然后重新刷浏览器。你应该会看到一个错误画面，你可以通过这一页丰富的信息看出你的程序崩溃的原因。当然你已经知道出错的原因是 greeting的赋值遗失了，不过 Sinatra还是会给你一个挺好的错误页面，让你能找到出错的具体位置。试试在这个错误页面上做以下操作：

1. 看看` sinatra.error `变量。 
2. 看看` REQUEST_ `变量里的信息。里面哪些知识是你已经熟悉了的。这是浏览器发给你的 gothonweb 应用程序的信息。这些知识对于日常网页浏览没有什么用处，但现在你要学会这些东西，以便写出web应用程序来。 

建立基本的模板
--------------

你已经试过用各种方法把这个Sinatra 程序改错，不过你有没有注意到「Hello World」不是一个好 HTML 网页呢？这是一个 web 应用，所以需要一个合适的HTML 响应页面才对。为了达到这个目的，下一步你要做的是将「Hello World」以较大的绿色字体显示出来。

第一步是建立一个` lib/views/index.erb `文件，内容如下：

```sh
<html>
    <head>
        <title>Gothons Of Planet Percal #25</title>
    </head>
<body>

  <% if greeting %>
    <p>I just wanted to say <em style="color: green; font-size: 2em;"><%= greeting %></em>.
  <% else %>
    <em>Hello</em>, world!
  <% end %>

</body>
</html>
```

什么是一个` .erb `的文件？ERB 的全名是 Embedded Ruby。` .erb `文件其实是一个内嵌一点 Ruby 代码的 HTML。如果你学过HTML的话，这些内容你看上去应该很熟悉。如果你没学过HTML，那你应该去研究一下，试着用HTML写几个网页，从而知道它的运作原理。既然这是一个` erb `模版，Sinatra 就会在模板中找到对应的位置，将参数的内容填充到模板中。例如每一个出现 `<%= greeting %> 的位置，内容都会被替换成对应这个变量名的参数。

为了让你的` lib/gothonweb.rb `处理模板，你需要写一写代码，告诉Sinatra 到哪里去找到模板进行加载，以及如何渲染(render)这个模板，按下面的方式修改你的文件：

```sh
require_relative "gothonweb/version"
require "sinatra"
require "erb"

module Gothonweb
  get '/' do
    greeting = "Hello, World!"
    erb :index, :locals => {:greeting => greeting}
  end
end
```

特别注意我改了` / `这个代码块最后一行的内容，这样它就可以调用` erb `然后把 greeting 变量传给它。

改好上面的程序后，刷新一下浏览器中的网页，你应该会看到一条和之前不同的绿色信息输出。你还可以在浏览器中通过「查看源代码(View Source)」看到模板被渲染成了标准有效的HTML 源代码。

这么讲也许有些太快了，我来详细解释一下模板的运作原理吧：

1. 在` lib/gothonweb.rb `你添加了一个` erb `函数调用。 
2. 这个` erb `函数知道怎么载入` lib/views `目录夹里的` .erb `的文件。它知道去抓哪些文件（在这个例子里是` index.erb `)。因为你传了一个参数进去（` erb :index … `)。 
3. 现在，当浏览器读取` / `且` lib/gothonweb.eb `匹配然后执行` get '/' do `区段，它再也没有只是回传字串` greeting `，而是调用` erb `然后传入` greeting `作为一个变量。 
4. 最后，你让` lib/views/index.erb `去检查` greeting `这个变量，如果这个变量存在的话，就打印出变量里的内容。如果不存在的话，就会打印出一个预设的内容。 

要深入理解这个过程，你可以修改` greeting `变量以及 HTML ，看看会友什么效果。然后也创作另外一个叫做` lib/views/foo.erb `的模板。然后把` erb :index `改成` erb :foo `。从这个过程中你也可以看到，你传入给erb的第一个参数只要匹配到lib/views下的.erb` 文件名称，就可以被渲染出来了。

加分练习
-----------

1. 到 [Sinatra](http://www.sinatrarb.com/) 这个框架的官方网站去阅读更多文件。 
2. 实验一下你在上述网站中看到的所有东西，包括他们的范例代码。 
3. 阅读有关于 HTML5 和 CSS3 相关的东西，自己练习写几个` .html `和` .css `文件。 
4. 如果你有一个懂 Rails 的朋友可以帮你的画，你可以自己试着使用 Rails 完成一下练习 50,51,52，看看结果会是什么样子。 


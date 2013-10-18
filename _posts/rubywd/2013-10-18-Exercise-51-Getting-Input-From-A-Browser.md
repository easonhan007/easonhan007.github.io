---
layout: post
title: "练习51:  从浏览器中取得输入" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

虽然能让浏览器显示「Hello World」是很有趣的一件事情，但是如果能让用户通过表单(form)向你的应用程序提交信息就更有趣了。这节练习中，我们将使用form 改进你的web 程序，并且搞懂如何为一个网站程序写自动化测试。

Web 运作原理
------------

该学点无趣的东西了。在建立 form 前你需要先多学一点关于 web的运作原理。这里讲的并不完整，但是相当准确，在你的程序出错时，它会帮你找到出错的原因。另外，如果你理解了form 的应用，那么建立form 对你来说就会更容易了。

我将以一个简单的图示讲起，它向你展示了web 请求的各个不同的部分，以及信息传递的大致流程：

为了方便讲述HTTP 请求(request) 的流程，我在每条线上面加了字母标签以作区别。

1. 你在浏览器中输入网址http://learnpythonthehardway.org/，然后浏览器会通过你的电脑的网路设备发出request（线路A）。 
2. 你的request 被传送到网际网路（线路B），然后再抵达远端服务器（线路C），然后我的服务器将接受这个request。 
3. 我的服务器接受 request 后，我的 web 应用程序就去处理这个请求（线路D），然后我的网页应用程序就会去运行 / (index) 这个「处理程序(handler)」。 
4. 在代码 return 的时候，我的服务器就会发出响应(response)，这个响应会再通过线路D传递到你的浏览器。 
5. 这个网站所在的服务器将响应由线路D获取，然后通过线路C传至网际网路。 
6. 响应通过网路网路由线路B传至你的电脑，电脑的网路卡再通过线路A将响应传给你的浏览器。 
7. 最后，你的浏览器显示了这个响应的内容。 

这段详解中用到了一些术语。你需要掌握这些术语，以便在谈论你的 web 应用时你能明白而且应用它们：

浏览器(browser)
------------------

这是你几乎每天都会用到的软件。大部分人不知道它真正的原理，他们只会把它叫作「网际网路」。它的作用其实是接收你输入到地址栏网址(例如http://learnpythonthehardway.org)，然后使用该信息向该网址对应的服务器提出请求(request)。

IP 位址 ( Address )
---------------------

通常这是一个像 http://learnpythonthehardway.org/ 一样的URL (Uniform Resource Locator，统一资源定位符 )，它告诉浏览器该打开哪个网站。前面的 http 指出了你要使用的协议(protocol)，这里我们用的是「超文本传输协议(Hyper-Text Transport Protocol)」。你还可以试试ftp://ibiblio.org/，这是一个「FTP文件传输协议(File Transport Protocol)‘的例子。learnpythonthehardway.org 这部分是「主机名(hostname)」，也就是一个便于人阅读和记忆的字串，主机名会被匹配到一串叫作「IP 位址」的数字上面，这个「IP 位址」就相当于网路中一台电脑的电话号码，通过这个号码可以访问到这台电脑。最后，URL中还可以尾随一个「路径「，例如 http://learnpythonthehardway.org/book/ 中的 /book/，它对应的是服务器上的某个文件或者某些资源，通过访问这样的网址，你可以向服务器发出请求，然后获得这些资源。网站地址还有很多别的组成部分，不过这些是最主要的。

连接(connection)
------------------

一旦浏览器知道了协议(http)、服务器(learnpythonthehardway.org)、以及要获得的资源，它就要去建立一个连接。这 个过程中，浏览器让操作系统(Operating System, OS) 打开计算机的一个「端口(port)」（通常是80端口），端口准备好以后，操作系统会回传给你的程序一个类似文件的东西，它所做的事情就是通过网路传输 和接收资料，让你的电脑和learnpythonthehardway.org这个网站所属的服务器之间实现资料交流。当你使用 http://localhost:4567/ 访问你自己的站点时，发生的事情其实是一样的，只不过这次你告诉了浏览器要访问的是你自己的电脑(localhost)，要使用的端口不是默认的80，而 是 4567 。你还可以直接访问http://learnpythonthehardway.org:80/，这和不输入端口效果一样，因为HTTP的默认端口本来就 是80。

请求(request)
--------------

你的浏览器通过你提供的地址建立了连接，现在它需要从远端服务器要到它（或你）想要的资源。如果你在URL的结尾加了 /book/，那你想要的就是/book/ 对应的文件或资源，大部分的服务器会直接为你调用/book/index.html 这个文件，不过我们就假装不存在好了。浏览器为了获得服务器上的资源，它需要向服务器发送一个「请求」。这里我就不讲细节了，为了得到服务器上的内容，你必须先向服务器发送一个请求才行。有意思的是，「资源」不一定非要是文件。例如当浏览器向你的应用程序提出请求的时候，服务器返回的其实是你的代码生成 的一些东西。

服务器(server)
----------------

服务器指的是浏览器另一端连接的电脑，它知道如何回应浏览器请求的文件和资源。大部分的 web 服务器只要发送文件就可以了，这也是服务器流量的主要部分。不过你学的是使用 Ruby 组建一个服务器，这个服务器知道如何接受请求，然后返回用 Ruby 处理过的字符串。当你使用这种处理方式时，你其实是假装把文件发给了浏览器，其实你用的都只是代码而已。就像你在《练习50》中看到的，要构建一个「响 应」其实也不需要多少代码。

响应(response)
---------------

这就是你的服务器回复给你的请求，传回至浏览器的HTML，它里边可能有css、javascript、或者图片等内容。以文件响应为例，服务器只 要从磁盘读取文件，发送给浏览器就可以了，不过它还要将这些内容包在一个特别定义的「header]」中，这样浏览器就会知道它获取的是什么类型的内容。 以你的web 应用程序为例，你发送的其实还是一样的东西，包括 header 也一样，只不过这些资料是你用 Ruby 代码即时生成的。

这个可以算是你能在网上找到的关于浏览器如何访问网站的最快的快速课程了。这节课程应该可以帮你更容易地理解本节的练习，如果你还是不明白，就到处 找资料多多了解这方面的信息，知道你明白为止。有一个很好的方法，就是你对照着上面的图示，将你在《练习50》中创建的 web 程序中的内容分成几个部分，让其中的各部分对应到上面的图示。如果你可以正确地将程序的各部分对应到这个图示，你就大致开始明白它的运作原理了。

表单(form)的运作原理
--------------------

熟悉「表单」最好的方法就是写一个可以接收表单资料的程序出来，然后看你可以对它做些什么。先将你的lib/gothonsweb.rb 修改成下面的样子：

```sh
require_relative "gothonweb/version"
require "sinatra"
require "erb"

module Gothonweb
  get '/' do
    greeting = "Hello, World!"
    erb :index, :locals => {:greeting => greeting}
  end

  get '/hello' do
    name = params[:name] || "Nobody"
    greeting = "Hello, #{name}"
    erb :index, :locals => {:greeting => greeting}
  end
end
```

重启你的 Sinatra（按CTRL-C后重新运行），确认它有运行起来，然后使用浏览器访问 http://localhost:4567/hello，这时浏览器应该会显示 “I just wanted to say Hello , Nobody.”，接下来，将浏览器的地址改成 http://localhost:4567/hello?name=Frank，然后你可以看到页面显示为 “Hello, Frank.”，最后将 name=Frank 修改为你自己的名字，你就可以看到它对你说 Hello 了。

让我们研究一下你的程序里做过的修改。

1. 我们没有直接为 greeting 赋值，而是使用了 params Hash 从浏览器获取数据。这Sinatra 个函数会将一组在 URL ? 后面的部份的 key / value 组加进 prarms Hash 里。 
2. 然后我从 params[:name] 中找到 name 的值，并为 greeting 赋值，这部份相信你已经很熟悉了。 
3. 其他的内容和以前是一样的，我们就不再分析了。 

URL中该还可以包含多个参数。将本例的URL改成这样子： http://localhost:4567/hello?name=Frank&greet=Hola。然后修改代码，让它去存取 prarams[:name] 和 params[:greet]，如下所示：

```sh
greeting = "#{greet}, #{name}"
```

创建HTML表单
-------------

你可以通过URL参数实现表单提交，不过这样看上去有些丑陋，而且不方便一般人使用，你真正需要的是一个「POST表单」，这是一种包含了\<form\>标签的特殊 HTML 文件。这种表单收集使用者输入并将其传递给你的web程序，这和你上面实现的目的基本是一样的。

让我们来快速建立一个，从中你可以看出它的运作原理。你需要创建一个新的HTML文件，叫做 lib/views/hello_form.erb：

```sh
<html>
    <head>
        <title>Sample Web Form</title>
    </head>
<body>

<h1>Fill Out This Form</h1>

<form action="/hello" method="POST">
    A Greeting: <input type="text" name="greet">
    <br/>
    Your Name: <input type="text" name="name">
    <br/>
    <input type="submit">
</form>

</body>
</html>
```

然后将 lib/gothonsweb.rb改成这样：

```sh
require_relative "gothonweb/version"
require "sinatra"
require "erb"

module Gothonweb

  get '/' do
    greeting = "Hello, World!"
    erb :index, :locals => {:greeting => greeting}
  end

  get '/hello' do
    erb :hello_form
  end

  post '/hello' do
    greeting = "#{params[:greet] || "Hello"}, #{params[:name] || "Nobody"}"
    erb :index, :locals => {:greeting => greeting}
  end

end
```

都写好以后，重启 web 程序，然后通过你的浏览器访问它。

这回你会看到一个表单，它要求你输入「一个问候语句(A Greeting)」和「你的名字(Your Name)」，等你输入完后点击「提交(Submit)」按钮，它就会输出一个正常的问候页面，不过这一次你的URL还是 http://localhost:4567/hello，并没有添加参数进去。

在hello_form.erb 里面关键的一行是\<form action="/hello" method="POST"\>，它告诉你的浏览器以下内容：

1. 从表单中的各个栏位收集使用者输入的资料。 
2. 让浏览器使用一种POST类型的请求，将这些资料发送给服务器。这是另外一种浏览器请求，它会将表单栏位「隐藏」起来。 
3. 将这个请求发送至/hello URL，这是由action="/hello"告诉浏览器的。 
4. 你可以看到两段\<input\>标签的名字属性(name)和代码中的变数是对应的，另外我们在 class index 中使用的不再只是 GET 方法，而是另一个 POST 方法。 

这个新程序的运作原理如下：

1. 浏览器访问到 web 程序的 /hello 目录，它发送了一个 GET 请求，于是我们的 get '/hello/ 就运行了并传回了hello_form。 
2. 你填好了浏览器的表单，然后浏览器依照\<form\>中的要求，将资料通过POST 请求的方式发给web程序。 
3. Web 程序运行了 post '/hello' 而不是不是 get '/hello/来处理这个请求。 
4. 这个 post '/hello'完成了它正常的功能，将 hello 页面返回，这里并没有新的东西，只是一个新函数名称而已。 

作为练习，在 lib/views/index.erb 中添加一个链接，让它指向 /hello，这样你可以反复填写并提交表单查看结果。确认你可以解释清楚这个链接的工作原理，以及它是如何让你实现在 lib/views/index.erb 和lib/views/hello_form.erb之间循环跳转的，还有就是要明白你新修改过的 Ruby 代码，你需要知道在什么情况下会运行到哪一部分代码。

Creating A Layout Template
----------------------------

在你下一节练习建立游戏的过程中，你需要建立很多的小 HTML 页面。如果你每次都写一个完整的网页，你会很快感觉到厌烦的。幸运的是你可以建立一个「外观 (layout」模板，也就是一种提供了通用的 headers 和 footers 的外壳模板，你可以用它将你所有的其他网页包裹起来。好开发人员会尽可能减少重复动作，所以要做一个好开发人员，使用外观模板是很重要的。

将 lib/views/index.erb 修改成这样：

```sh
<% if greeting %>
  <p>I just wanted to say <em style="color: green; font-size: 2em;"><%= greeting %></em>.
<% else %>
  <em>Hello</em>, world!
<% end %>
```

然后把 lib/views/hello_form.erb 修改成这样：

```sh
<h1>Fill Out This Form</h1>

<form action="/hello" method="POST">
    A Greeting: <input type="text" name="greet">
    <br/>
    Your Name: <input type="text" name="name">
    <br/>
    <input type="submit">
</form>
```

面这些修改的目的，是将每一个页面顶部和底部的反复用到的「样板 (boilerplate)」代码剥掉。这些被剥掉的代码会被放到一个单独的lib/views/layout.erb 文件中，从此以后，这些反复用到的代码就由lib/views/layout.erb 来提供了。

上面的都改好以后，建立一个 lib/views/layout.erb 文件，内容如下：

```sh
<html>
  <head>
    <title>Gothons From Planet Percal #25</title>
  </head>
  <body>
    <%= yield %>
  </body>
</html>
```

Sinatra 预设会自动去找名字为 layout 的外观模板，并且使用它作为其他模板的「基础」模板。你也可以修改已经用作任何页面的基础模板的 template。重启你的程序观察一下，然后试着用各种方法修改你的layout模板，不要修改你别的模板，看看输出会有什么样的变化。

为表单撰写自动测试代码
-----------------------

使用浏览器测试 web 程序是很容易的，只要点刷新按钮就可以了。不过毕竟我们是开发人员嘛，如果我们可以写一些代码来测试我们的程序，为什么还要重复手动测试呢？接下来你 要做的，就是为你的web 程序写一个小测试。这会用到你在《练习47》学过的一些东西，如果你不记得的话，可以回去复习一下。

我已经为此建立了一个简单的小函数，让你判断(assert) web程序的响应，这个函数有一个很合适的名字，就叫 assert_response。创建一个 tests/tools.rb 文件，内容如下：

```sh
require 'test/unit'

def assert_response(resp, contains=nil, matches=nil, headers=nil, status=200)

  assert_equal(resp.status, status, "Expected response #{status} not in #{resp}")

  if status == 200
    assert(resp.body, "Response data is empty.")
  end

  if contains
    assert((resp.body.include? contains), "Response does not contain #{contains}")
  end

  if matches
    reg = Regexp.new(matches)
    assert reg.match(contains), "Response does not match #{matches}"
  end

  if headers
    assert_equal(resp.headers, headers)
  end

end
```

最后，执行 test/test_gothonsweb.rb 去测试你的程序：

```sh
$ ruby test/test_gothonweb.rb 
Loaded suite test/test_gothonweb
Started
.
Finished in 0.023839 seconds.

1 tests, 9 assertions, 0 failures, 0 errors, 0 skips

Test run options: --seed 57414
```

rack/test 函数库包含了一串很简单的 API 可以让你处理请求。他们是 get, put, post, delete 和 head 函数，模拟程序会遇到的各类类型请求。

所有假的 (mock) request 函数会有一样的参数模式：

```sh
get '/path', params={}, rack_env={}
```
* /path 是 request 路径，而且可以选择性的包含一个 query string。 
* params 是一组 query/post 的 Hash 参数，一个 request body 字串，或者是 nil 
* rack_env 是一个 Rack 环境值 Hash。这可以用来设置 request 的 header 和其他 request 相关的信息，例如 session 内的资料。 

这样的运作方式就不用实际运作一个真的 web 服务器，如此一来你就可以使用自动化测试代码去测试，当然同时你也可以使用浏览器去测试一个执行中的服务器。

为了验证(validate) 函数的响应，你需要使用 test/tools.rb 中定义的assert_response 函数，里面内容是：

To validate responses from this function, use the assert_response function from test/tools.rb which has:

```sh
assert_response(resp, contains=nil, matches=nil, headers=nil, status=200)
```

把你调用 get 或 post 得到的响应传递给这个函数，然后将你要检查的内容作为参数传递给这个函数。你可以使用 contains参数来检查响应中是否包含指定的值，使用 status 参数可以检查指定的响应状态。这个小函数其实包含了很多的信息，所以你还是自己研究一下的比较好。

在 test/test_gothonsweb.rb 自动测试脚本中，我首先确认 /foo URL 传回了一个「404 Not Found」响应，因为这个 URL其实是不存在的。然后我检查了/hello 在 GET 和 POST 两种请求的情况下都能正常运作。就算你没有弄明白测试的原理，这些测试代码应该是很好读懂的。

花一些时间研究一下这个最新版的web程序，重点研究一下自动测试的运作原理。

加分练习
----------
1. 阅读和HTML 相关的更多资料，然后为你的表单设计一个更好的输出格式。你可以先在纸上设计出来，然后用HTML 去实现它。 
2. 这是一道难题，试着研究一下如何进行文件上传，通过网页上传一张图片，然后将其保存到磁盘中。 
3. 更难的难题，找到 HTTP RFC 文件（讲述HTTP 运作原理的技术文件），然后努力阅读一下。这是一篇很无趣的文件，不过偶尔你会用到里边的一些知识。 
4. 又是一道难题，找人帮你设置一个 web 服务器，例如Apache、Nginx、或者thttpd。试着让服务器伺服一下你建立的.html 和.css 文件。如果失败了也没关系，web 服务器本来就都有点烂。 
5. 完成上面的任务后休息一下，然后试着多建立一些 web 程序出来。你应该仔细阅读 Sinatra 中关于会话(session)的内容，这样你可以明白如何存留使用者的状态信息。 


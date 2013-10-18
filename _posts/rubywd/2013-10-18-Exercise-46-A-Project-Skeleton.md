---
layout: post
title: "练习46:  一个项目骨架" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

这里你将学会如何建立一个项目「骨架」目录。这个骨架目录具备让项目跑起来的所有基本内容。它里边会包含你的项目文件布局、自动化测试代码，模块，以及安装脚本。当你建立一个新项目的时候，只要把这个目录复制过去，改改目录的名字，再编辑里面的文件就行了。

骨架内容: Linux/OSX
--------------------

首先使用下述命令创建你的骨架目录：

```sh
$ mkdir -p projects
$ cd projects/
$ mkdir skeleton
$ cd skeleton
$ mkdir bin lib lib/NAME test
```

我使用了一个叫 projects 的目录，用来存放我自己的各个项目。然后我在里边建立了一个叫做 skeleton 的文件夹，这就是我们新项目的基础目录。其中叫做 NAME 的文件夹是你的项目的主文件夹，你可以将它任意取名。

接下来我们要配置一些初始文件：

```sh
$ touch lib/NAME.rb
$ touch lib/NAME/version.rb
```

然后我们可以建立一个` NAME.gemspec `的文件在我们的项目的根目录，这个文件在安装项目的时候我们会用到它：

```sh
# -*- encoding: utf-8 -*-
$:.push File.expand_path("../lib", __FILE__)
require "NAME/version"

Gem::Specification.new do |s|
  s.name        = "NAME"
  s.version     = NAME::VERSION
  s.authors     = ["Rob Sobers"]
  s.email       = ["rsobers@gmail.com"]
  s.homepage    = ""
  s.summary     = %q{TODO: Write a gem summary}
  s.description = %q{TODO: Write a gem description}

  s.rubyforge_project = "NAME"

  s.files         = `git ls-files`.split("\n")
  s.test_files    = `git ls-files -- {test,spec,features}/*`.split("\n")
  s.executables   = `git ls-files -- bin/*`.split("\n").map{ |f| File.basename(f) }
  s.require_paths = ["lib"]
end
```

编辑这个文件，把自己的联络方式写进去，然后放到那里就行了。

最后你需要一个简单的测试专用(我们将会在下一节中提到 Test )的骨架文件叫` test/test_NAME.rb `:

```sh
require 'test/unit'

class MyUnitTests < Test::Unit::TestCase

  def setup
    puts "setup!"
  end

  def teardown
    puts "teardown!"
  end

  def test_basic
    puts "I RAN!"
  end

end
```

安装 Gems
----------

Gems 是 Ruby 的套件系统，所以你需要知道怎么安装它和使用它。不过问题就来了。我的本意是让这本书越清晰越干净越好，不过安装软件的方法是在是太多了，如果我要一步一步写下来，那10 页都写不完，而且告诉你吧，我本来就是个懒人。

所以我不会提供详细的安装步骤了，我只会告诉你需要安装哪些东西，然后让你自己搞定。这对你也有好处，因为你将打开一个全新的世界，里边充满了其他人发布的软件。

接下来你需要安装下面的软件套件：

* git - [http://git-scm.com/](http://git-scm.com/) 
* rake - [http://rake.rubyforge.org/](http://rake.rubyforge.org/) 
* rvm - [https://rvm.beginrescueend.com/](https://rvm.beginrescueend.com/) 
* rubygems - [http://rubygems.org/pages/download](http://rubygems.org/pages/download) 
* bundler - [http://gembundler.com/](http://gembundler.com/)
 
不要只是手动下载并且安装这些软件套件，你应该看一下别人的建议，尤其看看针对你的操作系统别人是怎样建议你安装和使用的。同样的软件套件在不一样的操作系统上面的安装方式是不一样的，不一样版本的 Linux 和 OSX 会有不同，而 Windows 更是不同。

我要预先警告你，这个过程会是相当无趣。在业内我们将这种事情叫做「yak shaving(剃牦牛)」。它指的是在你做一件有意义的事情之前的一些准备工作，而这些准备工作又是及其无聊冗繁的。你要做一个很酷的 Ruby 项目，但是创建骨架目录需要你安装一些软件到件，而安装软件套件之前你还要安装package installer (软件套件安装工具)，而要安装这个工具你还得先学会如何在你的操作系统下安装软件，真是烦不胜烦呀。

无论如何，还是克服困难吧。你就把它当做进入程式俱乐部的一个考验。每个开发人员都会经历这条道路，在每一段「酷」的背后总会有一段「烦」的。

使用这个骨架
-------------

剃牦牛的事情已经做的差不多了，以后每次你要新建一个项目时，只要做下面的事情就可以了：

1. 拷贝这份骨架目录，把名字改成你新项目的名字。 
2. 再将` NAME `模块和` NAME.rb `更名为你需要的名字，它可以是你项目的名字，当然别的名字也行。 
3. 编辑你的` NAME.gemspec `文件，让它包含你新项目的相关资讯。 
4. 重命名` test/test_NAME.rb `，让它的名字匹配到你模块的名字。 
5. 开始写程式吧。 

小测验
------

这节练习没有加分练习，不过需要你做一个小测验：

1. 找文件阅读，学会使用你前面安装了的软件套件。 
2. 阅读关于` NAME.gemspec `的文件，看它里边可以做多少配置。 
3. 建立一个项目，在` NAME.rb `里写一些代码。 
4. 在` bin `目录下放一个可以运行的脚本，找材料学习一下怎样建立可以在系统下运行的 Ruby 脚本。 
5. 确定你建立的` bin `教本，有在` NAME.gemspec `中被参照到，这这样你安装时就可以连它安装进去。 
6. 使用你的` NAME.gemspec `和` gem build `、` gem install `来安装你写的程式和确定它能用。然后使用` gem uninstall `去移除它。 
7. 弄懂如何使用 Bundler 来自动建立一个骨架目录。 


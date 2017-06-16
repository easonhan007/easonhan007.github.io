---
layout: post
title: "练习52:  创造你的网页游戏" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

这本书马上就要结束了。本章的练习对你是一个真正的挑战。当你完成以后，你就可以算是一个能力不错的 Ruby 初学者了。为了进一步学习，你还需要多读一些书，多写一些程序，不过你已经具备进一步学习的技能了。接下来的学习就只是时间、动力、以及资源的问题了。

在本章练习中，我们不会去创建一个完整的游戏，取而代之的是我们会为《练习42》中的游戏建立一个“引擎(engine)”，让这个游戏能够在浏览 器中运行起来。这会涉及到将《练习42》中的游戏「重构(refactor)」，将《练习47》中的架构混合进来，添加自动测试代码，最后建立一个可以 运行游戏的web 引擎。
这是一节很「庞大」的练习。我预测你要花一周到一个月才能完成它。最好的方法是一点一点来，每晚上完成一点，在进行下一步之前确认上一步有正确完成。

重构《练习42》的游戏
--------------------

你已经在两个练习中修改了 gothonweb 项目，这节练习中你会再修改一次。这种修改的技术叫做「重构(refactoring)」，或者用我喜欢的讲法来说，叫「修修补补(fixing stuff)」。重构是一个程序术语，它指的是清理旧代码或者为旧代码添加新功能的过程。你其实已经做过这样的事情了，只不过不知道这个术语而已。这 是写软体过程的第二个自然属性。

你在本节中要做的，是将《练习47》中的可以测试的房间地图，以及《练习42》中的游戏这两样东西归并到一起，创建一个新的游戏架构。游戏的内容不会发生变化，只不过我们会通过“重构”让它有一个更好的架构而已。

第一步是将 ex47.rb 的内容复制到 gothonweb/lib/map.rb 中，然后将` ex47_tests.rb `的内容复制到` gothonweb/test/test_map.rb `中，然后再次运行测试，确认他们还能正常运作。

> Note: 从现在开始我不会再向你展示运行测试的输出了，我就假设你回去运行这些测试，而且知道怎样的输出是正确的。

将《练习47》的代码拷贝完毕后，你就该开始重构它，让它包含《练习42》中的地图。我一开始会把基本架构为你准备好，然后你需要去完成map.rb和map_tests.rb 里边的内容。

首先要做的是使用 Room 类来构建基本的地图架构：

```sh
class Room

  attr_accessor :name, :description, :paths

  def initialize(name, description)
    @name = name
    @description = description
    @paths = {}
  end

  def go(direction)
    @paths[direction]
  end

  def add_paths(paths)
    @paths.update(paths)
  end

end

central_corridor = Room.new("Central Corridor",
%q{
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an 
escape pod.

You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body.  He's blocking the door to the
Armory and about to pull a weapon to blast you.
})


laser_weapon_armory = Room.new("Laser Weapon Armory",
%q{
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding.  It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container.  There's a keypad lock on the box
and you need the code to get the bomb out.  If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb.  The code is 3 digits.
})


the_bridge = Room.new("The Bridge",
%q{
The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot.

You burst onto the Bridge with the netron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship.  Each of them has an even uglier
clown costume than the last.  They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
})


escape_pod = Room.new("Escape Pod",
%q{
You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.
You inch backward to the door, open it, and then carefully
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pod to
get off this tin can.

You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes.  It seems like
hardly any Gothons are on the ship, so your run is clear of
interference.  You get to the chamber with the escape pods, and
now need to pick one to take.  Some of them could be damaged
but you don't have time to look.  There's 5 pods, which one
do you take?
})


the_end_winner = Room.new("The End",
%q{
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to
the planet below.  As it flies to the planet, you look
back and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same
time.  You won!
})


the_end_loser = Room.new("The End",
%q{
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body
into jam jelly.
})

escape_pod.add_paths({
    '2' => the_end_winner,
    '*' => the_end_loser
})

generic_death = Room.new("death", "You died.")

the_bridge.add_paths({
    'throw the bomb' => generic_death,
    'slowly place the bomb' => escape_pod
})

laser_weapon_armory.add_paths({
    '0132' => the_bridge,
    '*' => generic_death
})

central_corridor.add_paths({
    'shoot!' => generic_death,
    'dodge!'=> generic_death,
    'tell a joke' => laser_weapon_armory
})

START = central_corridor
```

你会发现我们的 Room 类和地图有一些问题：

1. 在进入一个房间以前会打出一段文字作为房间的描述，我们需要将这些描述和每个房间关联起来，这样房间的次序就不会被打乱了，这对我们的游戏是一件好事。这些描述本来是在 if-else 结构中的，这是我们后面要修改的东西。
2. 原版游戏中我们使用了专门的程序来生成一些内容，例如炸弹的激活键码，舰舱的选择等，这次我们做游戏时就先使用预设值好了，不过后面的加分练习里，我会要求你把这些功能再加到游戏中。
3. 我为所有的游戏中的失败结尾写了一个 generic_death，你需要去补全这个函式。你需要把原版游戏中所有的失败结尾都加进去，并确保代码能正确运行。
4. 我添加了一种新的转换模式，以"*"为标记，用来在游戏引擎中实现「catch-all」动作。

等你把上面的代码基本写好以后，接下来就是引导你继续写下去的自动测试的内容 test/test_map.rb 了：

```sh
require 'test/unit'
require_relative '../lib/map'

class MapTests < Test::Unit::TestCase

  def test_room()
    gold = Room.new("GoldRoom",
                %q{This room has gold in it you can grab. There's a
                door to the north.})
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
  end

  def test_room_paths()
    center = Room.new("Center", "Test room in the center.")
    north = Room.new("North", "Test room in the north.")
    south = Room.new("South", "Test room in the south.")

    center.add_paths({'north' => north, 'south' => south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)
  end

  def test_map()
    start = Room.new("Start", "You can go west and down a hole.")
    west = Room.new("Trees", "There are trees here, you can go east.")
    down = Room.new("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west' => west, 'down' => down})
    west.add_paths({'east' => start})
    down.add_paths({'up' => start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
  end

  def test_gothon_game_map()
    assert_equal(START.go('shoot!'), generic_death)
    assert_equal(START.go('dodge!'), generic_death)

    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
  end

end
```

你在这部分练习中的任务是完成地图，并且让自动测试可以完整地检查过整个地图。这包括将所有的 generic_death 物件修正为游戏中实际的失败结尾。让你的代码成功运行起来，并让你的测试越全面越好。后面我们会对地图做一些修改，到时候这些测试将保证修改后的代码还可以正常工作。

会话(session)和用户跟踪
-------------------------

在你的 web 程序运行的某个位置，你需要追踪一些信息，并将这些信息和用户的浏览器关联起来。在HTTP 协议的框架中，web 环境是「无状态(stateless)」的，这意味着你的每一次请求和你其它的请求都是相互独立的。如果你请求了页面A，输入了一些资料，然后点了一个页 面B 的链接，那你在页面A 输入的数据就全部消失了。

解决这个问题的方法是为 web 程序建立一个很小的资料储存功能，给每个浏览器赋予一个独一无二的数字，用来跟踪浏览器所作的事情。这个功能通常适用资料库或者是存储在磁盘上的文件来实 现。在 Sinatra 这个框架中实现这样的功能是很容易的，以下就是一个这样的例子（使用 Rack middleware)：

```sh
require 'rubygems'
require 'sinatra'

use Rack::Session::Pool

get '/count' do
  session[:count] ||= 0
  session[:count] +=1
  "Count: #{session[:count]}"
end

get '/reset' do
  session.clear
  "Count reset to 0."
end
```

建立引擎
----------

你应该已经写好了游戏地图和它的单元测试代码。现在我要求你制作一个简单的游戏引擎，用来让游戏中的各个房间运转起来，从玩家收集输入，并且记住玩家到了那一幕。我们将用到你刚学过的会话来制作一个简单的引擎，让它可以：

1. 为新使用者启动新的游戏。 
2. 将房间展示给使用者。 
3. 接受使用者的输入。 
4. 在游戏中处理使用者的输入。 
5. 显示游戏的结果，继续游戏的下一幕，知道玩家角色死亡为止。 

为了建立这个引擎，你需要将我们久经考验的lib/gothonsweb.rb 搬过来，建立一个功能完备的、基于 session 的游戏引擎。这里的难点是我会先使用基本的 HTML 文件创建一个非常简单的版本，接下来将由你完成它，基本的引擎是这个样子的：

```sh
require_relative "gothonweb/version"
require_relative "map"
require "sinatra"
require "erb"

module Gothonweb

  use Rack::Session::Pool

  get '/' do
    # this is used to "setup" the session with starting values
    p START
    session[:room] = START
    redirect("/game")
  end

  get '/game' do
    if session[:room]
      erb :show_room, :locals => {:room => session[:room]}
    else
      # why is there here? do you need it?
      erb :you_died
    end
  end

  post '/game' do
    action = "#{params[:action] || nil}"
    # there is a bug here, can you fix it?
    if session[:room]
      session[:room] = session[:room].go(params[:action])
    end
    redirect("/game")
  end

end
```

下一步，你应该删除` lib/views/hello_form.erb `和 lib/views/index.erb 然后创作两个在上述 code 提到的 template，这里是一个非常简单的` lib/views/show_room.erb `:

```sh
<h1><%= room.name %></h1>

<pre>
<%= room.description %>
</pre>

<% if room.name == "death" %>
  <p>
  <a href="/">Play Again?</a>
  </p>
<% else %>
  <p>
  <form action="/game" method="POST">
    - <input type="text" name="action"> <input type="SUBMIT">
  </form>
  </p>
<% end %>
```

这就用来显示游戏中的房间的模板。接下来，你需要在使用者跑到地图的边界时，用一个模板告诉使用者他的角色的死亡信息，也就是lib/views/you_died.erb 这个模板：

```sh
<h1>You Died!</h1>

<p>Looks like you bit the dust.</p>
<p><a href="/">Play Again</a></p>
```

准备好了这些文件，你现在可以做下面的事情了：

1. 让测试代码 test/test_gothonsweb.rb 再次运行起来，这样你就可以去测试这个游戏。由于 session 的存在，你可能顶多只能实现几次点击，不过你应该可以做出一些基本的测试来。 
2. 执行 lib/gothonsweb.rb` 脚本，试玩一下你的游戏。 
3. 你需要和往常一样刷新和修正你的游戏，慢慢修改游戏的HTML 文件和引擎，直到你实现游戏需要的所有功能为止。 

你的期末考试
---------------

你有没有觉着我一下子给了你超多的信息呢？那就对了，我想要你在学习技能的同时可以有一些可以用来鼓捣的东西。为了完成这节练习，我将给你最后一套 需要你自己完成的练习。你将注意到，到目前为止你写的游戏并不是很好，这只是你的第一版代码而已。你现在的任务是让游戏更加完善，实现下面的这些功能：

1. 修正代码中所有我提到和没提到的bug，如果你发现了新的bug，你可以告诉我。 
2. 改进所有的自动测试，让你可以测试更多的内容，直到你可以不用浏览器就能测到所有的内容为止。 
3. 让HTML 页面看上去更美观一些。 
4. 研究一下网页登录系统，为这个程序创建一个登录界面，这样人们就可以登录这个游戏，并且可以保存游戏高分。 
5. 完成游戏地图，尽可能地把游戏做大，功能做全。 
6. 给用户一个「帮助系统」，让他们可以查询每个房间里可以执行哪些命令。 
7. 为你的游戏添加新功能，想到什么功能就添加什么功能。 
8. 创建多个地图，让用户可以选择他们想要玩的一张来进行游戏。你的 lib/gothonsweb.rb 应该可以运行提供给它的任意的地图，这样你的引擎就可以支持多个不同的游戏。 
9. 最后，使用你在练习 48 和49 中学到的东西来创建一个更好的输入处理器。你手头已经有了大部分必要的代码，你只需要改进语法，让它和你的输入表单以及游戏引擎挂钩即可。 

祝你好运！


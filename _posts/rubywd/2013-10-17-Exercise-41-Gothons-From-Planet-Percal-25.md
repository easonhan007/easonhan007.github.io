---
layout: post
title: "练习41:  来自 Percal 25 号行星的哥顿人(Gothons)" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

你在上一节中发现 Hash 的秘密功能了吗？你可以解释给自己吗？让我来给你解释一下，顺便和你自己的理解对比看有什么不同。这里是我们要讨论的代码：

```sh
cities[:find] = method(:find_city)
puts cities[:find].call(cities, state)
```

你要记住一个函式也可以作为一个变量，为了要将一个代码区段储存在一个变量里，我们创造了一个东西叫「proc」，proc 是 procedure 缩写。在这段代码中，首先我们调用了 Ruby 内建的函式` method `，它会回传一个 proc 版的` find_city `函式。然后我们将之除存在一个 Hash 里 ：key 是` :find `，value 是` cities `。。这和我们将省和市关联起来的代码做的事情一样，只不过在这个情况里是个 proc。

好了，所以一旦我们知道` find_city `是在Hash中 :find 的位置，这就意味着我们可以去调用它。第二行代码可以分解成如下步骤：

1. Ruby 读到了` cities `，然后知道了它是一个 「Hash」。 
2. 然后看到了` [:find] `，于是 Ruby 就从索引找到了 cities Hash 中对应的位置，并且获取了该位置的内容。 
3.` [:find] `这个位置的内容是我们的函式` find_city `，所以Ruby就知道了这里表示一个函式，于是当它碰到` .call `就开始了 proc调用。 
4.` cities `、` state `这两个参数将被传递到函式` find_city `中，然后这个函式就被运行了。 
5.` find_city `接着从` cities `中寻找` states `，并且回传它找到的内容，如果什么都没找到，就返回一个信息说它什么都没找到。 
6. Ruby 接受` find_city `传回的资讯，最后将该资讯赋值给一开始的` city_found `这个变量。 

我再教你一个小技巧。如果你倒着阅读的话，代码可能会变得更容易理解。让我们来试一下，一样是那行：

1. ` state `和` city `是… 
2. 最为参数传递给… 
3. 一个 proc 位于… 
4. ` :find `然后寻找，目的地为… 
5. ` cities `这个 Hash… 
6. 最后印到屏幕上 

还有一种方法读它，这回是「由里向外」。

1. 找到表示式的中心位置，此次为` [:find] `。 
2. 逆时针追溯，首先看到的是一个叫` cities `的 Hash，这样就知道了` cities `中的` :find `元素。 
3. 上一步得到一个函式。继续逆时针寻找，看到的是参数。 
4. 参数传递给函式后，函式会传回一个值。然后再逆时针寻找。 
5. 最后，我们到了` city_found `=的赋值位置，并且得到了最终结果。 

数十年的程序经验下来，我在读代码的过程中已经用不到上面的三种方法了。我只要瞄一眼就能知道它的意思。甚至给我一整页的代码，我也可以一眼瞄 出里边的 bug 和错误。这样的技能是花了超乎常人的时间和精力才锻炼得来的。在磨练的过程中，我学会了下面三种读代码的方法：

1. 从前向后。 
2. 从后向前。 
3. 逆时针方向。 

现在我们来写这次的练习，写完后再过一遍，这节练习其实挺有趣的。

代码不少，不过还是从头写完吧。确认它能运行，然后玩一下看看。

```sh
def prompt()
  print "> "
end

def death()
  quips = ["You died.  You kinda suck at this.",
    "Nice job, you died ...jackass.",
    "Such a luser.",
    "I have a small puppy that's better at this."]
  puts quips[rand(quips.length())]
  Process.exit(1)
end

def central_corridor()
  puts "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
  puts "your entire crew.  You are the last surviving member and your last"
  puts "mission is to get the neutron destruct bomb from the Weapons Armory,"
  puts "put it in the bridge, and blow the ship up after getting into an "
  puts "escape pod."
  puts "\n"
  puts "You're running down the central corridor to the Weapons Armory when"
  puts "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
  puts "flowing around his hate filled body.  He's blocking the door to the"
  puts "Armory and about to pull a weapon to blast you."

  prompt()
  action = gets.chomp()

  if action == "shoot!"
    puts "Quick on the draw you yank out your blaster and fire it at the Gothon."
    puts "His clown costume is flowing and moving around his body, which throws"
    puts "off your aim.  Your laser hits his costume but misses him entirely.  This"
    puts "completely ruins his brand new costume his mother bought him, which"
    puts "makes him fly into an insane rage and blast you repeatedly in the face until"
    puts "you are dead.  Then he eats you."
    return :death

  elsif action == "dodge!"
    puts "Like a world class boxer you dodge, weave, slip and slide right"
    puts "as the Gothon's blaster cranks a laser past your head."
    puts "In the middle of your artful dodge your foot slips and you"
    puts "bang your head on the metal wall and pass out."
    puts "You wake up shortly after only to die as the Gothon stomps on"
    puts "your head and eats you."
    return :death

  elsif action == "tell a joke"
    puts "Lucky for you they made you learn Gothon insults in the academy."
    puts "You tell the one Gothon joke you know:"
    puts "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
    puts "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
    puts "While he's laughing you run up and shoot him square in the head"
    puts "putting him down, then jump through the Weapon Armory door."
    return :laser_weapon_armory

  else
    puts "DOES NOT COMPUTE!"
    return :central_corridor
  end
end

def laser_weapon_armory()
  puts "You do a dive roll into the Weapon Armory, crouch and scan the room"
  puts "for more Gothons that might be hiding.  It's dead quiet, too quiet."
  puts "You stand up and run to the far side of the room and find the"
  puts "neutron bomb in its container.  There's a keypad lock on the box"
  puts "and you need the code to get the bomb out.  If you get the code"
  puts "wrong 10 times then the lock closes forever and you can't"
  puts "get the bomb.  The code is 3 digits."
  code = "%s%s%s" % [rand(9)+1, rand(9)+1, rand(9)+1]
  print "[keypad]> "
  guess = gets.chomp()
  guesses = 0

  while guess != code and guesses < 10
    puts "BZZZZEDDD!"
    guesses += 1
    print "[keypad]> "
    guess = gets.chomp()
  end

  if guess == code
    puts "The container clicks open and the seal breaks, letting gas out."
    puts "You grab the neutron bomb and run as fast as you can to the"
    puts "bridge where you must place it in the right spot."
    return :the_bridge
  else
    puts "The lock buzzes one last time and then you hear a sickening"
    puts "melting sound as the mechanism is fused together."
    puts "You decide to sit there, and finally the Gothons blow up the"
    puts "ship from their ship and you die."
    return :death
  end
end

def the_bridge()
  puts "You burst onto the Bridge with the netron destruct bomb"
  puts "under your arm and surprise 5 Gothons who are trying to"
  puts "take control of the ship.  Each of them has an even uglier"
  puts "clown costume than the last.  They haven't pulled their"
  puts "weapons out yet, as they see the active bomb under your"
  puts "arm and don't want to set it off."

  prompt()
  action = gets.chomp()

  if action == "throw the bomb"
    puts "In a panic you throw the bomb at the group of Gothons"
    puts "and make a leap for the door.  Right as you drop it a"
    puts "Gothon shoots you right in the back killing you."
    puts "As you die you see another Gothon frantically try to disarm"
    puts "the bomb. You die knowing they will probably blow up when"
    puts "it goes off."
    return :death

  elsif action == "slowly place the bomb"
    puts "You point your blaster at the bomb under your arm"
    puts "and the Gothons put their hands up and start to sweat."
    puts "You inch backward to the door, open it, and then carefully"
    puts "place the bomb on the floor, pointing your blaster at it."
    puts "You then jump back through the door, punch the close button"
    puts "and blast the lock so the Gothons can't get out."
    puts "Now that the bomb is placed you run to the escape pod to"
    puts "get off this tin can."
    return :escape_pod
  else
    puts "DOES NOT COMPUTE!"
    return :the_bridge
  end
end

def escape_pod()
  puts "You rush through the ship desperately trying to make it to"
  puts "the escape pod before the whole ship explodes.  It seems like"
  puts "hardly any Gothons are on the ship, so your run is clear of"
  puts "interference.  You get to the chamber with the escape pods, and"
  puts "now need to pick one to take.  Some of them could be damaged"
  puts "but you don't have time to look.  There's 5 pods, which one"
  puts "do you take?"

  good_pod = rand(5)+1
  print "[pod #]>"
  guess = gets.chomp()

  if guess.to_i != good_pod
    puts "You jump into pod %s and hit the eject button." % guess
    puts "The pod escapes out into the void of space, then"
    puts "implodes as the hull ruptures, crushing your body"
    puts "into jam jelly."
    return :death
  else
    puts "You jump into pod %s and hit the eject button." % guess
    puts "The pod easily slides out into space heading to"
    puts "the planet below.  As it flies to the planet, you look"
    puts "back and see your ship implode then explode like a"
    puts "bright star, taking out the Gothon ship at the same"
    puts "time.  You won!"
    Process.exit(0)
  end
end

ROOMS = {
  :death => method(:death),
  :central_corridor => method(:central_corridor),
  :laser_weapon_armory => method(:laser_weapon_armory),
  :the_bridge => method(:the_bridge),
  :escape_pod => method(:escape_pod)
}

def runner(map, start)
  next_one = start

  while true
    room = map[next_one]
    puts "\n--------"
    next_one = room.call()
  end
end

runner(ROOMS, :central_corridor)
```

你应该看到的结果
----------------

```sh
$ ruby ex41.rb

--------
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an 
escape pod.


You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body.  He's blocking the door to the
Armory and about to pull a weapon to blast you.
> dodge!
Like a world class boxer you dodge, weave, slip and slide right
as the Gothon's blaster cranks a laser past your head.
In the middle of your artful dodge your foot slips and you
bang your head on the metal wall and pass out.
You wake up shortly after only to die as the Gothon stomps on
your head and eats you.

--------
Such a luser.

$ ruby ex41.rb 

--------
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an 
escape pod.


You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body.  He's blocking the door to the
Armory and about to pull a weapon to blast you.
> tell a joke
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.

--------
You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding.  It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container.  There's a keypad lock on the box
and you need the code to get the bomb out.  If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb.  The code is 3 digits.
[keypad]> 123 
BZZZZEDDD!
[keypad]> 234
BZZZZEDDD!
[keypad]> 345
BZZZZEDDD!
[keypad]> 456
BZZZZEDDD!
[keypad]> 567
BZZZZEDDD!
[keypad]> 678
BZZZZEDDD!
[keypad]> 789
BZZZZEDDD!
[keypad]> 384
BZZZZEDDD!
[keypad]> 764
BZZZZEDDD!
[keypad]> 354
BZZZZEDDD!
[keypad]> 263
The lock buzzes one last time and then you hear a sickening
melting sound as the mechanism is fused together.
You decide to sit there, and finally the Gothons blow up the
ship from their ship and you die.

--------
You died.  You kinda suck at this.
```

加分练习
--------

1. 解释一下返回至下一个房间的运作原理。 2.建立更多的房间，让游戏规模变大。 
2. 除了让每个函式打印出自己以外，试试学习一下「文件注解(doc comments)」。 
3. 看看你能不能将房间描述写成文件注解，然后修改运行它的代码，让它把文档注解打印出来。 
4. 一旦你用了文件注解作为房间描述，你还需要让这个函式打出用户提示吗？试着让运行函数的代码打出用户提示来，然后将用户输入传递到各个函式。你的函式应该只是一些 if 语句组合，将结果印出来，并且返回下一个房间。 
5. 这其实是一个小版本的「有限状态机(finite state machine)」，找资料阅读了解一下，虽然你可能看不懂，但还是找来看看吧 


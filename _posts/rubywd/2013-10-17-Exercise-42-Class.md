---
layout: post
title: "练习42:  类" 
description: "笨方法学ruby"
category: ruby
tags: [ruby]
---
{% include JB/setup %}

虽说将函式放到 Hash 里是很有趣的一件事情，你应该也会想到「如果 Ruby 内建这件事情该多好」。事实上也的确有，那就是 ` class ` 这个关键字。你可以使用 ` class ` 创建更棒的 「函式 Hash」，比你在上节练习中做的强大多了。Class（类）有着各种各样强大的功能和用法，但本书不会深入讲这些内容，在这里，你只要你学会把它们当作高级的「函式字典」使用就可以了。

用到「` class `」的程序语言被称作「Object Oriented Programming（面向对象编程序语言」。这是一种传统的写程序的方式，你需要做出「东西」来，然后你「告诉」这些东西去完成它们的工作。类似的事 情你其实已经做过不少了，只不过还没有意识到而已。记得你做过的这个吧：

```sh
stuff = ['Test', 'This', 'Out']
puts stuff.join(' ')
```
其实你这里已经使用了 ` class `。 stuff 这个变量其实是一个 Array Class。而` stuff.join() `调用了 Array 函式中的 join，然后传递了字串` ' ' `（就是一个空格），这也是一个 class  —— 它是一个 String class (字符串类)。到处都是 class！

其实你这里已经使用了 ` class `。` stuff `这个变量其实是一个list ` class `（列表类）。而’ ‘.join(stuff)里调用函式join的字符串’ ‘（就是一个空格）也是一个` class ` ——它是一个string ` class ` (字符串类)。到处都是` class `！

还有一个概念是 object（物件），不过我们暂且不提。当你建立过几个` class ` 后就会学到了。怎样建立` class `呢？和你建立` ROOMS `Hash 的方法差不多，但其实更简单：

```sh
` class ` TheThing
  attr_reader :number

  def initialize()
    @number = 0
  end

  def some_function()
    puts "I got called."
  end

  def add_me_up(more)
    @number += more
    return @number
  end
end

# two different things
a = TheThing.new
b = TheThing.new

a.some_function()
b.some_function()

puts a.add_me_up(20)
puts a.add_me_up(20)
puts b.add_me_up(30)
puts b.add_me_up(30)

puts a.number
puts b.number
```

看到了在` @number `前面的` @ `吧？这是一个实例变量 (instance variable)。每个在` TheThing `中你建立的实例都会拥有` @number `中自己的值。我们不能透过直接打` a.number `直接拿到` number `。除非我们特别使用` attr_reader :number `，宣告让外界能存取资料。

若要让` @number write-only `，我们可以使用` attr_writer :number `。为了让它可以既可读又可写，我们可以使用` attr_accessor :number `。Ruby 使用了这些优良的物件导向原则来封装资料。

下来，看到` initialize `函式了吗？这就是你为建立 ` class ` 设置内部变量的方式。你可以用以` @ `符号开头的方式去设定它们。另外看到我们使用了` add_me_up() `为你建立` number `加值。后面你可以看到我们怎样可以使用这种方法为数字加值，然后打印出来。

Class 是很强大的东西，你应该好好读读相关的东西。尽可能多找些东西读并且多多实验。你其实知道它们该怎么用，只要试试就知道了。其实我马上就要去练吉他了，所以我不会让你写练习了。你将使用 ` class ` 写一个练习。

接下来我们将把练习 41 的内容重写一遍，不过这回我们将使用 ` class `：

```sh
` class ` Game

  def initialize(start)
    @quips = [
      "You died.  You kinda suck at this.",
      "Nice job, you died ...jackass.",
      "Such a luser.",
      "I have a small puppy that's better at this."
    ]
    @start = start
    puts "in init @start = " + @start.inspect
  end

  def prompt()
    print "> "
  end

  def play()
    puts "@start => " + @start.inspect
    next_room = @start

    while true
      puts "\n--------"
      room = method(next_room)
      next_room = room.call()
    end
  end

  def death()
    puts @quips[rand(@quips.length())]
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
      puts "Like a world ` class ` boxer you dodge, weave, slip and slide right"
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
end

a_game = Game.new(:central_corridor)
a_game.play()
```

你应该看到的结果
----------------

这个版本的游戏和你的上一版效果应该是一样的，其实有些代码都几乎一样。比较一下两版程序码，弄懂其中不同的地方，重点在需要理解这些东西：

1. 怎样建立一个 ` class ` Game 并且放函式到里面去。 
2. ` initialize `是一个特殊的初始方法，怎样预设重要的变量在里面。 
3. 你如何透过将在 ` class ` 下这个关键字再巢状排列这些定义的方式为` class ` 添加函式。 
4. 你如何透过在名称底下加进巢状内容来添加函式的。 
5. ` @ `的概念，还有它在` initialize `、` play `和` death `是怎样被使用的。 
6. 最后我们怎样建立了一个 Game，然后透过` play() `让所有的东西运行起来。 

加分练习 研究一下dict是什么东西，应该怎样使用。 再为游戏添加一些房间，确认自己已经学会使用` class ` 。 创建一个新版本，里边使用两个` class `，其中一个是Map，另一个是Engine。提示:把play放到Engine里面。

加分练习
--------

1. 再为游戏添加一些房间，确认自己已经学会使用 ` class `。 
2. 建一个新版本，里边使用两个 ` class `，其中一个是` Map `，另一个是` Engine `。提示:把 play 放到` Engine `里面。 


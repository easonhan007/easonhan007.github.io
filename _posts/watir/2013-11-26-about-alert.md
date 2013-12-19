---
layout: post
title: "爱在watir(5)————关于alert的那些事情"
description: "如何处理alert,confrim及prompt，教程其实很可以写的更好看"
category: watir
tags: [watir]
---
{% include JB/setup %}

coco病了，办公室很多人都病了，尽管秋天是伤感的季节，但不应该是流感的季节。不过很奇怪，今年的流感总是不期而至，徘徊数周，然后依依不舍的离去。好像程序员们的身体是病毒的理想宿主，因为他们总是在加班，疏于锻炼。

coco平时也不太运动，对她来说运动量最大的事情莫过于逛街，这两年电商越发红火，coco连逛街都越来越少。由于缺乏锻炼，流感一到，coco第一个缴枪投降。

tom想下班去探望一下coco，不过他实在是太忙，晚上加班到很晚，根本没有时间去嘘寒问暖，不过就算是有时间地点人物起因，tom也不敢去coco家，也就根本不会有经过和结果。

对tom开始纠结了。对于程序员来说，纠结是一种通病，他们经常在纠结中寻求最优解，到后来却发现一切只是为了寻求现实的平衡而已。

就在tom纠结的时候，coco的电话来了。

coco说她其实没有生病，只是找个借口去别的公司面试了一下而已。

别的公司?tom心中有些失落。别的公司可能薪水会更多，而且不用每天疯狂加班，这对coco是好事；但是如果coco真的走了，tom心中却又恋恋不舍，仿佛删掉自己苦心写出的功能特性一样。

coco说她面试估计是挂了，不知道怎么回事，tom竟然隐隐有些高兴。coco约tom晚上去她家吃饭，晚点也没关系，她有点事情想向tom请教。

tom忙不迭的一口答应下来，然后疯狂coding，并下定决心晚上坚决不加班。

下班的时间到了，刚从医院归来的项目经理fred宣布了一个好消息和一个坏消息。好消息是今天晚上的盒饭公司请客；坏消息是今天晚上大家都要稍微加一会班。tom还没等他说完就急匆匆的冲向大门，fred措手不及，眼睁睁的看着tom溜走，他愣在原地。

一阵沉默后，fred如梦方醒。他拨打tom的电话，却发现怎么都拨不通。fred可能不知道现在智能手机都有来电防火墙功能，而fred的号码静静的躺在tom等几个同事的黑名单里。

tom都了coco楼下，犹豫了半小时后终于上了楼；再犹豫了十五分钟后，tom终于敲了门。

这顿饭tom吃的很多，紧张感也渐渐消除。tom甚至还夸coco厨艺高超，这让coco无比受用。

饭后coco请教了tom一个问题。coco下午面试的时候被javascript alert框的问题给难住了，watir到底是怎么处理alert的呢？

tom笑了笑说："这个其实不难。"

于是tom写下了下面这些演示代码。

```ruby
# 检查alert是否存在
browser.alert.exists?

# 获取alert的文本内容
browser.alert.text

# 关闭alert
browser.alert.ok
browser.alert.close
```

tom解释说上面的代码是针对javascript里面alert()函数所弹出的对话框而进行处理的。在使用chrome浏览器的时候，按下F12，然后在Console也就是控制台里写上```alert('17test.info')回车后就可以看到alert的效果了。

与alert类似，javascript还有confrim和prompt两种原生对话框。但是由于这种对话框的样式不够优雅，体验不够良好，越来越多的网站已经不再使用原生对话框了。不过处理原生javascript对话框的方式还是应该掌握的。

tom又给出了处理confrim和prompt的代码

```ruby
# Accept confirm
browser.alert.ok

# Cancel confirm
browser.alert.close

# Enter text to prompt
browser.alert.set "Prompt answer"

# Accept prompt
browser.alert.ok

# Cancel prompt
browser.alert.close
```

讲完这一些时间已经很晚了。tom连忙告别，coco也赶紧道谢。这天晚上tom在睡觉时嘴角弯成了上弦月，谁也不知道他到底梦到了些什么。



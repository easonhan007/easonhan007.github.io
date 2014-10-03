---
layout: post
title: "ios auto layout constraint的3条规则"
description: "ios auto layout constraint的3条规则"
category: autolayout
tags: [autolayout]
---
{% include JB/setup %}

### 3个规则

Auto Layout是ios 6之后引入的自动布局方式，由于现在ios机器屏幕分辨率及大小已经五花八门，因此auto layout已经变的越来越重要。

Auto layout在使用的时候其实不太方便和直观，其中最麻烦的是constraint究竟应该设置在哪个对象上。

这时候就应该follow下面的3个规则：

* 如果constraint描述的是1个父view下的2个直接子view之间的关系，也就是说这2个子view属于同一个父view，那么就把这个constraint设置在父view上；

* 如果constraint描述的是父子之间的关系，那么把constraint设置在父view上；

* 如果constraint描述的是不在同一个父view下2个子view之间的关系，那么就要把这个constraint设置在这2个子view的共同祖先上；


### 位置关系公式

2个view之间的关系可以用下面的公式来计算

```
object1.property1 = (object2.property2 * multiplier) + constant value

```

举例来说，如果1个button位于其父view的中心，那么根据公式可以得到

```
button.center.x = (button.superview.center.x * 1) + 0
button.center.y = (button.superview.center.y * 1) + 0

```

基于此公式，我们分解一下constraintWithItem:attribute:related By:toItem:attribute:multiplier:constant:方法

* constraintWithItem: 对应object1; 

* attribute: 对应property1; 

* relatedBy: 对应公式中的等号; 

* toItem: 对应object2;

* attribute: 对应property2;

* multiplier: 对应multiplier;

* constant: 对应constant value;

因此在使用constraintWithItem:attribute:related By:toItem:attribute:multiplier:constant:方法时，最好先还原一下这个公式，这样就有的放矢了。


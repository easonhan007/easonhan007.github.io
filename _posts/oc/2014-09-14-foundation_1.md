---
layout: post
title: "Foundation教程(1)——基础"
description: "About foundation basic"
category: object-c
tags: [ios, object-c]
---
{% include JB/setup %}

Foundation是Object-C开发中所用到的底层库。提供了strings, arrays, dictionares等对象和相关方法。

Foundation对象一般有2种风格：mutable(可变的)和immutable(不可变的)。

举例来说，NSArray类可以存储一组对象，不过无法进行增删改操作，因为NSArray是不可变的。同样的，NSString对象创建后也不可以改变。

之所以有这样2种风格是因为：

* 如果1个对象是immutable的，那么这个对象就不会改变其在内存中的存储方式，因此性能会更好；

* 如果将immutable的对象传给其他对象，那么你当然就可以确定该对象不会被其他对象修改；

我们为immutable对象创建其mutable版本，比如

```

NSMutableArray *mutableArray = [NSMutableArray arrayWithArray:immutableArray];

```

Mutable和immutable对象各有其用。一般情况下，immutable对象会更加常见。





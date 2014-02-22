---
layout: post
title: "如何使用mongodb查询null条件只返回存在的document"
description: ""
category: mongodb
tags: [mongodb]
---
{% include JB/setup %}

在使用MongoDB进行find查询的时候，null条件可以显示的指定出来，如下面的例子:

```
> db.c.find()
{ "_id" : ObjectId("4ba0f0dfd22aa494fd523621"), "y" : null }
{ "_id" : ObjectId("4ba0f0dfd22aa494fd523622"), "y" : 1 }
{ "_id" : ObjectId("4ba0f148d22aa494fd523623"), "y" : 2 }

> db.c.find({"y" : null})
{ "_id" : ObjectId("4ba0f0dfd22aa494fd523621"), "y" : null }
```

这样就可以找到```y==null```所有记录了。

不过麻烦的事情是null条件还可以查出不存在该条件的记录。比如下面的例子会返回所有没有key z的记录：

```
>db.c.find({"z" : null})
{"_id" : ObjectId("4ba0f0dfd22aa494fd523621"), "y" : null }
{"_id" : ObjectId("4ba0f0dfd22aa494fd523622"), "y" : 1 }
{"_id" : ObjectId("4ba0f148d22aa494fd523623"), "y" : 2 }
```

如果我们只想返回```z==null```的所有记录，而不是__key z不存在的记录__，那么就必须这样做了。

```
> db.c.find({"z" : {"$in" : [null], "$exists" : true}})
```
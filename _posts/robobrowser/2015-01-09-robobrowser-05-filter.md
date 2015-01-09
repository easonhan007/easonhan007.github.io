---
layout: post
title: "还没被玩坏的robobrowser(5)——Beautiful Soup的过滤器"
description: "Beautiful Soup的过滤器"
category: robobrowser
tags: [robobrowser]
---
{% include JB/setup %}

### 背景  

本节的知识还是属于Beautiful Soup的内容。

Beautiful Soup的find和find_all方法非常强大，他们支持下面一些类型的过滤器。

### 字符串

最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的```<b>```标签:

```python
soup.find_all('b')
```

### 正则表达式
如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示```<body>```和```<b>```标签都应该被找到:

```python
import re
for tag in soup.find_all(re.compile("^b")):
      print(tag.name)
```

下面代码找出所有名字中包含”t”的标签:

```python
for tag in soup.find_all(re.compile("t")):
      print(tag.name)
```

### 列表 
如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有```<a>```标签和```<b>```标签:

```python
soup.find_all(["a", "b"])
```

### True
True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点

```python
for tag in soup.find_all(True):
  print(tag.name)
```

### 方法
如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 ,如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False

下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:

```python
def has_class_but_no_id(tag):
  return tag.has_attr('class') and not tag.has_attr('id')
```
将这个方法作为参数传入 find_all() 方法,将得到所有<p>标签:

``` python
soup.find_all(has_class_but_no_id)
```


文本版权归乙醇所有，欢迎转载，但请标明出处。

下一节：点击链接

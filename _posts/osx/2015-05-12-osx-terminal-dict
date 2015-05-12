---
layout: post
title: "如何在osx的终端下使用字典"
description: "如何在osx的终端下使用字典"
category: osx
tags: [osx]
---
{% include JB/setup %}

因为各种原因我经常要在osx上查英文单词，在osx系统下，查字典其实是一件非常优雅的事情，三指轻触，简单快速。在terminal中其实也是这样，3指轻触需要查询的单词，释义一触即发，用户体验非常好。不过如果没有触摸板，是否可以直接在命令行中使用命令查询单词呢？答案是肯定的，经过尝试，我发现了如下一些方案。

### 方案1:命令行中调用字典应用

```shell
open dict://the_word_you_looking_for
```

效果如下图 
![](http://images.cnitblog.com/blog2015/146263/201505/121118084234878.png)

使用这条命令可以直接打开字典应用并查询相应单词。不过这不够geek，还需要改进。

### 方案2:使用python调用系统api

osx系统中自带的python可以访问apple的一些原生api，于是便有了下面的脚本

```python
# dict.py
#!/usr/bin/python

import sys
from DictionaryServices import *

def main():
    try:
        searchword = sys.argv[1].decode('utf-8')
    except IndexError:
        errmsg = 'You did not enter any terms to look up in the Dictionary.'
        print errmsg
        sys.exit()
    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    if not dictresult:
        errmsg = "'%s' not found in Dictionary." % (searchword)
        print errmsg.encode('utf-8')
    else:
        print dictresult.encode('utf-8')

if __name__ == '__main__':
    main()
```

使用方法

```shell
chmod +x dict.py
mv dict.py dict
ln -s /where/your/dict.py/is/dict /usr/local/bin/dict
dict the_word_you_look_for
```

效果如下
```
dict hello

hello
*[hә'lәu']
interj. 喂, 嘿

```

### 方案3:在线查询

系统字典虽好，但是词汇量及相应周边有限，仍然略有不足。其实比较好的一个方案是在线查询，可以查到更多更准确的释义。

在这个方案里我们要用到terminal中运行的浏览器[w3m](http://w3m.sourceforge.net/)。

首先安装w3m

```
brew install w3m
```

然后再写一个名为youdao的shell脚本,因为我们是去有道词典进行查询，所以命名如此

```shell
touch youdao
chmod +x youdao
ln -s /where/your/youdao/is/youdao /usr/local/bin/youdao
```

其内容如下
```shell
#! /bin/sh
if [ -z "$1" ]
then
  echo 'Usage youdao <word>'
else
  w3m http://dict.youdao.com/search?q=$1
fi
```

这样使用

```
youdao the_word_you_looking_for
```

效果如下图
![](http://images.cnitblog.com/blog2015/146263/201505/121119147351188.png)


按q退出，按space向下浏览。

### 方案4:在线查询，如果不需要中文释义的话

```shell
curl dict://dict.org/d:<word_to_search_for>
```
该方案也适用于liunx

![](http://images.cnitblog.com/blog2015/146263/201505/121122037205861.png)




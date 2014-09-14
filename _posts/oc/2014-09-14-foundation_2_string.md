---
layout: post
title: "Foundation教程(2)——String"
description: "About String in Object-C"
category: object-c
tags: [ios, object-c]
---
{% include JB/setup %}

Stirng应该是计算机科学中最重要的类型了。因为我们可以直接阅读String，其他类型却不会如此的平易近人。

### 创建string

你可以这样创建1个字符串：

  NSString *emptyString = [[NSString alloc] init];

这样做表意明确而且语法正确，但这却是没多大用处的。因为NSString是immutable的(参考上一节)，所以上面的代码创建了1个空字符串，但你却无法修改它。

一般情况下，我们这样创建NSString:

  NSString *aString = @"This is a string";

@符号告诉编译器该代码是创建NSString对象而不是标准的C字符串。我们可以直接向新建的NSString发送消息：

  NSInteger sizeOfString = [@"Hello World!" length];

这种定义NSString对象的方法被称为_literals_。


### 大小写转换

  NSString *str = @"This is a string";

  // 转大写 THIS IS A STRING
  NSString *uppercaseStr = [str uppercaseString];

  // 转小写 this is a string
  NSString *lowercaseStr = [str lowercaseString];

  // 首字符大写 This Is A String
  NSString *capitalizedStr = [str capitalizedString];
  

### 子串Substring

  NSString *str = @"This is a string";
  
  // 截取前3个字符 "Thi"
  NSString *startSubStr = [str substringToIndex:3];

  // 从第3个字符开始截取 "s is a string"
  NSString *endSubString = [str substringFromIndex:3];

  // 范围截取 3-5 "is is"
  //NSRange接受2个参数from, length,其中from从0开始
  NSRange theRange = NSMakeRange(2, 5); 
  NSString *substr = [str substringWithRange:theRange];

### 字符串比较

首先要注意，*不能*像下面这样进行比较

  if(firstStr == secondStr) {
    printf("Equal\n");
  }

这是因为==仅仅比较这两个变量的指针，而不是比较其指向的值。实际上上面代码的作用是比较2个指针是不是指向同一块内存区域。

这样比较才是正确的:

  if([firstStr isEqualToString:secondStr]) {
    // do something
    printf("Equal\n");
  }

isEqualToString方法是大小写敏感的。this 和 This是不相等的字符串。


### 搜索字符串

rangeOfString方法可以判断1个字符串是否包含另一个子串。该方法返回NSRange，如果子串不存在字符串种，那么NSRange的location属性就等于NSNotFound常量。

  NSString *str = "This is a string";
  NSRange range = [str rangeOfString:@"that"];

  if(range.location == NSNotFound) {
    // not found
  } else {
    found 
  }

在搜索子串时还可以指定忽略大小写

  NSString* sourceString = @"Four score and seven years ago";
  NSRange range = [sourceString rangeOfString:@"SEVEN"
                               options:NSCaseInsensitiveSearch];

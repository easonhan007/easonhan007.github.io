---
layout: post
title: "IOS每日一练(2)--UISwitch的使用"
description: "如何使用UISwitch"
category: ios
tags: [ios]
---
{% include JB/setup %}

## 背景

app需要让用户去开关某些选项。

## 解决方案

最简单的办法是使用UISwitch类。

## 示例

首先在ViewController.m中添加mianSwitch属性

```objective-c
#import "ViewController.h"

@interface ViewController ()
@property (nonatomic, strong) UISwitch *mainSwitch;
@end

@implementation ViewController

```

然后在viewDidLoad方法中添加初始化mainSwitch的代码。

```objective-c
- (void)viewDidLoad {
  [super viewDidLoad];

  self.mainSwitch = [[UISwitch alloc] initWithFrame:
                     CGRectMake(100, 100, 0, 0)];

  [self.view addSubview:self.mainSwitch];
}

```

可以使用UISwitch对象的setOn:方法来改变switch的状态。

```objective-c
[self.mainSwitch setOn:YES];
```

通过UISwitch对象的isOn方法来判断开关的状态。

```objective-c
if ([self.mainSwitch isOn]) {
    NSLog(@"Is ON");
} else {
    NSLog(@"Is OFF");
}
```

我们还可以给UISwitch对象添加target来监听开关的状态改变

```objective-c
[self.mainSwitch addTarget:self
                    action:@selector(switchIsChanged:)
          forControlEvents:UIControlEventValueChanged];

- (void)switchIsChanged:(UISwitch *)paramSender {
  NSLog(@"Sender is = %@", paramSender);
  
  if ([paramSender isOn]) {
      NSLog(@"The switch is turned on");
  } else {
      NSLog(@"The switch is turned off");
  }
}

```

最后完整代码如下：

```objective-c
- (void)viewDidLoad {
  [super viewDidLoad];
  // Do any additional setup after loading the view, typically from a nib.
  self.mainSwitch = [[UISwitch alloc] initWithFrame:
                     CGRectMake(100, 100, 0, 0)];
  [self.mainSwitch setOn:YES];
  if ([self.mainSwitch isOn]) {
      NSLog(@"Is ON");
  } else {
      NSLog(@"Is OFF");
  }
  
  [self.mainSwitch addTarget:self
                      action:@selector(switchIsChanged:)
            forControlEvents:UIControlEventValueChanged];
  
  [self.view addSubview:self.mainSwitch];
}


- (void)switchIsChanged:(UISwitch *)paramSender {
  NSLog(@"Sender is = %@", paramSender);
  
  if ([paramSender isOn]) {
      NSLog(@"The switch is turned on");
  } else {
      NSLog(@"The switch is turned off");
  }
}

```

在控制台中，你将看到如下日志：

```
The switch is turned on
Sender is =<UISwitch: 0x7f8678c7e4e0; 
frame = (100 100; 51 31); 
layer = <CALayer: 0x7f8678c7b730>>
```


## 思考题

如何去定制UISwitch的样式。



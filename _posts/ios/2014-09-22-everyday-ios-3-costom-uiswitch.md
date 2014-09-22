---
layout: post
title: "IOS每日一练(3)--定制UISwitch"
description: "定制UISwitch"
category: ios
tags: [ios]
---
{% include JB/setup %}

## 背景
需要定制UISwitch的样式。

## 解决方案
使用tintColor和onTintColor等属性。


## 示例

```objective-c
#import "ViewController.h"

@interface ViewController ()
@property (nonatomic, strong) UISwitch *mainSwitch;
@end

@implementation ViewController

- (void)viewDidLoad {
  [super viewDidLoad];
  // Do any additional setup after loading the view, typically from a nib.
  self.mainSwitch = [[UISwitch alloc] initWithFrame:CGRectZero];
  self.mainSwitch.center = self.view.center;
  [self.view addSubview:self.mainSwitch];
  
  // custom the switch
  self.mainSwitch.tintColor = [UIColor redColor];
  self.mainSwitch.onTintColor = [UIColor brownColor];
  self.mainSwitch.thumbTintColor = [UIColor greenColor];
    
    // how to use on and off image since ios6
//    self.mainSwitch.offImage = self.mainSwitch.onImage = [UIImage imageNamed:@"On"];
//    self.mainSwitch.offImage = self.mainSwitch.offImage = [UIImage imageNamed:@"Off"];
    
}
```
上面代码讲switch的关闭时的颜色设置成了红色，开启时候是灰色，小圆点设置成绿色。

由此可知，定制UISwitch的颜色可以使用下面的属性：

* tintColor:关闭时候的颜色

* onTintColor:开启时候的颜色

* thumbTintColor:圆点的颜色

**注意，上述属性只适用于ios6及以后的版本**

另外可以替换switch的开启和关闭的图片,具体属性是```onImage```和```offImage```。**图片大小必须是77*22。**



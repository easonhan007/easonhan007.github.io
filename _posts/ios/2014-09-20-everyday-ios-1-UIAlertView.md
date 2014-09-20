---
layout: post
title: "IOS每日一练(1)--UIAlertView的使用"
description: "如何使用UIAlertView"
category: ios
tags: [ios]
---
{% include JB/setup %}

## 背景

app需要给用户一些提示，比如需要提示用户进行确认，要求用户输入用户名和密码等。

## 解决方案

最简单的办法是使用UIAlertView类。

## 示例

### 最简模式

```objective-c
- (void)viewDidAppear:(BOOL)animated {
	[super viewDidAppear:animated];

  UIAlertView *alert = [[UIAlertView alloc]
                        initWithTitle:@"Alert"
                        message:@"You will see the alert"
                        delegate:nil
                        cancelButtonTitle:@"Cancel"
                        otherButtonTitles:@"OK",nil];
  [alert show];
}
```

UIKit提供了如下4种的Alert样式：

```objective-c
typedef NS_ENUM(NSInteger, UIAlertViewStyle) {
	UIAlertViewStyleDefault = 0, 
	UIAlertViewStyleSecureTextInput, 
	UIAlertViewStylePlainTextInput,
	UIAlertViewStyleLoginAndPasswordInput
};
```
上面的例子默认使用了第一种

### 如何判断用户点击了哪个按钮

这需要实现UIAlertViewDelegate协议，并且实现**alertView:clickedButtonAtIndex:**方法。

```objective-c
// ViewController.h
#import <UIKit/UIKit.h>

@interface ViewController : UIViewController <UIAlertViewDelegate>
@end
```

首先在ViewController中添加下面2个方法，用于返回alert中按钮的title：

```objective-c
- (NSString *)yesButtonTitle {
    return @"Yes";
}

- (NSString *)noButtonTitle {
    return @"No";
}
```
然后在viewDidAppear:animated方法中添加如下代码

```objective-c
- (void)viewDidAppear:(BOOL)animated {
  [super viewDidAppear:animated];
    
  self.view.backgroundColor = [UIColor whiteColor];
  NSString *message = @"Are you sure you want to open this link in Safari";
  
  UIAlertView *alert = [[UIAlertView alloc]
                        initWithTitle:@"Open Link"
                        message:message
                        delegate:self
                        cancelButtonTitle:[self noButtonTitle]
                        otherButtonTitles:[self yesButtonTitle], nil];
  [alert show];
}
```

最后实现alertView:clickedButtonAtIndex:方法

```objective-c
- (void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex {
  NSString *btnTitle = [alertView buttonTitleAtIndex:buttonIndex];
  
  if ([btnTitle isEqualToString:[self yesButtonTitle]]) {
      NSLog(@"User click YES button");
  } else if ([btnTitle isEqualToString:[self noButtonTitle]]) {
      NSLog(@"User click NO button");
  }
}

```
这里需要注意，我们使用了alertView对象的buttonTitleAtIndex:方法来获取被点击按钮对应的title，然后通过判断title来确定究竟是哪个按钮被点击了。

这样做的好处是增加了代码的可读性和可维护性，修改的过程中不容易引入缺陷。

### 获取用户输入

下面的代码演示了如何获取用户输入的信用卡号

```objective-c
- (void)viewDidAppear:(BOOL)animated {
  // 获取用户的信用卡号
  UIAlertView *alert = [[UIAlertView alloc]
                        initWithTitle:@"Credit Card Number"
                        message:@"Please enter your credit card number"
                        delegate:self
                        cancelButtonTitle:@"Cancel"
                        otherButtonTitles:@"OK", nil];
  [alert setAlertViewStyle:UIAlertViewStylePlainTextInput];
  
  UITextField *textField = [alert textFieldAtIndex:0];
  textField.keyboardType = UIKeyboardTypeNumberPad;
  [alert show];
}
```

## 思考题

如何使用UIAlertView实现提示用户输入密码以及提示用户输入用户名和密码进行登陆?



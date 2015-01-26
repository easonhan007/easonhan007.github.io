---
layout: post
title: "使用swift和rails来实现ios账号系统"
description: "User Accounts on iOS with Ruby on Rails and Swift"
category: ios
tags: [ios]
---
{% include JB/setup %}

前不久看到这样一篇教程[User Accounts on iOS with Ruby on Rails and Swift](http://www.raywenderlich.com/85528/user-accounts-ios-ruby-rails-swift)，里面描述了如何使用swift和rails来前后台配合来实现一个简单的类似twitter的东东。

不过里面使用到了亚马逊河heroku的云服务，在我泱泱大国，海外蛮夷的这些雕虫小技我们是用不上的。于是便随手修改了一下，把rails的后台改成了纯本地实现，摒弃了亚马逊的存储服务和heroku的托管，一切变得和谐多了。修改过后的程序源码在[这里](https://github.com/easonhan007/railsauth).现在终于可以愉快的学习这个教程了。

### 使用方法

```
git clone https://github.com/easonhan007/railsauth.git

cd railsauth

bundle 

rails s

```

本地服务已经起了，然后就可以follow原教程的步骤进行学习了。

注意，下载好原教程的脚手架代码后，记得把HTTPHelper.swift这个里的

```swift
static let API_AUTH_NAME = "<YOUR_HEROKU_API_ADMIN_NAME>"
static let API_AUTH_PASSWORD = "<YOUR_HEROKU_API_PASSWORD>"
static let BASE_URL = "https://XXXXX-XXX-1234.herokuapp.com/api"
```

修改为

```swift
static let API_AUTH_NAME = "eason"
static let API_AUTH_PASSWORD = "password"
static let BASE_URL = "http://localhost:3000/api"
```

应该一切都就绪了，现在终于可以去学习一下原教程了。

---
layout: post
title: "安装wamp和wordpress"
description: "快速搭建wordpress的开发环境"
category: 
tags: [wordpress]
---
{% include JB/setup %}

### 下载安装包

点击[这里](http://pan.baidu.com/s/1iO9OD)__提取密码:rkzz__下载所有安装包。

### 安装wamp

[WAMP]()是一个windows上的php开发集成环境，一键安装php,apache和mysql，非常方便。

双击wampserver2.2exxxxxxxxxx.exe文件进行安装，安装过程中直接下一步即可。

注意一下mysql安装时候的默认root密码，这个很关键，不然等会安装wordpress的时候就会比较麻烦。

另外安装过iis的同学注意停掉iis服务，因为iis占用80端口与apache的默认端口会发生冲突。

成功安装完wamp后桌面右下角的任务栏里应该会出现一个小托盘，点击这个托盘，在弹出菜单里选择倒数第四项__启动所有服务__。如果托盘变绿，那么安装成功，否则安装有问题，需要自己再三检查。

### 安装wordpress

解压wordpress-3.5.2-zh_CN.zip文件，注意，直接解压到当前目录就好了。

将解压出来的文件重命名成wordpress,并放到你的wamp安装路径下的www目录下。

例如，如果你的wamp安装在D盘，那么你应该将解压出的文件夹放到D:\wamp\www这个路径下。

在浏览器里访问http://localhost/wordpress/。

这时候应该出现wp-config.php文件不存在的提示，点击__创建配置文件__按钮。

然后又是一段提示，这时候点击__现在就开始__按钮。

这时候会出现配置数据库的表单。

* 数据库名默认test；
* 用户名填写root
* 密码为空，但是要输入一个空格；
* 数据库主机和表前缀都不要修改；

继续下一步，下面将创建wordpress blog的一些基本信息。

注意admin的密码一定要记住，不然后面的工作就有点麻烦了。

设置完站点信息后就基本完事了，恭喜大家得到了自己的第一个wordpress blog。
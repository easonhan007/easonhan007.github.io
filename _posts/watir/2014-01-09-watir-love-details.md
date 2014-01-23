---
layout: post
title: "爱在watir(8)————细枝末节"
description: "关于watir webdriver的细节"
category: watir
tags: [watir]
---
{% include JB/setup %}

一个人的时候，tom喜欢把音乐声音放大最大，这样就没人可以打扰到他。在这段时间里，他是纯粹的，什么都不用想，一种断层的空灵。

不过很可惜，工作以后tom越来越难得的完全放空一次。有人通过喝酒将自己放空，有人通过运动将自己放空，tom喜欢音乐，各种声音交杂在一起，他感到轻松，如释重负。

tom最近心里总是藏着一些事情，像是负担着一块石头，总是无法落地。他清楚自己是记挂着coco，因为过完年coco很可能会离开，匆匆却又从容不迫，也许离开后他们将再无交集。离开代表着结束，尽管从未开始。

coco进来问问题的频率渐渐高了起来，她现在能将一些连贯的事情通过watir的代码去完成了，于是乎能接触到更多的细节，也就是各种大坑小坑，偶尔栽进去一次是很正常的，爬起来，拍拍身上的尘土继续向前，这才是接近成功的态度。

有些细节coco现在可以自己解决了，因为乙醇翻译的[watir-webdriver官方文档](www.17test.info)里有很多，有一些是很不起眼但却是很重要的细节，coco将这些细节记录下来，下次遇到就不会摔得头破血流了。

比如自动下载。在webdriver里，下载并不是通过点击下载链接然后操作浏览器弹出的一些dialog来实现的。在watir-webdriver里，应该通过配置去实现自动下载的功能。代码如下：

```
# firefox

download_directory = "#{Dir.pwd}/downloads"
download_directory.gsub!("/", "\\") if Selenium::WebDriver::Platform.windows?
 
profile = Selenium::WebDriver::Firefox::Profile.new
profile['browser.download.folderList'] = 2 # custom location
profile['browser.download.dir'] = download_directory
profile['browser.helperApps.neverAsk.saveToDisk'] = "text/csv,application/pdf"
 
b = Watir::Browser.new :firefox, :profile => profile

# chrome 

download_directory = "#{Dir.pwd}/downloads"
download_directory.gsub!("/", "\\") if  Selenium::WebDriver::Platform.windows?
 
profile = Selenium::WebDriver::Chrome::Profile.new
profile['download.prompt_for_download'] = false
profile['download.default_directory'] = download_directory
 
b = Watir::Browser.new :chrome, :profile => profile

```

还有就是cookie，通过cookie可以实现一些自动登陆的功能。chrome和firefox启动的时候是不会带上登录态的，这点困扰了coco很久，后来tom告诉她可以通过设置cookie来模拟一个登陆的状态，watir webdriver中cookie的操作是很简单的。

```
require 'watir-webdriver'
browser = Watir::Browser.new
browser.cookies.clear
browser.cookies.add 'foo', 'bar', :path => "/", :expires => 10.days.from_now, :secure => true
browser.cookies.delete 'foo'
browser.cookies.to_hash

```

最后一点就是basic authentication。这个东西的表象是访问一个页面，然后弹出一个类似原生js弹出框的东西，要输入用户名和密码才能继续访问。coco一开始总是想着用什么办法往弹出框里写入内容，后来tom及时纠正了她。处理basic authentication的方法应该是将用户名和密码放到url里。

```
require 'watir-webdriver'
b = Watir::Browser.start 'http://admin:password@yourwebsite.com'
```

从知道到能做到，细节往往是最大的敌人。细节是木桶的那块短板，阿哥琉斯的脚踝，往往都是最脆弱也是最容易被忽视的地方。

tom就觉得自己被coco忽视了，coco却一直在等待，她觉得两人之间的窗户纸需要男性来捅破才最为合理。两人陷入了一种微妙的平衡，一边是积极主动却见好就收，另一边则是游刃有余却默默等待。一切看似很好，平静而和谐，但两人心里都是深深的焦虑。

离开等于结束？或是尽快开始，不要去纠结一些细枝末节的事情？

接近年底，tom手头上的事情渐渐少了，他可以早点回家，把自己关在房里，把音乐调到最大声，享受喧闹的宁静。

coco也不太加班了，她一人走在回家的路上，北风瑟瑟，也许有人陪自己一起吃饭也是一件很惬意的事情。她想到了tom，第一时间想到了tom，实际上她现在总有想到tom，有问题找tom成了她的习惯。据说一件事情只要坚持60天就可以成为习惯，从coco刚折腾watir开始，时间不知不觉过去了好几个月。tom把自己变成了coco的习惯，只是两个人都没有意识到这一点。

四周行人匆匆，偶尔有情侣并肩走过，爱情有一种感染力，让相爱的人感到更幸福，却让孤独的人感到更孤独。

coco拨通了tom的电话，也许一切都可以从今夜正式开始。

tom沉浸在重金属的硬摇滚声浪里，旁若无物。

床头，电话有规律的震动着。

电话那头，coco终于放弃了尝试。她决定回家，零食还有很多，看来足够疗伤。

就在coco刚走到小区门口的那一刻，全城停电。人们开始咒骂，开始尖叫，黑暗让孤独更加立体。

伤感涌上心头。coco有点想哭。

"当你孤单你会想起谁，是不是想找个人来陪?"

这句话是即是coco现在的心声，也是coco手机的铃声。铃声响起，在黑暗中显得格外悠扬，格外响亮......



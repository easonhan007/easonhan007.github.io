---
layout: post
title: "rails4 routes基本使用"
description: "rails4 routes基本使用"
category: rails4
tags: [rails4]
---
{% include JB/setup %}

### 限制http method

基本方式

```ruby
match 'products/:id' => 'products#show', via: :get
```

简写

```ruby
get 'products/:id' => 'products#show'
post 'products' => 'products#create'

```

同一个url对应多个http method

```ruby
match 'products/:id' => 'products#show', via: [:get, :post]
```

一个url对应所有http method

```ruby
match 'products' => 'products#index', via: :any
```

### Segment Keys

基本方式

```ruby
get 'products/:id' => 'products#show'
```
这样的话http://example.com/products/4,params[:id] = 4;

```ruby
link_to "Products",
        controller: "products",
        action: "show",
        id: 1
```

### Optional Segment Keys

如下所示，用小括号()

```ruby
aatch ':controller(/:action(/:id(.:format)))', via: :any
```

### Redirect Routes

定义routes时直接定义跳转逻辑，使用redirect方法

```ruby
get "/google", to: redirect('https://google.com/')
```

redirect方法接受block，可以接收params参数

下面实现了api的version跳转，api内部逻辑升级，但对外接口保持不变

```ruby
match 'api/v1/:api',
      to: redirect { |params| "api/v2/#{params[:api].pluralize}" },
      via: any
```
redirect方法可以设置跳转时的status

```ruby
match "/api/v1/:api", to:
  redirect(status: 302) { |params| "/api/v2/#{params[:api].pluralize}" },
  via: :any

```

### Segment Key Constraints

```ruby

get ':controller/show/:id' => :show, constraints: {:id => /\d+/}
get ':controller/show/:id' => :show_error

```
上面的例子里就不需要在controller里判断id是否合法了。另外routes里默认正则默认加\A#regexp#\z的

由于经常要对id的格式做限制，上面的例子有简写的办法


```ruby

get ':controller/show/:id' => :show, id: /\d+/
get ':controller/show/:id' => :show_error

```

constraints也可以接收block

```ruby
get 'records/:id' => "records#protected",
constraints: proc { |req| req.params[:id].to_i < 100 }

```

### Route Globbing

对于这个url /items/list/base/books/fiction


```ruby

get 'items/list/*specs', controller: 'items', action: 'list'

```

可以得到params[:specs] = base/books/fiction


### Named routes

基本用法

```ruby
get 'help' => 'help#index' as: 'help'

link_to "Help", help_path

```

Level up

对于下面的link_to调用

```ruby

get "item/:id" => "items#show"

link_to "Auction of #{item.name}", controller: "items",
action: "show",
id: item.id

```

可以定义为

```ruby

get "item/:id" => "items#show", as: "item"

link_to "Auction of #{item.name}", item_path(id: item.id)

```

加点语法糖衣，等于

```ruby
link_to "Auction of #{item.name}", item_path(item.id)

link_to "Auction of #{item.name}", item_path(item)
```

Level up

对于多个参数，要按顺序传

```ruby

get "auction/:auction_id/item/:id" => "items#show", as: "item"

link_to "Auction of #{item.name}", item_path(auction, item)

```

Level up

隐藏id，创建更可读的url

```ruby
defto_param
  description.parameterize 
end

item_path(auction, item) => /auction/3/item/cello-bow

```

### Scoping Routing Rules

scope之前

```ruby
get'auctions/new'=>'auctions#new' 
get'auctions/edit/:id'=>'auctions#edit' 
post'auctions/pause/:id'=>'auctions#pause'
```
scope之后

```ruby
scope controller::auctions do
  get 'auctions/new' => :new
  get 'auctions/edit/:id' => :edit 
  post 'auctions/pause/:id' => :pause
end

```

scope path后

```ruby
scope path:'/auctions',controller::auctions do 
  get 'new' => :new
  get 'edit/:id' => :edit
  post 'pause/:id' => :pause
end
```

使用name prefix

```ruby
scope:auctions,as:'admin' do
  get 'new' => :new, as: 'new_auction' #=>link_to 'xxx', admin_new_auction_url
end
```

namespace隐式定义了controller和path以及prefix name

```ruby
namespace :auctions,:controller=>:auctions do 
  get 'new' => :new
  get 'edit/:id' => :edit
  post 'pause/:id' => :pause
end

```

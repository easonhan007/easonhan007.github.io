---
layout: post
title: "让sublime使用vim模式"
description: "让sublime使用vim模式"
category: sublime
tags: [sublime, vim]
---
{% include JB/setup %}

如何在sublime中启用vim模式
--------------------------

在Setting-User中增加如下配置，重新启动sublime既可

	{
			"ignored_packages": [],
			"vintage_start_in_command_mode": true
	}

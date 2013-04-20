---
layout: page
title: 乙醇的blog
tagline: Supporting tagline
---
{% include JB/setup %}
## All Posts

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>




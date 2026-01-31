---
title: "Home"
layout: default
---

👋 Welcome to my blog!  
Hope you get some fun here! 😄

* Table of Contents
{:toc}


## 📝 Latest Posts

<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      <span>📅 ({{ post.date | date: "%Y-%m-%d" }})</span>
      <div>
        {{ post.excerpt | strip_html | truncate: 160 }}
      </div>
    </li>
  {% endfor %}
</ul>
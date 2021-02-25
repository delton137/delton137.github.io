---
id: 2115
title: Articles
date: 2015-09-22T20:03:57+00:00
author: delton137
layout: page
geo_public:
---

Note: After 02-03-2021, new articles are posted on my <a href="https://danelton.substack.com/">Substack</a><br />! Please subscribe there!

<ul class="listing">
{% for post in site.posts %}
    {% if post.layout == "post" %}
        {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
        {% if year != y %}
            {% assign year = y %}
            <li class="listing-seperator">{{ y }}</li>
        {% endif %}
        <li class="listing-item">
            <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
            <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
        </li>
    {% endif %}
{% endfor %}
</ul>

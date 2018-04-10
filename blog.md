---
id: 2114
title: Blog
date: 2018-04-08T20:03:57+00:00
author: delton137
layout: page
guid: https://moreisdifferent.wordpress.com/?page_id=2114
geo_public:
---

<ul class="listing">
{% for post in site.posts %}
    {% if post.layout == "blog" %}
        {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
        {% if year != y %}
            {% assign year = y %}
            <li class="listing-seperator">{{ y }}</li>
        {% endif %}
        <li class="listing-item">
            <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
            <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
            <div class="entry">
              {{ post.content | truncatewords:40}}
            </div>
            <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
        </li>
    {% endif %}
{% endfor %}
</ul>

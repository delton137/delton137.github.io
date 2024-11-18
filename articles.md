---
id: 2115
title: Articles
date: 2015-09-22T20:03:57+00:00
author: delton137
layout: page
geo_public:
---

Note: As of February 2021, new articles are mostly being posted on [my Substack](https://moreisdifferent.blog/)!

<iframe src="https://moreisdifferent.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

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
    {% if post.layout == "redirected" %}
    {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
    {% if year != y %}
        {% assign year = y %}
        <li class="listing-seperator">{{ y }}</li>
    {% endif %}
    <li class="listing-item">
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
        <a href="{{ post.redirect_to }}" title="{{ post.title }}">{{ post.substacktitle}}</a>
    </li>
    {% endif %}
{% endfor %}
</ul>

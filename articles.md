---
id: 2115
title: Articles
date: 2015-09-22T20:03:57+00:00
author: delton137
layout: page
geo_public:
---

Note: As of February 2021, most new articles are being posted on [my Substack](https://moreisdifferent.blog/)!

<iframe src="https://moreisdifferent.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

<ul class="listing">
{% assign year = "" %}
{% for post in site.posts %}
    {% if post.hidden %}
        {% continue %}
    {% endif %}

    {% capture y %}{{ post.date | date:"%Y" }}{% endcapture %}
    {% if year != y %}
        {% assign year = y %}
        <li class="listing-seperator">{{ y }}</li>
    {% endif %}

    {% if post.layout == "post" %}
        <li class="listing-item">
            <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
            <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
            {% if post.metascience %}
              <span class="badge badge-metascience">Metascience</span>
            {% endif %}
            {% if post.progress_studies %}
              <span class="badge badge-progress">Progress Studies</span>
            {% endif %}
            {% if post.fda %}
              <span class="badge badge-fda">FDA</span>
            {% endif %}
            {% if post.ai %}
              <span class="badge badge-ai">AI</span>
            {% endif %}
        </li>
    {% elsif post.layout == "redirected" %}
        <li class="listing-item">
            <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
            <a href="{{ post.redirect_to }}" title="{{ post.title }}">{{ post.substacktitle }}</a>
            {% if post.metascience %}
              <span class="badge badge-metascience">Metascience</span>
            {% endif %}
            {% if post.progress_studies %}
              <span class="badge badge-progress">Progress Studies</span>
            {% endif %}
            {% if post.fda %}
              <span class="badge badge-fda">FDA</span>
            {% endif %}
            {% if post.ai %}
              <span class="badge badge-ai">AI</span>
            {% endif %}
        </li>
    {% endif %}
{% endfor %}
</ul>

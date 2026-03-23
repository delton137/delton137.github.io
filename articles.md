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

<div class="tag-filters">
  <span>Filter:</span>
  <button class="badge filter-btn active" data-filter="all">All</button>
  <button class="badge badge-metascience filter-btn" data-filter="metascience">Metascience</button>
  <button class="badge badge-progress filter-btn" data-filter="progress_studies">Progress Studies</button>
  <button class="badge badge-fda filter-btn" data-filter="fda">FDA</button>
  <button class="badge badge-ai filter-btn" data-filter="ai">AI</button>
  <button class="badge badge-covid filter-btn" data-filter="covid">Long COVID</button>
</div>

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
        {% capture tags %}{% if post.metascience %}metascience {% endif %}{% if post.progress_studies %}progress_studies {% endif %}{% if post.fda %}fda {% endif %}{% if post.ai %}ai {% endif %}{% if post.covid %}covid {% endif %}{% endcapture %}
        <li class="listing-item" data-tags="{{ tags | strip }}">
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
            {% if post.covid %}
              <span class="badge badge-covid">Long COVID</span>
            {% endif %}
        </li>
    {% elsif post.layout == "redirected" %}
        {% capture tags %}{% if post.metascience %}metascience {% endif %}{% if post.progress_studies %}progress_studies {% endif %}{% if post.fda %}fda {% endif %}{% if post.ai %}ai {% endif %}{% if post.covid %}covid {% endif %}{% endcapture %}
        <li class="listing-item" data-tags="{{ tags | strip }}">
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
            {% if post.covid %}
              <span class="badge badge-covid">Long COVID</span>
            {% endif %}
        </li>
    {% endif %}
{% endfor %}
</ul>

<script>
document.addEventListener('DOMContentLoaded', function() {
  function applyFilter(filter) {
    var buttons = document.querySelectorAll('.filter-btn');
    buttons.forEach(function(b) { b.classList.remove('active'); });
    var active = document.querySelector('.filter-btn[data-filter="' + filter + '"]');
    if (active) active.classList.add('active');

    var items = document.querySelectorAll('.listing-item');
    items.forEach(function(item) {
      if (filter === 'all') {
        item.style.display = '';
      } else {
        var tags = item.getAttribute('data-tags') || '';
        item.style.display = tags.indexOf(filter) !== -1 ? '' : 'none';
      }
    });

    var separators = document.querySelectorAll('.listing-seperator');
    separators.forEach(function(sep) {
      var hasVisible = false;
      var next = sep.nextElementSibling;
      while (next && !next.classList.contains('listing-seperator')) {
        if (next.classList.contains('listing-item') && next.style.display !== 'none') {
          hasVisible = true;
          break;
        }
        next = next.nextElementSibling;
      }
      sep.style.display = hasVisible ? '' : 'none';
    });
  }

  document.querySelectorAll('.filter-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var filter = this.getAttribute('data-filter');
      applyFilter(filter);
      history.replaceState(null, '', filter === 'all' ? location.pathname : '?tag=' + filter);
    });
  });

  // Auto-apply filter from URL parameter
  var params = new URLSearchParams(location.search);
  var tag = params.get('tag');
  if (tag) applyFilter(tag);
});
</script>

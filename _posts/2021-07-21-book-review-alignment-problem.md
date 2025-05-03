---
id: 10018
title: Book review of &#8220;The Alignment Problem&#8221; by Brian Christian
facebookcomments: true
author: Dan Elton
layout: post
permalink: /2021/07/21/book-review-alignment-problem.html
categories:
  - AI safety
  - Machine learning
  - AI
tags:
  - AI safety
  - Machine learning
  - AI
ai: true
---
<figure><img class="alignright" src="/assets/Alignment_Problem_cover.jpeg" alt="The Alignment Problem book cover" width="200" height="300" /></figure>

**_The Alignment Problem_**
476 pages (329 pages text, the rest is footnotes/index). 
By Brian Christian


This book is the culmination of over a year of dedicated work and interviews with over 100 world-class experts. The brilliant thing about this book is that it is so information dense and full of interesting anecdotes that people of any level of expertise stand to gain something from it. He’s carefully tuned it so a wide variety of people can enjoy it without getting bored or overwhelmed. 

This book covers the well known problems of bias and brittleness in machine learning, including the following well-known cases - the Richard Caruana’s example of pneumonia triage system that went haywire, the COMPAS parole recommendation system, the Google Photos “gorilla” tag fiasco, word2vector gender bias, and the 2018 fatal Uber car crash in Tempe, Arizona. You’d be mistaken to think of this as just another book warning about data bias, lack of robustness, and the potential for discrimination and the perpetuation of inequalities, however. 
 
Sprinkled between the warnings and calls for action are remarkably clear descriptions of modern machine learning techniques and how they relate and/or were inspired by recent developments in neuroscience, cognitive science, developmental psychology, and the social sciences. The author dives into the nitty gritty of how present day AI systems work and does not shy away from explaining current technical challenges.

 The way he explains reinforcement learning and links it to research on the dopamine in the brain was one of the highlights of the book for me  (I had forgotten how dopamine was linked to temporal difference error, and his description of the history of study on dopamine was fascinating). Not all of the concepts were new to me, but in every case the way he explained each concept was very new to me and wonderful to read. I learned new concepts too. For instance, I never understood what the difference between “on policy” and “off policy” RL systems was until I read his explanation. Other concepts I picked up were “cooperative reinforcement learning”, “shaping”, and various “impact metrics”. If you haven’t heard of these terms and are interested in AI safety, I heartily recommend this book. 

This book follows a trend of seamlessly linking near term and far term AI safety concerns which has been a trend since the publication of Nick Bostrom’s 2014 meditation on far future AI, “Superintelligence”. The book is very “down to earth” -- you may be surprised that the standard arguments about why we should be concerned about long term AI risk that we’ve heard from Elon Musk, Sam Harris, etc are largely absent from this book (most notoriously, the “paperclip maximizer”). This is refreshing because those arguments draw on assumptions (such as fast takeoff) which are very hard to defend with empirical data or the current science on AI. (I still find those arguments convincing enough to warrant serious investment of resources to prevent risk, but they aren’t necessarily the best first arguments to present to someone)  Instead the author follows an ingenious strategy - he starts with current problems in AI and some near future concerns (for instance with driverless cars driving off the road or home robots that refuse to be turned off.) Then, by providing sufficient technical background, he proceeds to explain why these are really hard problems, some of the solutions that are being worked on, and the limitations of the solutions proposed so far. The book is cautiously optimistic, showing how meaningful progress on the alignment problem is already occurring. So far the problems with AI that we are encountering *right now* appear tractable, which should motivate more people and resources to flow into AI Safety rather than trying to regulate progress to a standstill, which is  impossible and likely to be harmful.  At the same time, however, by the end of the book the reader will have a deep appreciation of the challenges ahead and the need for extreme caution as we move towards more and more intelligent and powerful AI. 

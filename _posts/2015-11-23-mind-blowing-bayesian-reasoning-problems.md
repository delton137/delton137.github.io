---
id: 2321
title: More counterintuitive Bayesian reasoning problems
comments: true
date: 2015-11-23T05:53:22+00:00
author: delton137
layout: post
guid: https://moreisdifferent.wordpress.com/?p=2321
permalink: /2015/11/23/mind-blowing-bayesian-reasoning-problems/
geo_public:
  - "0"
publicize_google_plus_url:
  - https://plus.google.com/+DanElton/posts/QoHaUzPMN5V
publicize_twitter_user:
  - moreisdifferent
publicize_tumblr_url:
  - http://.tumblr.com/post/133779008298
publicize_path_id:
  - 5652a9dfc3e83f8bb15821c0
categories:
  - Bayesian inference
  - machine learning
  - statistics
tags:
  - Bayesian inference
  - machine learning
  - statistics
---
Remember how in my last post I said Bayesian reasoning is counter-intuitive? It&#8217;s simultaneously maddening and fascinating because clearly, given we accept with certainty the assumptions that go into model/hypothesis selection and the prior, the application of Bayes&#8217; theorem gives the correct probability for each model/hypothesis in light of the evidence presented.

Last time I gave the canonical example of a test for a disease. Humans tend to not take into account that if the base rate (over all frequency of having a disease) is very low, then a positive result on a test may not be very meaningful. If the probability of the test giving a false positive is 1%, and the base rate is also 1%, then the chance that you have disease given a positive result is only 50%. Once you understand this, the non-intuitive nature goes away.

Here I will give two more examples of highly non-intuitive Bayesian problems.

# The Monty Hall problem

The famous Monty Hall problem can be solved with Bayes&#8217; rule. A statement of the problem is:

_There are three doors, labelled 1, 2, 3. A single prize has been hidden between one of them. You get to select one door. Initially your chosen door will not be opened. Instead, the gameshow host will choose one of the other two doors, and he will do so in such a way as to not reveal the prize. After this, you will be given a fresh choice among the 2 remaining doors &#8211; you can stick with your first choice, or switch to the other closed door._

Imagine you picked door 1. The gameshow host picks door 3, opening to reveal no prize. Should you (a.) stick with door 1, (b.) switch to door 2, or (c.) does it make no difference?

If you have not heard of this problem before, think it over a while.

The Bayes&#8217; theorem solution is as follows: Denote the possible outcomes as:

 <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-9f65a1cfa19cc02fe1c8f54a8919d33a_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#68;&#95;&#49;" title="Rendered by QuickLaTeX.com" height="16" width="21" style="vertical-align: -4px;" />= the prize is between door 1

 <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-2a97a2c4502fc2721a2b2e57508eb79d_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#68;&#95;&#50;" title="Rendered by QuickLaTeX.com" height="15" width="22" style="vertical-align: -3px;" />= the prize is between door 2

 <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a1079333bcf1a7ce8983e618a81548b2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#68;&#95;&#51;" title="Rendered by QuickLaTeX.com" height="15" width="22" style="vertical-align: -3px;" />= the prize is between door 3

We know <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a9f53ce7ab42f5f641798aa86f9a1c41_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#68;&#95;&#49;&#41;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#51;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="83" style="vertical-align: -6px;" />. The question is what is [/latex]P(D_2 | D)[/latex]? We use the symbol  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-21ddec8dd029b3a304f32a63e00f0daa_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#68;" title="Rendered by QuickLaTeX.com" height="12" width="15" style="vertical-align: 0px;" />to denote the data/evidence we have, which is the fact that the gameshow host opened door 3. We can solve this using Bayes&#8217; theorem:

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-dd2ed20fc6d1178df68b1c6d3ef04cef_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#68;&#95;&#50;&#124;&#69;&#41;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#80;&#40;&#69;&#32;&#124;&#68;&#95;&#50;&#41;&#80;&#40;&#68;&#95;&#50;&#41;&#32;&#125;&#123;&#32;&#80;&#40;&#69;&#41;&#32;&#125;" title="Rendered by QuickLaTeX.com" height="29" width="189" style="vertical-align: -9px;" />

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-9b32c5cfbf59661764e1427a39e74864_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#68;&#95;&#50;&#124;&#69;&#41;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#80;&#40;&#69;&#32;&#124;&#68;&#95;&#50;&#41;&#80;&#40;&#68;&#95;&#50;&#41;&#32;&#125;&#123;&#80;&#40;&#69;&#32;&#124;&#68;&#95;&#49;&#41;&#80;&#40;&#68;&#95;&#49;&#41;&#32;&#43;&#80;&#40;&#69;&#32;&#124;&#68;&#95;&#50;&#41;&#80;&#40;&#68;&#95;&#50;&#41;&#125;" title="Rendered by QuickLaTeX.com" height="29" width="293" style="vertical-align: -9px;" />

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-e96ba5f4593ae2fd84427a64fe477591_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#113;&#117;&#97;&#100;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#40;&#32;&#49;&#41;&#40;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#50;&#125;&#41;&#125;&#32;&#123;&#32;&#40;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#51;&#125;&#41;&#40;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#50;&#125;&#41;&#32;&#43;&#32;&#40;&#49;&#41;&#40;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#51;&#125;&#41;&#125;&#32;" title="Rendered by QuickLaTeX.com" height="35" width="110" style="vertical-align: -13px;" />

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-75ae7b44b5d77e9c4719dc5f44e83ad9_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#113;&#117;&#97;&#100;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#50;&#125;&#123;&#51;&#125;&#32;" title="Rendered by QuickLaTeX.com" height="22" width="27" style="vertical-align: -6px;" />

Therefore it is better to switch to door 2. By switching to door 2, we double our chance of winning from  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-dbd03e60bd01705013f9203f96c3a268_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#51;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="7" style="vertical-align: -6px;" />to <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-323d7bf1d3ffbff6f4d5fdde3e5e954a_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#50;&#125;&#123;&#51;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="7" style="vertical-align: -6px;" />. The tricky part of the calculation is calculating the normalizing factor <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-10a9d9ba3665b4bd73cda08e1096a25a_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#69;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="41" style="vertical-align: -4px;" />, where we must consider the probability the game show host will open door 3 when the prize is behind door 1 (=1/2) and the case where the prize is behind door 2 (=1).

Note the following mind-blowing shortcut to solving the problem:

Since door 3 was opened, we know <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a5866efcacb201320ffe8e2083ce41eb_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#68;&#95;&#51;&#41;&#32;&#61;&#32;&#48;" title="Rendered by QuickLaTeX.com" height="18" width="83" style="vertical-align: -4px;" />. The gameshow host did nothing to interfere with door 1. Thus  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-305fa411d22957d9b1c3d5745e122131_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#68;&#95;&#49;&#41;&#32;&#61;&#32;&#49;&#47;&#51;" title="Rendered by QuickLaTeX.com" height="19" width="101" style="vertical-align: -5px;" />as it was in the beginning. Now, we know <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-1faa0898521fb4209c8e31a943cfd098_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#68;&#95;&#49;&#41;&#32;&#43;&#32;&#80;&#40;&#68;&#95;&#50;&#41;&#32;&#43;&#32;&#80;&#40;&#68;&#95;&#51;&#41;&#32;&#61;&#32;&#49;" title="Rendered by QuickLaTeX.com" height="18" width="225" style="vertical-align: -4px;" />, so <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-7b11056ace370994ddfaacd8f92e6d03_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#68;&#95;&#50;&#41;&#32;&#61;&#32;&#50;&#47;&#51;" title="Rendered by QuickLaTeX.com" height="19" width="101" style="vertical-align: -5px;" />!

# Bayesian model comparison

Bayes&#8217; theorem allows us to compare the likelihoods of different models being true. To take a concrete example, let&#8217;s assume we have black box with a button attached. Whenever we hit the button, and a light on top of the box blinks either green or red. We hit the button a number times, obtaining a sequence:

GRRGGRGRRGRG&#8230;

Let&#8217;s say say we model the black box as a &#8216;bent coin&#8217;. Thus, our model says that each outcome is statistically independent from previous outcomes and the probability of getting green is <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a21edaae2e69f9ac17bd9b1e65f3ac6e_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#103;" title="Rendered by QuickLaTeX.com" height="14" width="17" style="vertical-align: -6px;" />. Using Bayes&#8217; rule, we can infer the most likely value of  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a21edaae2e69f9ac17bd9b1e65f3ac6e_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#103;" title="Rendered by QuickLaTeX.com" height="14" width="17" style="vertical-align: -6px;" />for this model, and compute the probability of any  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a21edaae2e69f9ac17bd9b1e65f3ac6e_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#103;" title="Rendered by QuickLaTeX.com" height="14" width="17" style="vertical-align: -6px;" />given a sequence of observations. In the interest of space, I won&#8217;t solve it here.

We might have a different model, though. We may model the black box as a dice. If the dice lands on 1, the green light goes on, otherwise, the red light goes on. This corresponds to our earlier, more general model, but with  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a21edaae2e69f9ac17bd9b1e65f3ac6e_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#103;" title="Rendered by QuickLaTeX.com" height="14" width="17" style="vertical-align: -6px;" />fixed at <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-b34501abd0db358fcf4cbd4813ae35e2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#103;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#54;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="50" style="vertical-align: -6px;" />. The first model has a free parameter, <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a21edaae2e69f9ac17bd9b1e65f3ac6e_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#103;" title="Rendered by QuickLaTeX.com" height="14" width="17" style="vertical-align: -6px;" />, while the second model does not.

The method of Bayesian model comparison can tell us which model is more likely. Instead of analyzing the situation with a single model, we now consider both models at the same time. I like to use the term &#8216;metamodel&#8217; for this. In our metamodel, we assume equal prior probabilities for each model. We denote the sequence of flashes we observed as <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-fc35f5bd46a614acd7f109479c10b81c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#115;" title="Rendered by QuickLaTeX.com" height="8" width="8" style="vertical-align: 0px;" />. Model 1 is denoted <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-be18f73f4b4ab49a231d02014d29317e_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#32;&#123;&#72;&#125;&#95;&#49;" title="Rendered by QuickLaTeX.com" height="16" width="21" style="vertical-align: -4px;" />, and model 2 is denoted  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-7f9b108f867d05761876b70d18c7f4a7_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#32;&#123;&#72;&#125;&#95;&#50;" title="Rendered by QuickLaTeX.com" height="15" width="22" style="vertical-align: -3px;" />(the symbol  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-5346d29aea48941aad3fd2e7a78bb7be_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;" title="Rendered by QuickLaTeX.com" height="12" width="15" style="vertical-align: 0px;" />stands for &#8216;hypothesis&#8217;, a word which we take as synonymous with &#8216;model&#8217;).

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-ff5eebb98b275820996c5114c103c426_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#49;&#32;&#124;&#32;&#115;&#41;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#32;&#80;&#40;&#32;&#115;&#32;&#124;&#32;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#49;&#41;&#32;&#80;&#40;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#49;&#41;&#32;&#125;&#123;&#32;&#80;&#40;&#115;&#41;&#32;&#125;" title="Rendered by QuickLaTeX.com" height="29" width="179" style="vertical-align: -9px;" />

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-da16d18289d6b955beb785c3fb4121f3_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#50;&#32;&#124;&#32;&#115;&#41;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#32;&#80;&#40;&#32;&#115;&#32;&#124;&#32;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#50;&#41;&#32;&#80;&#40;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#49;&#41;&#32;&#125;&#123;&#32;&#80;&#40;&#115;&#41;&#32;&#125;" title="Rendered by QuickLaTeX.com" height="29" width="179" style="vertical-align: -9px;" />

The relative probability of model 2 over model 1 is encoded in the ratio of the posterior probabilities:

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-9edf3675eb2316689c4cba04e67ed978_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#80;&#40;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#49;&#32;&#124;&#32;&#115;&#41;&#32;&#125;&#123;&#80;&#40;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#50;&#32;&#124;&#32;&#115;&#41;&#32;&#125;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#80;&#40;&#115;&#124;&#32;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#49;&#41;&#125;&#123;&#80;&#40;&#115;&#124;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#50;&#41;&#125;" title="Rendered by QuickLaTeX.com" height="29" width="127" style="vertical-align: -9px;" />

The ratio tells us the relative probability that model 1 is correct. Note that absolute probabilities of model 1 and model 2 can be computed from this using the fact that  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-45425fa59350e6af70c37dd65c16508b_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#49;&#124;&#115;&#41;&#43;&#80;&#40;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#72;&#125;&#95;&#50;&#32;&#124;&#115;&#41;&#61;&#49;" title="Rendered by QuickLaTeX.com" height="18" width="180" style="vertical-align: -4px;" />That&#8217;s all on model comparison for now. A more detailed discussion can be found in MacKay&#8217;s book.

# The case of the blood stains

This problem is taken directly MacKay&#8217;s book:

<pre>Two people have left traces of their own blood at the scene of a
 crime. A suspect, Oliver, is tested and found to have type ‘O’
 blood. The blood groups of the two traces are found to be of type
 ‘O’ (a common type in the local population, having frequency 60%)
 and of type ‘AB’ (a rare type, with frequency 1%). Do these data
 (type ‘O’ and ‘AB’ blood were found at scene) give evidence in
 favour of the proposition that Oliver was one of the two people
 present at the crime?</pre>

At first glance, lawyer may easily convince the jury that the presence of the type &#8216;O&#8217; blood stain provides evidence that Oliver was present. The lawyer may argue the while the degree of weight it should carry may be small, since type &#8216;O&#8217; is fairly common, nonetheless the presence of type &#8216;O&#8217; should count as positive evidence. However, this is not the case!

Denote the proposition &#8216;the suspect and one unknown person were present&#8217; by <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-05813704fb74f4112070a63a15e143dc_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#83;" title="Rendered by QuickLaTeX.com" height="12" width="12" style="vertical-align: 0px;" />. The alternative, <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-c927f15e7f339ef785b5b9234cc216fe_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#98;&#97;&#114;&#123;&#83;&#125;" title="Rendered by QuickLaTeX.com" height="15" width="12" style="vertical-align: 0px;" />, states that &#8220;two unknown people from the population were present&#8221;.

If we assume that the suspect, Oliver, was present, then the likelihood of the data is simply the likelihood of having a person with blood type &#8216;AB&#8217;:

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-42d3bef0609f212e537b3b51b2cfd80b_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#68;&#124;&#83;&#41;&#32;&#61;&#32;&#112;&#95;&#123;&#65;&#66;&#125;&#32;&#61;&#32;&#46;&#48;&#49;" title="Rendered by QuickLaTeX.com" height="18" width="160" style="vertical-align: -4px;" />

The likelihood of the other case is the likelihood that two unknown people drawn from the population have blood types &#8216;AB&#8217; and &#8216;O&#8221;:

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-83074a72531d6dd1436530ee1e89ba16_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#40;&#68;&#124;&#92;&#98;&#97;&#114;&#123;&#83;&#125;&#41;&#32;&#61;&#32;&#50;&#32;&#112;&#95;&#123;&#65;&#66;&#125;&#112;&#95;&#123;&#79;&#125;&#32;&#61;&#32;&#46;&#48;&#56;&#51;" title="Rendered by QuickLaTeX.com" height="19" width="199" style="vertical-align: -4px;" />

The second case is more likely. The likelihood ratio is

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-c9e08368100da55b4670df097bc54d19_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#46;&#48;&#49;&#125;&#123;&#46;&#48;&#56;&#51;&#125;&#32;&#61;&#32;&#46;&#56;&#51;" title="Rendered by QuickLaTeX.com" height="22" width="73" style="vertical-align: -6px;" />

Thus the data actually provides weak evidence against the supposition that Oliver was present. Why is this?

We can gain some insight by first considering another suspect, Alberto, who has blood type <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-e058cf579f9e10b5bcffcd1e6c2e08b1_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#65;&#66;" title="Rendered by QuickLaTeX.com" height="12" width="27" style="vertical-align: 0px;" />. We denote the hypothesis that Alberto was present by <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-3e7ba10154ff8a05dcf3dc7f17e954df_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#83;&#39;" title="Rendered by QuickLaTeX.com" height="14" width="16" style="vertical-align: 0px;" />, and the hypothesis that he wasn&#8217;t present <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-c927f15e7f339ef785b5b9234cc216fe_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#98;&#97;&#114;&#123;&#83;&#125;" title="Rendered by QuickLaTeX.com" height="15" width="12" style="vertical-align: 0px;" />. In this case, the ratio is:

<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-54bf268f4001649a51331b5c5ca4b969_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#83;&#39;&#125;&#123;&#92;&#98;&#97;&#114;&#123;&#83;&#125;&#125;&#61;&#92;&#102;&#114;&#97;&#99;&#123;&#112;&#95;&#123;&#79;&#125;&#125;&#123;&#50;&#112;&#95;&#123;&#65;&#66;&#125;&#112;&#95;&#123;&#79;&#125;&#125;&#61;&#92;&#102;&#114;&#97;&#99;&#123;&#46;&#54;&#125;&#123;&#40;&#50;&#41;&#40;&#46;&#48;&#49;&#41;&#40;&#46;&#54;&#41;&#125;&#61;&#53;&#48;" title="Rendered by QuickLaTeX.com" height="27" width="229" style="vertical-align: -9px;" />

Clearly, in this case, the evidence does support the hypothesis that Alberto was there. MacKay elaborates: (my emphasis added)

Now let us change the situation slightly; imagine that 99% of people are of blood type O, and the rest are of type AB. Only these two blood types exist in the population. The data at the scene are the same as before. Consider again how these data influence our beliefs about Oliver, a suspect of type O, and Alberto, a suspect of type AB. Intuitively, we still believe that the presence of the rare AB blood provides positive evidence that Alberto was there. But does the fact that type O blood was detected at the scene favour the hypothesis that Oliver was present? If this were the case, that would mean that regardless of who the suspect is, the data make it more probable they were present; everyone in the population would be under greater suspicion, which would be absurd. The data may be compatible with any suspect of either blood type being present, but if they provide evidence for some theories, they must also provide evidence against other theories.

Here is another way of thinking about this: imagine that instead of two people’s blood stains there are ten (independent stains), and that in the entire local population of one hundred, there are ninety type O suspects and ten type AB suspects. Consider a particular type O suspect, Oliver: without any other information, and before the blood test results come in, there is a one in 10 chance that he was at the scene, since we know that 10 out of the 100 suspects were present. We now get the results of blood tests, and find that nine of the ten stains are of type AB, and one of the stains is of type O. Does this make it more likely that Oliver was there? No, there is now only a one in ninety chance that he was there, since we know that only one person present was of type O.

MacKay continues to elaborate this problem by doing a more explicit calculation. In the end the conclusion is:

If there are more type O stains than the average number expected under hypothesis <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-c927f15e7f339ef785b5b9234cc216fe_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#98;&#97;&#114;&#123;&#83;&#125;" title="Rendered by QuickLaTeX.com" height="15" width="12" style="vertical-align: 0px;" />, then the data give evidence in favour of the presence of Oliver. Conversely, if there are fewer type O stains than the expected number under <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-c927f15e7f339ef785b5b9234cc216fe_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#98;&#97;&#114;&#123;&#83;&#125;" title="Rendered by QuickLaTeX.com" height="15" width="12" style="vertical-align: 0px;" />, then the data reduce the probability of the hypothesis that he was there.

Note the similarity with the drug test example. The base rate of blood stains must be considered.

# Bayesian statistics in court

Ideally, a jury would apply Bayesian reasoning to rank the likelihood of different hypotheses. The chance that a person is a suspect is denoted <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-05813704fb74f4112070a63a15e143dc_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#83;" title="Rendered by QuickLaTeX.com" height="12" width="12" style="vertical-align: 0px;" />, and the probability is encoded in the ratio <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-7448c9d66a370ddfd7e192b8daec2dc4_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#83;&#125;&#123;&#92;&#98;&#97;&#114;&#123;&#83;&#125;&#125;" title="Rendered by QuickLaTeX.com" height="23" width="10" style="vertical-align: -7px;" />. In the words of MacKay:

&#8220;In my view, a jury&#8217;s task should generally be to multiply together carefully evaluated likelihood ratios from each independent piece of evidence with an equally carefully reasoned prior probabilities.&#8221;

The potential for Bayesian methods to improve the criminal justice system is huge. The issue though is that statistics can also be easily manipulated by subtle changes in the inputs. Judges and juries can easily be misled if they have no understanding of statistics. One solution is to train the jury in Bayesian statistics during the course of the case, and this has been used by lawyers to help juries understand complicated blood stain DNA evidence. However, many judges (who usually lack a deep understanding of statistics) are immensely skeptical of whether the jury can properly analyze complex statistical data without being hoodwinked. From their point of view, statistics are too opaque. There is the question of the confidence that can be placed in the jury to properly apply Bayesian methodology, even after training. Should juries be quizzed on their ability to do Bayesian reasoning before being allowed to deliberate? The challenge is to explain complicated statistical methodologies in a way that lay people can understand, and no solution has yet been found that all parties agree upon. For this reason, the use of Bayesian statistics in courts has been banned in the UK. Obviously, this is not at all an optimal situation.

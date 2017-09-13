---
id: 2462
title: Maximum entropy priors
date: 2015-12-28T22:19:45+00:00
author: delton137
layout: post
guid: https://moreisdifferent.wordpress.com/?p=2462
permalink: /2015/12/28/maximum-entropy-priors/
publicize_google_plus_url:
  - https://plus.google.com/+DanElton/posts/i8C5YRMvnHV
publicize_tumblr_url:
  - http://.tumblr.com/post/136138550918
publicize_path_id:
  - 5681b58d14fe574207c6e5bf
dsq_needs_sync:
  - "1"
categories:
  - Bayesian inference
  - machine learning
  - python
  - Uncategorized
tags:
  - machine learning
  - python
---
How do we assign priors?

If we don&#8217;t have any prior knowledge, then the obvious solution is to use the **principle of indifference. **This principle says that if we have no reason for suspecting one outcome over any other, than all outcomes must be considered equally likely. Jakob Bernoulli called this the &#8220;principle of insufficient reason&#8221;, a play on the &#8220;principle of sufficient reason&#8221;, which asserts that everything must have a reason or cause. This may be the case, but if we are ignorant of reasons, we cannot say that one outcome will be more likely than any other.
  
<!--more-->

This tells us how to assign a prior if we have zero knowledge of a distribution like <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a80be6e42ac3b3c6528958bbfa21f92c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#80;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="37" style="vertical-align: -4px;" />. But what about if we know some information about <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a80be6e42ac3b3c6528958bbfa21f92c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#80;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="37" style="vertical-align: -4px;" /> such as the average or variance of the distribution?

The principle of **maximum entropy **tells us how to extend the principle of indifference to such cases.

By entropy, we mean the Shannon entropy of the distribution:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-cfdb9850a89ef80c3340c4229c69b8c5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#72;&#40;&#120;&#41;&#32;&#61;&#32;&#92;&#115;&#117;&#109;&#95;&#105;&#32;&#45;&#32;&#112;&#95;&#105;&#32;&#92;&#108;&#111;&#103;&#40;&#112;&#95;&#105;&#41;" title="Rendered by QuickLaTeX.com" height="19" width="172" style="vertical-align: -5px;" />

The Shannon entropy gives the average information that we expect to obtain from sampling the distribution. Information is quantified using the Shannon measure, which says that the information contained in an observation is given by:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-ca22f15ad7fcc6cbbd00c0bdd64a136c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#72;&#32;&#61;&#32;&#45;&#92;&#108;&#111;&#103;&#40;&#112;&#41;&#32;&#61;&#32;&#92;&#108;&#111;&#103;&#40;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#112;&#125;&#41;" title="Rendered by QuickLaTeX.com" height="25" width="172" style="vertical-align: -9px;" />

Remember that we are thinking of probability distributions as being due to human ignorance. The Shannon measure quantifies this. Outcomes that are very unexpected give us more information, while expected outcomes give us little information.

**Example of how Shannon&#8217;s formula measures information &#8211; Wenglish**
  
The most teachable example of Shannon&#8217;s measure in action I have read so far is to consider a fictitious language called Wenglish. Wenglish is like English, in that the probability of each letter is equal to the probabilities of letters in English. The probability of _a _for instance is .0625, while the probability of _z _is only ~.001. Consider we have created a list of 2^15=32,768 Wenglish words, and we have someone choose one at random without looking it. If we learn that the first letter is _z, _this conveys a lot of information, since it narrows down the possibilities &#8211; on average only 32 words in the list start with z. If we learn the first letter is _a, _this conveys less information, since a lot of words start with _a_. If you want to read more about this, and several other examples, see McKay&#8217;s book, Chapter 4 ([free pdf)](http://www.inference.phy.cam.ac.uk/mackay/itprnn/ps/65.86.pdf). Shannon&#8217;s formula captures this by using <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-94498d7a8fa6380fba47e4bcc34c3465_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#49;&#47;&#112;" title="Rendered by QuickLaTeX.com" height="18" width="26" style="vertical-align: -5px;" />. The use of the \logarithm ensures that the measure is additive when probability distributions are combined.

The entropy of a distribution is the average Shannon information of the distribution. Distributions that are more spread out have the highest entropy, while distributions that have sharp peaks have lower entropy.

**Maximum entropy applied
  
** Now, lets consider how we apply the MaxEnt principle. For simplicity, we consider a probability distribution over a discrete space indexed by <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-695d9d59bd04859c6c99e7feb11daab6_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#105;" title="Rendered by QuickLaTeX.com" height="12" width="6" style="vertical-align: 0px;" />. Suppose we know the averages of 2 different functions  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a4e5cedf4be69194cd40c59e4dc017eb_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#60;&#102;&#95;&#49;&#40;&#105;&#41;&#62;&#32;&#61;&#32;&#70;&#95;&#49;" title="Rendered by QuickLaTeX.com" height="18" width="108" style="vertical-align: -4px;" />and <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-ad6e4292d3387894b6e7711737d157af_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#60;&#102;&#95;&#50;&#40;&#105;&#41;&#62;&#61;&#32;&#70;&#95;&#50;" title="Rendered by QuickLaTeX.com" height="18" width="109" style="vertical-align: -4px;" />. Now we wish to maximize the entropy of the distribution subject to these constraints. We also have the constraint:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-7f7800bb16a030eec33c15a334997bd4_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#115;&#117;&#109;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#112;&#95;&#105;&#61;&#49;" title="Rendered by QuickLaTeX.com" height="20" width="91" style="vertical-align: -6px;" />

We use Langrange multipliers to find the maxima. Strictly speaking, what follows is not a proof, because we do not prove that the extremum we find is a maximum, and we are not proving the validity of setting the derivative to zero. (this type method would fail to find the maximum of <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-e66ce626e045fe4d14fbdf378f875aa5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#102;&#40;&#120;&#41;&#32;&#61;&#32;&#45;&#92;&#109;&#98;&#111;&#120;&#123;&#97;&#98;&#115;&#125;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="121" style="vertical-align: -4px;" />, for example). For the more mathematically inclined, full proofs can be [found here](http://www.latex.uconn.edu/~kconrad/blurbs/analysis/entropypost.pdf).

We construct the following function:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-3fa48dca6162481351afee145481566f_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#70;&#40;&#112;&#95;&#49;&#44;&#99;&#100;&#111;&#116;&#115;&#44;&#112;&#95;&#110;&#44;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;&#44;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#44;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#50;&#41;&#32;&#61;&#32;&#45;&#92;&#115;&#117;&#109;&#108;&#105;&#109;&#105;&#116;&#115;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#32;&#112;&#95;&#105;&#32;&#92;&#108;&#111;&#103;&#40;&#112;&#95;&#105;&#41;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;&#40;&#92;&#115;&#117;&#109;&#108;&#105;&#109;&#105;&#116;&#115;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#32;&#112;&#95;&#105;&#32;&#45;&#32;&#49;&#41;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#40;&#92;&#115;&#117;&#109;&#108;&#105;&#109;&#105;&#116;&#115;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#32;&#112;&#95;&#105;&#32;&#102;&#95;&#49;&#40;&#105;&#41;&#32;&#45;&#32;&#70;&#95;&#49;&#41;&#32;&#43; &#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#50;&#40;&#92;&#115;&#117;&#109;&#108;&#105;&#109;&#105;&#116;&#115;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#32;&#112;&#95;&#105;&#32;&#102;&#95;&#50;&#40;&#105;&#41;&#32;&#45;&#32;&#70;&#95;&#50;&#41;" title="Rendered by QuickLaTeX.com" height="42" width="582" style="vertical-align: -6px;" />

The extremum is found when
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-cb38323c23e0b8673407b538b4d8ca3c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#92;&#112;&#97;&#114;&#116;&#105;&#97;&#108;&#32;&#70;&#125;&#123;&#92;&#112;&#97;&#114;&#116;&#105;&#97;&#108;&#32;&#112;&#95;&#105;&#125;&#32;&#61;&#32;&#48;" title="Rendered by QuickLaTeX.com" height="26" width="55" style="vertical-align: -9px;" />
  
for all <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a96ceab54454ad1675ec483c1ba0a5f9_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#105;" title="Rendered by QuickLaTeX.com" height="12" width="6" style="vertical-align: 0px;" />.

We obtain:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-63a4b4cea80be7ff4935bc6a2a4b066a_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#45;&#49;&#32;&#45;&#32;&#92;&#108;&#111;&#103;&#40;&#112;&#95;&#105;&#41;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#32;&#102;&#95;&#49;&#40;&#105;&#41;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#50;&#32;&#102;&#95;&#50;&#40;&#105;&#41;&#32;&#61;&#32;&#48;" title="Rendered by QuickLaTeX.com" height="18" width="319" style="vertical-align: -4px;" />
  
so
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-da27d1eb1071b07f3710705d64ad085c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#105;&#32;&#61;&#32;&#101;&#94;&#123;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;&#32;&#45;&#32;&#49;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#32;&#102;&#95;&#49;&#40;&#105;&#41;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#50;&#32;&#102;&#95;&#50;&#40;&#105;&#41;&#125;" title="Rendered by QuickLaTeX.com" height="21" width="187" style="vertical-align: -4px;" />

or for a probability function over <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-96c6d1c3558202fce52168ea41bd2635_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#108;&#97;&#116;&#101;&#120;&#98;&#102;&#123;&#82;&#125;" title="Rendered by QuickLaTeX.com" height="17" width="72" style="vertical-align: -4px;" />:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-320259a9ff808935e7a2b9641e023673_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#40;&#120;&#41;&#32;&#61;&#32;&#101;&#94;&#123;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;&#32;&#45;&#32;&#49;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#32;&#102;&#95;&#49;&#40;&#120;&#41;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#50;&#32;&#102;&#95;&#50;&#40;&#120;&#41;&#125;" title="Rendered by QuickLaTeX.com" height="21" width="211" style="vertical-align: -4px;" />

Where <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-00bcef05c6227a7970e5e79a7ae55863_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;" title="Rendered by QuickLaTeX.com" height="15" width="17" style="vertical-align: -3px;" />, <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-002259f38b7f9f7fbad4a32fbd485d6c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;" title="Rendered by QuickLaTeX.com" height="16" width="16" style="vertical-align: -4px;" />, and  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-ecb9da3b4cb22b36ed04a511faa28dba_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#50;" title="Rendered by QuickLaTeX.com" height="15" width="17" style="vertical-align: -3px;" />are set such that the constraints are satisfied.

**Some examples**
  
Let&#8217;s quickly run through some of the simplest cases. First, consider no constraints. Then
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-365835725543b81487720127399768a1_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#105;&#32;&#61;&#32;&#101;&#94;&#123;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;&#32;&#45;&#32;&#49;&#125;&#32;&#61;&#32;&#99;" title="Rendered by QuickLaTeX.com" height="19" width="112" style="vertical-align: -4px;" />
  
To satisfy our the constraint that all probabilities sum to 1, then
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-16cb8d794f61617b5789cb99b3a6ce37_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#105;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#110;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="50" style="vertical-align: -6px;" />

Now lets say that <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-f4625f4d64d63a0a9e8b0b5b3f875e9a_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#102;&#95;&#49;&#40;&#120;&#41;&#32;&#61;&#32;&#120;" title="Rendered by QuickLaTeX.com" height="18" width="74" style="vertical-align: -4px;" />, with  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-58e0e9f3ab11040309808a128a7d4f69_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#60;&#102;&#95;&#49;&#40;&#120;&#41;&#62;&#32;&#61;&#32;&#109;&#117;" title="Rendered by QuickLaTeX.com" height="18" width="121" style="vertical-align: -4px;" />and  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-5752955a6694f7470b64f00044d0ca2e_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#102;&#95;&#50;&#40;&#120;&#41;&#32;&#61;&#32;&#40;&#120;&#45;&#109;&#117;&#41;&#94;&#50;" title="Rendered by QuickLaTeX.com" height="19" width="143" style="vertical-align: -4px;" />and <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-aa89d847fe456c89ce1698396091dd8f_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#60;&#102;&#95;&#50;&#40;&#120;&#41;&#62;&#32;&#61;&#32;&#92;&#115;&#105;&#103;&#109;&#97;" title="Rendered by QuickLaTeX.com" height="18" width="106" style="vertical-align: -4px;" />. In other words, we know the mean and variance of <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-8863bc5cbc489c6ced8b011198837d87_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="33" style="vertical-align: -4px;" />, but nothing else.

Then
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-7e364277cdd8b3b46ce6a4267bf01beb_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#40;&#120;&#41;&#32;&#61;&#32;&#101;&#94;&#123;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;&#32;&#45;&#32;&#49;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#32;&#120;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#50;&#32;&#40;&#120;&#45;&#109;&#117;&#41;&#94;&#50;&#125;" title="Rendered by QuickLaTeX.com" height="21" width="212" style="vertical-align: -4px;" />

A wild Gaussian has appeared! The condition that  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-875af2dfbc45a0033a23ff759786fba5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#105;&#110;&#116;&#95;&#123;&#92;&#109;&#97;&#116;&#104;&#98;&#102;&#123;&#82;&#125;&#125;&#112;&#40;&#120;&#41;&#100;&#120;" title="Rendered by QuickLaTeX.com" height="20" width="76" style="vertical-align: -6px;" />be finite requires  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-f39e91335e5df51274e4c20aa5345daf_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#32;&#61;&#32;&#48;" title="Rendered by QuickLaTeX.com" height="16" width="51" style="vertical-align: -4px;" />and <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-be9de2be674ceca4a51276e713b5fbd4_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#50;&#32;&#60;&#32;&#48;" title="Rendered by QuickLaTeX.com" height="15" width="51" style="vertical-align: -3px;" />. After solving for the Lagrange multipliers we obtain:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-54067bf94de0ddfbaab3f84a900c9ca1_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#40;&#120;&#41;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#92;&#115;&#113;&#114;&#116;&#123;&#50;&#92;&#112;&#105;&#32;&#92;&#115;&#105;&#103;&#109;&#97;&#125;&#125;&#32;&#101;&#94;&#123;&#92;&#102;&#114;&#97;&#99;&#123;&#40;&#120;&#45;&#109;&#117;&#41;&#94;&#50;&#125;&#123;&#50;&#92;&#115;&#105;&#103;&#109;&#97;&#94;&#50;&#125;&#125;" title="Rendered by QuickLaTeX.com" height="36" width="158" style="vertical-align: -11px;" />

**The loaded dice**
  
Let&#8217;s consider a &#8220;loaded dice&#8221;. The average number of dots returned from a fair dice is 21/6 = 7/2 = 3.5. Let&#8217;s suppose that we are told that instead we have a dice which yields an average of <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-165946f3f354fdc30c8dc1a27b454746_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#60;&#112;&#95;&#105;&#62;&#32;&#61;&#32;&#92;&#109;&#117;" title="Rendered by QuickLaTeX.com" height="15" width="81" style="vertical-align: -4px;" />, where  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a96ceab54454ad1675ec483c1ba0a5f9_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#105;" title="Rendered by QuickLaTeX.com" height="12" width="6" style="vertical-align: 0px;" />is between 1 and 6. What is the MaxEnt prior for <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-5f7322a67a9435b5569858b63eef409b_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#40;&#112;&#95;&#49;&#44;&#32;&#112;&#95;&#50;&#44;&#32;&#112;&#95;&#51;&#44;&#32;&#112;&#95;&#52;&#44;&#32;&#112;&#95;&#53;&#44;&#32;&#112;&#95;&#54;&#41;" title="Rendered by QuickLaTeX.com" height="18" width="151" style="vertical-align: -4px;" />? First, we generalize to an  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-42b0327b435c036eb54ec6b7037b9b6c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#110;" title="Rendered by QuickLaTeX.com" height="8" width="11" style="vertical-align: 0px;" />sided die, (at the end, we set <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-bafb885312a43ebfa9c564bcc3aeb744_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#110;&#61;&#54;" title="Rendered by QuickLaTeX.com" height="12" width="43" style="vertical-align: 0px;" />.

From our above result, the unnormalized distribution is:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-dfcca89407c709e52f72b81b5f14d7c1_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#105;&#32;&#61;&#32;&#101;&#94;&#123;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;&#32;&#45;&#32;&#49;&#32;&#43;&#32;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#32;&#105;&#125;" title="Rendered by QuickLaTeX.com" height="19" width="110" style="vertical-align: -4px;" />

To get this in a nicer form, set  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-2d78e7646cc60545c8cd37f36b62b018_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#101;&#94;&#123;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#48;&#32;&#45;&#32;&#49;&#125;&#32;&#61;&#32;&#67;" title="Rendered by QuickLaTeX.com" height="15" width="79" style="vertical-align: 0px;" />and pull that constant out front:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-2de570f689678ac1a5e5041407ecad14_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#105;&#32;&#61;&#32;&#67;&#32;&#101;&#94;&#123;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#32;&#105;&#125;" title="Rendered by QuickLaTeX.com" height="19" width="81" style="vertical-align: -4px;" />
  
Now set <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-bc52d9e8c1db808a84f2b819a8a149f5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#101;&#94;&#123;&#92;&#108;&#97;&#109;&#98;&#100;&#97;&#95;&#49;&#125;&#32;&#61;&#32;&#114;" title="Rendered by QuickLaTeX.com" height="15" width="55" style="vertical-align: 0px;" />:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-723d7e9564a68bea69b7753c6c5071f5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#105;&#32;&#61;&#32;&#67;&#32;&#114;&#94;&#105;" title="Rendered by QuickLaTeX.com" height="19" width="66" style="vertical-align: -4px;" />
  
Now we have the normalization condition:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-cdd8977a13914a7a825739445ea4b9b6_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#115;&#117;&#109;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#32;&#67;&#32;&#114;&#94;&#105;&#32;&#61;&#49;" title="Rendered by QuickLaTeX.com" height="21" width="104" style="vertical-align: -6px;" />
  
The left hand side is a [geometric series](http://latexworld.wolfram.com/GeometricSeries.html):
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-8f748b293c2274612cc64c4dbb318b36_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#115;&#117;&#109;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#32;&#114;&#94;&#105;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#114;&#32;&#40;&#114;&#94;&#110;&#45;&#49;&#41;&#125;&#123;&#114;&#45;&#49;&#125;" title="Rendered by QuickLaTeX.com" height="27" width="134" style="vertical-align: -7px;" />
  
Using this to find  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-85a6149f802b63b7e3afb9c435de3cb2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#67;" title="Rendered by QuickLaTeX.com" height="12" width="14" style="vertical-align: 0px;" />we obtain:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-293027d14ce188d6164e84a0d26ee145_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#105;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#114;&#45;&#49;&#125;&#123;&#114;&#40;&#114;&#94;&#110;&#45;&#49;&#41;&#125;&#32;&#114;&#94;&#105;" title="Rendered by QuickLaTeX.com" height="25" width="106" style="vertical-align: -9px;" />

Now let&#8217;s solve for  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-ff5d1c6f0d9e38fe42ad788412f79259_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#114;" title="Rendered by QuickLaTeX.com" height="8" width="8" style="vertical-align: 0px;" />in terms of  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-4d8ac042b9a68b9e7a247bdc9e3939a5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#109;&#117;" title="Rendered by QuickLaTeX.com" height="8" width="26" style="vertical-align: 0px;" />explicitly. We have the following condition:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-0063312ffcae31c89f2fc1801e3dae7a_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#115;&#117;&#109;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#92;&#102;&#114;&#97;&#99;&#123;&#114;&#45;&#49;&#125;&#123;&#114;&#40;&#114;&#94;&#110;&#45;&#49;&#41;&#125;&#32;&#105;&#32;&#114;&#94;&#123;&#105;&#125;&#32;&#61;&#32;&#92;&#109;&#117;" title="Rendered by QuickLaTeX.com" height="25" width="153" style="vertical-align: -9px;" />

We need to know the following sum:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a42b0e921754de641b599b2b4925347a_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#115;&#117;&#109;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#32;&#105;&#32;&#114;&#94;&#105;" title="Rendered by QuickLaTeX.com" height="21" width="64" style="vertical-align: -6px;" />

This sum can be obtained by differentiating the sum of the geometric series. The result is
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a853f97732fd447e929276b2cae45068_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#115;&#117;&#109;&#95;&#123;&#105;&#61;&#49;&#125;&#94;&#110;&#32;&#105;&#32;&#114;&#94;&#105;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#110;&#114;&#94;&#123;&#110;&#43;&#50;&#125;&#45;&#40;&#110;&#43;&#49;&#41;&#114;&#94;&#123;&#110;&#43;&#49;&#125;&#43;&#114;&#125;&#123;&#40;&#114;&#45;&#49;&#41;&#94;&#50;&#125;" title="Rendered by QuickLaTeX.com" height="30" width="223" style="vertical-align: -10px;" />

The equation for  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-ff5d1c6f0d9e38fe42ad788412f79259_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#114;" title="Rendered by QuickLaTeX.com" height="8" width="8" style="vertical-align: 0px;" />becomes:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-8339c92bcf2641ee791ff9c42c521d9a_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#110;&#114;&#94;&#123;&#110;&#43;&#49;&#125;&#45;&#40;&#110;&#43;&#49;&#41;&#114;&#94;&#110;&#43;&#49;&#61;&#32;&#92;&#109;&#117;&#40;&#114;&#94;&#110;&#32;&#45;&#32;&#49;&#41;&#40;&#114;&#32;&#45;&#49;&#41;" title="Rendered by QuickLaTeX.com" height="19" width="319" style="vertical-align: -4px;" />

Unfortunately, this equation doesn&#8217;t have any analytical solution, but it can be solved numerically, by finding the roots of:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-3057ea1a6a747f84f2aff5ff3d753071_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#40;&#110;&#45;&#92;&#109;&#117;&#41;&#114;&#94;&#123;&#110;&#43;&#49;&#125;&#43;&#40;&#92;&#109;&#117;&#45;&#110;&#45;&#49;&#41;&#114;&#94;&#110;&#43;&#92;&#109;&#117;&#32;&#114;&#45;&#92;&#109;&#117;&#43;&#49;&#61;&#48;" title="Rendered by QuickLaTeX.com" height="19" width="354" style="vertical-align: -4px;" />

Let&#8217;s graph what  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-5b8ca16ace10addf6881f3068527dee5_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#95;&#105;" title="Rendered by QuickLaTeX.com" height="12" width="15" style="vertical-align: -4px;" />looks like. I wrote the following the Python code:

<pre class="brush: python; collapse: false; title: ; wrap-lines: false; notranslate" title="">import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

n = 6
mu = 2

func = \lambda r : (n-\mu)*r**(n+1) + (mu-n-1)*r**n + \mu*r - \mu + 1

initial_guess = .3
r = fsolve(func, initial_guess)

index = np.zeros([n])
p = np.zeros([n])

for i in range(1,n+1):
index[i-1] = i
p[i-1] = ((1-r)/(1-r**n))*r**(i-1)

plt.bar(index, p)
plt.ylabel('p')
plt.xlabel('dice roll')
plt.show()
</pre>

<pre>for <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-5b521343adccbb6cc15716369baa57d2_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#109;&#117;&#32;&#61;&#32;&#51;&#46;&#53;" title="Rendered by QuickLaTeX.com" height="13" width="71" style="vertical-align: 0px;" /> we have:
<img class="alignnone wp-image-2809" src="http://www.danielcelton.com/wp-content/uploads/2015/12/mu3-5.png" alt="mu3.5" width="432" height="323" srcset="http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu3-5.png 800w, http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu3-5-300x225.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu3-5-768x576.png 768w" sizes="(max-width: 432px) 100vw, 432px" />
for <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-6fcdb708a697f9f5c3d71f29859ac1b9_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#109;&#117;&#32;&#61;&#32;&#50;" title="Rendered by QuickLaTeX.com" height="12" width="57" style="vertical-align: 0px;" /> we have:</pre>

<img class="alignnone wp-image-2807" src="http://www.danielcelton.com/wp-content/uploads/2015/12/mu2.png" alt="mu2" width="438" height="328" srcset="http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu2.png 800w, http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu2-300x225.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu2-768x576.png 768w" sizes="(max-width: 438px) 100vw, 438px" />
  
For  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-901c6293e3284beec4f9a70aa3e2e1ea_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#109;&#117;&#32;&#61;&#32;&#53;" title="Rendered by QuickLaTeX.com" height="13" width="57" style="vertical-align: 0px;" />we have:
  
<img class="alignnone wp-image-2808" src="http://www.danielcelton.com/wp-content/uploads/2015/12/mu5.png" alt="mu5" width="442" height="331" srcset="http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu5.png 800w, http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu5-300x225.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu5-768x576.png 768w" sizes="(max-width: 442px) 100vw, 442px" />
  
For  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-8d4b019e21d1f346fec7513d578dbc0f_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#109;&#117;&#32;&#61;&#32;&#53;&#46;&#57;" title="Rendered by QuickLaTeX.com" height="13" width="72" style="vertical-align: 0px;" />we have:
  
**<img class="alignnone wp-image-2814" src="http://www.danielcelton.com/wp-content/uploads/2015/12/mu5-9.png" alt="mu5.9" width="447" height="335" srcset="http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu5-9.png 800w, http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu5-9-300x225.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2015/12/mu5-9-768x576.png 768w" sizes="(max-width: 447px) 100vw, 447px" />
  
** the algebraic computations were cumbersome, but it works!
  
**
  
Why _some_ physicists love MaxEnt
  
** MaxEnt is of interest to some physicists because it provides a framework for understanding the results of statistical mechanics as exercises in entropy maximization and inference. This connection was first described in a [1956 paper by E.T. Jaynes](http://bayes.wustl.edu/etj/articles/theory.1.pdf). Jaynes showed that statistical mechanics isn&#8217;t really &#8220;physics&#8221; at all. Semantically, one can draw a distinction between physical theory (ie. quantum mechanics), that can tell us the possible energy levels in a system, <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-bec1bff6828628b7d0e9b4506c95df2c_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#69;&#95;&#105;" title="Rendered by QuickLaTeX.com" height="15" width="18" style="vertical-align: -3px;" />, and statistical mechanics, which is a framework for constructing a probability distribution  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-9a84d209c11832e208967e5ef55f9c82_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#80;&#95;&#105;" title="Rendered by QuickLaTeX.com" height="15" width="16" style="vertical-align: -3px;" />for the probability that the system is in state  <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-a96ceab54454ad1675ec483c1ba0a5f9_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#105;" title="Rendered by QuickLaTeX.com" height="12" width="6" style="vertical-align: 0px;" />given some (macroscopic) constraints. As the simplest example, we instance, we may know the average energy of the system.. In that case, we obtain the famous Boltzmann distribution for the canonical ensemble:
  
<img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-8b90f610e1eebd02f94ba7c1c346094a_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#112;&#40;&#105;&#41;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#90;&#125;&#101;&#94;&#123;&#45;&#92;&#98;&#101;&#116;&#97;&#32;&#69;&#95;&#105;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="109" style="vertical-align: -6px;" />

Where <img src="http://www.moreisdifferent.com/wp-content/ql-cache/quicklatex.com-20c9b353885c580f64c7c9f10256fa95_l3.png" class="ql-img-inline-formula quicklatex-auto-format" alt="&#32;&#92;&#98;&#101;&#116;&#97;&#32;&#61;&#32;&#49;&#47;&#84;" title="Rendered by QuickLaTeX.com" height="18" width="66" style="vertical-align: -5px;" />. (for a full derivation, [see here](http://www.tkm.kit.edu/downloads/TheoryF2012.pdf), pg. 27. Another slightly simpler exposition can be [found here](http://www.latex.nyu.edu/faculty/kleeman/SLecture5.pdf)).

Different thermodynamic ensembles yield MaxEnt distributions, depending on the constraints imposed.

Does MaxEnt actually lead to any new that we didn&#8217;t already know from the textbook (ensemble) approach to statistical mechanics? No. For this reason, my phyicists are quick to dismiss it.

However, sometimes new frameworks allow us to push the boundaries of a theory in new directions (for example, the framework of Feynman path integrals allowed scattering amplitudes to be calculated which couldn&#8217;t be calculated before). In this case, physicists are interested in bridging the gap between equilibrium statistical mechanics and non-equilibrium stat mechanics. If you open a non-equilibrium statistical mechanics book, you will find non-equilibrium systems being tackled by two different approaches. In one approach, you will find methods that study small perturbations from the equilibrium case, such as the Boltzmann theory of transport for slightly out of equilibrium gases, and the popular theory of linear response. These approaches work good for understanding what happens when a few tracer molecules are introduced into a gas, or how a system responds when a small electric field that is turned on. These theories do not work very well for system which are far from equilibrium, such as living systems, or systems being driven by strong external fields. For such systems, one finds a collection of ad-hoc methods, which go under names such as master equations, memory functions, Langevin equation, and the generalized diffusion equation. There is a growing understanding that these ad-hoc methods can be understood as examples of MaxEnt being extended to the non-equilibrium case. When MaxEnt is extended to non-equilibrium case we have to consider all the trajectories a system can take through time, subject to some constraints. For instance, we may want to consider how a system may move from state A to state B. One considers the space of possible trajectories that meet these endpoint constraints, and construct a maximum-entropy distribution ( on this space of possible trajectories. This approach was first introduced by E.T. Jaynes in 1980 as the &#8220;[principle of maximum entropy production](http://www.annualreviews.org/doi/abs/10.1146/annurev.pc.31.100180.003051)&#8220;.  He called the generalization &#8220;[maximum calliber](http://journals.aps.org/rmp/abstract/10.1103/RevModPhys.85.1115)&#8221; (MaxCal). The calculations involved are very similar to Feynman path integrals, and can only be done explicitly for very simple systems (such as a driven harmonic oscillator).  The cool thing with such calculations is that one can recover many of the ad-hoc equations of non-equilibrium stat mech. Therefore, there is growing optimism that MaxCal can help us learn fundamentally new ways of describing the behavior of out-of equilibrium systems.
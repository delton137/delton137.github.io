---
id: 1785
title: Why do we see the frequencies we do?
date: 2015-05-22T23:47:42+00:00
author: delton137
layout: post
guid: https://moreisdifferent.wordpress.com/?p=1785
permalink: /2015/05/22/why-do-we-see-the-frequencies-we-do/
geo_public:
  - "0"
publicize_google_plus_url:
  - https://plus.google.com/+DanElton/posts/iALBVpXbgJS
publicize_tumblr_url:
  - http://moreisdifferentblog.tumblr.com.tumblr.com/post/119637617238
publicize_path_id:
  - 555fc02fb42cdcaca2bba4f8
publicize_linkedin_url:
  - 'https://www.linkedin.com/updates?discuss=&scope=90218007&stype=M&topic=6007663019847409664&type=U&a=JQ6Y'
categories:
  - Uncategorized
tags:
  - Nontechnical
  - spectroscopy
  - water
---
Why can&#8217;t we see in the infrared or ultraviolet?
  
<!--more-->The reason is that our eyes are the result of millions of years of evolution. Millions of years ago, our ancestors lived in the ocean, so they had to see through water. Water is mostly transparent to visible light, but absorbs most other forms of electromagnetic radiation rather strongly. Even when our ancestors started living on land, our eyes remained full of &#8216;vitreous humour&#8217;, which is mostly water. You can&#8217;t really appreciate how marvellously tuned our eyes are to seeing through water until you see the absorption data itself on a log-log plot, for instance as plotted in the famous textbook 

_Classical_ _Electrodynamics_ by J.D. Jackson:

[<img class="  wp-image-1786 aligncenter" src="http://www.danielcelton.com/wp-content/uploads/2015/05/jackson_water_spec.gif?w=222" alt="Jackson_water_spec" width="561" height="759" />](http://www.danielcelton.com/wp-content/uploads/2015/05/jackson_water_spec.gif)The visible range is only a tiny part of the absorption spectrum, located between the two vertical dashed lines.

I believe some of the data Jackson shows comes from the [master&#8217;s thesis of David J. Sigelstein](https://mospace.umsystem.edu/xmlui/handle/10355/11599), which is publicly available [here](http://www.philiplaven.com/Segelstein.txt). To create a plot like this took a lot of work &#8211; experimental data had to be collected from many different sources, since the frequency range of any given experimental setup ends up being rather limited. The lowest frequencies between 10^9 &#8211; 10^12 Hz are in the GHz-THz range and are measured using dielectric spectrometers. Even within this range, the range of each experimental apparatus is limited, so one has to link together experimental data from 2 &#8211; 3 different sources of experimental data. Likewise there are separate measurements for the infrared, visible and UV parts of the spectra.

Here is my own plot of the data, plotted with the matplotlib Python library:
  
[<img class="alignnone  wp-image-1788" src="http://www.danielcelton.com/wp-content/uploads/2015/05/siegelstein_n_k.png?w=300" alt="Siegelstein_n_k" width="614" height="346" srcset="http://www.moreisdifferent.com/wp-content/uploads/2015/05/siegelstein_n_k.png 1557w, http://www.moreisdifferent.com/wp-content/uploads/2015/05/siegelstein_n_k-300x169.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2015/05/siegelstein_n_k-768x433.png 768w, http://www.moreisdifferent.com/wp-content/uploads/2015/05/siegelstein_n_k-1024x577.png 1024w, http://www.moreisdifferent.com/wp-content/uploads/2015/05/siegelstein_n_k-1200x676.png 1200w" sizes="(max-width: 614px) 100vw, 614px" />](http://www.danielcelton.com/wp-content/uploads/2015/05/siegelstein_n_k.png)

&#8216;n&#8217; is the index of refraction &#8211; it tells how much light is bent, and also how fast it travels in the water. &#8216;k&#8217; is the absorption. (technical note &#8211; the &#8216;k&#8217; I plot is the &#8216;extinction coefficient&#8217;, which is slightly different from the &#8220;infrared&#8221; or optical absorption coefficient (alpha) plotted in Jackson. The difference that only becomes really apparent at lower frequencies.)

Let me label all of those peaks. Each peak corresponds to a seperate absorption process in water. Here is a summary of the processes involved:

&#8212; .5 cm<sup>-1</sup> &#8211; The &#8220;Debye&#8221; absorption due to collective polarization relaxation. [Mircowaves use the _big_ peak here to efficiently heat food.](https://moreisdifferent.wordpress.com/2013/07/14/a-misconception-about-microwaves/) 
  
&#8212; 1 &#8211; 100  cm<sup>-1</sup> &#8211; H-bond network vibrational and relaxation modes (there are many)
  
&#8212; 200 cm<sup>-1</sup> &#8211; H-bond stretching absorption
  
&#8212; ~600 cm<sup>-1 </sup> &#8211; Librational (rotational) absorption
  
&#8212; 1500  cm<sup>-1  </sup>Bending
  
&#8212; ~2000 cm<sup>-1</sup> Bending + librational overtone
  
&#8212; ~3500 cm<sup>-1</sup> Symetric & antisymetric stretching
  
&#8212; 4000 &#8211; 10,000 cm<sup>-1</sup> lots of weak overtone peaks
  
&#8212; ~40,000 cm<sup>-1</sup> the so-called &#8220;UV edge&#8221; &#8211; at this frequency, the radiation is high enough energy to ionize water &#8211; ie. to kick out electrons from the molecules. The absorption at frequencies above this edge is all is due to ionization processes and Compton scattering between light and electrons.

Besides seeing why we see in the visible, there is another neat thing you can observe in Jackson&#8217;s figure if you look closely &#8211; you can see why water is blue. Of course, everyone knows that water _appears_ blue when it reflects the blue sky. Less people are aware of the fact that water has an intrinsically blue color. If you look very carefully at the Jackson figure, you will see that there is more absorption towards the lower frequency (red) end of the spectrum. Here is a  &#8220;zoomed in&#8221; picture of what&#8217;s going on:
  
[<img class="  wp-image-1789 aligncenter" src="http://www.danielcelton.com/wp-content/uploads/2015/05/zoom_in_visible.png?w=155" alt="zoom_in_visible" width="306" height="592" srcset="http://www.moreisdifferent.com/wp-content/uploads/2015/05/zoom_in_visible.png 292w, http://www.moreisdifferent.com/wp-content/uploads/2015/05/zoom_in_visible-155x300.png 155w" sizes="(max-width: 306px) 100vw, 306px" />](http://www.danielcelton.com/wp-content/uploads/2015/05/zoom_in_visible.png)

As you can see, there are several absorption peaks that overlap with the red, yellow and green parts of the visible spectrum. These overtones are quantum mechanical in nature and are described in a bit more detail [here](http://www.dartmouth.edu/~etrnsfer/water.htm). Because blue is absorbed least and red is absorbed more, water appears blue. The effect is very subtle, however, because the absorption is extremely small (note the logarithmic scale). The effect can be observed by eye by taking a tube of water about a few meters long with clear windows on each end, and looking through it. Scuba divers are also aware of this phenomena &#8211; if you dive deep enough, the water will appear slightly blue-ish, even on a cloudy day when the sky is grey.
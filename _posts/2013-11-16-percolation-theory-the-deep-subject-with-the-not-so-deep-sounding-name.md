---
id: 1485
title: 'Percolation Theory &#8211; the deep subject with the not-so-deep sounding name'
comments: true
date: 2013-11-16T00:11:49+00:00
author: delton137
layout: post
guid: http://moreisdifferent.wordpress.com/?p=1485
permalink: /2013/11/16/percolation-theory-the-deep-subject-with-the-not-so-deep-sounding-name/
categories:
  - physics
---
<p dir="ltr">
  I first discovered percolation theory about a year ago and was instantly fascinated.  I now consider it to be one of the deepest subjects in science.
</p>

<p dir="ltr">
  <!--more-->
</p>

<p dir="ltr">
  <strong>The percolation of water.</strong><br /> Percolation theory is named after percolation, which is the flow of water through a porous medium, such as coffee grinds. To get acquainted with this, let us consider a rock which has many small cavities. Let us assume the cavities are spherical and randomly distributed. An interesting question to ask is:
</p>

<p dir="ltr">
  <em>“At what volume fraction of cavities does the rock become permeable?”</em>
</p>

<p dir="ltr">
  This question can be phrased in a more precise way:
</p>

<p dir="ltr">
  <em>“Let us randomly place spherical cavities of radius</em> <em>r in a medium, allowing them to overlap. At what volume fraction of cavities is water able to travel arbitrarily long distances through the medium?”</em><a href="http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_ex.png"><img class="size-medium wp-image-1488 aligncenter" alt="percolation_ex" src="http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_ex.png?w=300" width="267" height="205" srcset="http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_ex.png 520w, http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_ex-300x232.png 300w" sizes="(max-width: 267px) 100vw, 267px" /></a>A way to visualize this is to picture a slab of this rock, with a thickness L, covered with water on top. The rock extends infinitely to the left and right. At a certain critical volume fraction, called the percolation threshold, water will always be able to find a path through the rock, regardless of the thickness L.
</p>

<p dir="ltr">
  For this simple example, the solution for the critical volume density is easy to guess. If you guessed that the critical volume threshold is ½ , you would be wrong! The threshold (in 3 dimensions) is actually:
</p>

<p dir="ltr">
  0.289573 +/- .000002
</p>

<p dir="ltr">
  In other words, when the cavities start to occupy ~28% of the volume, a path is always possible. I am not sure what I found more startling &#8211; the fact that the threshold is so low, or the fact that nobody has been able to prove exactly what the threshold is!  The threshold is determined using a computer simulation, but computers can only simulate finite systems. Thus, there is an uncertainty in the number!
</p>

<p dir="ltr">
  Part of the &#8220;deepness&#8221; of percolation theory is that it is filled with extremely simple mathematical questions which have never been solved. Even more startling is the fact that (as far as I can tell), mathematicians don’t even have a very good idea about how to even start a solution! Thus we see that from this mundane looking physical process (sorry geologists!) a deep puzzle emerges.
</p>

<p dir="ltr">
  <strong>Percolation on lattices.</strong><br /> In our previous example we considered cavities distributed arbitrarily through space. It was an example of what is called continuum percolation. Some other example percolation thresholds for<a href="http://en.wikipedia.org/wiki/Percolation_threshold#Thresholds_for_3D_continuum_models"> continuous percolation </a>can be found on Wikipedia.
</p>

<p dir="ltr">
  Most of the percolation theory written down so far deals with percolation on lattices. For instance, consider a square grid.  The chance that a given square is a &#8220;cavity&#8221; is a fixed probability, P. Using <a href="http://demonstrations.wolfram.com/PercolationOnASquareGrid/">an applet</a> from Wolfram Demonstrations, I generated the following pictures:
</p>

<p dir="ltr">
  <a href="http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_squares.png"><img class="size-medium wp-image-1489 aligncenter" alt="percolation_squares" src="http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_squares.png?w=137" width="213" height="505" /></a>To the best of our knowledge, the percolation threshold on the square lattice is:
</p>

<p dir="ltr">
  P_c  = 0.59274605(3)
</p>

<p dir="ltr">
  With the applet, I was able to get percolation at P = .58, but that was with a finite system. If I had made the system larger, percolation wouldn’t have occurred until P = .59&#8230;
</p>

<p dir="ltr">
  <strong>Site percolation vs. bond percolation</strong>
</p>

<p dir="ltr">
  The type of example I just gave is an example of site-percolation. In bond percolation, we picture &#8216;water&#8217; moving along along bonds/edges rather through sites/squares.
</p>

<p dir="ltr">
  Let us adopt the more general terminology. Instead of referring to ‘<em>cavities’</em>, let us call them ‘<em>sites</em>’.  Edges are called ‘<em>bonds</em>’. A series of connected sites is called a &#8216;<em>cluster</em>&#8216;. At the percolation threshold, clusters of infinite size exist.
</p>

<p dir="ltr">
  The following table I compiled shows site and bond percolation thresholds for some simple lattices:<a href="http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_thresholds.png"><img class="size-medium wp-image-1490 aligncenter" alt="percolation_thresholds" src="http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_thresholds.png?w=300" width="488" height="377" srcset="http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_thresholds.png 681w, http://www.moreisdifferent.com/wp-content/uploads/2013/11/percolation_thresholds-300x232.png 300w" sizes="(max-width: 488px) 100vw, 488px" /></a>A few of these are known exactly, but most are not.
</p>

<p dir="ltr">
  Just to whet your appetite further for his subject, here are some interesting facts about the types of clusters which appear at the percolation threshold:
</p>

&#8212; Clusters exhibit fractal scaling and fractal shapes.

&#8212; The distribution of cluster sizes follows a power law, with a &#8216;fat&#8217; tail.

<p dir="ltr">
  And to set your mind spinning, here are some examples of percolation thresholds in nature:
</p>

<p dir="ltr">
  &#8212; enough cracks form in rock, allowing trapped natural gas to be extracted (“fracking”).
</p>

&#8212; a disease starts to spread along a social network when the average number of social interactions per person reaches a certain number.

<p dir="ltr">
  &#8212;  A language is taken up by a critical fraction of well-connected speakers, allowing it to dominate all other languages in a certain geographic area.
</p>

<p dir="ltr">
  &#8212; galactic matter reaches a critical density, allowing the formation of stars and galaxies.
</p>

<p dir="ltr">
  &#8212; the probability of chemical bonding reaches a critical value, causing a liquid to turn into a gellatin at a certain temperature.
</p>

<p dir="ltr">
  &#8212; A heterogeneous material becomes conductive when the metallic fraction reaches a certain threshold.
</p>

<p dir="ltr">
  A good book on this subject is <a href="http://www.amazon.com/Introduction-Percolation-Theory-Dietrich-Stauffer/dp/0748402535">&#8220;Introduction to Percolation Theory&#8221;</a> by Dietrich Stauffer and Ammon Aharony. It&#8217;s one of those books which I&#8217;d love to read in full if I had more free time.
</p>

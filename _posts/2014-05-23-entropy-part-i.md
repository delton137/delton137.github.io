---
id: 1516
title: 'Entropy : part I'
comments: true
date: 2014-05-23T04:48:13+00:00
author: delton137
layout: post
guid: http://moreisdifferent.wordpress.com/?p=1516
permalink: /2014/05/23/entropy-part-i/
geo_public:
  - "0"
categories:
  - physics
tags:
  - entropy
---
This will be the first in a series of articles about **entropy**

Entropy, colloquially defined, is a measure of the amount of disorder in a system. This statement doesn’t really say much though, because how do we define the amount of ‘disorder’ in a system? That is the question which I hope to elucidate. Precisely defining entropy requires using physics, which means there will be formulas and ‘technical’ details. [I put technical in quotes here since these type of technical details are actually the most important details.]

Still, I hope that this will be readable by the average reader.

<!--more-->

I will not be doing any mathematical derivations here, they can be found in many textbooks. Instead, this will be a lighter fare, with interesting commentary provided by yours truly.

The following will assume you are familiar with the concept of a thermodynamic ensemble. A thermodynamic ensemble is a collection of systems each with its own microscopic state. However all of the systems in the ensemble have certain macroscopic quantities in common, for instance they may all have the same temperature, volume and mass (number of atoms). These quantities are called constraints. As a concrete example, consider a glass of water with a certain temperature and volume. We may have many glasses of water that look identical on the macro scale, but they are different on microscopic level &#8212; the molecules have different positions and velocities. In other words, many microscopic states can exist which yield the same macroscopic properties of interest &#8211; an &#8220;ensemble&#8221; is simply the collection of all such microscopic states. The probability of a given microstate is given by a probability function particular to that ensemble.

The importance of entropy is emphasized by the following fact from statistical mechanics: given a particular ensemble, the probability function is precisely the one which maximizes the entropy of the ensemble subject to the constraints (ie. the fixed macroscopic variable, such as fixed temperature, pressure, etc).

This point cannot be emphasized enough, especially since when one derives the probability function for the constant temperature (canonical) ensemble, one focuses on minimizing the free energy of the ensemble. Maximizing the entropy to find the probability distribution for different states is more general though. (In fact, entropy is sometimes called the &#8220;thermodynamic potential&#8221;.)

It is interesting to compare entropy with another well known concept from physics, energy. Most people have a pretty good idea of what energy is is &#8212; it is a quantity which is conserved , at least for a particular isolated system.  In life, however, we usually cannot deal with particular systems &#8211; knowing a &#8216;particular system&#8217; would require knowing all the positions and velocities of all the particles in the system at a given instant in time which is impossible even for a classical system. Therefore, we must work with ensembles &#8212; collections of possible systems consistent with the macroscopic observables, which are the constraints. Entropy is only defined for ensembles. Entropy is a measure of our lack of knowledge. When entropy is high, there are many possible microstates consistent with our constraints/observations, or in other words our knowledge is lacking about the exact state of the system.  For classical systems then, entropy is not a fundamental quantity like energy, because it is related to lack of knowledge of the observer.  For quantum systems,  however, entropy is fundamental, because one can never have an exact state of a system &#8211; states are described in terms of a probability density just like ensembles are.

One can also see the distinction between classical and quantum in terms of the uncertainty principle &#8211; the more we constrain one observable, another observable necessarily becomes unconstrained. We can never constrain all the variables in quantum system.

There are three definitions of entropy that one sees a lot.

The thermodynamic definition **S = Q/ T  **

(Q = heat due to work, T = temperature. Discovered by [Rudolf Clausius](http://en.wikipedia.org/wiki/Rudolf_Clausius) in 1854)

The statistical mechanics definition **S = k ln(W)**

(k = the Boltzmann constant. W = the number of possible states of the system consistent with the thermodynamic variables being held constant (temperature, pressure, number of particles, etc)  Ln() is the natural logarithm. Discovered by Boltzmann in 1877 and inscribed on his grave.)

The information theoretic definition **S = -k  sum  p\_i  ln(p\_i)**

( k = the Boltzmann constant. p_i = the probability of state i. First introduced by [J. Willard Gibbs in the context of statistical mechanics](http://en.wikipedia.org/wiki/Gibbs_entropy#Gibbs_Entropy_Formula), reintroduced by [Claude Shannon](http://en.wikipedia.org/wiki/Shannon_entropy) in the context of information theory in 1948. Von Neumann also arrived at an equation of this form when he discovered the [definition of entropy in quantum mechanics](http://en.wikipedia.org/wiki/Von_Neumann_entropy) in 1955. )

The third definition is the most general and the other two can be shown to be equivalent to the third, although they were originally derived in different contexts.

I am planning to do a blog post about each of these definitions of entropy, along with other topics related to entropy.

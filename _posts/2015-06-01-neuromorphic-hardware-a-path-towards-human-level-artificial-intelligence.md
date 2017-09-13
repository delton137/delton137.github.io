---
id: 1798
title: 'Neuromorphic hardware &#8211; a path towards human-level artificial intelligence'
date: 2015-06-01T03:12:36+00:00
author: delton137
layout: post
guid: https://moreisdifferent.wordpress.com/?p=1798
permalink: /2015/06/01/neuromorphic-hardware-a-path-towards-human-level-artificial-intelligence/
publicize_google_plus_url:
  - https://plus.google.com/+DanElton/posts/BTYrqGUwEbW
publicize_twitter_user:
  - moreisdifferent
publicize_tumblr_url:
  - http://moreisdifferentblog.tumblr.com.tumblr.com/post/120409735173
publicize_path_id:
  - 556bcdb3f5c6710f991ea597
publicize_linkedin_url:
  - 'https://www.linkedin.com/updates?discuss=&scope=90218007&stype=M&topic=6010976067773353984&type=U&a=QoUc'
categories:
  - Neuroscience
  - non-technical
tags:
  - AI
  - futurism
  - Nontechnical
---
Recently we have seen a slew of popular films that deal with artificial intelligence &#8211; most notably _The Imitation Game,_ _Chappie_, _Ex Machina,_ and _Her._ However, despite over five decades of research into artificial intelligence, there remain many tasks that humans find simple which computers cannot do. Given the slow progress of AI, for many the prospect of computers with human-level intelligence seems further away today than it did when Isaac Asimov&#8217;s classic _I, Robot_ was published in 1950.  The fact is, however, that today neuromorphic chips offer a plausible path to realizing human-level artificial intelligence within the next few decades. <!--more-->


  
Starting in the early 2000&#8217;s there was a realization that neural network models – based on how the human brain works – could solve many tasks that could not be solved by other methods. The buzzphrase &#8216;[deep learning](http://en.wikipedia.org/wiki/Deep_learning)&#8216; has become a catch-all term for neural network models and related techniques. Neuromorphic chips implement deep learning algorithms directly into hardware and thus are vastly faster and more efficient than running neural network models on conventional computer hardware. Neuromorphic chips are currently being developed by a variety of public and private entities, including DARPA, the EU, IBM and Qualcomm.



**The representation problem
  
** 

A key difficulty solved by neural networks is the problem of programming conceptual categories into a computer, also called the “representation problem”. Programming a conceptual category requires constructing a “representation” in the computer&#8217;s memory to which phenomena in the world can be mapped. For example &#8220;Clifford&#8221; __would be mapped to the category of “dog” and also “animal” and “pet”, while a VW Beatle would be mapped to “car”. Constructing a representation is very difficult since the members of a category can vary greatly in their appearance – for instance a “human”­ may be male or female, old or young, and tall or short. Even a simple object, like a cube, will appear different depending on the angle it is viewed from and how it is lit. Since such conceptual categories are constructs of the human mind, it makes sense that we should look at how the brain itself stores representations. Neural networks store representations in the connections between neurons (called synapses), each of which contains a value called a “weight”. Instead of being programmed, neural networks learn what weights to use through a process of training. After observing enough examples, neural networks can categorize new objects they have never seen before, or at least offer a best guess. Today neural networks have become a dominant methodology for solving classification tasks such as handwriting recognition, speech to text, and object recognition.

**Key differences** 

Neural networks are based on simplified mathematical models of how the brain&#8217;s neurons operate. While any mathematical model can be simulated on today’s computers, today&#8217;s hardware is very inefficient for simulating neural network models. This inefficiency can be traced to fundamental differences between how the brain operates vs how digital computers operate. While computers store information as a string of 0s and 1s, the synaptic “weights” the brain uses to store information can fall anywhere in a range of values – ie. the brain is analog rather than digital. More importantly, in a computer the number of signals that can be processed at the same time is limited by the number of CPU cores – this may be between 8-12 on a typical desktop or 1000-100,000 on a supercomputer. While 100,000 sounds like a lot, this is tiny compared to the brain, which simultaneous processes up to a _trillion_ (1,000,000,000,000) signals in a massively parallel fashion.

**Low power consumption**

The two main differences between brains and today’s computers (parallelism & analog storage) contribute to the brain’s amazing energy efficiency. Natural selection made the brain remarkably energy efficient, since hunting for food is difficult. The human brain consumes only 20 Watts of a power, while a supercomputing complex capable of simulating a tiny fraction of the brain can consume millions of Watts. The main reason for this is that computers operate at much higher frequencies than the brain and power consumption typically grows with the cube of frequency. Additionally, as a general rule digital circuitry consumes more power than analog &#8211; for this reason, some parts of today’s cellphones are being built with analog circuits to improve battery life. A final reason for the high power consumption of today’s chips is that they require all signals be perfectly synchronized by a central clock, requiring a timing distribution system that complicates circuit design and increases power consumption by up to 30%. Copying the brain&#8217;s energy efficient features (low frequencies, massive parallelism, analog signals, asynchronicity) makes a lot of economic sense and is currently the main driving force behind the development of neuromorphic chips.

**Fault tolerance**

Another force behind the development of neuromorphic chips is the fact that, like the brain, they are fault-tolerant – if a few components fail the chip continues functioning normally.  Some neuromorphic chip designs can sustain defect rates [as high as 25%](http://media.scgp.stonybrook.edu/presentations/20110713_Likharev.pdf) ! This is very different than today&#8217;s computer hardware, where the failure of a single component usually renders the entire chip unusable. The need for precise fabrication has driven up the cost of chip production exponentially as component sizes have become smaller. Neuromorphic chips require lower fabrication tolerances and thus are cheaper to make.

**The Crossnet approach**

Many different design architectures are being pursued. Severals of today&#8217;s designs are built around the crossbar latch, a grid of nanowires connected by &#8216;latching switches&#8217;. Here at Stony Brook University, professor Konstantin K. Likharev has developed his own design called the &#8220;Crossnet&#8221;.<figure id="attachment_1801" class="thumbnail wp-caption aligncenter style="width: 310px">

[<img class="size-medium wp-image-1801" src="http://www.danielcelton.com/wp-content/uploads/2015/06/feed_foward_crossnet.png?w=300" alt="One possible layout, showing two 'somas', or cicuits that simulate the basic functions of a neuron. " width="300" height="236" srcset="http://www.moreisdifferent.com/wp-content/uploads/2015/06/feed_foward_crossnet.png 968w, http://www.moreisdifferent.com/wp-content/uploads/2015/06/feed_foward_crossnet-300x236.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2015/06/feed_foward_crossnet-768x604.png 768w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.danielcelton.com/wp-content/uploads/2015/06/feed_foward_crossnet.png)<figcaption class="caption wp-caption-text">One possible layout, showing two &#8216;somas&#8217;, or cicuits that simulate the basic functions of a neuron. The green circles play the role of synapses.  [From presentation of K.K. Likharev.](http://media.scgp.stonybrook.edu/presentations/20110713_Likharev.pdf) </figcaption></figure> 

One possible layout is show above. Electronic devices called &#8216;somas&#8217; play the role of the neuron&#8217;s cell body, which is to add up the inputs and fire an output.  Somas can mimic neurons with several different levels of sophistication, depending on what is required for the task at hand. Importantly, somas can communicate via spikes, (short lived electrical impulses) since there is growing evidence that spike train timing in the brain carries important information and is important for certain types of learning. The red and blue lines represent axons and dendrites, the two types of neural wires. The green circles connect these wires and play the role of synapses. Each of these &#8216;latching switches&#8217; must be able to hold a &#8216;weight&#8217;, which is encoded in either a variable capacitance or variable resistance. In principle, memristers would be an ideal component here, if one could be developed that is cheap to produce and has high reliability. Crucially, all of the crossnet architecture can be implemented in traditional silicon-based (&#8220;CMOS&#8221;-like) technology. Each crossnet (as shown in the figure) is designed so they can be stacked, with additional wires connecting somas on different layers. In this way, neuromorphic crossnet technology can achieve component densities that rival the human brain.

**Near-future applications**

What applications can we expect from neuromorphic chips? According to Dr. Likarev, a professor of physics at Stony Brook University, in the short term neuromorphic chips have a myriad of applications including big data mining, character recognition, surveillance, robotic control and in driverless car technology. Google already uses neural-network like algorithms to assist in things like [search and ad placement](http://www.wired.com/2015/04/jeff-dean/).  Because neuromorphic chips have low power consumption it is conceivable that some day in the near future all cell phones will contain a neuromorphic chip which will perform tasks such as speech to text or translating road signs from foreign languages. Currently there are apps available that perform these tasks, but they require connecting to the cloud to perform the necessary computations.

**Cognitive architectures** 

According to Prof. Likharev, neuromorphic chips are the only current technology which can conceivably “mimic the mammalian cortex with practical power consumption”. Prof. Likharev estimates that his own &#8216;crossnet&#8217; technology can in principle implement the same number of neurons and connections as the brain on approximately 10 x 10 cms of silicon. Implementing the human brain with neuromorphic chips will require much more than just just creating the requisite number of neuron and connections, however. The human brain consists of thousands of interacting components or subnetworks. A collection of components and their pattern of connection is known as a ‘cognitive architecture’.   The cognitive architecture of the brain is largely unknown, but there are serious efforts underway to map it, most notably Obama&#8217;s [BRAIN initiative](https://en.wikipedia.org/wiki/BRAIN_Initiative) and the [EU&#8217;s Human Brain Project](https://www.humanbrainproject.eu/), which has the ambitious (some say overambitious) goal of simulating the [entire human brain](http://www.wired.com/2013/05/neurologist-markam-human-brain/) in the next decade. Neuromorphic chips are perfectly suited to testing out different hypothetical cognitive architectures and simulating how cognitive architectures may change due to aging or disease.

That fact that there are so many near term benefits to neuromorphic computing has led many tech giants and governments to start investing in neuromorphic chips (prominent examples include the EU&#8217;s [BrainScaleS project](http://www.artificialbrains.com/brainscales), the UK&#8217;s [SpiNNaker](http://www.artificialbrains.com/spinnaker) brain simulation machine, [IBM&#8217;s &#8220;synaptic chips&#8221;,](http://research.ibm.com/cognitive-computing/neurosynaptic-chips.shtml#fbid=AOLQ4UWlEy4) DARPA&#8217;s [SyNAPSE program](http://www.artificialbrains.com/darpa-synapse-program), and [Brain Corporation](http://www.artificialbrains.com/brain-corporation), a research company funded by Qualcomm). Looking at the breadth and scope of these projects, one can now see a clear path down which humanity will achieve human level AI.  The main unknown is how long it will take for the correct cognitive architectures to be developed along with techniques needed for training and programming them.  None the less, the fundamental physics of neuromorphic hardware is solid &#8211; namely, that they can in principle mimic the brain in component density and power consumption (and with thousands of times the speed). Even if some governments seek to ban the development of strong AI, it will be realized by someone, somewhere.  What happens then [is a matter of speculation](http://en.wikipedia.org/wiki/Technological_singularity).  If AI is capable of improvement, (as it likely would be if able to connect to the internet) the results could be disastrous for humanity. [As discussed by the philosopher Nick Bolstrom](http://www.econtalk.org/archives/2014/12/nick_bostrom_on.html) and others, developing containment and &#8216;constrainment&#8217; methods for AI is not as easy as merely &#8216;installing a kill switch&#8217;.  Therefore, we best start thinking hard about such issues now, before it is too late.

_[Follow @moreisdifferent on Twitter](http://twitter.com/moreisdifferent)_

**Further reading:**
  
Monroe, Don. &#8220;[Neuromorphic Computing Gets Ready for the (Really) Big Time](http://cacm.acm.org/magazines/2014/6/175183-neuromorphic-computing-gets-ready-for-the-really-big-time/fulltext)&#8221; _Communications of the ACM_, Vol. 57 No. 6, Pages 13-15
  
<http://www.artificialbrains.com/>
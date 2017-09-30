# Geoffrey Hinton on what's wrong with convolutional neural networks

I am going to be posting some loose notes on different biologically-inspired machine learning lectures. In this note I summarize a talk given in 2014 by Geoffrey Hinton where he discusses some shortcomings of convolutional neural networks (CNNs). Convo nets have been remarkably successful. The current deep learning boom can be traced to .

<!--more-->
[youtube https://www.youtube.com/watch?v=rTawFwUvnLE]

According to Hinton, it is actually unfortunate that CNNs work so well, because they have serious shortcomings which he believes "will be hard to get rid of". One of these is backpropagation, which, while foundational to current deep learning, requires a lot of data to construct the gradients.

Convolutional networks use multiple layers of feature detectors. Each feature detector is local, so feature detectors are repeated across space. Pooling layers give a small amount of translational invariance, but not much. Pooling layers look at a small group of nearby neurons and then just pick the neuron with the highest activation.

According to Hinton, the psychology of shape perception suggests that the human brain achieves translational and rotational invariance in a much better way. According to Hinton, the brain projects everything onto a linear manifold. We know that, roughly speaking, the brain has two seperate pathways - a "what" pathway, and a "where" pathway (see the "[https://en.wikipedia.org/wiki/Two-streams_hypothesis](two-streams hypothesis)"). Neurons in the "what" pathway respond to a particular type of stimulus regardless of where it is in the visual field. Neurons in the "where" pathway are responsible for encoding where things are. As a side note, it is hypothesized that the "where" pathway has a lower resolution then the "what" pathway.

The important thing to recognize here about the "what" pathway is that it doesn't know where objects are without the "where" pathway telling it. If a person's "where" pathway is damaged, they can tell if an object is present, but can't keep track of where it is in the visual field and where it is in relation to other objects. This leads to [https://en.wikipedia.org/wiki/Simultanagnosia](Simultanagnosia), a rare neurological condition where patients can only perceive one object at a time.

We know that edge detectors in the first layer of the visual cortex (V1) do not have translational invariance -- each detector only detects things in a small visual field. The same is true in CNNs. The difference between the brain and a CNN occurs in the higher levels. Hinton posits that the brain has modules he calls "capsules" which are particularly good at handling different types of visual stimulus and encoding things like pose -- for instance, there might be one for cars and another for faces. The brain must have a mechanism for "routing" low level visual information to what it believes is the best capsule for handling it. Note that capsules would lie in the "what" pathway, because they don't know where things are. The "where" information is saved in a seperate system. For most vision applications today, "where" information is not important.

According to Hinton, CNNs do routing by pooling. Pooling was introduced to reduce redundancy of representation and reduce the number of parameters, recognzing that precise location is not important for object detection. However, according to Hinton, deep learning engineers haven't really thought about routing specifically.

Hinton argues that the human vision system imposes rectangular coordinate frames on objects. Some simple examples found by the psychologist Irving Rock are as follows:

<img class="alignnone wp-image-3496" src="http://www.danielcelton.com/wp-content/uploads/2017/08/Screen-Shot-2017-08-27-at-1.53.41-PM-300x159.png" alt="" width="279" height="148" /><img class="alignnone wp-image-3497" src="http://www.danielcelton.com/wp-content/uploads/2017/08/Screen-Shot-2017-08-27-at-1.53.51-PM-300x229.png" alt="" width="270" height="206" />

This means linear translation is easy for the brain to handle, but rotation is hard. Studies have found the mental rotation takes time proportionate to the amount of rotation requires.

CNNs cannot do handle rotation at all. According to Hinton, CNNs cannot do 'handedness' detection, ie. they can't tell a left shoe from a right shoe.

Taking the concept of a capsule further and speaking very hypothetically, Hinton proposes that capsules may be related to cortical microcolumns. Capsules may encode information such as orientation, scale, velocity, and color. Like neurons in the output layer of a CNN, a capsule outputs a probability of whether an entity is present, but additionally have information about the orientation or pose. This is very useful, because it can allow the brain to figure out if two objects, such as mouth and a nose, are subcomponents of an underlying object (a face). According to Hinton, may have a high dimensional "pose space", with 20 or so dimensions. Hinton suggests it is easy to determine non-coincidental poses in high dimensions. Hinton says that computer vision should be like inverse graphics. So, while a graphics engine multiplies a rotation matrix times a vector to get the appearance of an object in a particular pose relative to the viewer, a vision system should take appearance and back out the matrix that gives that pose.

Toward the end of the lecture, Hinton shows a system that comnbines these concepts. Hinton's system does about as well as a CNN. However, his system is much slower.  

# More information
* [http://www.cs.toronto.edu/~fritz/absps/transauto6.pdf](unpublished research paper: *Transforming Auto-encoders*)

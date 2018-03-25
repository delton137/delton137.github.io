---
id: 10003
title: Motivations for studying how to interpret molecular machine learning models
comments: true
author: Dan Elton 
layout: post
permalink: /2018/03/23/reasons-for-interpreting-molecular-machine-learning.html
categories:
  - data science
  - machine learning
tags:
  - interpretability
...

As noted recently, there is little consensus on what a good interpretation of a model means and how to evaluate the usefulness of different methods of interpretation.[^Kim2017arXiv] There are many reasons for interpretation - to check robustness, guard against discrimination, to ensure privacy, and others. Here I want to motivate studying interpretability in the context of understanding molecules and molecular design. In this context, there are several reasons interpretation may be done:

-   To ensure the featurization+model is capturing known structure –
    property relationships. If it is not, this may suggest ways to
    improve the featurization+model.

-   To discover structure-property relations the model is using which
    conflict with chemical theory (these can easily creep in from biased
    training data or spurious correlations in the data).

-   To discover new structure-property relationships that were
    previously unknown and may be useful for molecular design.

-   To discover latent variables the model is using that may be useful
    for human designers.

The interpretation of models can also be important in the context of QSPR/QSAR models that are used in rules and regulations regarding molecules. The OECD has agreed on guidelines for chemical QSAR modeling, stating that “To facilitate the consideration of a QSAR model for regulatory purposes, it should be associated with ... a mechanistic interpretation, if possible”.[^OECDrecommendation] In the context of hazardous materials, which may be either highly toxic and/or sensitive to detonation, there is interest in using machine learning models to predict things like toxicity and sensitivity in order to give early warning to synthetic chemists so proper safety protocols can be implemented.[^Mathieu2016] If such models were to be put in use in a laboratory or industrial setting, ensuring
they are trustworthy and robust would be very important.

Interpretation, broadly construed, is being able to give an explanation as to what a model is doing to make a prediction in terms that are understandable to humans. What constitutes an “explanation" varies depending on the precise situation at hand. Philosophers have long pointed out that explanations can be nested. We all are familiar with how children, for instance, are often not satisfied with high level explanations and may ask questions to dig several layers deeper.

It's worth noting that quantum mechanical methods, such as density functional theory, can also be challenging to interpret, with some practitioners regarding them as black boxes. The challenge of interpreting quantum chemistry calculations originates from the fact that the complete wavefunction of a molecule, apart from being difficult to compute and approximate, is much too large for a human to understand. Creating human interpretable representations of molecules was recently listed as a grand challenge for the simulation of matter in the 21st century.[^Reiher2018]

The concept of interpretation depth is important for understanding the landscape of what is meant by interpretation in machine learning. As an example of how several levels of interpretation may exist, we consider a prototypical convolutional neural network which has been trained to classify different breeds of cats. One may first encounter this type of discussion:

-   **(description of accuracy)** “The model learned how
    to identify cats based on photographs. The accuracy for Siamese cats
    was 45%, the accuracy for Persian cats was 30%, ... a confusion
    matrix showed that..."

We do not consider this type of discussion an interpretation but rather a detailed description of the performance or accuracy of the model. We mention this only because descriptions of model accuracy, mapping of the domain of applicability, and residual analyses are sometimes lumped under interpretation. In our view, interpretations attempt to explain how the model reached its predictions, not how accurate the model is. A high level interpretation may be as follows

-   **(high level interpretation)** “An occlusion
    analysis and heatmap showed that the model primarily
    relies on the cat’s ears, nose and mouth to make its predictions.
    The tail and legs of the cat are not used. An analysis of color
    sensitivity showed that color information is not used, but since
    some breeds are distinguished easily by color this indicates a
    possible way the model could be improved."

More detailed descriptions may then be given

-   **(mid level interpretation)** “By training our model
    with a deconvnet[^Zeiler2014] attached we visualized the learned
    filter maps in each layer. Layer two looked at fur patches with
    different shapes and luminance properties. Layer three identified
    body parts such as differently shaped eyes and ears. Layer 4 looked
    at aggregated features such as different facial geometries...”

-   **(low level interpretation)** “We performed a Taylor
    decomposition on the output and layer-wise relevance
    propagation[^Montavon20181] to understand category relevance in
    each layer. We applied filtering methods to create
    detailed maps of now information flows through the network. Parts of
    the weight space of the model were visualized using t-SNE to
    understand the structure of the learned manifold(s). The importance
    of individual neurons in each layer to the prediction of each breed
    type was computed and visualized.”

Although new insights can be gleaned from each new level of interpretation, as interpretation becomes lower level, it tends to become more detailed and complicated, sometimes requiring more mathematical understanding to parse (for instance, understanding the properties of manifolds may require knowledge of Riemannian geometry or topology). At the lowest level, one can end up stating all of the mathematical computations the model performs, which is typically not useful.

A starting point for many discussions of interpretability is the interpetability-accuracy or interpretability-complexity tradeoff.[^Webb20148] While the tradeoff is rooted in reality, it is increasingly outdated and discussions of it can be misleading.[^Polishchuk20172618] The tradeoff assumes that only simple models are interpretable and often a delineation between “white box" models (linear regression, decision trees) that are assumed to be not very accurate and “black box" models (neural networks, kernel SVMs) which are assumed to be more accurate. While good tools for the interpretation of complex models, such as deep neural networks, are often unavailable, they are being rapidly developed.[^Guha20051109] Just as the sciences of psychology and neuroscience allow us to explain the functioning of the brain despite its enormous complexity, in an analogous fashion it seems likely we will soon be able to explain the functioning of deep networks. (It would not make much sense to say that the behaviour of a macaque monkey is “not interpretable". At most we can say certain aspects of monkey behaviour are not interpretable *at this time*.)

Just as model types categorized as “black boxes" are becoming increasingly interpretable, model types categorized as “white boxes" are becoming increasingly difficult to interpret in the era of big data. For instance, rule-based learning is hard to understand when there are thousands of rules to sift through, and decision trees become hard to understand when they very wide and deep. The intperetability-accuracy trade-off motivates a common practice whereby an interpretable model is trained next to non interpretable one. For instance, linear models and partial least squares models have been trained next to neural networks.[^Guha20041440] However, this doesn't seem very rigorous. More recently, a method for "distilling" a neural network into a decision tree was developed.[^Frosst2017arxiv]


## References
[^Kim2017arXiv]: Doshi-Velez and B. Kim, ArXiv e-prints (2017), 1702.08608.
[^OECDrecommendation]: [237th Joint Meeting of the Chemicals Committee](http//www.oecd.org/chemicalsafety/risk-assessment/37849783.pdf), P. Working Party on Chemicals, and Biotechnology, OECD principles for the Validation, for Regulatory Purposes, of (Q)SAR Models (2004).
[^Mathieu2016]: Mathieu, Industrial & Engineering Chemistry Research 55, 7569 (2016).
[^Reiher2018]: Aspuru-Guzik, R. Lindh, and M. Reiher, ACS Central Science 0, null (2018).
[^Zeiler2014]: D. Zeiler and R. Fergus, in Computer Vision – ECCV 2014, edited by D. Fleet, T. Pajdla, B. Schiele, and T. Tuytelaars (Springer International Publishing, Cham, 2014), pp. 818–833, ISBN 978-3-319-10590-1.
[^Montavon20181]: Montavon, W. Samek, and K.-R. M¨uller, Digital Signal Processing 73, 1 (2018), ISSN 1051-2004.
[^Webb20148]: J. Webb, T. Hanser, B. Howlin, P. Krause, and J. D. Vessey, Journal of Cheminformatics 6, 8 (2014), ISSN 1758-2946, URL https//doi.org/10.1186/1758-2946-6-8.
[^Polishchuk20172618]: Polishchuk, Journal of Chemical Information and Modeling 57, 2618 (2017).
[^Guha20051109]: Guha, D. T. Stanton, and P. C. Jurs, Journal of Chemical Information and Modeling 45, 1109 (2005).
[^Zhangarxiv2018]: Zhang and S.-C. Zhu, ArXiv e-prints (2018), 1802.00614.
[^Guha20041440]: Guha and P. C. Jurs, Journal of Chemical Information and Computer Sciences 44, 1440 (2004), URL http//dx.doi.org/10.1021/ci0499469.
[^Frosst2017arxiv]: Frosst and G. E. Hinton, CoRR abs/1711.09784 (2017).

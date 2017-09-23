---
id: 3329
title: Testing out decision trees, AdaBoosted trees, and random forest
comments: true
date: 2017-01-03T01:38:23+00:00
author: delton137
layout: post
guid: http://www.moreisdifferent.com/?p=3329
permalink: /2017/01/03/testing-out-decision-trees-adaboosted-trees-and-random-forest/
categories:
  - machine learning
  - python
tags:
  - data science
  - decision trees
  - machine learning
---
Recently I experimented with decision trees for classification, to get a better idea of how they work. First I created some 2 dimensional training data with 2 categories, using sci-kit-learn:

<!--more-->

{% highlight python %}

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons, make_circles, make_classification

n_samples = 1000

X1, Y1 = make_classification(n_samples = n_samples, n_features=2, n_redundant=0,
 n_informative=2, n_clusters_per_class=1,
 class_sep=1, random_state=0)

X2, Y2 = make_moons(n_samples = n_samples, noise=0.3, random_state=0)
{% endhighlight %}

Next I wrote some code to test a decision tree with different numbers of splits for the two data sets:

{% highlight python %}

def split(X):
 mid = len(X)//2
 return X[0:mid], X[mid:]

def plot_dt_vs_num_splits(X, Y, max_num_splits = 5, plot_step = .02):

 #split train and test data
 Xtrain, Xtest = split(X)
 Ytrain, Ytest = split(Y)

 #make meshgrid for plotting
 x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
 y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
 xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
 np.arange(y_min, y_max, plot_step))

plt.figure(2,figsize=(25,10))

splits = [1,2,5,10,100]
 num_splits = len(splits)

 for n in range(num_splits):
 dt = DecisionTreeClassifier(criterion = 'gini', max_depth=splits[n])
 dt.fit(Xtrain, Ytrain)

 #plot on mesh
 Z = dt.predict(np.c_[xx.ravel(), yy.ravel()])
 Z = Z.reshape(xx.shape)
 plt.subplot(1, num_splits, n+1)
 plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
 plt.scatter(X[:, 0], X[:, 1], marker='o', c=Y)
 plt.title("n_splits = " + str(splits[n]) +
 "\n train data accuracy = " + str(dt.score(Xtrain,Ytrain)) +
 "\n test data accuracy = " + str(dt.score(Xtest,Ytest)), fontsize=15)

plt.subplots_adjust(hspace=0)
 plt.axis("tight")
 plt.show()

plot_dt_vs_num_splits(X1, Y1)
plot_dt_vs_num_splits(X2, Y2)
{% endhighlight %}

<img class="alignnone wp-image-3351" src="http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits-300x134.png" alt="decision_tree_vs_num_splits" width="690" height="308" srcset="http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits-300x134.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits-768x344.png 768w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits-1024x458.png 1024w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits.png 1428w" sizes="(max-width: 690px) 100vw, 690px" />

<img class="alignnone wp-image-3350" src="http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits_2-300x134.png" alt="decision_tree_vs_num_splits_2" width="685" height="306" srcset="http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits_2-300x134.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits_2-768x343.png 768w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits_2-1024x458.png 1024w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/decision_tree_vs_num_splits_2.png 1430w" sizes="(max-width: 685px) 100vw, 685px" />

Here decision trees are exhibiting their classic weakness &#8211; so-called &#8220;high bias&#8221;, ie overfitting. Here, the tree was able to fit the data

first set of data (1000 points, 2 Gaussians) perfectly after 10 splits. In the case of the second data sets (1000 points, &#8216;moons&#8217;), the test data

accuracy decreases going from 10 to 100 splits, while the training data accuracy improves to 1, which is a sign of overfitting.

That is why people use boosted ensembles of trees. An ensemble is a weighted sum of models. In ensembles, many simple models can be combined to create a more complex one. The real utility of ensembles comes from how they are trained though, using boosting methods ([wikipedia](https://en.wikipedia.org/wiki/Boosting_(machine_learning))), which are a set of different techniques for training ensembles while preventing (or more technically delaying) overfitting.

#AdaBoost

(max depth of base estimators = 2) 

<img class="alignnone wp-image-3349" src="http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits-300x134.png" alt="ada_boost_decision_tree_vs_num_splits" width="669" height="299" srcset="http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits-300x134.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits-768x344.png 768w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits-1024x458.png 1024w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits.png 1428w" sizes="(max-width: 669px) 100vw, 669px" />**

 <img class="alignnone wp-image-3348" src="http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits_2-300x134.png" alt="ada_boost_decision_tree_vs_num_splits_2" width="665" height="297" srcset="http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits_2-300x134.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits_2-768x343.png 768w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits_2-1024x458.png 1024w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/ada_boost_decision_tree_vs_num_splits_2.png 1430w" sizes="(max-width: 665px) 100vw, 665px" />**

# Random Forest

(max depth of base estimators = 2)

Random forest is currently one of the most widely used classification techniques in business. Trees have the nice feature that it is possible to explain in human-understandable terms how the model reached a particular decision/output.  Here random forest outperforms Adaboost, but the &#8216;random&#8217; nature of it seems to be becoming apparent.. 

<img class="alignnone wp-image-3347" src="http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits-300x134.png" alt="random_forrest_decision_tree_vs_num_splits" width="658" height="294" srcset="http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits-300x134.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits-768x344.png 768w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits-1024x458.png 1024w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits.png 1428w" sizes="(max-width: 658px) 100vw, 658px" />

<img class="alignnone wp-image-3346" src="http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits_2-300x134.png" alt="random_forrest_decision_tree_vs_num_splits_2" width="656" height="293" srcset="http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits_2-300x134.png 300w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits_2-768x343.png 768w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits_2-1024x458.png 1024w, http://www.moreisdifferent.com/wp-content/uploads/2017/01/random_forrest_decision_tree_vs_num_splits_2.png 1430w" sizes="(max-width: 656px) 100vw, 656px" />

more commentary will follow.

# Talks on boosted trees

[Peter Prettenhofer &#8211; Gradient Boosted Regression Trees in scikit-learn](https://www.youtube.com/watch?v=IXZKgIsZRm0&t=1555s)

[Trevor Hastie (a more detailed talk on Boosting / Ensembles)](https://www.youtube.com/watch?v=wPqtzj5VZus&t=317s)

[MIT : boosting](https://www.youtube.com/watch?v=UHBmv7qCey4&t=2352s) (a mishmash of general concepts)

[Nando de Freitas : decision trees ](https://www.youtube.com/watch?v=-dCtJjlEEgM)

[Nando de Freitas : Random forest ](https://www.youtube.com/watch?v=3kYujfDgmNk&t=438s)

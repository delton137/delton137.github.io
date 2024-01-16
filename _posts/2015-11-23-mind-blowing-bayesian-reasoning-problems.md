---
id: 23211
title: More counterintuitive Bayesian reasoning problems
facebookcomments: true
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
Remember how in my last post I said Bayesian reasoning is counter-intuitive? It’s simultaneously maddening and fascinating because clearly, given we accept with certainty the assumptions that go into model/hypothesis selection and the prior, the application of Bayes’ theorem gives the correct probability for each model/hypothesis in light of the evidence presented.

Last time I gave the canonical example of a test for a disease. Humans tend to not take into account that if the base rate (over all frequency of having a disease) is very low, then a positive result on a test may not be very meaningful. If the probability of the test giving a false positive is 1%, and the base rate is also 1%, then the chance that you have disease given a positive result is only 50%. Once you understand this, the non-intuitive nature goes away.

Here I will give two more examples of highly non-intuitive Bayesian problems.

# The Monty Hall problem

The famous Monty Hall problem can be solved with Bayes’ rule. A statement of the problem is:

_There are three doors, labelled 1, 2, 3. A single prize has been hidden between one of them. You get to select one door. Initially your chosen door will not be opened. Instead, the gameshow host will choose one of the other two doors, and he will do so in such a way as to not reveal the prize. After this, you will be given a fresh choice among the 2 remaining doors – you can stick with your first choice, or switch to the other closed door._

Imagine you picked door 1. The gameshow host picks door 3, opening to reveal no prize. Should you (a.) stick with door 1, (b.) switch to door 2, or (c.) does it make no difference?

If you have not heard of this problem before, think it over a while.

The Bayes’ theorem solution is as follows: Denote the possible outcomes as:

 $$ D_1$$= the prize is between door 1

 $$ D_2$$= the prize is between door 2

 $$ D_3$$= the prize is between door 3

We know $$ D$$to denote the data/evidence we have, which is the fact that the gameshow host opened door 3. We can solve this using Bayes’ theorem:

$$ P(D_2|E) = \frac{P(E |D_2)P(D_2) }{ P(E) }$$

$$ P(D_2|E) = \frac{P(E |D_2)P(D_2) }{P(E |D_1)P(D_1) +P(E |D_2)P(D_2)}$$

$$ \quad = \frac{( 1)(\frac{1}{2})} { (\frac{1}{3})(\frac{1}{2}) + (1)(\frac{1}{3})} $$

$$ \quad = \frac{2}{3} $$

Therefore it is better to switch to door 2. By switching to door 2, we double our chance of winning from  $$ P(E)$$, where we must consider the probability the game show host will open door 3 when the prize is behind door 1 (=1/2) and the case where the prize is behind door 2 (=1).

Note the following mind-blowing shortcut to solving the problem:

Since door 3 was opened, we know $$ P(D_2) = 2/3$$!

# Bayesian model comparison

Bayes’ theorem allows us to compare the likelihoods of different models being true. To take a concrete example, let’s assume we have black box with a button attached. Whenever we hit the button, and a light on top of the box blinks either green or red. We hit the button a number times, obtaining a sequence:

GRRGGRGRRGRG…

Let’s say say we model the black box as a ‘bent coin’. Thus, our model says that each outcome is statistically independent from previous outcomes and the probability of getting green is $$ p_g$$given a sequence of observations. In the interest of space, I won’t solve it here.

We might have a different model, though. We may model the black box as a dice. If the dice lands on 1, the green light goes on, otherwise, the red light goes on. This corresponds to our earlier, more general model, but with  $$ p_g$$, while the second model does not.

The method of Bayesian model comparison can tell us which model is more likely. Instead of analyzing the situation with a single model, we now consider both models at the same time. I like to use the term ‘metamodel’ for this. In our metamodel, we assume equal prior probabilities for each model. We denote the sequence of flashes we observed as $$ \mathcal{H}$$stands for ‘hypothesis’, a word which we take as synonymous with ‘model’).

$$ P(\mathcal{H}_1 | s) = \frac{ P( s | \mathcal{H}_1) P(\mathcal{H}_1) }{ P(s) }$$

$$ P(\mathcal{H}_2 | s) = \frac{ P( s | \mathcal{H}_2) P(\mathcal{H}_1) }{ P(s) }$$

The relative probability of model 2 over model 1 is encoded in the ratio of the posterior probabilities:

$$ \frac{P(\mathcal{H}_1 | s) }{P(\mathcal{H}_2 | s) } = \frac{P(s| \mathcal{H}_1)}{P(s|\mathcal{H}_2)}$$

The ratio tells us the relative probability that model 1 is correct. Note that absolute probabilities of model 1 and model 2 can be computed from this using the fact that

$$ P(\mathcal{H}_1|s)+P(\mathcal{H}_2 |s)=1 $$

That’s all on model comparison for now. A more detailed discussion can be found in MacKay’s book.

# The case of the blood stains

This problem is taken directly MacKay’s book:

<pre>Two people have left traces of their own blood at the scene of a
 crime. A suspect, Oliver, is tested and found to have type ‘O’
 blood. The blood groups of the two traces are found to be of type
 ‘O’ (a common type in the local population, having frequency 60%)
 and of type ‘AB’ (a rare type, with frequency 1%). Do these data
 (type ‘O’ and ‘AB’ blood were found at scene) give evidence in
 favour of the proposition that Oliver was one of the two people
 present at the crime?</pre>

At first glance, lawyer may easily convince the jury that the presence of the type ‘O’ blood stain provides evidence that Oliver was present. The lawyer may argue the while the degree of weight it should carry may be small, since type ‘O’ is fairly common, nonetheless the presence of type ‘O’ should count as positive evidence. However, this is not the case!

Denote the proposition ‘the suspect and one unknown person were present’ by $$ \bar{S}$$, states that “two unknown people from the population were present”.

If we assume that the suspect, Oliver, was present, then the likelihood of the data is simply the likelihood of having a person with blood type ‘AB’:

$$ P(D|S) = p_{AB} = .01$$

The likelihood of the other case is the likelihood that two unknown people drawn from the population have blood types ‘AB’ and ‘O”:

$$ P(D|\bar{S}) = 2 p_{AB}p_{O} = .083$$

The second case is more likely. The likelihood ratio is

$$ \frac{.01}{.083} = .83$$

Thus the data actually provides weak evidence against the supposition that Oliver was present. Why is this?

We can gain some insight by first considering another suspect, Alberto, who has blood type $$ \bar{S}$$. In this case, the ratio is:

$$ \frac{S'}{\bar{S}}=\frac{p_{O}}{2p_{AB}p_{O}}=\frac{.6}{(2)(.01)(.6)}=50$$

Clearly, in this case, the evidence does support the hypothesis that Alberto was there. MacKay elaborates: (my emphasis added)

Now let us change the situation slightly; imagine that 99% of people are of blood type O, and the rest are of type AB. Only these two blood types exist in the population. The data at the scene are the same as before. Consider again how these data influence our beliefs about Oliver, a suspect of type O, and Alberto, a suspect of type AB. Intuitively, we still believe that the presence of the rare AB blood provides positive evidence that Alberto was there. But does the fact that type O blood was detected at the scene favour the hypothesis that Oliver was present? If this were the case, that would mean that regardless of who the suspect is, the data make it more probable they were present; everyone in the population would be under greater suspicion, which would be absurd. The data may be compatible with any suspect of either blood type being present, but if they provide evidence for some theories, they must also provide evidence against other theories.

Here is another way of thinking about this: imagine that instead of two people’s blood stains there are ten (independent stains), and that in the entire local population of one hundred, there are ninety type O suspects and ten type AB suspects. Consider a particular type O suspect, Oliver: without any other information, and before the blood test results come in, there is a one in 10 chance that he was at the scene, since we know that 10 out of the 100 suspects were present. We now get the results of blood tests, and find that nine of the ten stains are of type AB, and one of the stains is of type O. Does this make it more likely that Oliver was there? No, there is now only a one in ninety chance that he was there, since we know that only one person present was of type O.

MacKay continues to elaborate this problem by doing a more explicit calculation. In the end the conclusion is:

If there are more type O stains than the average number expected under hypothesis $$ \bar{S}$$, then the data reduce the probability of the hypothesis that he was there.

Note the similarity with the drug test example. The base rate of blood stains must be considered.

# Bayesian statistics in court

Ideally, a jury would apply Bayesian reasoning to rank the likelihood of different hypotheses. The chance that a person is a suspect is denoted $$ \frac{S}{\bar{S}}$$. In the words of MacKay:

“In my view, a jury’s task should generally be to multiply together carefully evaluated likelihood ratios from each independent piece of evidence with an equally carefully reasoned prior probabilities.”

The potential for Bayesian methods to improve the criminal justice system is huge. The issue though is that statistics can also be easily manipulated by subtle changes in the inputs. Judges and juries can easily be misled if they have no understanding of statistics. One solution is to train the jury in Bayesian statistics during the course of the case, and this has been used by lawyers to help juries understand complicated blood stain DNA evidence. However, many judges (who usually lack a deep understanding of statistics) are immensely skeptical of whether the jury can properly analyze complex statistical data without being hoodwinked. From their point of view, statistics are too opaque. There is the question of the confidence that can be placed in the jury to properly apply Bayesian methodology, even after training. Should juries be quizzed on their ability to do Bayesian reasoning before being allowed to deliberate? The challenge is to explain complicated statistical methodologies in a way that lay people can understand, and no solution has yet been found that all parties agree upon. For this reason, the use of Bayesian statistics in courts has been banned in the UK. Obviously, this is not at all an optimal situation.

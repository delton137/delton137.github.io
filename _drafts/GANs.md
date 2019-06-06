choosing an objective function for a GAN
========================================

The original paper on GANs[@Goodfellow2014:2672] presented the following
optimization problem as $$\label{eqn:objfun}
    \min_G \max_D V(D,G) = \mathbb{E}_{\bs{x}\in p_{\ff{data}}(\bs{x})}[\log D(\bs{x})] + \mathbb{E}_{\bs{z}\in p_{\bs{z}}(\bs{z})} [\log(1 - D(G(\bs{z}))]$$
This form of the objective function (also called the value function) has
a nice theoretical interpretation as a two person minimax game. The
solution to the minimax problem can be interpreted as a Nash equilibria,
a concept from game theory. However, this objective function is rarely
used in practice. Firstly, as noted in the original paper, this
objective function does not provide a very strong gradient signal when
training starts and $\log(1 - D(G(\bs{z}))$ is close to zero. To get a
larger gradient when training $G$, it is better to maximize
$\log( D(G(\bs{z})))$ when training the generator.

Before moving onto other objective functions, it is worth trying to
understand what this objective function does. The objective function in
equation [\[eqn:objfun\]] can be expressed in terms of the
Jensen-Shannon divergence $JS(p,q)$:[@Goodfellow2014:2672]
$$\mathcal{C}(G) = -\log (4) + 2 JS(p_{\ff{data}}, p_{\theta_{G}})$$
**Jensen-Shannon divergence** is defined as:
$$JS(p,q) = \frac{1}{2} \left[ D_{\ff{KL}}\left(p\bigg{|}\bigg{|} \frac{p+q}{2}\right)  +  D_{\ff{KL}}\left(q\bigg|\bigg| \frac{p+q}{2}\right) \right]$$
where $D_{\ff{KL}}(p||q)$ is the famous **Kullback-Leibler (KL)
divergence**: $$\label{eqn:KLdiv}
    D_{\ff{KL}}(p||q) = \int d\bs{x} p(\bs{x}) \log \frac{p(\bs{x})}{q(\bs{x})}$$

KL divergence is always greater than zero and equals zero if and only if
$p(\bs{x}) = q(\bs{x})$. While KL divergence measures the similarity
between two distributions, it is not symmetric and violates the triangle
inequality, so it is not a metric.[@Mehta2018arxiv] Jenson-Shannon
divergence is a metric and therefore is sometimes called Jenson-Shannon
distance. It can be shown that minimizing the log-likelihood of data
under a model is the same as minimizing the KL divergence between the
data distribution and the model distribution (ie.
$\min D_{\ff{KL}}(p_{\ff{data}} ||p_\theta)$).[@Mehta2018arxiv]

Objective function [\[eqn:objfun\]] runs into issues in high dimensional
spaces. Empirically, most high dimensional real world data lies close to
a low dimensional manifold. Therefore, when training a GAN it becomes
extremely unlikely that the initial generator distribution $G(\bs{x})$
overlaps with the target distribution -- it would be like finding a
needle in a haystack. If there is little or no intersection between
distributions, KL divergence become infinite and the gradient signal
becomes zero. JS divergence is better behaved in the sense that it


Load data
{% highlight python %}
mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
{% endhighlight %}

Create a ***placeholder*** variable
{% highlight python %}
x = tf.placeholder(tf.float32, [None, 784])
{% endhighlight %}

{% highlight python %}
y = tf.nn.softmax(tf.matmul(x, W) + b)
{% endhighlight %}

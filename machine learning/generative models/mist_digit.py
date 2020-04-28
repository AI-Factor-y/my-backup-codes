from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

batch_xs, batch_ys = mnist.train.next_batch(100)
data = batch_xs[0]
label = batch_ys[0]
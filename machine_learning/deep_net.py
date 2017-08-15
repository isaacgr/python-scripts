# objective is to take the mnist set, feed it to a nn and output
# the correct number

# our feautres will be a pixel value (0 or 1)
# is it part of the number or is is white space
'''
input -> weight -> hidden layer 1 -> activation function -> weights -> hidden layer 2
..... -> output layer
'''
# feed forward nn, the data gets passed straight through
# compare the ouput  to the intended output with a cost function
# then use an optimizer to attempt to minimize that cost
# that then goes back and manipulates the weights (backpropogation)
# then feed forward + backpropogation = epoch

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data", one_hot=True)
# one hot will output data as below
# only one feature is 'on' at a time
'''
0 = [1,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0]
3 = [0,0,0,1,0,0,0,0,0]
'''
# these can be unique
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100 # go through batches of 100 features at a time and feed them to the nn to maniputlate the weights

# height x width
# 28x28 = 784
x = tf.placeholder('float',[None, 784])
y = tf.placeholder('float')

def neural_network_model(data):
    # will create a tensor(array) of wieghts
    # the bias is added at the end (input*weights + bias)
    hidden_1_layer = {
        'weights':tf.Variable(tf.random_normal([784, n_nodes_hl1])),
        'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))
        }

    hidden_2_layer = {
    'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
    'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))
        }

    hidden_3_layer = {
        'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
        'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))
        }

    output_layer = {
        'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
        'biases': tf.Variable(tf.random_normal([n_classes]))
        }

    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1) #threshold function, takes the value and passes to activation function

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.add(tf.matmul(l3, output_layer['weights']), output_layer['biases'])

    return output

def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
    # has a parameter that is learning rate, default to 0.001
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    #cycles of feed forward and backpropogation
    hm_epochs = 10
    with tf.Session() as sess:
        # begins the session
        sess.run(tf.global_variables_initializer())
        # train the data
        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples/batch_size)): # tells us how many times we need to cycle
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})  # optimizing the cost by modifying the weights being passed to the layers
                epoch_loss += c
            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss', epoch_loss)
        # once weights are optimized, run them through the model
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1)) # get the maximum value in those arrays, and compare them
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))

train_neural_network(x)

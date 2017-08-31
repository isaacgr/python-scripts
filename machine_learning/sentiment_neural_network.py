# objective is to take the mnist set, feed it to a nn and output
# the correct number

# our feautres will be a pixel value (0 or 1)
# is it part of the number or is is white space
'''
input -> weight -> hidden layer 1 -> activation function -> weights -> hidden layer 2
..... -> output layer
'''
# feed forward nn, the data gets passed straight through
# compare the ouput  to the intended output with a cost function (how close are we to the intended target)
# then use an optimizer to attempt to minimize that cost(AdamOptimizer, SGD, AdaGrad)
# that then goes back and manipulates the weights (backpropogation)
# then feed forward + backpropogation = epoch (this is one cycle of feedforward and backpropogation)

import tensorflow as tf
from create_sentiment_featuresets import create_featuresets_and_labels
import numpy as np

train_x, train_y, test_x, test_y = create_featuresets_and_labels('pos.txt', 'neg.txt')

# one hot will output data as below
# only one feature is 'on' at a time
'''
0 = [1,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0]
3 = [0,0,0,1,0,0,0,0,0]
'''
# these can be unique
# deep nn with multiple layers
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 2
batch_size = 100

x = tf.placeholder('float',[None, len(train_x[0])]) # just a string of pixel values, dont need to maintain the shape
y = tf.placeholder('float')

def neural_network_model(data):
    # will create a tensor(array) of wieghts
    # the bias is added at the end (input*weights + bias)
    # the weights are a tensorflow Variable
    # that variable is a random_normal
    # we will specify the shape of that normal
    hidden_1_layer = {
        'weights':tf.Variable(tf.random_normal([len(train_x[0]), n_nodes_hl1])),
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
    # complete setting up the basics of a computation graph
    return output

def train_neural_network(x):
    prediction = neural_network_model(x)
    # using cross entropy with logits as our cost function
    # calculate the difference between our prediction and known label
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
    # has a parameter that is learning rate, default to 0.001
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    # cycles of feed forward and backpropogation
    hm_epochs = 10
    with tf.Session() as sess:
        # begins the session
        sess.run(tf.global_variables_initializer())
        # train the data
        for epoch in range(hm_epochs):
            epoch_loss = 0

            i=0
            while i < len(train_x):
                start = i
                end = i+batch_size
                batch_x = np.array(train_x[start:end])
                batch_y = np.array(train_y[start:end])

                _, c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})  # optimizing the cost by modifying the weights being passed to the layers
                epoch_loss += c
                i += batch_size

            print('Epoch', epoch+1, 'completed out of', hm_epochs, 'loss', epoch_loss)
        # once weights are optimized, run them through the model
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1)) # get the maximum value in those arrays, and compare them
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy', accuracy.eval({x: test_x, y: test_y}))

train_neural_network(x)

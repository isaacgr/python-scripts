# a tensor is an array object
# tensor flow is matrix manipulation (function on tensors)

import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1,x2) # just an abstract tensor in computation graph

with tf.Session() as sess:
    output = sess.run(result)  # this is the actual multiplication
    print(output)

#sess.close()     # need to close the session when completed, dont need to do this with the above code

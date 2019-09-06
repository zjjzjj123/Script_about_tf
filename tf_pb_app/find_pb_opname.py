import tensorflow as tf

gf = tf.GraphDef()
# gf.ParseFromString(open('model1.pb', 'rb').read())
gf.ParseFromString(open('graph_opt_mobile.pb','rb').read())
for n in gf.node:
    print(n.name + ' ===> ' + n.op)
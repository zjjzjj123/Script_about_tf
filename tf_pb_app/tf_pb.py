'''
1.使用tf保存成pb文件  然后利用pb文件快速建立结构图
2.明天写一个blog  有关pb文件的
3.输入要正确  输出要正确
4.知道输入和输出的名字很重要 可以根据脚本读取各个网络输出的部分
'''

import tensorflow as tf
from tensorflow.python.framework import graph_util
import os
import netron
from tensorflow.python.platform import gfile

def creat_pb():
    with tf.Session(graph=tf.Graph()) as sess:
        x = tf.placeholder(tf.int32,name='x')
        y = tf.placeholder(tf.int32,name='y')
        b = tf.Variable(1,name='b')
        xy = tf.multiply(x,y)
        op = tf.add(xy,b,name='op')
        sess.run(tf.global_variables_initializer())
        constant_graph = graph_util.convert_variables_to_constants(sess,sess.graph_def,['x','y','op'])
        print(sess.run(op,feed_dict={x:1,y:2})) # 输出op节点的值

        with tf.gfile.FastGFile('model1.pb','wb') as f:
            f.write(constant_graph.SerializeToString()) #

def restore_pb():
    sess = tf.Session()
    with tf.gfile.FastGFile('model1.pb','rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())  #解析图
        graph = sess.graph.as_default()
        tf.import_graph_def(graph_def,name='') #这里定义名称的话后面一定要用到
        sess.run(tf.global_variables_initializer())

        print(sess.run('b:0')) #'b:0'必须按照这样的格式
        input_x = sess.graph.get_tensor_by_name('x:0')
        input_y = sess.graph.get_tensor_by_name('y:0')
        op = sess.graph.get_tensor_by_name('op:0')
        print(sess.run(op,feed_dict={input_x:2,input_y:3}))

def view_pb():
    pb_file = 'model1.pb'
    netron.start(pb_file)
def creat_pb2():
    with tf.Session(graph=tf.Graph()) as sess:
        x = tf.placeholder(tf.int32,name='x')
        y = tf.placeholder(tf.int32,name='y')
        b = tf.Variable(1,name='b')

        xy = tf.multiply(x,y,name='xy')
        op = tf.add(xy,b,name='op')

        sess.run(tf.global_variables_initializer())
        constant_graph = graph_util.convert_variables_to_constants(sess,sess.graph_def,['x','y','op'])
        with tf.gfile.FastGFile('model2.pb','wb') as f:
            f.write(constant_graph.SerializeToString())


def restored_pb2():
    with tf.gfile.FastGFile('model2.pb','rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        graph = tf.get_default_graph()
        tf.import_graph_def(graph_def,name='')
        sess_graph = tf.Session(graph=graph)
        sess_graph.run(tf.global_variables_initializer())

        print(sess_graph.run('b:0'))
        input_x = sess_graph.graph.get_tensor_by_name('x:0')
        input_y = sess_graph.graph.get_tensor_by_name('y:0')
        op = sess_graph.graph.get_tensor_by_name('op:0')
        print(sess_graph.run(op,feed_dict={input_x:2,input_y:3}))


if __name__ == '__main__':
    print('start')
    creat_pb2()
    print('end')

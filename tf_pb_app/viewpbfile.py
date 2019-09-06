import tensorflow as tf
from keras.models import load_model
from tensorflow.python.platform import gfile

# import netron
# model = 'framewise_recognition_under_scene.pb'
# netron.start(model)
import netron
model = 'graph_opt_mobile.pb'
netron.start(model)

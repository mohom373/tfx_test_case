import os
import random
import tensorflow as tf
import PIL.Image
from io import BytesIO


IMG_HEIGHT = 180
IMG_WIDTH = 180

flower_classes = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

label_map = {
    'daisy': 0,
    'dandelion': 1,
    'roses': 2,
    'sunflowers': 3,
    'tulips': 4
}

# The following functions can be used to convert a value to a type compatible
# with tf.train.Example.

def _bytes_feature(value):
  """Returns a bytes_list from a string / byte."""
  if isinstance(value, type(tf.constant(0))):
    value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _float_feature(value):
  """Returns a float_list from a float / double."""
  return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))

def _int64_feature(value):
  """Returns an int64_list from a bool / enum / int / uint."""
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def serialize_example(image_string, label):
    image_shape = tf.io.decode_jpeg(image_string).shape

    feature = {
        'label': _int64_feature(label),
        'image_raw': _bytes_feature(image_string),
    }

    example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
    return example_proto.SerializeToString()

def write_TFRecord(image_path, label):
    image = PIL.Image.open(image_path)
    image = image.resize((IMG_HEIGHT, IMG_WIDTH))

    with BytesIO() as output:
        image.save(output, format='JPEG')
        image_bytes = output.getvalue()

    example = serialize_example(image_bytes, label)
    return example

"""
  Open a new TFRecord and use the different paths of 
  train and test data to create train and test tfrecord files
"""
def open_and_write_TFRercord(train_data_dir, test_data_dir, train_tfrecord, test_tfrecord):
  with tf.io.TFRecordWriter(train_tfrecord) as writer:
      for flower_class in flower_classes:
          for file in os.listdir(os.path.join(train_data_dir, flower_class)):
              image_path = os.path.join(train_data_dir, flower_class, file)
              label = label_map[flower_class]
              writer.write(write_TFRecord(image_path, label))

  with tf.io.TFRecordWriter(test_tfrecord) as writer:
      for flower_class in flower_classes:
          for file in os.listdir(os.path.join(test_data_dir, flower_class)):
              image_path = os.path.join(test_data_dir, flower_class, file)
              label = label_map[flower_class]
              writer.write(write_TFRecord(image_path, label))

print("Train and test TFRecord files created.")

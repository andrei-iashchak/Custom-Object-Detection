import urllib
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import json
import time
import glob

from io import StringIO
from PIL import Image

from flask import Flask
from flask import request
from flask import jsonify

import requests
from io import BytesIO

from multiprocessing.dummy import Pool as ThreadPool

MAX_NUMBER_OF_BOXES = 10
MINIMUM_CONFIDENCE = 0.6

# Path to frozen detection graph. This is the actual model that is used for the object detection.
MODEL_NAME = 'output_inference_graph'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'


def load_image_from_url(URL):
    resp = urllib.urlopen(URL)
    return np.asarray(bytearray(resp.read()), dtype="uint8")

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)

def detect_objects(image_url):
    image_np = load_image_from_url(image_url)
    image_np_expanded = np.expand_dims(image_np, axis=0)

    return sess.run([detection_boxes, detection_scores, detection_classes, num_detections], feed_dict={image_tensor: image_np_expanded})


# TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image-{}.jpg'.format(i)) for i in range(1, 4) ]

# Load model into memory
print('Loading model...')
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

print('detecting...')
with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# @NOTE: Can be moved to left and became executes on flask hook
app = Flask(__name__)
print('flask app initialized...')
@app.route('/')
def index():
    image_path = request.args.get('image')
    print(image_path)
    print(type(image_path))
    result = detect_objects(image_path)
    return jsonify(result)

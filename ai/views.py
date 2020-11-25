from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import numpy
import json
from tensorflow import Graph

import pandas as pd
import os
import keras
import matplotlib.pyplot as plt
from keras.layers import Dense, GlobalAveragePooling2D
from keras.applications import MobileNet
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.optimizers import Adam

img_height, img_width = 224, 224
# with open('./models/imagenet_classes.json', 'r') as f:
#     labelInfo = f.read()

model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model = load_model('./training_model/chest-xray-pneumonia-improved.h5')


def studyImage(request):
    # file_object = request.FILES['file']
    # file = FileSystemStorage()
    # file.save(file_object.name, file_object)
    # return render(request, 'ai/pneumonia_results.html')

    fileObj = request.FILES['file']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    testimage = '.' + filePathName
    img = image.load_img(testimage, target_size=(244, 244))
    x = image.img_to_array(img)
    x = numpy.expand_dims(x, axis=0)
    x = preprocess_input(x)
    # x = x / 255
    # x = x.reshape(1, img_height, img_width, 3)
    with model_graph.as_default():
        with tf_session.as_default():
            p_good, p_ill = numpy.around(model.predict(x), decimals=2)[0]

    import numpy as np
    # predictedLabel = str(np.argmax(predi[0]))

    p_good = round(p_good*100, 2)
    p_ill = round(p_ill*100, 2)


    context = {'filePathName': filePathName, 'p_good': p_good, 'p_ill': p_ill}
    return render(request, 'ai/pneumonia_results.html', context)

# def get_rez(pic):
#     img = image.load_img(pic, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
#     p_good, p_ill = np.around(model.predict(x), decimals=2)[0]
#     return {'p_good': p_good, 'p_ill': p_ill}


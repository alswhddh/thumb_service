from flask import Blueprint, render_template , request
from sqlalchemy import func

import os
import base64
import io
from PIL import Image
import cv2
import numpy as np

from keras.models import Model, load_model

bp = Blueprint('face',__name__,url_prefix='/face')
# model = load_model('C:/Users/User/Documents/web/thumb/nail/keras_models/2020_11_23_17_19_13.h5')
model = load_model('./nail/keras_models/beautiModel.h5')

@bp.route('/',methods=('GET', 'POST'))
def _class():
    if request.method == "GET":
        return render_template('thumbnail/beautiScore.html')
    if request.method =="POST":
        imageData = str(request.form['test'])
        
        prediction = round(score_predict(imageData),3)
        return render_template('thumbnail/beautiScore.html',imageData = imageData , prediction = prediction)

def stringToRGB(base64_string):
    imgdata = base64.b64decode(base64_string)
    dataBytesIO = io.BytesIO(imgdata)
    image = Image.open(dataBytesIO)
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

def score_predict(data):
    splitIndex = data.find(',')
    data = data[splitIndex+1:]
    testImg = stringToRGB(data)

    testimg_resized = cv2.resize(testImg,(350,350))
    testimg_resized = testimg_resized.astype(np.float32) / 255
    testimg_resized = np.expand_dims(testimg_resized, axis=0)
    predict = model.predict(testimg_resized)

    return predict[0][0]
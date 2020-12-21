from flask import Blueprint, render_template , request
from sqlalchemy import func

import os
import base64
import io
from PIL import Image
import cv2
import numpy as np
import face_recognition

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
        
        prediction , imgData = score_predict(imageData)
        prediction = round(prediction,3)
        imgData = cv2.imencode('.jpg', imgData)
        b64_string = "data:image/jpeg;base64," + base64.b64encode(imgData[1]).decode('utf-8')
        return render_template('thumbnail/beautiScore.html',imageData = b64_string , prediction = prediction)

def stringToRGB(base64_string):
    imgdata = base64.b64decode(base64_string)
    dataBytesIO = io.BytesIO(imgdata)
    image = Image.open(dataBytesIO)
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

def score_predict(data):
    splitIndex = data.find(',')
    data = data[splitIndex+1:]
    testImg = stringToRGB(data)

    face_locations = face_recognition.face_locations(testImg)

    if len(face_locations) == 0:
        return 0

    top, right, bottom, left = face_locations[0]
    top -= 50
    right += 50
    bottom += 50
    left -=50
    if top < 0:top=0
    if right < 0:right=0
    if bottom < 0:bottom=0
    if left < 0:left=0

    face_image = testImg[top:bottom, left:right]

    face_image = cv2.resize(face_image,(350,350))
    testimg_resized = face_image.astype(np.float32) / 255
    testimg_resized = np.expand_dims(testimg_resized, axis=0)
    predict = model.predict(testimg_resized)

    return predict[0][0] , face_image
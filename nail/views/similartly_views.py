from flask import Blueprint, render_template , request
from sqlalchemy import func
from ..models import thumbnail
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

import pickle
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
from torchvision import models
import base64
import io
from PIL import Image
import cv2
import numpy as np
import pandas as pd
from torchvision import datasets, transforms
from sklearn.metrics.pairwise import cosine_similarity

bp = Blueprint('similar',__name__,url_prefix='/similar')

file=open("./nail/static/data/imgVectors","rb")
allVectors=pickle.load(file)

@bp.route('/',methods=('GET', 'POST'))
def _similar():
    if request.method == "GET":
        return render_template('thumbnail/similarly.html')
    if request.method =="POST":      
        querySet = thumbnail.query
        df = pd.read_sql(querySet.statement, querySet.session.bind)
        imageData = str(request.form['test'])
        resultDf = getSimilarly(imageData , df)
        title = resultDf['title'].values[:5]
        imageAdr = resultDf['imgAdr'].values[:5]
        return render_template('thumbnail/similarly.html' ,imageData = imageData , title = title , imageAdr = imageAdr)

class Img2VecResnet18():
    def __init__(self): 
        self.device = torch.device("cpu")
        self.numberFeatures = 2048
        self.modelName = "resnet-50"
        self.model, self.featureLayer = self.getFeatureLayer()
        self.model = self.model.to(self.device)
        self.model.eval()
        self.toTensor = transforms.ToTensor()
        
        # normalize the resized images as expected by resnet18
        # [0.485, 0.456, 0.406] --> normalized mean value of ImageNet, [0.229, 0.224, 0.225] std of ImageNet
        self.normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        
    def getVec(self, img):
        image = self.normalize(self.toTensor(img)).unsqueeze(0).to(self.device)
        embedding = torch.zeros(1, self.numberFeatures, 1, 1)
        
        # _ in-place 연산자
        def copyData(m, i, o): embedding.copy_(o.data)

        h = self.featureLayer.register_forward_hook(copyData)
        self.model(image)
        h.remove()

        return embedding.numpy()[0, :, 0, 0]

    def getFeatureLayer(self):
        
        cnnModel = models.resnet50(pretrained=True)
        layer = cnnModel._modules.get('avgpool')
        self.layer_output_size = 2048
        
        return cnnModel, layer

def stringToRGB(base64_string):
    imgdata = base64.b64decode(base64_string)
    dataBytesIO = io.BytesIO(imgdata)
    image = Image.open(dataBytesIO)
    image = image.convert('RGB') # RGB 3차원으로 변경해서 이미지정규화
    return image

def getSimilarly(imgdata , data):
    splitIndex = imgdata.find(',')
    imgdata = imgdata[splitIndex+1:]

    im = stringToRGB(imgdata)
    img2vec = Img2VecResnet18()
    transformationForCNNInput = transforms.Compose([transforms.Resize((224,224))])

    upImgData = {}
    testIm = transformationForCNNInput(im)
    vec = img2vec.getVec(testIm)
    upImgData['newImage'] = vec

    v1 = np.array(list(allVectors.values()))
    v2 = np.array(list(upImgData.values()))
    sim_ = cosine_similarity(v1,v2)
    idx_keys = list(allVectors.keys())
    col_keys = list(upImgData.keys())

    matrix_ = pd.DataFrame(idx_keys,columns=['title'])
    matrix_['similarity']= sim_
    matrix_

    df_result = pd.merge(data[['title','imgAdr']],matrix_,left_on='title',right_on='title',how='inner')
    df_result = df_result.sort_values(ascending=False , by="similarity")
    return df_result

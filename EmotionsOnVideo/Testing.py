import cv2
import numpy as np
import warnings
from .apps import model
warnings.filterwarnings('ignore')


# Final Preprcessing of images function
def grayScale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def preprocessor(img):
    if len(img.shape) < 3:
        img = img.reshape((img.shape[0], img.shape[1], 1))
    else:
        img = grayScale(img)
    img = img/255
    return img

def predict_result(img_org):

    img_org = cv2.imdecode(np.fromstring(img_org.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    image_resize = 48
    emotion = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    # expressions = {'0':'happy', '1':'disgust', '2':'fear',
    #                '3':'sad', '4':'neutral', '5':'angry', '6':'surprise'}

    img = cv2.resize(img_org, (image_resize, image_resize))

    img = np.array(list(map(preprocessor, [img])))
    img = img.reshape(1, image_resize, image_resize, 1)
    #cm_pred = model.predict_classes(img)
    #text = expressions.get(str(cm_pred[0]))

    cm_pred = model.predict(img)
    # print(np.argmax(cm_pred[0]))
    # text = expressions.get(str(np.argmax(cm_pred[0])))
    text = emotion[np.argmax(cm_pred[0])]

    return text

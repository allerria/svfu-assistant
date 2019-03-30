import face_recognition
import pandas as pd
import numpy as np
import cv2
from flask import request, Flask

prepods_with_embeddings = pd.read_csv("prepods_with_photo2.csv")


def recognize(img):
    embedding = np.array([face_recognition.face_encodings(img)[0]])
    print(prepods_with_embeddings.ix[np.argmin(np.linalg.norm(prepods_with_embeddings.ix[:, 7:] - embedding)), :7])


app = Flask(__name__)


@app.route('/recognize', methods=['POST'])
def get_recognize():
    filestr = request.files['file'].read()
    # convert string data to numpy array
    npimg = np.fromstring(filestr, np.uint8)
    # convert numpy array to image
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    recognize(img)
    return ""


app.run(host="0.0.0.0", port=5001)

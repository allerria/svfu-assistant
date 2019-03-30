from api import *
import face_recognition
import numpy as np
import pandas as pd
import cv2


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    return response
#
# with open("prepods_with_photo2.csv", "r") as f:
#     print(f.read())
#
# prepods_with_embeddings = pd.read_csv("prepods_with_photo2.csv")
#
#
# def recognize(img):
#     embedding = np.array([face_recognition.face_encodings(img)[0]])
#     print(prepods_with_embeddings.ix[np.argmin(np.linalg.norm(prepods_with_embeddings.ix[:, 7:] - embedding)), :7])
#
#
# @app.route('/recognize', methods=['POST'])
# def get_recognize():
#     filestr = request.files['file'].read()
#     # convert string data to numpy array
#     npimg = np.fromstring(filestr, np.uint8)
#     # convert numpy array to image
#     img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
#     recognize(img)
#     return ""


if __name__ == '__main__':
    db.bind(**app.config['PONY'])
    db.generate_mapping()
    app.run(host='0.0.0.0')

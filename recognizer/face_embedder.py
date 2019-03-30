# import pandas as pd
# import numpy as np
# import face_recognition
# from urllib import request
# import cv2
#
#
# def url_to_image(url):
#     # download the image, convert it to a NumPy array, and then read
#     # it into OpenCV format
#     resp = request.urlopen(url)
#     image = np.asarray(bytearray(resp.read()), dtype="uint8")
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#
#     # return the image
#     return image
#
#
# def load_prepods_embeddings():
#     prepods = pd.read_csv("prepods.csv")
#     encodings = []
#
#     for idx, url in enumerate(prepods['img_url']):
#         # download the image URL and display it
#         if type(url) != str or url.rsplit(".", 1)[
#             -1].lower() == "gif" or url == "https://www.s-vfu.ru/upload/no_photo.jpg":
#             encodings.append([10.0] * 128)
#             continue
#         image = url_to_image(url)
#         encoding = face_recognition.face_encodings(image)
#         if len(encoding) == 0:
#             encodings.append([10.0] * 128)
#             continue
#         encodings.append(encoding[0])
#         print(idx)
#
#     kek = pd.concat([prepods, pd.DataFrame(data=encodings)], axis=1)
#     kek.to_csv("prepods_with_photo2.csv")

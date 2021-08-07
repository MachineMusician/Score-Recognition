# padding image with white
# for square image

import numpy as np
import cv2
import pandas as pd
from glob import glob
import os

note_name = ["Eight", "Half", "Quarter", "Sixteenth", "Whole"]

image_size = 256


for note in note_name:
    # train data
    if not os.path.exists("data_{}/datasets-train/Notes/".format(image_size) + note):
        os.makedirs("data_{}/datasets-train/Notes/".format(image_size) + note)

    image_list = glob("data/datasets-train/Notes/"+note+"/*.jpg")

    for note_image in image_list:

        path = "data_{}/".format(image_size)+note_image.replace("\\", "/")[5:]
        print(path)
        image = cv2.imread(note_image, cv2.IMREAD_GRAYSCALE)
        white_image = np.full((256, 256), 255, dtype=np.uint8)
        white_image[96:160, 96:160] = image
        cv2.imwrite(path, white_image)

    # validation data
    if not os.path.exists("data_{}/datasets-val/Notes/".format(image_size) + note):
        os.makedirs("data_{}/datasets-val/Notes/".format(image_size) + note)

    image_list = glob("data/datasets-val/Notes/"+note+"/*.jpg")
    for note_image in image_list:
        path = "data_{}/".format(image_size)+note_image.replace("\\", "/")[5:]

        image = cv2.imread(note_image, cv2.IMREAD_GRAYSCALE)
        white_image = np.full((256, 256), 255, dtype=np.uint8)
        white_image[96:160, 96:160] = image
        cv2.imwrite(path, white_image)


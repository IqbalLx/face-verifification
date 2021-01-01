import cv2
import os
import numpy as np

import config
import utils


class Model:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

    def train(self):
        images = os.listdir(
            config.DATA_ROOT
        )  # list semua path data wajah pada folder train data

        print("[INFO] Preparing Training Data...")
        image_arrays = []  # Containes semua array data wajah
        image_ids = []  # Container semua ID data wajah
        for i, image_path in enumerate(images):  # Looping semua path data wajah
            splitted_path = image_path.split(".")
            # print(splitted_path)
            image_id = int(splitted_path[1])  # Ambil ID data wajah

            image = cv2.imread(os.path.join(config.DATA_ROOT, image_path))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            image_array = np.array(image, "uint8")  # Ambil array data wajah

            image_arrays.append(image_array)  # Store array data wajah ke list/container
            image_ids.append(image_id)  # Store ID data wajah ke list/container
            utils.pretty_print(len(images), i)

        print("[INFO] Training Start!")
        self.recognizer.train(image_arrays, np.array(image_ids))  # Train recognizer
        self.recognizer.save(config.MODEL_PTH)  # Save model recognizer
        print("[INFO] TRAIN RECOGNIZER SUCCESS!")

    def load(self):
        self.recognizer.read(config.MODEL_PTH)
        return self.recognizer
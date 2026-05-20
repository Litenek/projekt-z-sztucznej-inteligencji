import cv2
import numpy as np
import os


class LineGenerator:
    def __init__(self, width=224, height=224):
        self.width = width
        self.height = height

    def create_sample(self, save_path):
        img = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        p1 = (np.random.randint(0, self.width), np.random.randint(0, self.height))
        p2 = (np.random.randint(0, self.width), np.random.randint(0, self.height))

        cv2.line(img, p1, p2, (255, 255, 255), 2)

        cv2.inwrite(save_path, img)
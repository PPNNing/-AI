import pytesseract
from PIL import Image
import cv2
import numpy as np

def get_number(img):
    img=img.crop((1160,1177,1211,1206))
    img.save("number.png")
    img=cv2.imread("number.png")
    for i in range(0,29):
        for j in range(0,51):
            if img[i,j,0]<100:
                img[i,j]=[255,255,255]
            else:
                img[i][j]=[0,0,0]
    img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thr = cv2.threshold(gry, 127, 255, cv2.THRESH_BINARY_INV)[1]
    res = pytesseract.image_to_string(thr,lang='eng',config=r'-c tessedit_char_whitelist=0123456789 --psm 6')
    return int(res)

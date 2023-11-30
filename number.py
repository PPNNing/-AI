import pytesseract
from PIL import Image
import cv2
import numpy as np

def get_number(img):
    rawImage = Image.open(img)
    rawImage=rawImage.crop((1160,1177,1211,1204))
    rawImage=np.array(rawImage)
    height, width,deep = rawImage.shape
    gray = cv2.cvtColor(rawImage, cv2.COLOR_BGR2GRAY)
    dst = np.zeros((height, width, 1), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            grayPixel = gray[i, j]
            dst[i, j] = 255 - grayPixel
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    string = pytesseract.image_to_string(binary, lang='eng', config='--psm 6 --oem 3 -c ''tessedit_char_whitelist''=0123456789')
    return int(string)

img="1.png"#截图路径
print(get_number(img))
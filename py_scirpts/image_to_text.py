import cv2
import re
import numpy as np
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt 
from . import summarise
print("Ready.")

IMG_DIR= 'media/photos_to_summarize/'
####
#### PREPROCESSING FUNCTIONS
####

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal


def remove_noise(image):
    return cv2.medianBlur(image, 5)

#thresholding


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation


def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)

#erosion


def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)

#opening - erosion followed by dilation


def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection


def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction


def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(
        image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching


def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


# Plotting image 
def plot_img(imread_obj):
    b,g,r= cv2.split(imread_obj)
    rgb_image= cv2.merge([r,g,b])
    plt.imshow(rgb_image)
    plt.title("orignal image")
    plt.show()



def read_image(image_name):
    print(IMG_DIR + str(image_name))
    image = cv2.imread(IMG_DIR + str(image_name))
    # plot_img(image)

    # Preprocess image


    gray= get_grayscale(image)
    thresh= thresholding(gray)
    # plt.imshow(thresh)
    # plt.show()

    opening1 = opening(gray)
    # plt.imshow(opening1)
    # plt.show()

    canny1 = canny(gray)
    # plt.imshow(canny1)
    # plt.show()
    #
    print('output from orignal: ')
    # pytesseract.pytesseract.tesseract_cmd = '‪C:/Program Files/Tesseract-OCR/tesseract.exe'
    print(pytesseract.image_to_string(thresh))
    text= pytesseract.image_to_string(thresh)
    # print(text)
    #
    Cleaned_text = text.replace('\r', ' ').replace('\n', ' ').replace(" |", "")
    print("Cleaned Text",Cleaned_text)
    summarised_text = summarise.driver_fun(Cleaned_text)
    return summarised_text
    # txtfile= open("RES.txt", 'w')
    # n= txtfile.write(text)
    # txtfile.close()

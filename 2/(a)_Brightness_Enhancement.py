import cv2
import matplotlib.pyplot as plt
import numpy as np


def plotImage(image, imgTitle, id):
    plt.subplot(1, 2, id)
    plt.imshow(image, cmap = "gray")
    plt.title(imgTitle)


def brightnessEnhancement(image, low, high, val):
    height, width = image.shape

    for row in range(height):
        for col in range(width):
            if image[row][col] >= low and image[row][col] <= high:
                image[row][col] += val


def Main():

    image = cv2.imread("Task-02\photographer.png", cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (512, 512))

    plotImage(image, "Original Image", 1)

    low = 100
    high = 200
    val = 50

    brightnessEnhancement(image, low, high, val)
    plotImage(image, "Enhanced Image", 2)

    plt.tight_layout()
    plt.show()


Main()

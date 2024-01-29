import cv2
import matplotlib.pyplot as plt
import numpy as np


def plotImage(image, imgTitle, id):
    plt.subplot(2, 2, id)
    plt.imshow(image, cmap = "gray")
    plt.title(imgTitle)


def differnceImage(image1, image2):

    height, width = image1.shape
    diffImage = image1.copy()

    for row in range(height):
        for col in range(width):
            diffImage[row][col] = abs(int(image1[row][col]) - int(image2[row][col]))

    return diffImage


def powerLawTransform(image, gamma):

    height, width = image.shape
    transformedImage = image.copy()

    c = 1

    for row in range(height):
        for col in range(width):
            pixel = image[row, col] / 255
            transformedPixel = c * (pixel**gamma)
            transformedImage[row, col] = int(transformedPixel * 255)

    return transformedImage


def LogarithmicTransform(image):

    height, width = image.shape
    transformedImage = image.copy()

    c = 1

    for row in range(height):
        for col in range(width):
            pixel = image[row, col] / 255
            transformedPixel = c * np.log(1 + pixel)
            transformedImage[row, col] = int(transformedPixel * 255)

    return transformedImage


def inverseLogarithmicTransform(image):

    height, width = image.shape
    transformedImage = image.copy()

    c = 1

    for row in range(height):
        for col in range(width):
            pixel = image[row, col] / 255
            transformedPixel = c * (10 ** (pixel - 1))
            transformedImage[row, col] = int(transformedPixel * 255)

    return transformedImage


def Main():

    image = cv2.imread("./Task-02/Fractured_Spine.tif")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (512, 512))

    plotImage(image, "Original Image", 1)

    gamma = 0.7
    powerLawImage = powerLawTransform(image, gamma)
    plotImage(powerLawImage, f"Power Law Image (gamma = {gamma})", 2)

    inverseLogImage = inverseLogarithmicTransform(image)
    plotImage(inverseLogImage, "Inverse Log Transform Image", 3)

    # logImage = LogarithmicTransform(image)
    # plotImage(logImage,2,2,3,"Log Transform Image")

    diffImage = differnceImage(powerLawImage, inverseLogImage)
    plotImage(diffImage, "Difference Image", 4)

    plt.tight_layout()
    plt.show()


Main()

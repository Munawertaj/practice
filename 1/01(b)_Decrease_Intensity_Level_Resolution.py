import numpy as np
import matplotlib.pyplot as plt
import cv2

def plotImage(image, imgTitle, id):
    plt.subplot(2,4,id)
    plt.imshow(image, cmap = 'gray')
    plt.title(imgTitle)

def decreaseIntensityResolution(image, bits):
    height, width = image.shape
    updateImage = np.zeros((height, width), dtype= np.uint8)

    level = 2 ** bits

    for i in range(1, bits):
        level //= 2
        step = 255 // (level - 1)

        for row in range(height):
            for col in range(width):
                updateImage[row][col] = (round(image[row][col] / step)) * step
        
        title = f"{level} - Gray levels"
        plotImage(updateImage, title, i + 1)

def main():

    image = cv2.imread("./Task-01/cat.jpg", cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (512, 512))

    plotImage(image, "Original Image(256-Gray Levels)", 1)

    decreaseIntensityResolution(image, 8)

    plt.tight_layout()
    plt.show()


main()
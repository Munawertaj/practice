import numpy as np
import matplotlib.pyplot as plt
import cv2


def plotImage(image, imgTitle, id):
    plt.subplot(2, 4, id)
    plt.imshow(image, cmap = "gray")
    plt.title(imgTitle)


def decreaseSpatialResolution(image):

    height, width = image.shape

    for i in range(1, 8):
        height = height // 2
        width = width // 2

        updateImage = np.zeros((height, width), dtype=np.uint8)

        for row in range(height):
            for col in range(width):
                updateImage[row][col] = image[row * 2][col * 2]
        
        image = updateImage
        title = f"{width} * {height}"
        plotImage(image, title, i + 1)


def main():

    image = cv2.imread("./Task-01/cat.jpg", cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (512, 512))

    plotImage(image, "Original Image", 1)

    decreaseSpatialResolution(image)

    plt.tight_layout()
    plt.show()


main()

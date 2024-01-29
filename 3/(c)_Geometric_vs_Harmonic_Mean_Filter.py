import cv2
import matplotlib.pyplot as plt
import numpy as np


def addSaltAndPepperNoise(image):

    noiseIntensity = 0.015  # 0% of the pixels will be affected
    noisyImage = image.copy()
    height, width = image.shape

    noisyPixels = int(noiseIntensity * height * width)
    noisyCoordinates = np.random.randint(0, high=height, size=(noisyPixels, 2))

    for pixel in noisyCoordinates:
        row, col = pixel
        if np.random.rand() < 0.5:
            noisyImage[row, col] = 0
        else:
            noisyImage[row, col] = 255

    return noisyImage


def harmonicMeanFiltering(image, mask_size):
    height, width = image.shape
    filterImage = np.zeros_like(image, dtype=float)

    for row in range(height):
        for col in range(width):
            r_start = max(0, row - mask_size // 2)
            r_end = min(height, row + mask_size // 2 + 1)
            c_start = max(0, col - mask_size // 2)
            c_end = min(width, col + mask_size // 2 + 1)

            total = 0
            sum_inverse = 0

            for i in range(r_start, r_end):
                for j in range(c_start, c_end):
                    sum_inverse += 1 / (image[i, j] + 0.00001)
                    total += 1

            pixel = total / sum_inverse
            filterImage[row, col] = min(255, pixel)

    return np.uint8(filterImage)


def geometricMeanFiltering(image, mask):

    height, width = image.shape
    filterImage = image.copy()

    for row in range(height):
        for col in range(width):
            r = row - (mask // 2)
            c = col - (mask // 2)

            multiples = 1
            count = 0

            for i in range(r, r + mask, 1):
                for j in range(c, c + mask, 1):

                    if (i >= 0 and i < height and j >= 0 and j < width):
                        if (image[i][j]):
                            multiples = multiples * int(image[i][j])
                            count += 1
            
            count = max(1, count)
            filterImage[row][col] = multiples ** (1 / count)

    return np.uint8(filterImage)


def calculatePsnr(image1, image2, max_pixel_value):
    image1, image2 = np.float64(image1), np.float64(image2)
    mse = np.mean((image1 - image2) ** 2)
    if mse == 0:
        return float('inf')

    psnr = 20 * np.log10(max_pixel_value) - 10 * np.log10(mse)
    return psnr


def plotImage(image, x, y, z, imageTitle):

    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.subplot(x, y, z)
    plt.imshow(img)
    plt.title(imageTitle)


def Main():

    image = cv2.imread("./Task-03/characters.tif")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (512, 512))

    plotImage(image, 2, 2, 1, "Original Image")

    noisyImage = addSaltAndPepperNoise(image)
    plotImage(noisyImage, 2, 2, 2, "Noisy Image")

    mask = 3

    harImg = harmonicMeanFiltering(noisyImage, mask)
    plotImage(harImg, 2, 2, 3, "Harmonic Mean Filter Image")

    geoImg = geometricMeanFiltering(noisyImage, mask)
    plotImage(geoImg, 2, 2, 4, "Geometric Mean Filter Image")

    print("Noise image PSNR = " + str(calculatePsnr(image, noisyImage, 255)))
    print("Harmonic filter PSNR = " + str(calculatePsnr(image, harImg, 255)))
    print("Geometric filter PSNR = " + str(calculatePsnr(image, geoImg, 255)))

    plt.tight_layout()
    plt.show()


Main()

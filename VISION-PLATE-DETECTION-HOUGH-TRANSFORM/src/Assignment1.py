import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


def hough_lines_transform(input_edged_image):

    # Creating theta range
    theta = np.arange(0, 180, 1)

    # Creating reusable cos and sin value
    cos = np.cos(theta)
    sin = np.sin(theta)

    # Creating rho range
    rho_range = round(math.sqrt(input_edged_image.shape[0] ** 2 + input_edged_image.shape[1] ** 2))

    # Generating accumulator matrix by using theta and rho
    accumulator = np.zeros((2 * rho_range, len(theta)))

    # To get edges pixel location (like (x,y))
    edge_pixels = np.where(input_edged_image == 255)
    coordinates = list(zip(edge_pixels[0], edge_pixels[1]))

    # FOR DRAWING PLATE EDGES WITH EDGE_PIXELS #
    # print(min(list(edge_pixels[1])), max(list(edge_pixels[1]))
    # print(min(list(edge_pixels[0])),max(list(edge_pixels[0])))
    x_min = min(list(edge_pixels[1]))
    x_max = max(list(edge_pixels[1]))
    y_min = min(list(edge_pixels[0]))
    y_max = max(list(edge_pixels[0]))
    cv2.line(image, (x_min, y_min), (x_min, y_max), (0, 0, 255), 2)
    cv2.line(image, (x_max, y_min), (x_max, y_max), (0, 0, 255), 2)
    cv2.line(image, (x_min, y_min), (x_max, y_min), (0, 0, 255), 2)
    cv2.line(image, (x_min, y_max), (x_max, y_max), (0, 0, 255), 2)

    # FOR DRAWING PLATE EDGES WITH ACCUMULATOR #
    # Calculating rho value for each edge coordinate
    for p in range(len(coordinates)):
        for t in range(len(theta)):
            rho = int(round(coordinates[p][1] * cos[t] + coordinates[p][0] * sin[t]))
            accumulator[rho, t] += 2

    # Threshold some high values
    edge_pixels2 = np.where(accumulator > 150)
    coordinates2 = list(zip(edge_pixels2[0], edge_pixels2[1]))

    # For drawing detected line by using line equation
    for i in range(0, len(coordinates2)):
        a = np.cos(coordinates2[i][1])
        b = np.sin(coordinates2[i][1])
        x0_h = a * coordinates2[i][0]
        y0_h = b * coordinates2[i][0]
        x1 = int(x0_h - 1000 * (-b))
        y1 = int(y0_h - 1000 * a)
        x2 = int(x0_h + 1000 * (-b))
        y2 = int(y0_h + 1000 * a)
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 255), 2)


if __name__ == "__main__":

    # Reading an image
    image = cv2.imread('images/Cars3.png')
    # Converting to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Creating edged image with Canny func.
    edged_image = cv2.Canny(gray_image, 605, 1250)

    hough_lines_transform(edged_image)  # Calling hough lines function

    # Printing edged image and image with detected lines
    cv2.imshow('Edges', edged_image)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

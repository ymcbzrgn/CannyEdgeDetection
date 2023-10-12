import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from matplotlib import pyplot as plt

def select_image():
    global path, image
    path = filedialog.askopenfilename()
    image = cv2.imread(path)

def update_blur_ratio(value):
    global blur_ratio
    blur_ratio = int(value)

def perform_canny_edge_detection():
    global path, image, blur_ratio
    if path is None or image is None:
        tk.messagebox.showerror("Error", "Please select an image first")
        return

    cv2.imshow("Original Image", image)
    cv2.waitKey(0)

    # Step 1: Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)

    # Step 2: Perform Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray_image, (blur_ratio, blur_ratio), 0)
    cv2.imshow("Blurred Image", blurred)
    cv2.waitKey(0)

    # Step 3: Compute gradient magnitude and direction using Sobel operator
    sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    gradient_direction = np.arctan2(sobel_y, sobel_x)

    gradient_magnitude = np.uint8(np.absolute(gradient_magnitude))
    cv2.imshow("Gradient Magnitude", gradient_magnitude)
    cv2.waitKey(0)

    # Step 4: Non-maximum suppression
    suppressed_image = np.zeros_like(gradient_magnitude)
    for i in range(1, gradient_magnitude.shape[0]-1):
        for j in range(1, gradient_magnitude.shape[1]-1):
            if gradient_direction[i, j] < 0:
                gradient_direction[i, j] += np.pi

            direction = gradient_direction[i, j] * 180 / np.pi

            # Check if the gradient magnitude at (i, j) is a local maximum
            # in the direction of the gradient
            if (direction >= 157.5 and direction <= 202.5) or (direction >= 337.5 and direction < 22.5):
                if gradient_magnitude[i, j] >= gradient_magnitude[i, j-1] and gradient_magnitude[i, j] >= gradient_magnitude[i, j+1]:
                    suppressed_image[i, j] = gradient_magnitude[i, j]
            elif (direction >= 67.5 and direction
                  <= 112.5) or (direction >= 247.5 and direction <= 292.5):
                if gradient_magnitude[i, j] >= gradient_magnitude[i-1, j+1] and gradient_magnitude[i, j] >= gradient_magnitude[i+1, j-1]:
                    suppressed_image[i, j] = gradient_magnitude[i, j]
            elif (direction >= 22.5 and direction <= 67.5) or (direction >= 202.5 and direction <= 247.5):
                if gradient_magnitude[i, j] >= gradient_magnitude[i-1, j] and gradient_magnitude[i, j] >= gradient_magnitude[i+1, j]:
                    suppressed_image[i, j] = gradient_magnitude[i, j]
            elif (direction >= 112.5 and direction <= 157.5) or (direction >= 292.5 and direction <= 337.5):
                if gradient_magnitude[i, j] >= gradient_magnitude[i-1, j-1] and gradient_magnitude[i, j] >= gradient_magnitude[i+1, j+1]:
                    suppressed_image[i, j] = gradient_magnitude[i, j]

    cv2.imshow("Non-maximum Suppression", suppressed_image)
    cv2.waitKey(0)

    # Step 5: Double thresholding
    lower_threshold = 150
    upper_threshold = 300
    edges = np.zeros_like(gradient_magnitude)
    weak_edges = np.zeros_like(gradient_magnitude)
    strong_edges = np.zeros_like(gradient_magnitude)

    for i in range(gradient_magnitude.shape[0]):
        for j in range(gradient_magnitude.shape[1]):
            if suppressed_image[i, j] > upper_threshold:
                edges[i, j] = 255
                strong_edges[i, j] = 255
            elif suppressed_image[i, j] < lower_threshold:
                edges[i, j] = 0
            else:
                edges[i, j] = 128
                weak_edges[i, j] = 128

    cv2.imshow("Double Thresholding", edges)
    cv2.waitKey(0)

    # Step 6: Edge tracking by hysteresis
    for i in range(1, gradient_magnitude.shape[0]-1):
        for j in range(1, gradient_magnitude.shape[1]-1):
            if weak_edges[i, j] == 128:
                if strong_edges[i-1, j-1] == 255 or strong_edges[i-1, j] == 255 or strong_edges[i-1, j+1] == 255 or strong_edges[i, j-1] == 255 or strong_edges[i, j+1] == 255 or strong_edges[i+1, j-1] == 255 or strong_edges[i+1, j] == 255 or strong_edges[i+1, j+1] == 255:
                    edges[i, j] = 255

    cv2.imshow("Edge Tracking by Hysteresis", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

path = None
image = None
blur_ratio = 1

root = tk.Tk()
root.title("Canny Edge Detector")

# Add the label and the scale widget for blur ratio
blur_label = tk.Label(root, text="Blur Ratio")
blur_label.pack()
blur_scale = tk.Scale(root, from_=1, to=71, resolution=2, orient=tk.HORIZONTAL, command=update_blur_ratio)
blur_scale.pack()

browse_button = tk.Button(root, text="Browse Image", command=select_image)
browse_button.pack()

submit_button = tk.Button(root, text="Submit", command=perform_canny_edge_detection)
submit_button.pack()

root.mainloop()

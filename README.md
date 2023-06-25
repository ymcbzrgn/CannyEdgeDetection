# CannyEdgeDetection

This repository contains an implementation of the Canny Edge Detection algorithm, a popular technique for edge detection in images. The algorithm was developed by John F. Canny in 1986 and is widely used in computer vision. The implementation is provided as a Tkinter application, allowing users to easily select images and apply the Canny Edge Detection algorithm.

## Table of Contents

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Algorithm Steps](#algorithm-steps)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use this repository, you will need to have Python installed on your machine. You can then clone this repository using the following command:

```bash
git clone https://github.com/ymcbzrgn/CannyEdgeDetection.git
```

After cloning the repository, navigate to the project directory and install the required dependencies:

```bash
cd CannyEdgeDetection
pip install -r requirements.txt
```

## Dependencies

This project requires the following libraries:

- numpy
- opencv-python
- matplotlib

The `tkinter` library, which is part of the standard Python library, is also required.

## Usage

To use the Canny Edge Detection application, you can run the main script as follows:

```bash
python main.py
```

This will open the Tkinter application. From there, you can use the "Choose Image" button to select the image you want to process. Adjust the blur scale as desired, then click the "Submit" button to apply the Canny Edge Detection algorithm.

## Algorithm Steps

In this implementation of the Canny Edge Detection algorithm, I have followed several key steps to achieve accurate edge detection:

1. **Gaussian Blur:** The initial step involves reducing noise in the image by convolving it with a Gaussian function. This blurring effect, controlled by the 'blur_ratio' parameter in the code, is essential for suppressing high-frequency noise and preparing the image for edge detection. The Gaussian function can be expressed as:

   \[ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \]

   Here, \( \mu \) represents the mean (the center of the Gaussian) and \( \sigma \) denotes the standard deviation (the width of the Gaussian).

2. **Gradient Calculation:** Following the Gaussian blur, the Sobel operator is employed to calculate the gradient magnitude and direction at each pixel in the image. This step plays a crucial role in edge detection as it allows the identification of regions with significant intensity changes. The gradient magnitude (\( G \)) is computed using the Euclidean norm of the gradient components:

   \[ G = \sqrt{G_x^2 + G_y^2} \]

   Additionally, the gradient direction (\( \theta \)) is determined as the arctangent of the ratio between the y and x gradient components:

   \[ \theta = \arctan\left(\frac{G_y}{G_x}\right) \]

   Here, \( G_x \) and \( G_y \) represent the gradients in the x and y directions, respectively.

3. **Non-maximum Suppression:** After obtaining the gradient magnitude and direction, a technique called non-maximum suppression is applied to thin the edges. This process involves scanning the image and suppressing any pixel that is not considered an edge. Only local maxima along the gradient direction are preserved, enhancing the accuracy of edge detection.

4. **Double Thresholding:** To determine the 'true' edges, a double thresholding technique is employed. Two threshold values, an upper threshold and a lower threshold, are set. Pixels with edge intensities above the upper threshold are identified as strong edges, while those below the lower threshold are discarded. Pixels with edge intensities between the two thresholds are labeled as weak edges.

5. **Edge Tracking by Hysteresis:** The final step involves edge tracking by hysteresis. This technique aims to connect the weak edges that remain after thresholding to the strong edges, effectively completing the edges and suppressing any remaining noise. If a weak edge pixel is connected to a strong edge pixel, it is considered part of an edge; otherwise, it is removed.

These steps collectively form the core of the Canny Edge Detection algorithm and serve as the foundation for the edge detection capabilities of this application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the Unlicense. See the [LICENSE](LICENSE) file for details.

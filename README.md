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

In this implementation of the Canny Edge Detection algorithm, I've followed several key steps:

1. **Gaussian Blur:** The first step in the process is to reduce noise in the image, which I've achieved by convolving the image with a Gaussian function. This 'blurring' effect is controlled by the 'blur_ratio' parameter in the code, which determines the size of the Gaussian kernel. The Gaussian function is given by:

    $$ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} $$

    where \( \mu \) is the mean (center of the Gaussian), and \( \sigma \) is the standard deviation (width of the Gaussian).

2. **Gradient Calculation:** Next, I've used the Sobel operator to compute the gradient magnitude and direction at each pixel in the image. This is a crucial step in edge detection, as it allows us to identify areas of the image where the intensity changes significantly. The gradient magnitude is calculated as the Euclidean norm of the gradient components:

    $$ G = \sqrt{G_x^2 + G_y^2} $$

    and the direction is calculated as the arctangent of the ratio of the gradient components:

    $$ \theta = \arctan\left(\frac{G_y}{G_x}\right) $$

    where \( G_x \) and \( G_y \) are the gradients in the x and y directions, respectively.

3. **Non-maximum Suppression:** After calculating the gradient, I've applied a technique called non-maximum suppression to thin the edges. This involves scanning the image and suppressing any pixel value that is not considered to be an edge.

4. **Double Thresholding:** This step involves determining which edges are 'true' edges. I've set two threshold values, and any pixel with an edge intensity higher than the upper threshold is considered a strong edge, while any pixel with an edge intensity lower than the lower threshold is discarded. Pixels with edge intensities between the two thresholds are considered weak edges.

5. **Edge Tracking by Hysteresis:** Finally, I've used a technique called edge tracking by hysteresis to track along the remaining pixels that have not been suppressed. If a weak edge pixel is connected to a strong edge pixel, it is considered to be part of an edge. Otherwise, the weak edge is removed.

These steps form the core of the Canny Edge Detection algorithm and are the basis for the edge detection capabilities of this application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the Unlicense. See the [LICENSE](LICENSE) file for details.

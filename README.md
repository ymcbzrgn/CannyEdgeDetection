# CannyEdgeDetection

This repository contains an implementation of the Canny Edge Detection algorithm, a popular technique for edge detection in images. The algorithm was developed by John F. Canny in 1986 and is widely used in computer vision. The implementation is provided as a Tkinter application, allowing users to easily select images and apply the Canny Edge Detection algorithm.

## Table of Contents

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
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

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the Unlicense. See the [LICENSE](LICENSE) file for details.

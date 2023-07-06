# DataAugmentation

# Data Augmentation Application

This repository contains a C++ application called `data_aug.cpp` and a Python script `data_aug_multi.py` for performing data augmentation on images. The purpose of this application is to read images, resize them to a width of 512 pixels, and apply gamma correction and brightness adjustments. Additionally, it generates training images with widths of 512 and 1024 pixels specifically for training a Pix2Pix model.

## C++ Application: `data_aug.cpp`

The `data_aug.cpp` file contains the source code for the C++ application responsible for performing the data augmentation tasks. The main functionalities of this application are as follows:

1. **Read Images**: The application reads input images from a specified directory.

2. **Resize Images**: The input images are resized to a width of 512 pixels while maintaining their aspect ratio.

3. **Gamma Correction**: Gamma correction is applied to the resized images to enhance their contrast.

4. **Brightness Adjustment**: Brightness adjustment is performed on the images to control their overall lightness or darkness.

5. **Train Image Generation**: In addition to the above transformations, the application also generates training images with widths of 512 and 1024 pixels. These images are specifically tailored for training a Pix2Pix model.

## Python Script: `data_aug_multi.py`

The `data_aug_multi.py` script is written in Python and utilizes multi-threading to efficiently generate augmented images. This script can be used in conjunction with the C++ application or as a standalone tool. The key features of this script are as follows:

1. **Multi-Threading**: The script employs multi-threading techniques to parallelize the generation of augmented images. This results in faster processing times, especially when dealing with a large number of images.

2. **Image Generation**: The script generates augmented images by applying the same transformations as the C++ application, including resizing to 512 pixels, gamma correction, and brightness adjustments.

## Prerequisites

Before using the C++ application and Python script, make sure you have the following prerequisites installed:

- C++ Compiler and Standard Library
- OpenCV library for C++
- Python 3.x
- OpenCV library for Python

## Usage

To use the C++ application, follow these steps:

1. Compile the `data_aug.cpp` file using your preferred C++ compiler and link it with the OpenCV library.

2. Run the compiled executable with the appropriate command-line arguments, specifying the input image directory and the output directory for augmented images.

To use the Python script, follow these steps:

1. Install the required c++ dependencies:
   ```
   OpenCV for c++
   ```

2. Run the `data_aug_multi.py` script with the appropriate command-line arguments, specifying the input image directory and the output directory for augmented images.

Please note that both the C++ application and the Python script expect a directory containing input images and will generate the augmented images in the specified output directory.

3. ```
   python data_aug_multi.py --src "Where your images are" --dst "Where yo want to save your images" 
   ```

## Acknowledgements

The C++ application and Python script were developed by Mila. If you have any questions or encounter any issues, please feel free to reach out to me at omrani [at] mila dot gmail dot come.

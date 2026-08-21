# Average Filtering Using 3×3, 5×5 and 7×7 Kernels

## 1. Introduction
Average filtering is a basic image processing technique used to reduce noise and smooth an image. It replaces each pixel with the average value of the pixels in its neighborhood.
In this project, average filtering is applied to a grayscale image using three different kernel sizes:
- 3×3 kernel
- 5×5 kernel
- 7×7 kernel
The results of the three filters are compared with the original grayscale image.

## 2. Objective
The main objectives of this project are:
1. To read an image in grayscale.
2. To create average filter kernels of different sizes.
3. To apply 3×3, 5×5 and 7×7 filters using 2D convolution.
4. To observe the effect of increasing the kernel size on image smoothing.
5. To compare the original image with the filtered images.

## 3. Technologies Used
- Python
- OpenCV
- NumPy
- Matplotlib

## 4. Average Filter
An average filter is a low-pass filter used for image smoothing.

## 5.Input Image
[![Input Image](input_img.jpg)](input_img.jpg)

## 6.Method
The following steps are performed:
Input Image
     ↓
Convert to Grayscale
     ↓
Create 3×3 Kernel
     ↓
Create 5×5 Kernel
     ↓
Create 7×7 Kernel
     ↓
Apply 2D Convolution
     ↓
Compare the Results
OpenCV's filter2D() function is used to perform the convolution operation.



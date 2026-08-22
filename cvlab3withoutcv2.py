import numpy as np
import matplotlib.pyplot as plt
def average_filter(image, kernel_size):
    pad = kernel_size // 2
    padded_image = np.pad(image, pad, mode='constant')
    output = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            neighborhood = padded_image[
                i:i + kernel_size,
                j:j + kernel_size
            ]
            average = np.mean(neighborhood)
            output[i, j] = average
    return output
img = cv2.imread('input_img.jpg', 0)
if img is None:
    print("Error: Image not found")
else:
    blur_3x3 = average_filter(img, 3)
    blur_5x5 = average_filter(img, 5)
    blur_7x7 = average_filter(img, 7)
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original GrayScale Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(blur_3x3, cmap='gray')
    plt.title('Average Filter (3x3)')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(blur_5x5, cmap='gray')
    plt.title('Average Filter (5x5)')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(blur_7x7, cmap='gray')
    plt.title('Average Filter (7x7)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
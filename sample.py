from src.image_processing import load_image, convert_to_grayscale
import cv2

# Load a road photograph.
image = load_image("data/sample_images/road.jpg")

# Convert it to grayscale.
grayscale = convert_to_grayscale(image)

# Apply three different kernel sizes.
blur_3 = cv2.GaussianBlur(grayscale, (3, 3), 0)
blur_5 = cv2.GaussianBlur(grayscale, (5, 5), 0)
blur_9 = cv2.GaussianBlur(grayscale, (9, 9), 0)
blur_11 = cv2.GaussianBlur(grayscale, (11, 11), 0)
# Display the results.
cv2.imshow("Original grayscale", grayscale)
cv2.imshow("Kernel 3", blur_3)
cv2.imshow("Kernel 5", blur_5)
cv2.imshow("Kernel 9", blur_9)
cv2.imshow("kernel 11", blur_11)

cv2.waitKey(0)
cv2.destroyAllWindows()
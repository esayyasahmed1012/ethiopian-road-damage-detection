from src.image_processing import load_image, convert_to_grayscale
<<<<<<< HEAD
=======
from src.visualization import display_image_results
>>>>>>> 4454735dbec689112b7330c16ce8def84b16f238
import cv2

# Load a road photograph.
image = load_image("data/sample_images/road.jpg")

# Convert it to grayscale.
grayscale = convert_to_grayscale(image)

# Apply three different kernel sizes.
<<<<<<< HEAD
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
=======
# blur_3 = cv2.GaussianBlur(grayscale, (3, 3), 0)
# blur_5 = cv2.GaussianBlur(grayscale, (5, 5), 0)
# blur_9 = cv2.GaussianBlur(grayscale, (9, 9), 0)
# blur_11 = cv2.GaussianBlur(grayscale, (11, 11), 0)
# # Display the results.
# cv2.imshow("Original grayscale", grayscale)
# cv2.imshow("Kernel 3", blur_3)
# cv2.imshow("Kernel 5", blur_5)
# cv2.imshow("Kernel 9", blur_9)
# cv2.imshow("kernel 11", blur_11)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2

# image = cv2.imread("road.jpg")

grayscale = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

blurred = cv2.GaussianBlur(
    grayscale,
    (5, 5),
    0
)

edges = cv2.Canny(
    blurred,
    50,
    150
)

results = {
    "original": image,
    "grayscale": grayscale,
    "blurred": blurred,
    "edges": edges
}

display_image_results(results)
>>>>>>> 4454735dbec689112b7330c16ce8def84b16f238

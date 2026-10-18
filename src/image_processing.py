from pathlib import Path
import cv2
import matplotlib.pyplot as plt


def processRoadImage(image_path: str) -> None:
    """load a road image and demonstrate basic image processing."""
    image_file = Path(image_path)
    # check whether the image exists.
    if not image_file.is_file():
        raise FileNotFoundError(f"Image not found: {image_file}")
    # load the image using OpenCV.
    image = cv2.imread(str(image_file))
    if image is None:
        raise ValueError(f"Could not read image: {image_file}")
    # convert BGR to RGB for correct matplotlib display.
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # convert the image to grayscale.
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # rduce noise with gaussian blur.
    blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)
    # detect edges using canny.
    edges = cv2.Canny(blurred, 50, 150)
    # create a directory for the results.
    output_dir = Path("results")
    output_dir.mkdir(parents=True, exist_ok=True)
    # save the edge-detection image.
    output_path = output_dir / f"{image_file.stem}_edges.png"
    if not cv2.imwrite(str(output_path), edges):
        raise OSError(f"Could not save image: {output_path}")
    # display the original and processed images.
    figure, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(image_rgb)
    axes[0].set_title("Original Road Image")

    axes[1].imshow(grayscale, cmap="gray")
    axes[1].set_title("Grayscale")

    axes[2].imshow(edges, cmap="gray")
    axes[2].set_title("Canny Edge Detection")

    for axis in axes:
        axis.axis("off")

    figure.tight_layout()
    plt.show()

    print(f"original image dimensions: {image.shape[1]} x {image.shape[0]}")
    print(f"procesed image saved to: {output_path}")


if __name__ == "__main__":
    processRoadImage("data/sample_images/road.jpg")
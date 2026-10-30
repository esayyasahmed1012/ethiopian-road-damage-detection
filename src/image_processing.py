
from pathlib import Path

import cv2
import numpy as np


def load_image(image_path: str | Path) -> np.ndarray:
    """
    load an image from disk.

    Args:
        image_path: Path to the input image.

    Returns:
        image as a NumPy array in OpenCV's BGR colour format.
    """
    image_path = Path(image_path)

    if not image_path.is_file():
        raise FileNotFoundError(
            f"image file does not exist: {image_path}"
        )

    image = cv2.imread(str(image_path))

    if image is None:
        raise ValueError(
            f"OpenCV could not read an image: {image_path}"
        )

    return image
def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """convert a colour image to grayscale."""

    if image is None or image.size == 0:
        raise ValueError("Input image cannot be empty.")

    if image.ndim == 2:
        return image.copy()

    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError(
            "expected a grayscale image or a three-channel BGR image."
        )

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def reduce_noise(
    grayscale_image: np.ndarray,
    kernel_size: int = 5,
) -> np.ndarray:
    """Reduce image noise using Gaussian blur."""

    if grayscale_image is None or grayscale_image.size == 0:
        raise ValueError("Input image cannot be empty.")

    if grayscale_image.ndim != 2:
        raise ValueError("Expected a grayscale image.")

    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError(
            "kernel_size must be a positive odd integer."
        )

    return cv2.GaussianBlur(
        grayscale_image,
        (kernel_size, kernel_size),
        0,
    )


def detect_edges(
    grayscale_image: np.ndarray,
    lower_threshold: int = 50,
    upper_threshold: int = 150,
) -> np.ndarray:
    """Detect edges using the Canny edge detector."""

    if grayscale_image is None or grayscale_image.size == 0:
        raise ValueError("Input image cannot be empty.")

    if grayscale_image.ndim != 2:
        raise ValueError("Expected a grayscale image.")

    if not (
        0 <= lower_threshold < upper_threshold <= 255
    ):
        raise ValueError(
            "Thresholds must satisfy "
            "0 <= lower_threshold < upper_threshold <= 255."
        )

    return cv2.Canny(
        grayscale_image,
        lower_threshold,
        upper_threshold,
    )


def process_image(image_path: str | Path) -> dict:
    """
    Execute the initial image-processing pipeline.
    """

    original = load_image(image_path)
    grayscale = convert_to_grayscale(original)
    blurred = reduce_noise(grayscale)
    edges = detect_edges(blurred)

    return {
        "original": original,
        "grayscale": grayscale,
        "blurred": blurred,
        "edges": edges,
    }

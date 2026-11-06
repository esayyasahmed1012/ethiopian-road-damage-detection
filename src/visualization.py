import matplotlib.pyplot as plt
import numpy as np
import cv2
def display_image_results(results: dict) -> None:
    """
    display the default image and its processed ones.
    """

    fig, axes = plt.subplots(2, 2, figsize=(10, 6))

    images = [
        ("Original Image", results["original"], "BGR"),
        ("Grayscale Image", results["grayscale"], "GRAY"),
        ("Blurred Image", results["blurred"], "GRAY"),
        ("Edge Image", results["edges"], "GRAY"), 
    ] 
    for ax, (title, image, color_format) in zip(
        axes.flat, images
    ):
        if color_format == "BGR":
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        ax.imshow(
            image,
            cmap="gray" if color_format == "GRAY" else None,
        )
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()
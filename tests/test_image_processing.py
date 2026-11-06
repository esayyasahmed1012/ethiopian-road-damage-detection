
import cv2
import numpy as np
import pytest

from src.image_processing import (
    convert_to_grayscale,
    detect_edges,
    load_image,
    process_image,
    reduce_noise,
)
def test_convert_to_grayscale():
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    grayscale = convert_to_grayscale(image)
    assert grayscale.shape == (100, 100)
    assert grayscale.dtype == np.uint8
def test_grayscale_image_is_copied():
    image = np.zeros((100, 100), dtype=np.uint8)
    grayscale = convert_to_grayscale(image)
    assert np.array_equal(grayscale, image)
    assert grayscale is not image
def test_reduce_noise():
    image = np.zeros((100, 100), dtype=np.uint8)
    blurred = reduce_noise(image)
    assert blurred.shape == image.shape
    assert blurred.dtype == np.uint8
def test_reduce_noise_rejects_even_kernel():
    image = np.zeros((100, 100), dtype=np.uint8)
    with pytest.raises(ValueError):
        reduce_noise(image, kernel_size=4)
def test_detect_edges():
    image = np.zeros((100, 100), dtype=np.uint8)
    cv2.rectangle(
        image,
        (20, 20),
        (80, 80),
        255,
        thickness=-1,
    )
    edges = detect_edges(image)
    assert edges.shape == image.shape
    assert edges.dtype == np.uint8
    assert np.count_nonzero(edges) > 0
def test_detect_edges_rejects_invalid_thresholds():
    image = np.zeros((100, 100), dtype=np.uint8)
    with pytest.raises(ValueError):
        detect_edges(
            image,
            lower_threshold=150,
            upper_threshold=50,
        )
def test_load_image(tmp_path):
    image = np.zeros((40, 60, 3), dtype=np.uint8)
    image_path = tmp_path / "test_road.png"
    assert cv2.imwrite(str(image_path), image)
    loaded_image = load_image(image_path)
    assert loaded_image.shape == (40, 60, 3)
def test_load_missing_image():
    with pytest.raises(FileNotFoundError):
        load_image("missing_road_image.png")
def test_process_image(tmp_path):
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(
        image,
        (20, 20),
        (80, 80),
        (255, 255, 255),
        thickness=-1,
    )
    image_path = tmp_path / "road.png"
    assert cv2.imwrite(str(image_path), image)
    result = process_image(image_path)
    assert set(result.keys()) == {
        "original",
        "grayscale",
        "blurred",
        "edges",
    }
    assert result["original"].shape == (100, 100, 3)
    assert result["grayscale"].shape == (100, 100)
    assert result["blurred"].shape == (100, 100)
    assert result["edges"].shape == (100, 100)

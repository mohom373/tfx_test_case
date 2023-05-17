## Script to brighten images that are under a brightness threshhold


import os
import glob
import random
from PIL import Image, ImageEnhance

def increase_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def process_images(input_path, output_path, darken_threshold=128, brighten_factor=1.5):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for root, dirs, files in os.walk(input_path):
        rel_path = os.path.relpath(root, input_path)
        output_subdir = os.path.join(output_path, rel_path)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        images = glob.glob(os.path.join(root, "*.jpg")) + glob.glob(os.path.join(root, "*.png"))

        for image_path in images:
            image = Image.open(image_path)
            image_filename = os.path.basename(image_path)
            output_image_path = os.path.join(output_subdir, image_filename)

            if image.histogram()[128] < darken_threshold:
                bright_image = increase_brightness(image, brighten_factor)
                bright_image.save(output_image_path)
            else:
                image.save(output_image_path)

# Provide your input and output paths here
input_path = "flowers_original_dark_dataset/train"
output_path = "brightened_images"
# Set your darkness threshold
darkness_threshold = 64

process_images(input_path, output_path, darkness_threshold, 2.0)

print("Processing completed. Darkened images have been saved to the 'brightened_images' directory.")

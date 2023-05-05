## Script to darken 25% of images

import os
import random
from PIL import Image, ImageEnhance
import glob

def process_images(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for root, dirs, files in os.walk(input_path):
        rel_path = os.path.relpath(root, input_path)
        output_subdir = os.path.join(output_path, rel_path)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        images = glob.glob(os.path.join(root, "*.jpg")) + glob.glob(os.path.join(root, "*.png"))

        num_to_darken = len(images) // 4
        random.seed(10)
        images_to_darken = random.sample(images, num_to_darken)

        for image_path in images:
            image = Image.open(image_path)
            image_filename = os.path.basename(image_path)
            output_image_path = os.path.join(output_subdir, image_filename)

            if image_path in images_to_darken:
                enhancer = ImageEnhance.Brightness(image)
                darker_image = enhancer.enhance(0.3)
                darker_image.save(output_image_path)
            else:
                image.save(output_image_path)



input_directory = "flowers/train"
output_directory = "darkened_images"
process_images(input_directory, output_directory)
print("Processing completed. Darkened images have been saved to the 'darkened_images' directory.")
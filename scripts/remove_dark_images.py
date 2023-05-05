
#Takes a list of image paths and removes them
import os

from cleanvision.imagelab import Imagelab

def count_files(directory_path):
    file_count = 0

    for root, dirs, files in os.walk(directory_path):
        file_count += len(files)

    print(f"The total number of files in '{directory_path}' and its subdirectories is: {file_count}")



def remove_images(image_paths):
    for image_path in image_paths:
        if os.path.isfile(image_path):
            try:
                os.remove(image_path)
            except OSError as e:
                print(f"Error removing {image_path}: {e}")
        else:
            print(f"{image_path} is not a valid file path.")




# Specify path to folder containing the image files in your dataset
imagelab = Imagelab(data_path="darkened_images/")

issue_types = {"dark": {}}

imagelab.find_issues(issue_types=issue_types)


dark_images = imagelab.issues[imagelab.issues["is_dark_issue"] == True].sort_values(by=['dark_score'])

# Get a list of paths for the darkened images as a list
dark_image_files = dark_images.index.tolist()

# Count the files of darkned images before and after
# The second count should be (total amount of images - deleted darkned images)
count_files('darkened_images')

remove_images(dark_image_files)

count_files('darkened_images')

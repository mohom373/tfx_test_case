import os
import shutil

"""
This method takes the images and copies the files into a new dir for later use of a train/test split
"""
def create_train_dataset_from_images(directory_path, new_data_set_dir_path,new_name=None):
    if os.path.isdir(directory_path):
        new_dataset_dir = os.path.join(new_data_set_dir_path)

        if not os.path.exists(new_dataset_dir):
            os.makedirs(new_dataset_dir)

        directory_name = new_name if new_name else os.path.basename(directory_path)
        target_directory = os.path.join(new_dataset_dir, directory_name)

        if not os.path.exists(target_directory):
            shutil.copytree(directory_path, target_directory)
            print(f"Moved {'and renamed' if new_name else ''} '{directory_path}' to '{target_directory}'")
        else:
            print(f"Error: '{target_directory}' already exists.")
    else:
        print(f"{directory_path} is not a valid directory path.")


#create_train_dataset_from_original_images('darkened_images', 'train')

# Take the test dataset from the flowers or flowers_dark_dataset dir as both have the same test data
# might change in the future though!
#create_train_dataset_from_original_images('flowers/test', 'test')

# import package and dataset
import os
from PIL import Image
import numpy as np


# for loop to open images, loop through each folder name
def open_folder(path: str):
    # set image size to 128 pixels
    image_size = 128

    # initialize a list for images and labels
    image_list = []
    image_labels = []

    for folder_name, label in [('cell_images/Parasitized/', 1), ('cell_images/Uninfected/', 0)]:
        # folder path definition
        folder_path = os.path.join(path, folder_name)

        # path for each image, remove thumbs.db element
        image_path = [f for f in os.listdir(folder_path) if f.lower() != 'thumbs.db']
        # print(image_path)

        # iterate through images and indexes
        for the_image in image_path:
            # print(the_image)

            # iterating image variable
            image = Image.open(os.path.join(folder_path, the_image))
            # print(image)

            # resize images and add them to list dataset
            image = image.resize((image_size, image_size))
            image_list.append(np.array(image))
            image_labels.append(label)


    return np.array(image_list), np.array(image_labels)
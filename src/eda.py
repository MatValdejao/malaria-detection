# imports
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def max_min(arr: np.ndarray):
    return arr.max(), arr.min()


# will create a helper function for this to facilitate jupyter workflow ease
def train_test(image_list: np.ndarray, image_labels: np.ndarray, test_size: float):
    # check whether test_size is less than 1 and greater than zero
    if (test_size >= 1 or test_size <= 0):
        raise ValueError('Test size must be a dataset percentage (from 0-1).') 

    # split dataset
    X_train, X_test, Y_train, Y_test = train_test_split(image_list, image_labels, test_size=test_size, random_state=42)

    return X_train, X_test, Y_train, Y_test

def arrange_plots(images: np.ndarray, labels: np.ndarray):
    fig = plt.figure(figsize=(16, 8))

    # 2 by 5 grid format
    rows = 2
    cols = 5 

    for i in range(rows):
        for j in range(cols):
            # individual plot to grid
            ax = fig.add_subplot(rows, cols, i * cols + j + 1)
            ax.imshow(images[i * cols + j])
            
            # set title according to class
            if labels[i * cols + j]:
                ax.set_title('Parasitized Cell')
            else: 
                ax.set_title('Uninfeceted Cell')

    fig.show()
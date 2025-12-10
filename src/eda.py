import numpy as np

def max_min(arr):
    arr = np.array(arr)
    return arr.max(), arr.min()


# will create a helper function for this to facilitate jupyter workflow ease
def train_test(image_list, image_labels, test_size: float):
    # import function
    from sklearn.model_selection import train_test_split

    # check whether test_size is less than 1 and greater than zero
    if (test_size >= 1 or test_size <= 0):
        raise ValueError('Test size must be a dataset percentage (from 0-1).') 

    # split dataset
    X_train, X_test, Y_train, Y_test = train_test_split(image_list, image_labels, test_size=test_size, random_state=42)

    return X_train, X_test, Y_train, Y_test
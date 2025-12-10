import numpy as np
from sklearn.model_selection import train_test_split

def max_min(arr):
    arr = np.array(arr)
    return arr.max(), arr.min()


def train_test_split(arr):

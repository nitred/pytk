"""This module contains numpy operations."""
import numpy as np


def shuffle_two_arrays_in_unison(arr1=None, arr2=None):
    """
    Shuffle two 1D-numpy arrays index-wise.

    Corresponding indices are kept in both the arrays
    Assumes both the arrays are of same length.

    Args:
        arr1: numpy arrays
        arr2: numpy arrays

    Returns:
        arr1, arr2
        for eg. arr1 = [1,2,3] arr2 = [11,12,13]
    """
    if len(arr1) != len(arr2):
        raise Exception('Legth of two arrays is not equal')

    indices = np.random.permutation(len(arr1))
    return arr1[indices], arr2[indices]


def shuffle_and_split_numpy_array(arr1=None, percentage_split=None):
    """
    Shuffle a 1D-numpy array and returns two numpy arrays with a given split.

    Args:
        arr1: numpy array, numpy array to shuffle and split
        percentage_split: float, between 0-1 to split the array into

    Returns:
        arr1, arr2: Two numpy arrays with 'percentage_split' and 1-percentage_split elements
    """
    shuffled_np = np.random.shuffle(arr1)
    if percentage_split is None:
        return shuffled_np

    split_index = np.int(percentage_split * len(arr1))
    return arr1[0:split_index], arr1[split_index:]


def shuffle_numpy_array(arr1=None):
    """
    Shuffle a simple numpy array.

    Args:
        arr1: numpy array, array to be shuffled

    Returns:
        arr1: numpy array, shuffled array
    """
    return np.random.shuffle(arr1)

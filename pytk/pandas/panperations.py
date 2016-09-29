"""This module contains functions for pandas operations."""
import pandas as pd
import numpy as np


def read_csv_gz(filename=None, **kwargs):
    """
    Return a new dataframe by reading in a csv.gz.

    This function assumes that the file ends with .gz
    Accepts all the valid arguments supported by pandas.read_csv() function

    Args:
        filename: string
            The input filename to read in pandas, ending in .gz

    Returns:
        df: pandas dataframe
    """
    df = pd.read_csv(filename, compression='gzip', **kwargs)
    return df.copy()


def remove_nan_row_wise(df=None, **kwargs):
    """
    Return a dataframe with all nans removed, row wise.

    Accepts all the valid arguments supported by dataframe.dropna() function

    Args:
        df: pandas dataframe with rows containing nans

    Returns:
        df: pandas dataframe without nan-rows
    """
    return df.dropna(**kwargs)


def run_sliding_window(df, winlen=20):
    """
    Generate a numpy array with sliding window of winlen.

    Args:
        df: pandas df, input dataframe to create sliding windows from
        winlen: int, Length of the sliding window

    Returns:
        winX: numpy array, n x winlen
    """
    inpX = []
    for i in xrange(len(df)-winlen):
        inpX.append(df.iloc[i:i+winlen].as_matrix())
    winX = np.array(inpX)
    return winX

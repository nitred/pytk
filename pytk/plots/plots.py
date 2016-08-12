"""A module that contains basic plotting functions."""

from matplotlib import pyplot as plt


def get_new_figure(rows=0, cols=0, share=True):
    """Generate new figure and axes object and return it.

    Args:
        rows: int, the number of rows of subplot
        cols: int, the number of columns of subplots
        share: bool, whether X or Y or both axes should be shared

    Returns:
        figure: figure object
        axes: single or list of axes objects
    """
    if rows == 0 and cols == 0:
        figure, axes = plt.subplots()
    elif cols == 0:
        figure, axes = plt.subplots(rows, sharex=share)
    elif rows == 0:
        figure, axes = plt.subplots(1, cols, sharey=share)
    else:
        figure, axes = plt.subplots(rows, cols, sharex=share, sharey=share)
    return figure, axes


def plot(x, y=None, axes=None):
    """Basic pyplot.plot functions.

    Args:
        x: array, an array of numbers to be plotted. If y is None, then this
            becomes the Y-axis components and X-axis components becomes an
            array of ints starting from 0 to len(x).
        y: array (optional), an array of numbers to be plotted.
        axes: plt.axes (optional), the axes to be used to plot the data on. If
            None, then a fresh axes is generated.

    Returns:
        None
    """
    if axes is None:
        figure, axes = get_new_figure()

    if y is None:
        axes.plot(x)
    else:
        axes.plot(x, y)
    plt.show()

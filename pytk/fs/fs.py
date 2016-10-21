"""A file that contains file system related functions."""

import os


def get_list_of_file_names_from_dir(path):
    """A function that returns a list of files in a given path."""
    try:
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    except OSError as e:
        print "OSError in pynrtk.fs : {0}".format(e.strerror)
        raise


def get_list_of_file_names_from_dir_ascending(path):
    """A function that returns a list of files in a given path in ascending order."""
    return sorted(get_list_of_file_names_from_dir(path))


def get_list_of_file_paths_from_dir(path):
    """A function that returns a list of files with full filenames in a given path."""
    return [os.path.join(path, f) for f in get_list_of_file_names_from_dir(path)]


def get_list_of_file_paths_from_dir_ascending(path):
    """A function that returns a list of files with full filenames in a given path in ascending order."""
    return sorted(get_list_of_file_paths_from_dir(path))

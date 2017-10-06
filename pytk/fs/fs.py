"""A file that contains file system related functions."""

import glob
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


def get_list_of_filenames(directory,
                          extension="",
                          include_directory=True,
                          include_extension=True,
                          sort=True):
    """Get list filenames from a directory that end with a specific extension.

    Args:
        directory (str): Path of the directory.
        extension (str): The extension of the filenames that need to be returned.
        include_directory (bool): If False, the directory of the filename will be returned.
            If True, the full path of the filename with be returned.
        include_extension (bool): If False, the extension will be stripped from the
            filename. If True, the extension will be included in the filename.
        sort (bool): If True, sort the filenames. If False, return unsorted.

    Returns:
        list: The list of filenames (string) within the directory. The filenames
            can have the full path and extension depending on the arguments.
    """
    glob_regex = os.path.join(directory, "*" + extension)
    filenames = glob.glob(glob_regex)
    print(filenames[0])

    if not include_directory:
        filenames = [os.path.basename(filename) for filename in filenames]

    if (not include_extension) & (len(extension) > 0):
        extension_length = len(extension)
        filenames = [filename[:-extension_length] for filename in filenames]

    if sort:
        filenames = sorted(filenames)

    return filenames

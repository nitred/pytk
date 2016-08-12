"""A file that contains functions related to tarfiles."""

import tarfile


def print_tarfile_info(path):
    """A function that shows information of the tarfile using 'r' mode."""
    with tarfile.open(path, "r") as tar:
        count = 0
        for tarinfo in tar:
            count += 1
            print "{:0>4} {} is {} bytes in size and is".format(count,
                                                                tarinfo.name,
                                                                tarinfo.size),
            if tarinfo.isfile():
                print "a regular file."
            elif tarinfo.isdir():
                print "a directory."
            else:
                print "something else."


def get_list_of_file_tarinfos_in_tarfile(path):
    """A function that returns a list of all files as tarinfos in the tarfile."""
    with tarfile.open(path, "r") as tar:
        tarinfos = [tarinfo for tarinfo in tar.getmembers() if tarinfo.isfile()]
        return tarinfos


def get_list_of_member_filenames_in_tarfile(path):
    """A function that returns a list of all filenames in the tarfile."""
    with tarfile.open(path, "r") as tar:
        filenames = [tarinfo.name for tarinfo in tar.getmembers() if tarinfo.isfile()]
        return filenames


def get_list_of_member_filenames_in_tarfile_ascending(path):
    """A function that returns a list of all filenames in the tarfile in ascending order."""
    filenames = sorted(get_list_of_member_filenames_in_tarfile(path))
    return filenames

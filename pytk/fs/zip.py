"""A file that contains zip file extractions related functions."""

import zipfile
# import os


def get_list_of_member_files_and_folders_in_zipfile(zipfile_path):
    """Get a list of files and folders within the zipfile."""
    if zipfile.is_zipfile(zipfile_path):
        zf = zipfile.ZipFile(zipfile_path, 'r')
        return zf.namelist()
    else:
        raise IOError("{0} is not a zipfile!".format(zipfile_path))


# def get_list_of_member_filenames_in_zipfile(zipfile_path):
#     """Get a list of filenames within the zipfile."""
#     all_filenames = get_list_of_member_files_and_folders_in_zipfile(zipfile_path)
#     filenames = [filename for filename in all_filenames if os.path.isfile(filename)]
#     return filenames
#
#
# def get_list_of_member_folders_in_zipfile(zipfile_path):
#     """Get a list of folders within the zipfile."""
#     all_filenames = get_list_of_member_files_and_folders_in_zipfile(zipfile_path)
#     folders = [folder for folder in all_filenames if os.path.isdir(folder)]
#     return folders

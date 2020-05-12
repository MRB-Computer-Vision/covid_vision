from pathlib import Path
import os

def make_dir(path):
    """
    Create the directory and subdirectories
    @param path to create the directories
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def read_names(path):
    """
    Read the files with names of classes and returns one array with strings
    @param path to the file
    """
    file = open(path, 'r')
    return file.readlines()

def list_files(path, verbose = False):

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if ".jpg" or ".jpeg" in file:
                files.append(os.path.join(r, file))
    if verbose:
        for f in files:
            print(f)
    return files

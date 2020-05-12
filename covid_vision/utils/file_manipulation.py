from pathlib import Path
import os

def make_dir(path):
    """
    Create the directory and subdirectories
    @param path to create the directories
    """
    Path(path).mkdir(parents=True, exist_ok=True)

def download_from_google_drive(self, file_id, folder, name):
    """
    Download a file from Google
    @param file_id identifier from google drive
    @param folder where the file should be saved
    @param name name of the file where the file will be saved
    """
    make_dir(folder)
    gdd.download_file_from_google_drive(file_id=file_id, dest_path=folder + name, showsize=True)
    with zipfile.ZipFile(folder + name, 'r') as zip_ref:
        zip_ref.extractall(folder)

def read_names(path):
    """
    Read the files with names of classes and returns one array with strings
    @param path path to the file
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

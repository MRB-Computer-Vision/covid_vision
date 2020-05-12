from google_drive_downloader import GoogleDriveDownloader as gdd
from covid_vision.utils.file_manipulation import make_dir, list_files
import zipfile
import cv2


class DataLoader:
    def __init__(self, type):
        self.images = {}
        self.images['covid'] = []
        self.images['non-covid'] = []
        self.type = type

    def download_xray_datasets(self):
        file_id = "1SG5PorcAdZvTrp6KbivSHQv4TKgMqusW"
        self.download_from_google_drive(file_id=file_id, folder="data/", name="dataset_covid_19.zip")

    def download_from_google_drive(self, file_id, folder, name):
        """
        Download de um arquivo do google drive
        @param file_id identificador do google drive do arquivo
        @param folder pasta que será armazenado
        @param name nome do arquivo que será salvo
        """
        make_dir(folder)
        gdd.download_file_from_google_drive(file_id=file_id, dest_path=folder + name, showsize=True)
        with zipfile.ZipFile(folder + name, 'r') as zip_ref:
            zip_ref.extractall(folder)

    def load_dataset(self):
        if self.type is "xray":
            names_covid = list_files("data/Dataset COVID-19 Augmented/COVID-19")
            names_noncovid = list_files("data/Dataset COVID-19 Augmented/Non-COVID-19")

        for name in names_covid:
            self.images['covid'].append(cv2.imread(name))
        for name in names_noncovid:
            self.images['non-covid'].append(cv2.imread(name))
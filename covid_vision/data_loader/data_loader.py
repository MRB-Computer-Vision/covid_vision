from covid_vision.utils.file_manipulation import list_files, download_from_google_drive
import cv2


class DataLoader:

    def __init__(self, data_type):
        self.images = dict()
        self.images['covid'] = []
        self.images['non-covid'] = []
        self.data_type = data_type

    def _download_xray_datasets(self):
        """Download the XRay dataset from Google"""
        file_id = "1SG5PorcAdZvTrp6KbivSHQv4TKgMqusW"
        download_from_google_drive(file_id=file_id, folder="data/", name="dataset_covid_19.zip")


    def load_dataset(self):
        """ Load the dataset base on the specific type """
        if self.data_type == "xray":
            if not list_files("data/Dataset COVID-19 Augmented"):
                self._download_xray_datasets()
            names_covid = list_files("data/Dataset COVID-19 Augmented/COVID-19")
            names_noncovid = list_files("data/Dataset COVID-19 Augmented/Non-COVID-19")
        elif self.data_type == "ultrassound":
            raise NotImplementedError
        elif self.data_type == "computedtomography":
            raise NotImplementedError
        elif self.data_type == "anamnesis":
            raise NotImplementedError

        for name in names_covid:
            self.images['covid'].append(cv2.imread(name))
        for name in names_noncovid:
            self.images['non-covid'].append(cv2.imread(name))

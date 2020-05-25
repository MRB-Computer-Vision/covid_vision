import os
from tensorflow.keras.models import load_model
from keras.preprocessing import image
import numpy as np
from covid_vision.ml.models.abstract_classifier import ClassifierInterface
from covid_vision.utils.file_manipulation import download_from_google_drive, list_files


class CovidCXR(ClassifierInterface):
    model = None
    img_width, img_height = 224, 224
    CLASSES = ['non-COVID-19', 'COVID-19']
    model_path = 'data/covid_cxr.h5'
    def __init__(self):
        self.load_model()

    def _download_cxr_model(self):
        """Download the XRay dataset from Google"""
        file_id = "1KIsLmVv8jKTVG_LxchMZAvR7rugHy7uB"
        download_from_google_drive(file_id=file_id, folder="data/", name="covid_cxr.zip")


    def read_image(self, path):
        img = image.load_img(path, target_size=(self.img_width, self.img_height))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img = np.vstack([x])
        return img

    def load_model(self):

        if not os.path.exists(self.model_path):
            self._download_cxr_model()

        self.model = load_model(self.model_path,
                                custom_objects={"custom_loss": 'accuracy'},
                                compile=False)
        self.model.compile(optimizer='adam', loss='accuracy')

    def predict(self, image):
        '''
        Runs model prediction on 1 or more input images.
        :param x: Image(s) to predict
        :param model: A Keras model
        :return: A numpy array comprising a list of class probabilities for each prediction
        '''
        y = self.model.predict(image, batch_size=32)  # Run prediction on the perturbations
        if y.shape[1] == 1:
            probs = np.concatenate([1.0 - y, y], axis=1)  # Compute class probabilities from the output of the model
        else:
            probs = y
        return probs

import unittest
from unittest.mock import MagicMock
from covid_vision.data_loader.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    def setUp(self):

        pass

    def test_xray_data_loader(self):
        data_loader = DataLoader(data_type="xray")
        data_loader.load_dataset = MagicMock()
        self.assertIsInstance(data_loader.images, dict)
        self.assertIsInstance(data_loader.images['covid'], list)
        self.assertIsInstance(data_loader.images['non-covid'], list)

    def test_ultrassound_data_loader(self):
        data_loader = DataLoader(data_type="ultrassound")
        with self.assertRaises(NotImplementedError):
            data_loader.load_dataset()

    def test_computedtomography_data_loader(self):
        data_loader = DataLoader(data_type="computedtomography")
        with self.assertRaises(NotImplementedError):
            data_loader.load_dataset()

    def test_anamnesis_data_loader(self):
        data_loader = DataLoader(data_type="anamnesis")
        with self.assertRaises(NotImplementedError):
            data_loader.load_dataset()


if __name__ == '__main__':
    unittest.main()

import unittest

from covid_vision.data_loader.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        data_loader = DataLoader()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

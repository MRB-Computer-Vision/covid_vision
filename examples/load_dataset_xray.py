# -*- coding: utf-8 -*-

""" Example to test the dataloader

"""
from covid_vision.data_loader.data_loader import DataLoader

#Data loading
data_loader = DataLoader(data_type="xray")
data_loader.load_dataset()

#Check the loaded data
print("Count of COVID Images:", data_loader.images['covid'].__len__())
print("Count of Non-Covid Images:", data_loader.images['non-covid'].__len__())

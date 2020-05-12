from covid_vision.data_loader.data_loader import DataLoader

data_loader = DataLoader(data_type="xray")
data_loader.load_dataset()

print("Quantidade de imagens com covid:", data_loader.images['covid'].__len__())
print("Quantidade de imagens sem covid:", data_loader.images['non-covid'].__len__())

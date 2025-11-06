import kagglehub

# Dowload latest version
path = kagglehub.dataset_download("iarunava/cell-images-for-detecting-malaria")

print('Path to files: ', path)
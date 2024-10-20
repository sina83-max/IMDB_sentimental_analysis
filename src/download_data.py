import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Kaggle dataset identifier
dataset = 'lakshmi25npathi/imdb-dataset-of-50k-movie-reviews'

# Define the path where the dataset will be stored
data_dir = 'data/raw/'
zip_path = os.path.join(data_dir, 'imdb-dataset-of-50k-movie-reviews.zip')
csv_path = os.path.join(data_dir, 'IMDB Dataset.csv')


def download_data():
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    if not os.path.exists(csv_path):
        print("Downloading dataset from Kaggle...")
        api = KaggleApi()
        api.authenticate()  # This will authenticate using environment variables or kaggle.json

        api.dataset_download_files(dataset, path=data_dir, unzip=False)

        print("Dataset downloaded. Extracting the zip file...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)

        # Clean up the zip file after extraction
        os.remove(zip_path)
        print(f"Dataset extracted to {csv_path}")
    else:
        print(f"Dataset already exists at {csv_path}")


if __name__ == "__main__":
    download_data()

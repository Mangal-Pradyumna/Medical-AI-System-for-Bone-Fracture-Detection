
# download_dataset.py

"""
Python script to download the Human Bone Fractures Image Dataset from Kaggle using Kaggle API.
"""

import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_extract_dataset(kaggle_dataset, download_path='Human_Bone_Fractures'):
    """Download and extract dataset from Kaggle."""
    if os.path.exists(download_path):
        print(f"Dataset directory '{download_path}' already exists. Skipping download.")
        return

    api = KaggleApi()
    api.authenticate()

    print(f"Downloading dataset {kaggle_dataset}...")
    api.dataset_download_files(kaggle_dataset, path='.', unzip=False)

    zip_filename = kaggle_dataset.split('/')[-1] + '.zip'
    print(f"Extracting {zip_filename}...")

    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(download_path)

    os.remove(zip_filename)
    print(f"Dataset downloaded and extracted to '{download_path}'.")


if __name__ == '__main__':
    # Dataset identifier on Kaggle
    kaggle_dataset = 'jockeroika/human-bone-fractures-image-dataset'
    download_and_extract_dataset(kaggle_dataset)

"""
Instructions:
1. Install Kaggle API if not installed: pip install kaggle
2. Place your Kaggle API token (kaggle.json) in the ~/.kaggle/ directory (Linux/macOS) or C:\Users\<YourUser>\.kaggle\ (Windows).
3. Run this script using: python download_dataset.py
"""

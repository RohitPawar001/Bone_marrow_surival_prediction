import zipfile
import pandas as pd
import arff
import shutil
import os
import urllib.request as request
from pathlib import Path
from Bone_marrow_survival_prediction import logger
from Bone_marrow_survival_prediction.utils.comman import get_size
from Bone_marrow_survival_prediction.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

            
    def download_file(self):
        
        local_data_file_dir = os.path.dirname(self.config.local_data_file)
        if not os.path.exists(local_data_file_dir):
            os.makedirs(local_data_file_dir, exist_ok=True)

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            print(f"{filename} downloaded! with the following info: \n{headers}")
        else:
            print(f"File already exists of size: {os.path.getsize(self.config.local_data_file)}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        print(f"Extracted all files to {unzip_path}")
            
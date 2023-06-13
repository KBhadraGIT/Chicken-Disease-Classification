#Importing required dependencies
import os
import urllib.request as request
import zipfile
from pathlib import Path
################################################################
from chicken_disease import logger
from chicken_disease.utils import get_size
from chicken_disease.entity.config_entity import DataIngestionConfig

class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        """
        Initializes a DataIngestion object with the specified configuration.

        Args:
            config (DataIngestionConfig): The configuration object containing the necessary parameters.

        Returns:
            None
        """

        self.config = config


    def download_file(self):
        """
        Downloads a file from the specified source URL and saves it locally.

        If the file already exists, logs the file size. Otherwise, logs the downloaded file's information.

        Returns:
            None
        """

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    def extract_zip_file(self):
        """
        Extracts the contents of a zip file into the specified directory.

        Creates the directory if it does not exist.

        Returns:
            None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
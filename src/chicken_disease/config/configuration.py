#Import required dependencies
from chicken_disease.constants import *
from chicken_disease.utils import read_yaml, create_directories
from chicken_disease.entity.config_entity import DataIngestionConfig


#Data Ingestion
class ConfigurationManager:
    """
    A class for managing configuration settings and retrieving data ingestion configuration.

    ARGS:
        config_filepath (str): The filepath to the configuration file. Default is CONFIG_FILE_PATH.
        params_filepath (str): The filepath to the parameters file. Default is PARAMS_FILE_PATH.

    ATTRIBUTES:
        config (dict): A dictionary containing the configuration settings.
        params (dict): A dictionary containing the parameter settings.

    METHODS:
        get_data_ingestion_config(): Retrieves the data ingestion configuration.

    """
    
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        """
        Initializes a new instance of the ConfigurationManager class.

        ARGS:
            config_filepath (str): The filepath to the configuration file. Default is CONFIG_FILE_PATH.
            params_filepath (str): The filepath to the parameters file. Default is PARAMS_FILE_PATH.
        """

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieves the data ingestion configuration.

        RETURNS:
            DataIngestionConfig: An instance of the DataIngestionConfig class representing the data ingestion configuration.
        """

        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
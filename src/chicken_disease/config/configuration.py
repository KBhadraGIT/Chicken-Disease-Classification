#Import required dependencies
from chicken_disease.constants import *
from chicken_disease.utils import read_yaml, create_directories
from chicken_disease.entity.config_entity import (DataIngestionConfig,
                                                  ModelTrainerConfig)


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
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Retrieves the model trainer configuration.

        Returns:
            ModelTrainerConfig: The configuration object for the model trainer.
        """
        
        config = self.config.model_trainer
        
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(root_dir=Path(config.root_dir),
                                                  base_model_path=Path(config.base_model_path),
                                                  trained_model_path=Path(config.trained_model_path),
                                                  params_image_size=self.params.IMAGE_SIZE,
                                                  params_learning_rate=self.params.LEARNING_RATE,
                                                  params_include_top=self.params.INCLUDE_TOP,
                                                  params_weights=self.params.WEIGHTS,
                                                  params_classes=self.params.CLASSES)

        return model_trainer_config
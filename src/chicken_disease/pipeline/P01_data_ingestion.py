import sys
from chicken_disease.config.configuration import ConfigurationManager
from chicken_disease.components.data_ingestion import DataIngestion
from chicken_disease import logger, CDCException



STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    """
    A class representing a data ingestion training pipeline.

    Methods:
        -  __init__(): Initializes the DataIngestionTrainingPipeline object.
        -  main(): Executes the main data ingestion and training pipeline.

    Attributes:
        None
    """
    
    def __init__(self):
        """
        Initializes the DataIngestionTrainingPipeline object.
        """
        pass

        pass

    def main(self):
        """
        Executes the main data ingestion training pipeline.

        This method performs the following steps:
        1. Retrieves the data ingestion configuration from the ConfigurationManager.
        2. Initializes a DataIngestion object with the retrieved configuration.
        3. Downloads the file using the DataIngestion object.
        4. Extracts the contents of the downloaded zip file.
        
        Returns:
            None
        """

        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
    
        except Exception as e:
            logger.exception(CDCException(error_message=e, error_detail=sys))
            raise CDCException(error_message=e, error_detail=sys)
        

if __name__ == '__main__':
    try:
        logger.info(">>>>>>>>>>>>>>>>>>>>  INITIATING DATA INGESTION  <<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(">>>>>>>>>>>>>>>>>>>>  TERMINATING DATA INGESTION  <<<<<<<<<<<<<<<<<<<<")
    except Exception as e:
            logger.exception(CDCException(error_message=e, error_detail=sys))
            raise CDCException(error_message=e, error_detail=sys)
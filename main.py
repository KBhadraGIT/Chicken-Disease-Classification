import sys
from chicken_disease import *
from chicken_disease.pipeline.P01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease.pipeline.P02_model_trainer import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion"

try:
    logger.info("**"*20)
    logger.info(">>>>>>>>>>>>>>>>>>>>  INITIATING DATA INGESTION  <<<<<<<<<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(">>>>>>>>>>>>>>>>>>>>  TERMINATING DATA INGESTION  <<<<<<<<<<<<<<<<<<<<")
    logger.info("**"*20)

except Exception as e:
    logger.exception(CDCException(error_message=e, error_detail=sys))
    raise CDCException(error_message=e, error_detail=sys)

STAGE_NAME = "Model Training"

try:
    logger.info("**"*20)
    logger.info(">>>>>>>>>>>>>>>>>>>>  INITIATING MODEL TRAINING  <<<<<<<<<<<<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(">>>>>>>>>>>>>>>>>>>>  TERMINATING MODEL TRAINING  <<<<<<<<<<<<<<<<<<<<")
    logger.info("**"*20)

except Exception as e:
        logger.exception(CDCException(error_message=e, error_detail=sys))
        raise CDCException(error_message=e, error_detail=sys)
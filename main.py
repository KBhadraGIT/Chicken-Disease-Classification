import sys
from chicken_disease import logger, CDCException
from chicken_disease.pipeline.P01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(CDCException(error_message=e, error_detail=sys))
    raise CDCException(error_message=e, error_detail=sys)
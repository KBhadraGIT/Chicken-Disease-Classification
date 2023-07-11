import sys

from chicken_disease.config.configuration import ConfigurationManager
from chicken_disease.components.model_trainer import ModelTrainer
from chicken_disease import *


STAGE_NAME = "Training base model"

class ModelTrainingPipeline:

    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.fetch_base_model()
        model_trainer.base_model_trainer()
        

if __name__ == "__main__":
    try:
        logger.info("|==|"*20)
        logger.info(">>>>>>>>>>>>>>>>>>>>  INITIATING MODEL TRAINING  <<<<<<<<<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(">>>>>>>>>>>>>>>>>>>>  TERMINATING MODEL TRAINING  <<<<<<<<<<<<<<<<<<<<")
        logger.info("|==|"*20)

    except Exception as e:
            logger.exception(CDCException(error_message=e, error_detail=sys))
            raise CDCException(error_message=e, error_detail=sys)
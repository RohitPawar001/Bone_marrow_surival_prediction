
from Bone_marrow_survival_prediction import logger
from Bone_marrow_survival_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Bone_marrow_survival_prediction.pipeline.satge_02_data_validation import DataValidationPipeline
from Bone_marrow_survival_prediction.pipeline.stage_03_data_transformation_pipeline import DataTransformationPipeline
from Bone_marrow_survival_prediction.pipeline.stage_04_model_trainer_pipeline import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion satge"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation satge"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transfromation satge"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer  Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e
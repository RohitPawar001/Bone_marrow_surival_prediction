from Bone_marrow_survival_prediction.config.configuration import ConfigurationManager
from Bone_marrow_survival_prediction.components.model_trainer import ModelTrainer
from Bone_marrow_survival_prediction import logger 

STAGE_NAME = "model training stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} has started <<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} has completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    
                
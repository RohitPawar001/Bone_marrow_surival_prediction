from Bone_marrow_survival_prediction.config.configuration import ConfigurationManager
from Bone_marrow_survival_prediction.components.model_evaluation import ModelEvaluation
from Bone_marrow_survival_prediction import logger 

STAGE_NAME = "model evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):

        DAGSHUB_ACCESS_TOKEN = "490e6ae7bb9405fa77d80a472fcda7758b0d1abd"
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        metrics = model_evaluation.log_into_mlflow(DAGSHUB_ACCESS_TOKEN)

        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.excetion(e)
        raise e
from Bone_marrow_survival_prediction.config.configuration import ConfigurationManager
from Bone_marrow_survival_prediction.components.data_transformation import DataTransformation
from Bone_marrow_survival_prediction import logger 


STAGE_NAME = "data transformation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):

        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.train_test_split()

        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.excetion(e)
        raise e
import mlflow
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from urllib.parse import urlparse
from sklearn.metrics import accuracy_score, precision_score, f1_score
from Bone_marrow_survival_prediction import logger
from Bone_marrow_survival_prediction.entity.config_entity import ModelEvaluationConfig
from Bone_marrow_survival_prediction.utils.comman import setup_dagshub_mlflow_tracking



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):

        try:
            accuracy = accuracy_score(actual, pred)
            precision = precision_score(actual, pred, average='weighted')
            f1 = f1_score(actual, pred, average='weighted')
            return accuracy, precision, f1
        except Exception as e:
            print(f"Error calculating metrics: {e}")
            return 0, 0, 0
    
    def log_into_mlflow(self, access_token):
        
        try:
            
            setup_dagshub_mlflow_tracking(access_token)
            test_df = pd.read_csv(self.config.x_test_data_path)
            test_labels_df = pd.read_csv(self.config.y_test_data_path)
            
            
            X_test = test_df
            y_test = test_labels_df
            
           
            model = joblib.load(self.config.model_path)
            
           
            y_pred = model.predict(X_test)
            
           
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted')
            f1 = f1_score(y_test, y_pred, average='weighted')
            
            
            with mlflow.start_run():
               
                mlflow.log_metrics({
                    "accuracy": accuracy,
                    "precision": precision,
                    "f1_score": f1
                })
                
                
                mlflow.sklearn.log_model(
                    model, 
                    "model", 
                    registered_model_name="BoneMarrowSurvivalModel"
                )
                
                logger.info("Model and metrics logged successfully")
                
                return {
                    "accuracy": accuracy,
                    "precision": precision,
                    "f1_score": f1
                }
        
        except Exception as e:
            logger.exception(e)
            raise e
    
    

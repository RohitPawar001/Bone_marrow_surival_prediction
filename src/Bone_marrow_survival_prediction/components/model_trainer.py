
import pandas as pd
import os
from pathlib import Path
from Bone_marrow_survival_prediction import logger
from Bone_marrow_survival_prediction.entity.config_entity import ModelTrainerConfig
from sklearn.svm import SVC
import joblib

class ModelTrainer :
    def __init__(self, config:ModelTrainerConfig):
        self.config = config
        
    def train(self):
        x_train = pd.read_csv(self.config.train_data_path)
        y_train = pd.read_csv(self.config.y_train_path)
        x_test = pd.read_csv(self.config.test_data_path)
        y_test = pd.read_csv(self.config.y_test_path)
        
        
        svc = SVC(C=self.config.c, kernel = self.config.kernel,random_state=42)
        svc.fit(x_train,y_train)
        
        joblib.dump(svc,os.path.join(self.config.root_dir,self.config.model_name))
        logger.info(f" Model has been genertaed successfully")
        
    
    

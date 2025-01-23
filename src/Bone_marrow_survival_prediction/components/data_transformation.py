import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import mutual_info_classif
from imblearn.over_sampling import SMOTE
from collections import Counter
from Bone_marrow_survival_prediction.entity.config_entity import DataTransformationConfig
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

    
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    @staticmethod
    def is_string_numeric(val):
        try:
            float(val)
            return True
        except ValueError:
            return False

    def preprocess_data(self):
        data = pd.read_csv(self.config.data_path)

        if "Disease" in data.columns and data["Disease"].dtype == "O":
            encoder = OrdinalEncoder()
            data["Disease_encoded"] = encoder.fit_transform(data[["Disease"]])
            data.drop("Disease", axis=1, inplace=True)

        data.replace("?", np.nan, inplace=True)
        data.dropna(inplace=True)

        for feature in data.columns:
            if data[feature].dtype == "O":
                is_numeric = data[feature].apply(self.is_string_numeric)
                if is_numeric.all():  
                    data[feature] = data[feature].astype("float64")
                    logger.info(f"The {feature} feature is converted into float")

        return data

    def train_test_split(self):
        data = self.preprocess_data()  
         

        X = data.drop("survival_status",axis = 1)
        y = data["survival_status"]

        mi = mutual_info_classif(X, y)
        mi_df = pd.DataFrame({'Feature': X.columns, 'Mutual Information': mi})
        mi_df = mi_df.sort_values(by='Mutual Information', ascending=False)
        top_features = mi_df.head(5)['Feature']

        X = data[top_features]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        desired_percentage = 0.5

        current_counts = Counter(y_train)
        total_samples = len(y_train)
        minority_class = min(current_counts, key=current_counts.get)
        majority_class = max(current_counts, key=current_counts.get)

        desired_minority_count = int(total_samples * desired_percentage)
        minority_samples_needed = desired_minority_count - current_counts[minority_class]

        # Apply SMOTE to balance the dataset
        smote = SMOTE(sampling_strategy={minority_class: current_counts[minority_class] + minority_samples_needed})
        X_train, y_train = smote.fit_resample(X_train, y_train)

        X_train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        y_train.to_csv(os.path.join(self.config.root_dir, "y_train.csv"), index=False)
        X_test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        y_test.to_csv(os.path.join(self.config.root_dir, "y_test.csv"), index=False)

        logger.info("Splited data into train and test sets")

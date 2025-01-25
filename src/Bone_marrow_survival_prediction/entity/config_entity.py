from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path
    
    
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE : str
    unzip_dir : Path
    all_schema : dict
    
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path
    
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir : Path
    train_data_path: Path
    y_train_path :Path
    test_data_path : Path
    y_test_path : Path
    c : float
    kernel : str
    model_name : str
    target_column : str
    


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir : Path
    x_test_data_path : Path
    y_test_data_path : Path
    metric_file_name : Path
    model_path : Path
    all_params : dict
    target_column :str
    mlflow_uri : str
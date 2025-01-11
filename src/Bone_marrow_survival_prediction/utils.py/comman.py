import os
from box.exceptions import BoxValueError
import yaml
from Bone_marrow_survival_prediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} read_successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:Path,verbose=True):
    for Path in path_to_directories:
        os.makedirs(Path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at {Path}")
            

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at: {path}")
    
    
        
@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"json file loadded successfully from :{path}")
    
    return ConfigBox(content)


@ensure_annotations
def svae_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at :{path}")
   
   
@ensure_annotations
def load_bin(path:Path) ->Any:
    data = joblib.load(path)
    logger.info(f"binary file loadded successfully from: {path}")
    return data

@ensure_annotations
def get_size(path:Path) ->str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" ~{size_in_kb} KB"
    
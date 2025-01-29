
# Bone Marrow Survival Prediction

A machine learning project to predict survival outcomes for pediatric patients undergoing bone marrow transplant surgery, leveraging the UCI Machine Learning Repository dataset.

## 📋 Project Overview

This project implements a machine learning model to predict survival outcomes for children undergoing bone marrow transplant procedures. The system is deployed on AWS EC2 with complete CI/CD pipeline integration, containerized using Docker, and includes MLflow for experiment tracking and model versioning.

## 🔑 Key Features

- Survival prediction model for bone marrow transplant patients
- Automated CI/CD pipeline for seamless deployment
- Docker containerization for consistent environments
- MLflow integration for experiment tracking
- AWS EC2 deployment with high availability
- REST API endpoints for model inference

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **MLflow**: Model tracking and versioning
- **Docker**: Containerization
- **AWS Services**: EC2, ECR
- **CI/CD**: GitHub Actions
- **Web Framework**: Flask

## 🚀 Getting Started

### workflow 

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Uodate the entity
5. Update the configurayion manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


### Prerequisites

- Python 3.8+
- Docker
- AWS CLI configured
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/RohitPawar001/Bone_marrow_surival_prediction.git
cd Bone_marrow_surival_prediction
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
# or
venv\Scripts\activate     # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

1. Start MLflow server:
```bash
$env:MLFLOW_TRACKING_URI="your url"

$env:MLFLOW_TRACKING_USERNAME="your username"


$env:MLFLOW_TRACKING_PASSWORD="mlflow api key "
```

2. Run the application:
```bash
python app.py
```

### AWS EC2 Deployment

1. Build EC2 instance and coneect to the cli (ubuntu):

```shell 
sudo apt-get update -y

sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh

sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

2. create self-hosted runner:

3. save the secreate credentials :



## 📊 Dataset

The project uses the Bone Marrow Transplant Surgery Children dataset from the UCI Machine Learning Repository. The dataset includes various patient parameters and survival outcomes, providing a comprehensive base for prediction modeling.

### Features Include:
- Patient demographics
- Medical history
- Transplant-specific parameters
- Post-surgery recovery indicators

## 🔄 MLflow Integration

The project uses MLflow for:
- Experiment tracking
- Model versioning
- Parameter logging
- Performance metrics visualization
- Model registry



## ⚙️ CI/CD Pipeline

The project implements a robust CI/CD pipeline using GitHub Actions:

1. **Continuous Integration**:
   - Automated testing
   - Code quality checks
   - Docker image building

2. **Continuous Deployment**:
   - Automated deployment to AWS EC2
   - Docker container orchestration
   - Environment configuration



## 📝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👤 Authors

- Rohit Pawar





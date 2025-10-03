
CPU Usage Prediction
📌 Project Overview
This project predicts CPU usage from tabular system metrics. It demonstrates:
Data versioning with DVC
Reproducible ML pipelines (preprocess → train → evaluate)
Model training and evaluation
---
📂 Repository Structure
AV-APITHA/
│── .config                  # Colab/IDE configurations
│── .dvc/                     # DVC folder for data tracking
│── sample_data/              # Input dataset tracked by DVC
│── .dvcignore                # Files ignored by DVC
│── .gitignore                # Files ignored by Git
│── data.csv.dvc              # DVC-tracked dataset
│── dvc.yaml                  # DVC pipeline stages: preprocess → train → evaluate
│── dvc.lock                  # DVC lock file
│── preprocess.py             # Data preprocessing script
│── train.py                  # Model training script
│── evaluate.py               # Model evaluation script
⚙ Setup Instructions

1. Clone the repository:
git clone https://github.com/AV-APITHA/_cpu_usage_.git
cd AV-APITHA
2. Install dependencies:
pip install -r requirements.txt
3. Pull datasets tracked with DVC:
dvc pull
---
🚀 Running the Pipeline
Run the full pipeline:
dvc repro
> Note: Trained models and MLflow artifacts are ignored in GitHub (listed in .gitignore).
📈 Results & Evaluation
Evaluation metrics (RMSE, MAE, R²) are computed during the evaluation stage.
Residual plots and feature importance plots are generated locally in your environment.
MLflow is used to track experiments and log parameters, metrics, and models locally.


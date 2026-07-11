# Insurance Premium Category Classifier

## Overview

The **Insurance Premium Category Classifier** is a Machine Learning project that predicts the premium category of an insurance customer based on various demographic, financial, and policy-related features.

The goal of this project is to help insurance companies automate premium categorization, improve pricing strategies, and support faster decision-making during policy underwriting.

---

## Problem Statement

Insurance companies often need to determine the appropriate premium category for customers based on multiple factors such as:

* Age
* Gender
* BMI
* Smoking Status
* Number of Dependents
* Region
* Medical History
* Income Level
* Lifestyle Factors

Manually categorizing customers can be time-consuming and inconsistent. This project leverages Machine Learning techniques to automate the classification process.

---

## Project Workflow

```text
Data Collection
       │
       ▼
Data Cleaning & Preprocessing
       │
       ▼
Exploratory Data Analysis (EDA)
       │
       ▼
Feature Engineering
       │
       ▼
Train-Test Split
       │
       ▼
Model Training
       │
       ▼
Model Evaluation
       │
       ▼
Premium Category Prediction
```

---

## Dataset

The dataset contains customer information and corresponding premium categories.

### Features

| Feature         | Description                  |
| --------------- | ---------------------------- |
| Age             | Customer age                 |
| Gender          | Male/Female                  |
| BMI             | Body Mass Index              |
| Children        | Number of dependents         |
| Smoker          | Smoking status               |
| Region          | Customer region              |
| Charges         | Historical insurance charges |
| Income          | Annual income                |
| Medical History | Relevant medical conditions  |

### Target Variable

Premium Category:

* Low Premium
* Medium Premium
* High Premium

---

## Project Structure

```text
insurance-premium-category-classifier/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Training.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── models/
│   └── classifier.pkl
│
├── artifacts/
│   ├── scaler.pkl
│   ├── encoder.pkl
│   └── metrics.json
│
├── requirements.txt
├── README.md
└── app.py
```

---

## Technologies Used

* Python 3.x
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Joblib
* Flask / FastAPI (Optional)
* Streamlit (Optional)

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/insurance-premium-category-classifier.git

cd insurance-premium-category-classifier
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Train the Model

```bash
python src/train.py
```

### Make Predictions

```bash
python src/predict.py
```

### Run Web Application

#### Streamlit

```bash
streamlit run app.py
```

#### FastAPI

```bash
uvicorn app:app --reload
```

---

## Data Preprocessing

The following preprocessing steps are applied:

* Missing value handling
* Duplicate removal
* Outlier analysis
* Categorical feature encoding
* Feature scaling
* Train-test splitting

---

## Feature Engineering

Implemented feature engineering techniques include:

* Label Encoding
* One-Hot Encoding
* Feature Scaling
* Derived Features
* Correlation Analysis

---

## Machine Learning Models

The following models can be evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* Gradient Boosting
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)

---

## Evaluation Metrics

Classification performance is measured using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC Score

Example:

```text
Accuracy  : 92.5%
Precision : 91.8%
Recall    : 92.1%
F1 Score  : 91.9%
```

---

## Example Prediction

### Input

```json
{
  "age": 35,
  "gender": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "southeast"
}
```

### Output

```json
{
  "premium_category": "Medium Premium"
}
```

---

## Future Improvements

* Hyperparameter tuning
* Advanced feature engineering
* Model deployment using Docker
* CI/CD integration
* Cloud deployment (AWS, Azure, GCP)
* Real-time prediction API
* Model monitoring and drift detection

---

## Results

The final model successfully classifies insurance premium categories and can be integrated into underwriting systems to assist insurance providers in making faster and more consistent premium decisions.

---

## Author

**Dilli Ram Chaudhary**

* Data Science & Machine Learning Enthusiast
* Python Developer
* AI Research Student

---

## License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files...
```

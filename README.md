# ❤️ Heart Disease Prediction Using Machine Learning

An end-to-end machine learning project that predicts the presence of heart disease from medical attributes. The project compares multiple classification algorithms, evaluates their performance using holdout testing and stratified cross-validation, and deploys the selected model through an interactive Streamlit web application.

> ⚠️ **Medical Disclaimer:** This project is intended for educational, research, and demonstration purposes only. It is not a medical diagnostic tool and must not be used to make healthcare decisions.

## 🌐 Live Demo

**[🚀 Launch the Heart Disease Prediction App](https://codealpha-heart-disease-prediction-kvtdv2rnxrfcdl2f8hkkws.streamlit.app/)**

Explore the deployed application and interact with its prediction interface.

## 📌 Project Overview

Heart disease is a major global health concern. Machine learning can help analyze medical datasets and identify patterns associated with the presence of heart disease.

This project uses the **UCI Heart Disease Dataset** to build and compare multiple classification models. After evaluating performance on a holdout test set and through 5-fold stratified cross-validation, **Logistic Regression** was selected as the final model because of its consistent cross-validation performance.

The selected model is integrated into a Streamlit application for interactive predictions.

## 🎯 Objectives

- Analyze medical data associated with heart disease.
- Handle missing values and preprocess input features.
- Convert the original multi-class target into a binary classification problem.
- Train and compare multiple machine learning classifiers.
- Evaluate models using accuracy, precision, recall, and F1-score.
- Use stratified cross-validation to assess consistency.
- Deploy an interactive machine learning application using Streamlit.

## 📊 Dataset

**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/)

The project uses the Cleveland Heart Disease dataset with:

- **303 patient records**
- **13 input features**
- **1 target variable**

### Input Features

| Feature | Description |
|---|---|
| `age` | Patient age |
| `sex` | Sex |
| `cp` | Chest pain type |
| `trestbps` | Resting blood pressure |
| `chol` | Serum cholesterol |
| `fbs` | Fasting blood sugar |
| `restecg` | Resting electrocardiographic results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression induced by exercise |
| `slope` | Slope of the peak exercise ST segment |
| `ca` | Number of major vessels |
| `thal` | Thalassemia |

### Target Transformation

The original target contains values from 0 to 4. For this project, it was converted into a binary classification target:

- `0` → No Disease
- `1` → Disease Present

## ⚙️ Project Workflow

1. **Data loading:** Load the heart disease dataset.
2. **Preprocessing:** Handle missing values, encode categorical variables, and scale numerical features where required.
3. **Target preparation:** Convert the original target into a binary classification label.
4. **Model training:** Train multiple classification algorithms.
5. **Evaluation:** Compare holdout performance and 5-fold stratified cross-validation results.
6. **Model selection:** Select Logistic Regression based on its consistent cross-validation performance.
7. **Deployment:** Integrate the trained model into a Streamlit application.

## 🤖 Machine Learning Models

The following algorithms were evaluated:

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest Classifier
- XGBoost Classifier

### Holdout Test Results

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Logistic Regression | 88.52% | 83.87% | 92.86% | 88.14% |
| SVM | 88.52% | 83.87% | 92.86% | 88.14% |
| Random Forest | 88.52% | 83.87% | 92.86% | 88.14% |
| XGBoost | 90.16% | 84.38% | 96.43% | 90.00% |

### 5-Fold Stratified Cross-Validation Results

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Logistic Regression | 85.47% | 87.44% | 79.79% | 83.32% |
| SVM | 84.48% | 85.01% | 80.56% | 82.61% |
| Random Forest | 84.17% | 85.60% | 79.15% | 82.14% |
| XGBoost | 82.52% | 83.66% | 77.70% | 80.39% |

### Final Model Selection

Although XGBoost achieved the highest holdout accuracy, **Logistic Regression was selected as the final model** because it performed consistently across cross-validation and achieved the strongest cross-validation accuracy and F1-score among the evaluated models.

This comparison highlights why model selection should consider validation performance and consistency rather than relying on a single test score.

## 🖥️ Web Application

The project includes a Streamlit web application that connects the trained machine learning model to an interactive prediction interface.

**Live application:** [Open Heart Disease Prediction](https://codealpha-heart-disease-prediction-kvtdv2rnxrfcdl2f8hkkws.streamlit.app/)

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn, XGBoost
- **Data Processing:** Pandas, NumPy
- **Model Persistence:** Joblib
- **Web Framework:** Streamlit
- **Development Environment:** Jupyter Notebook / Python environment
- **Deployment:** Streamlit Community Cloud

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Bhuvanarajaram41-pixel/CodeAlpha-Heart-Disease-Prediction.git
cd CodeAlpha-Heart-Disease-Prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

If your main Streamlit file has a different filename, replace `app.py` with the correct filename.

## 📚 Key Learning Outcomes

Through this project, I gained practical experience in:

- Data preprocessing and missing-value handling
- Numerical feature scaling and categorical encoding
- Binary classification
- Logistic Regression, SVM, Random Forest, and XGBoost
- Model evaluation using multiple metrics
- Stratified cross-validation
- Model comparison and selection
- Saving and loading trained machine learning models
- Building and deploying a Streamlit application

## 🔮 Future Improvements

- Add model interpretability visualizations.
- Improve the application interface and user experience.
- Expand evaluation with additional validation strategies.
- Add automated tests for preprocessing and prediction.
- Document model limitations and dataset constraints in greater detail.

## ⚠️ Important Disclaimer

This application is a student machine learning project for educational and demonstration purposes. Its predictions may be incorrect and are not validated for clinical use. It must not be used to diagnose heart disease, determine treatment, or replace consultation with a qualified healthcare professional.

## 👩‍💻 Author

**Bhuvaneshwari R**

- [GitHub Profile](https://github.com/Bhuvanarajaram41-pixel)
- [Project Repository](https://github.com/Bhuvanarajaram41-pixel/CodeAlpha-Heart-Disease-Prediction)
- [Live Demo](https://codealpha-heart-disease-prediction-kvtdv2rnxrfcdl2f8hkkws.streamlit.app/)

---

*Developed as part of machine learning project work with CodeAlpha.*

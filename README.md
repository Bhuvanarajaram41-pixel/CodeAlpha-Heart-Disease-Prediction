# ❤️ Heart Disease Prediction using Machine Learning

A machine learning-based web application that predicts the presence of heart disease from medical attributes using multiple classification algorithms and provides an interactive prediction interface built with Streamlit.

> ⚠️ **Disclaimer:** This project is developed for educational, research, and demonstration purposes only. It is not a medical diagnostic tool and should not be used to make healthcare decisions.

---

## 📌 Project Overview

Heart disease is one of the major health challenges worldwide. Machine learning can be used to analyze medical data and identify patterns associated with the presence of heart disease.

This project uses the **UCI Heart Disease Dataset** to develop and compare multiple machine learning classification models. After evaluating their performance using both a holdout test set and 5-fold stratified cross-validation, **Logistic Regression** was selected as the final model based on its consistent cross-validation performance.

The trained model is integrated into an interactive **Streamlit web application** where users can enter medical parameters and obtain a model-based prediction.

---

## 🎯 Objectives

- Analyze medical data related to heart disease.
- Perform data preprocessing and missing-value handling.
- Convert the original multi-class target into a binary classification problem.
- Train multiple machine learning classification models.
- Compare model performance using multiple evaluation metrics.
- Select a suitable final model using cross-validation.
- Build an interactive prediction dashboard using Streamlit.
- Deploy the application for demonstration and portfolio use.

---

## 📊 Dataset

The project uses the **UCI Heart Disease Dataset**.

**Dataset source:** UCI Machine Learning Repository

The dataset contains:

- **303 patient records**
- **13 input features**
- **1 target variable**

### Features

| Feature | Description |
|---|---|
| `age` | Age of the patient |
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

### Target

The original `num` target contains multiple classes from 0 to 4.

For this project, it was converted into a binary classification target:

```text
0 → No Disease
1 → Disease Present

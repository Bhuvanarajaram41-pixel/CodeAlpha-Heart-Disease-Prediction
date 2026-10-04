import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="CardioPredict",
    page_icon="❤️",
    layout="wide"
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load("disease_prediction_pipeline.pkl")


model = load_model()


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #6b7280;
    margin-bottom: 30px;
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
}

.disclaimer {
    background-color: #262626;
    color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #555555;
    border-left: 5px solid #ff9800;
    margin-top: 30px;
    line-height: 1.6;
}

.disclaimer-title {
    color: #ffb74d;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 8px;
}

.disclaimer-text {
    color: #e5e7eb;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="title">❤️ CardioPredict</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning-Based Heart Disease Prediction'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter the patient's medical information below to generate "
    "a prediction using the trained machine learning model."
)

st.divider()


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.subheader("🩺 Patient Information")

col1, col2, col3 = st.columns(3)


# Age
with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=50
    )

# Sex
with col2:
    sex = st.selectbox(
        "Sex",
        options=[0, 1],
        format_func=lambda x:
            "Female" if x == 0 else "Male"
    )

# Chest pain
with col3:
    cp = st.selectbox(
        "Chest Pain Type",
        options=[1, 2, 3, 4],
        format_func=lambda x: {
            1: "Type 1",
            2: "Type 2",
            3: "Type 3",
            4: "Type 4"
        }[x]
    )


col1, col2, col3 = st.columns(3)


# Resting blood pressure
with col1:
    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=50,
        max_value=250,
        value=120
    )

# Cholesterol
with col2:
    chol = st.number_input(
        "Serum Cholesterol (mg/dl)",
        min_value=50,
        max_value=700,
        value=200
    )

# Fasting blood sugar
with col3:
    fbs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        options=[0, 1],
        format_func=lambda x:
            "No" if x == 0 else "Yes"
    )


col1, col2, col3 = st.columns(3)


# Rest ECG
with col1:
    restecg = st.selectbox(
        "Resting ECG",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "Normal",
            1: "ST-T Wave Abnormality",
            2: "Left Ventricular Hypertrophy"
        }[x]
    )

# Maximum heart rate
with col2:
    thalach = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150
    )

# Exercise induced angina
with col3:
    exang = st.selectbox(
        "Exercise-Induced Angina",
        options=[0, 1],
        format_func=lambda x:
            "No" if x == 0 else "Yes"
    )


col1, col2, col3 = st.columns(3)


# Oldpeak
with col1:
    oldpeak = st.number_input(
        "ST Depression (Oldpeak)",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

# Slope
with col2:
    slope = st.selectbox(
        "ST Segment Slope",
        options=[1, 2, 3],
        format_func=lambda x: {
            1: "Upsloping",
            2: "Flat",
            3: "Downsloping"
        }[x]
    )

# CA
with col3:
    ca = st.selectbox(
        "Number of Major Vessels (CA)",
        options=[0, 1, 2, 3],
        index=0
    )


# Thal
thal = st.selectbox(
    "Thalassemia (Thal)",
    options=[3, 6, 7],
    format_func=lambda x: {
        3: "Normal",
        6: "Fixed Defect",
        7: "Reversible Defect"
    }[x]
)


st.divider()


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button(
    "🔍 Predict Heart Disease Risk",
    use_container_width=True
):

    # Create input dataframe
    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "cp": [cp],
        "trestbps": [trestbps],
        "chol": [chol],
        "fbs": [fbs],
        "restecg": [restecg],
        "thalach": [thalach],
        "exang": [exang],
        "oldpeak": [oldpeak],
        "slope": [slope],
        "ca": [ca],
        "thal": [thal]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get prediction probabilities
    probabilities = model.predict_proba(input_data)[0]

    no_disease_probability = probabilities[0] * 100
    disease_probability = probabilities[1] * 100


    # --------------------------------------------------
    # RESULT
    # --------------------------------------------------

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error(
            "⚠️ Model Prediction: Disease"
        )

    else:

        st.success(
            "✅ Model Prediction: No Disease"
        )


    # --------------------------------------------------
    # PROBABILITY
    # --------------------------------------------------

    st.subheader("📊 Prediction Probability")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "No Disease",
            f"{no_disease_probability:.2f}%"
        )

    with col2:
        st.metric(
            "Disease",
            f"{disease_probability:.2f}%"
        )


    # Probability table

    probability_df = pd.DataFrame({
        "Outcome": [
            "No Disease",
            "Disease"
        ],
        "Probability": [
            f"{no_disease_probability:.2f}%",
            f"{disease_probability:.2f}%"
        ]
    })

    st.dataframe(
        probability_df,
        use_container_width=True,
        hide_index=True
    )
# --------------------------------------------------
# DISCLAIMER
# --------------------------------------------------


st.warning(
    """
    **⚠️ Important Disclaimer**

    This application is an educational machine learning project
    developed for research and demonstration purposes.

    It is **not a medical diagnostic tool** and should not be used
    to make healthcare decisions.

    Please consult a qualified healthcare professional for
    medical evaluation.
    """
)
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load your trained model
model = joblib.load("./models/titanic_model.pkl")  

st.title("Titanic Survival Predictor")

# User inputs
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Fare Paid", 0.0, 600.0, 50.0)
embarked = st.selectbox("Port of Embarkation", ["S", "C", "Q"])

# Preprocess input
sex_male = 1 if sex == "male" else 0
embarked_Q = 1 if embarked == "Q" else 0
embarked_S = 1 if embarked == "S" else 0

input_data = pd.DataFrame([{
    "Pclass": pclass,
    "Age": age,
    "SibSp": sibsp,
    "Parch": parch,
    "Fare": fare,
    "Sex_male": sex_male,
    "Embarked_Q": embarked_Q,
    "Embarked_S": embarked_S
}])

# Predict
if st.button("Predict"):
    result = model.predict(input_data)[0]
    if result == 1:
        st.success("This passenger would have SURVIVED!")
    else:
        st.error("This passenger would NOT have survived.")

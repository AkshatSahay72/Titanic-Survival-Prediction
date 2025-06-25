# 🚢 Titanic Survival Prediction App

A machine learning web app that predicts whether a passenger would survive the Titanic disaster — built with Python, scikit-learn, and Streamlit.

🔗 **Live App:** [titanic-survival-prediction-akshat72.streamlit.app](https://titanic-survival-prediction-akshat72.streamlit.app/)

---

## 📌 Project Overview

This project takes historical Titanic passenger data and predicts who would have survived based on input features like class, gender, age, and more. It’s built using:

- **Python**
- **Pandas & scikit-learn** for data preprocessing and model building
- **RandomForestClassifier** for classification
- **Streamlit** for the web app frontend

---

## 🧠 Features

- Input passenger details (class, age, gender, etc.)
- Get real-time survival predictions
- Hosted live with a clean UI
- Handles categorical encoding + model integration

---

## 🛠️ Tech Stack

| Tool         | Use                              |
|--------------|-----------------------------------|
| Python       | Core language                     |
| Pandas       | Data wrangling                    |
| scikit-learn | ML model                          |
| Joblib       | Model serialization               |
| Streamlit    | App UI & deployment               |

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/titanic-survival-prediction.git
cd titanic-survival-prediction

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

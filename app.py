import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("rfr_model.pkl", "rb"))

st.set_page_config(page_title="Salary Prediction App", layout="centered")

st.title("💼 Salary Prediction App")

# User input
age = st.number_input("Age", 18, 65, 25)
experience = st.slider("Years of Experience", 0, 40, 2)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])

job_titles = ['Content Marketing Manager', 'Data Analyst', 'Data Scientist', 'Digital Marketing Manager',
              'Director of Data Science', 'Director of HR', 'Director of Marketing', 'Financial Analyst',
              'Financial Manager', 'Front End Developer', 'Front end Developer', 'Full Stack Engineer',
              'Human Resources Coordinator', 'Human Resources Manager', 'Junior HR Coordinator', 'Junior HR Generalist',
              'Junior Marketing Manager', 'Junior Sales Associate', 'Junior Sales Representative',
              'Junior Software Developer', 'Junior Software Engineer', 'Junior Web Developer',
              'Marketing Analyst', 'Marketing Coordinator', 'Marketing Director', 'Marketing Manager',
              'Operations Manager', 'Others', 'Product Designer', 'Product Manager', 'Receptionist',
              'Research Director', 'Research Scientist', 'Sales Associate', 'Sales Director', 'Sales Executive',
              'Sales Manager', 'Sales Representative', 'Senior Data Scientist', 'Senior HR Generalist',
              'Senior Human Resources Manager', 'Senior Product Marketing Manager', 'Senior Project Engineer',
              'Senior Research Scientist', 'Senior Software Engineer', 'Software Developer', 'Software Engineer',
              'Software Engineer Manager', 'Web Developer']

job_title = st.selectbox("Job Title", job_titles)

# Create input dictionary
input_data = {
    "Age": age,
    "Gender": 1 if gender == "Male" else 0,
    "Education Level": {"Bachelor's": 0, "Master's": 1, "PhD": 2}[education],
    "Years of Experience": experience
}

# One-hot encode job title
for title in job_titles:
    input_data[title] = 1 if job_title == title else 0

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Ensure all features match training
expected_features = ['Age', 'Gender', 'Education Level', 'Years of Experience'] + job_titles
for col in expected_features:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[expected_features]

if st.button("Predict Salary"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Salary: {prediction:,.2f}")

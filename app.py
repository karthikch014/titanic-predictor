import streamlit as st
import pickle
import numpy as np

with open('model.pkl','rb') as model_file:
    model = pickle.load(model_file)

st.title("🚢 Titanic Survival Predictor")
st.write("Enter passenger details to predict survival:")

Pclass = st.selectbox("Passenger Class", [1, 2, 3])
Sex = st.selectbox("Sex", ["male", "female"])
Age = st.slider("Age", 1, 100, 25)
SibSp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
Parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
Fare = st.number_input("Fare Paid", 0.0, 500.0, 50.0)
Embarked = st.selectbox("Port of Embarkation", ['S', 'C', 'Q'])

Sex = 0 if Sex == 'male' else 1
Embarked = {'S': 0, 'C': 1, 'Q': 2}[Embarked]

input_data = np.array([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("🎉 The passenger would have survived!")
    else:
        st.error("💀 The passenger would not have survived.")

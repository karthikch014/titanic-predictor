# 🚢 Titanic Survival Predictor

A beginner-friendly machine learning project that predicts whether a Titanic passenger would have survived or not based on input features. Built using Logistic Regression and deployed using Streamlit.

---

## 📂 Project Structure

```
titanic-predictor/
│
├── app.py              # Streamlit app code
├── model.pkl           # Trained ML model (Pickle format)
├── requirements.txt    # Required Python libraries
├── Procfile            # Deployment file (for Heroku, optional)
└── README.md           # Project documentation
```

---

## 🧠 Features Used

The app uses the following features to predict survival:

- **Pclass**: Ticket class (1st, 2nd, 3rd)
- **Sex**: Gender of the passenger
- **Age**: Age in years
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Fare**: Passenger fare
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

---

## 🛠️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/karthikch014/titanic-predictor.git
cd titanic-predictor
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🌐 Deployment Options

You can deploy this app using:

- ✅ **Streamlit Community Cloud** *(Recommended for beginners – Free and no credit card required)*
- Render, Railway, HuggingFace Spaces, etc.

---

## 🧪 Live Demo

👉 [Click here to test the live app](https://titanic-predictor-5cgdyu3awxayttbfypcp86.streamlit.app/)  
_(Update this link after deploying your app on Streamlit or any platform)_

---

## 💾 Dataset Used

- **Source**: [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)
- A classic dataset used for learning classification and preprocessing.

---



---

## 🙋‍♂️ Author

**Karthik Ch**  
🔗 [GitHub Profile](https://github.com/karthikch014)

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and share.

---

## ⭐ Support

If you like this project, don't forget to **star ⭐** the repository. It encourages more such projects!

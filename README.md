# 🩺 AI Health Assistant

An intelligent, web-based Health Assistant that predicts potential diseases based on user-provided symptoms and suggests immediate medical precautions. Built with a robust 3-Tier Architecture using Python, Machine Learning, and Flask.

## 🚀 Features
- **Symptom Analysis:** Uses Natural Language Processing (NLP) techniques (CountVectorizer) to extract key medical terms from raw user input.
- **ML Prediction Engine:** Utilizes the Naive Bayes algorithm (MultinomialNB) trained on medical datasets to predict the most probable disease.
- **Actionable Advice:** Automatically fetches and displays recommended precautions and immediate next steps based on the predicted illness.
- **Interactive Web UI:** A clean, lightweight, and responsive frontend interface for seamless user interaction.

## 🛠️ Technology Stack
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Backend:** Python 3.x, Flask (REST API)
- **Machine Learning:** Scikit-Learn, Pandas, Joblib
- **Architecture:** 3-Tier Application Architecture (Presentation, Business Logic, Data Storage)

## ⚙️ How to Run Locally

Follow these steps to set up and run the project on your local machine:

**1. Clone the repository & Navigate to the directory**
```bash
git clone [https://github.com/your-username/AI_Health_Assistant.git](https://github.com/your-username/AI_Health_Assistant.git)
cd AI_Health_Assistant

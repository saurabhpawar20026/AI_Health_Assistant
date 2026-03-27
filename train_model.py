import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

print("Loading dataset...")
df = pd.read_csv('dataset.csv')

# Features and Labels
X = df['Symptoms']
y_disease = df['Disease']
y_precaution = df['Precaution']

# Create a machine learning pipeline (NLP + ML Model)
print("Training ML Model...")
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X, y_disease)

# Create a simple dictionary for precautions (Acting as Database)
precautions_db = dict(zip(df['Disease'], df['Precaution']))

# Save the trained model and database
joblib.dump(model, 'disease_model.pkl')
joblib.dump(precautions_db, 'precautions_db.pkl')

print("Model Trained and Saved Successfully!")
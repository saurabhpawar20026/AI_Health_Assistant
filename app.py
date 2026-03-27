from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load Trained Model and Database
try:
    model = joblib.load('disease_model.pkl')
    precautions_db = joblib.load('precautions_db.pkl')
except:
    print("Model not found. Please run train_model.py first.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_symptoms = data.get('symptoms', '')

    if not user_symptoms:
        return jsonify({'error': 'Please enter some symptoms.'})

    # Predict Disease
    predicted_disease = model.predict([user_symptoms])[0]
    
    # Fetch Precaution
    precaution = precautions_db.get(predicted_disease, "Consult a doctor for accurate advice.")

    return jsonify({
        'disease': predicted_disease,
        'precaution': precaution
    })

if __name__ == '__main__':
    app.run(debug=True)
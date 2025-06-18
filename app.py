from flask import Flask, request, render_template, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Inizializzazione Flask
app = Flask(__name__)

# Caricare il modello salvato
model_path = "spam_detection_model.joblib"
loaded_model = joblib.load(model_path)
loaded_classifier = loaded_model.named_steps['model']
loaded_tfidf_vectorizer = loaded_model.named_steps['tfidf']


# Homepage con input form
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint per la classificazione
@app.route('/classify', methods=['POST'])
def classify_email():
    email_text = request.form['email']
    email_vectorized = loaded_tfidf_vectorizer.transform([email_text])
    prediction = loaded_classifier.predict(email_vectorized)

    # Convertire predizione in Spam o Ham
    result = "Spam" if prediction[0] == 1 else "Ham"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

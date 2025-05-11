from flask import Flask, jsonify, request, render_template
from pipelines.feature_extractor import extract_features
from utils.logger import log_intrusion
from utils.threat_feed import enrich_with_threat_intel
import joblib
import os

app = Flask(__name__)

# Load the preprocessor and model
preprocessor, model = joblib.load('models/deep_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        packet = request.json
    else:
        packet = request.form.to_dict()

    # Extract raw features
    raw_features = extract_features(packet)
    print(f"Raw features: {raw_features}")
    print(f"Number of raw features: {len(raw_features)}")

    # Preprocess features to match the training pipeline
    processed_features = preprocessor.transform([raw_features])

    # Make prediction
    prediction = model.predict(processed_features)[0]
    
    alert = {
        "timestamp": packet.get("timestamp"),
        "summary": f"{'Threat' if prediction == 1 else 'Normal'} traffic detected."
    }

    if prediction == 1:
        enriched = enrich_with_threat_intel(packet)
        alert.update(enriched)
        log_intrusion(alert)

    return jsonify(alert)

if __name__ == '__main__':
    app.run(debug=True)

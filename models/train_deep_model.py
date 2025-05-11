import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load dataset
data = pd.read_csv('data/sample_netflow.csv')

# Preprocessing
X = data.drop(columns=['label'])
y = data['label']

categorical_columns = X.select_dtypes(include=['object']).columns
numeric_columns = X.select_dtypes(include=['int64', 'float64']).columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_columns),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
    ]
)

X_processed = preprocessor.fit_transform(X)
print(f"Number of features after preprocessing: {X_processed.shape[1]}")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the preprocessor and model together
joblib.dump((preprocessor, model), 'models/deep_model.pkl')
print("Model and preprocessor saved as 'models/deep_model.pkl'")

@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        packet = request.json
    else:
        packet = request.form.to_dict()

    # Extract raw features
    raw_features = extract_features(packet)

    # Wrap raw features in a DataFrame with the correct column names
    feature_columns = ['src', 'dst', 'proto', 'len']  # Replace with your actual column names
    raw_features_df = pd.DataFrame([raw_features], columns=feature_columns)

    # Preprocess features to match the training pipeline
    processed_features = preprocessor.transform(raw_features_df)

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

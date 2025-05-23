# Advanced Network Intrusion Detection System (NIDS)

## Overview

This project implements a Network Intrusion Detection System (NIDS) that uses machine learning to detect suspicious network activity. It captures live network packets, processes them, and classifies them as either normal or malicious traffic. The system is designed to provide real-time alerts and logging for detected intrusions.
# Features
Real-Time Packet Sniffing: Captures live network packets using the Scapy library and sends them to the Flask backend for analysis.
Machine Learning-Based Detection: Utilizes a trained Random Forest model to classify network traffic based on extracted features.
Threat Intelligence Enrichment: Enriches detected threats with additional information, such as known malicious IPs or protocols.
Logging: Logs all detected intrusions to a file (alerts.log) for monitoring and debugging purposes.
Web Interface: Provides a simple and clean web interface to display alerts and system status.
Extensibility: Modular design allows easy integration of additional features, such as new machine learning models or external threat intelligence feeds.
 
# Installation
Prerequisites
Python 3.8 or higher
pip (Python package manager)
Administrator/root privileges (required for packet sniffing)

# Steps
1 Clone the Repository.

2 Install Dependencies: Install all required Python packages:
pip install -r requirements.txt

3 Train the Machine Learning Model: Train the model using the provided dataset:
python models/train_deep_model.py

4 python models/train_deep_model.py
python app.py

5 Run the Packet Sniffer (Optional): If you want to capture live network packets, run the packet sniffer:
python pipelines/capture_sniffer.py
(Monitor the alerts displayed on the web interface)

# Technologies Used
Python: Core programming language for the project.
Flask: Web framework for the backend.
Scapy: Library for packet sniffing and network traffic analysis.
scikit-learn: Machine learning library for training and prediction.
pandas: Data manipulation and preprocessing.
joblib: Model serialization and deserialization.

# How It Works
## Packet Sniffing:

The capture_sniffer.py script captures live network packets using Scapy.
Each packet is converted into a JSON object and sent to the Flask app's /predict endpoint.

## Feature Extraction:

The feature_extractor.py script extracts relevant features (e.g., source IP, destination IP, protocol, packet length) from the packet data.
## Prediction:

The Flask app uses a pre-trained Random Forest model to classify the packet as either normal or malicious.
## Threat Intelligence Enrichment:

If a threat is detected, the threat_feed.py script enriches the alert with additional information (e.g., known malicious IPs).
## Logging:

Detected intrusions are logged to alerts.log for monitoring and debugging.

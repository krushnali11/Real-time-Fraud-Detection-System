 Real-time-Fraud-Detection-System
This project builds a real-time fraud detection system using Random Forest and Isolation Forest. It handles imbalanced data with SMOTE and uses feature scaling for accuracy. The system provides instant risk scoring via an interactive UI built with Streamlit.
# Real-Time Fraud Detection System

1. Overview
This project implements a real-time fraud detection system using a hybrid machine learning approach. It combines a Random Forest classifier to identify known fraud patterns with an Isolation Forest model to detect anomalous or previously unseen transaction behavior. The system generates a risk score for each transaction and enables instant evaluation through a simple web interface.

2. Features
- Fraud classification using Random Forest  
- Anomaly detection using Isolation Forest  
- SMOTE for handling imbalanced datasets  
- Real-time transaction scoring  
- Lightweight web interface built with Streamlit  

3. Tech Stack
Python, Scikit-learn, Pandas, NumPy, Streamlit

4. Project Structure
fraud-detection-system/  
├── app.py  
├── RealtimeFraudDetection.py  
├── rf_model.pkl  
├── iso_model.pkl  
├── scaler.pkl
└── README.md  

5.Setup and Usage
Install dependencies:
pip install -r requirements.txt

6.Run the application:
streamlit run app.py

7. Input Parameters
- Transaction amount  
- Time of day  
- Device score  
- Balance after transaction  

8. Output
- Fraud probability  
- Anomaly score  
- Final risk score  


The model is trained on simulated data with defined fraud patterns. It can be extended using real-world datasets for improved performance.

Krushnali Wasankarf

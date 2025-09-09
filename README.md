Symptoms-Based Disease Predictor

A Python-based machine learning application that predicts possible diseases based on user-input symptoms. It helps users identify potential health issues early and seek medical advice.



Features

🧠 Prediction System

Accepts multiple symptoms as input

Predicts the most likely disease

Provides probability scores for top predictions

Displays precautionary steps for predicted disease


📊 Visualizations

Symptom frequency distribution

Prediction confidence bar chart

Correlation between symptoms and diseases


🎯 Goal

Assist users in understanding possible illnesses quickly

Encourage early medical consultation and preventive care


Tech Stack

Language: Python

Data Handling: Pandas, NumPy

Machine Learning: Scikit-learn (Decision Tree, Random Forest, Naive Bayes)

Visualization: Matplotlib, Seaborn

Interface: Streamlit / Tkinter / Flask (choose based on project type)



Project Structure

DiseasePredictor/
│── data/
│   └── symptoms_dataset.csv
│── models/
│   └── trained_model.pkl
│── notebooks/
│   └── EDA.ipynb
│── app.py
│── requirements.txt
│── README.md


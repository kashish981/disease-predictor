
# app.py
import streamlit as st

# Preloaded symptom-to-disease dictionary
disease_symptoms = {
    "Common Cold": ["cough", "sore throat", "runny nose", "sneezing"],
    "Flu": ["fever", "chills", "muscle ache", "fatigue", "cough"],
    "COVID-19": ["fever", "dry cough", "loss of taste", "loss of smell", "shortness of breath"],
    "Malaria": ["fever", "chills", "sweating", "headache", "nausea"],
    "Diabetes": ["frequent urination", "increased thirst", "unexplained weight loss"],
    "Migraine": ["headache", "nausea", "sensitivity to light", "blurred vision"]
}

# All unique symptoms
all_symptoms = sorted(set(symptom for symptoms in disease_symptoms.values() for symptom in symptoms))


def predict_disease(user_symptoms):
    score = {}
    for disease, symptoms in disease_symptoms.items():
        d = set(symptoms).intersection(set(user_symptoms))
        score[disease] = len(d)

    sorted_diseases = sorted(score.items(), key=lambda x: x[1], reverse=True)
    best_match = sorted_diseases[0]

    if best_match[1] == 0:
        return "⚠️ No matching disease found. Please consult a doctor.", []
    else:
        top_diseases = [d for d, s in sorted_diseases if s == best_match[1]]
        return f"✅ Most likely disease(s): {', '.join(top_diseases)} (matched {best_match[1]} symptom(s))", top_diseases


# Streamlit UI
st.title("🩺 Symptom-Based Disease Predictor")

st.markdown("Enter your symptoms by selecting from the list below:")

selected_symptoms = st.multiselect("Select symptoms", all_symptoms)

if st.button("Predict Disease"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        result_text, possible_diseases = predict_disease(selected_symptoms)
        st.success(result_text)

        if possible_diseases:
            with st.expander("See matching diseases and symptoms"):
                for disease in possible_diseases:
                    st.write(f"**{disease}**")
                    st.write(f"Symptoms: {', '.join(disease_symptoms[disease])}")

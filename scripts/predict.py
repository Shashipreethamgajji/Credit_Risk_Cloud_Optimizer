import joblib
import pandas as pd

# Load models
credit_model = joblib.load("models/credit_risk_model.pkl")
cpu_model = joblib.load("models/cloud_cpu_hours_model.pkl")
storage_model = joblib.load("models/cloud_storage_gb_model.pkl")
cost_model = joblib.load("models/estimated_cost_model.pkl")

# Input new applicant data (manually or dynamically in Streamlit later)
new_applicant = {
    "age": 34,
    "annual_income": 52000,
    "loan_amount": 10000,
    "credit_history_length": 5,
    "previous_defaults": 1,
}

# Prepare dataframe
X_credit = pd.DataFrame([new_applicant])

# Predict risk label
risk_pred = credit_model.predict(X_credit)[0]
risk_map = {0: "Low", 1: "Medium", 2: "High"}
predicted_risk_label = risk_map.get(risk_pred, "Unknown")
print(f"\n🔎 Predicted Credit Risk: {predicted_risk_label}")

# Predict cloud usage based on credit score logic
credit_score = int((new_applicant["annual_income"] / 1000) +
                   (new_applicant["credit_history_length"] * 10) -
                   (new_applicant["previous_defaults"] * 50))
credit_score = min(850, max(300, credit_score))
risk_label_encoded = { "Low": 0, "Medium": 1, "High": 2 }.get(predicted_risk_label, 1)

X_cloud = pd.DataFrame([{
    "credit_score": credit_score,
    "risk_label_encoded": risk_label_encoded
}])

cpu = cpu_model.predict(X_cloud)[0]
storage = storage_model.predict(X_cloud)[0]
cost = cost_model.predict(X_cloud)[0]

# Output
print(f"\n🖥️  Predicted Cloud CPU Hours: {cpu:.2f}")
print(f"💾 Predicted Cloud Storage GB: {storage:.2f}")
print(f"💰 Predicted Estimated Cost: ${cost:.2f}")
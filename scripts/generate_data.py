import pandas as pd
import random
import uuid
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

def assign_resources(risk):
    if risk == "Low":
        return 0.5, 1.2
    elif risk == "Medium":
        return 1.5, 2.5
    else:
        return 3.0, 4.5

samples_per_class = 200
applications = []
cloud_usage = []

def generate_app(risk_label, credit_score_range):
    app_id = str(uuid.uuid4())
    age = random.randint(21, 65)
    income = random.randint(25000, 120000)
    loan_amt = random.randint(3000, 30000)
    credit_history_length = random.randint(1, 20)
    previous_defaults = random.randint(0, 3)
    employment_type = random.choice(["Salaried", "Self-Employed", "Unemployed"])

    # Assign fixed credit score based on risk
    credit_score = random.randint(*credit_score_range)

    cpu, storage = assign_resources(risk_label)
    estimated_cost = round(cpu * 0.2 + storage * 0.1, 2)

    applications.append({
        "application_id": app_id,
        "age": age,
        "annual_income": income,
        "loan_amount": loan_amt,
        "credit_history_length": credit_history_length,
        "previous_defaults": previous_defaults,
        "employment_type": employment_type,
        "credit_score": credit_score,
        "risk_label": risk_label
    })

    cloud_usage.append({
        "application_id": app_id,
        "credit_score": credit_score,
        "risk_label": risk_label,
        "cloud_cpu_hours": cpu,
        "cloud_storage_gb": storage,
        "estimated_cost": estimated_cost
    })

# Risk label and their credit score range
risk_ranges = {
    "Low": (700, 850),
    "Medium": (550, 699),
    "High": (300, 549)
}

for risk_label, score_range in risk_ranges.items():
    for _ in range(samples_per_class):
        generate_app(risk_label, score_range)

# Save CSVs
pd.DataFrame(applications).to_csv("data/synthetic_credit_data.csv", index=False)
pd.DataFrame(cloud_usage).to_csv("data/synthetic_cloud_usage.csv", index=False)

print("✅ Synthetic balanced data generated and saved to /data folder.")
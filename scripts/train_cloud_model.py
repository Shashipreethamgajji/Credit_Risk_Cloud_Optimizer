import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Load cloud usage data
df = pd.read_csv("data/synthetic_cloud_usage.csv")

# Encode risk label
df["risk_label_encoded"] = df["risk_label"].map({"Low": 0, "Medium": 1, "High": 2})

features = ["credit_score", "risk_label_encoded"]
targets = ["cloud_cpu_hours", "cloud_storage_gb", "estimated_cost"]

# Split features and targets
X = df[features]
results = {}

for target in targets:
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\n📊 Target: {target}")
    print(f"➡️  Mean Squared Error: {mse:.4f}")
    print(f"➡️  R² Score: {r2:.4f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, f"models/{target}_model.pkl")

    results[target] = {"mse": mse, "r2": r2}

print("\n✅ Cloud resource prediction models saved.")
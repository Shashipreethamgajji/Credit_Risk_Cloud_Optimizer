import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Load synthetic credit data
df = pd.read_csv("data/synthetic_credit_data.csv")

# Define features and target
features = ["age", "annual_income", "loan_amount", "credit_history_length", "previous_defaults"]
target = "risk_label"

# Encode target to numeric
df[target] = df[target].map({"Low": 0, "Medium": 1, "High": 2})

# Train-test split
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/credit_risk_model.pkl")

# Evaluate
y_pred = model.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
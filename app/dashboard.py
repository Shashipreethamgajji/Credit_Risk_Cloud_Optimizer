import streamlit as st
import joblib
import pandas as pd

# Load models
credit_model = joblib.load("models/credit_risk_model.pkl")
cpu_model = joblib.load("models/cloud_cpu_hours_model.pkl")
storage_model = joblib.load("models/cloud_storage_gb_model.pkl")
cost_model = joblib.load("models/estimated_cost_model.pkl")

# Styling
st.markdown("""
<style>
    .main {
        background-color: #f5f7fa;
        padding: 2rem;
    }
    .stMetric {
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("💳 Credit Risk & ☁️ Cloud Resource Optimizer")
st.subheader("Predict credit risk and estimate cloud usage & costs")
st.markdown("---")

# Sidebar inputs
st.sidebar.header("Input Parameters")

age = st.sidebar.slider("Age", 18, 70, 30)
annual_income = st.sidebar.number_input("Annual Income ($)", min_value=10000, max_value=200000, value=40000, step=1000)
loan_amount = st.sidebar.number_input("Loan Amount ($)", min_value=1000, max_value=100000, value=5000, step=1000)
credit_history_length = st.sidebar.slider("Credit History Length (years)", 0, 40, 5)
previous_defaults = st.sidebar.slider("Previous Defaults", 0, 10, 0)
employment_type = st.sidebar.selectbox("Employment Type", ["Salaried", "Self-Employed", "Unemployed"])

# New input required for cloud models
credit_score = st.sidebar.slider("Credit Score", 300, 850, 650)

# Map employment_type to numeric (not currently used in model)
employment_map = {"Salaried": 0, "Self-Employed": 1, "Unemployed": 2}
employment_num = employment_map[employment_type]

# Prepare input dataframe for credit risk model
input_credit = pd.DataFrame([{
    "age": age,
    "annual_income": annual_income,
    "loan_amount": loan_amount,
    "credit_history_length": credit_history_length,
    "previous_defaults": previous_defaults,
}])

# Predict Credit Risk
risk_pred_num = credit_model.predict(input_credit)[0]
risk_map_reverse = {0: "Low", 1: "Medium", 2: "High"}
risk_pred = risk_map_reverse[risk_pred_num]

# Prepare input dataframe for cloud resource models
input_cloud = pd.DataFrame([{
    "credit_score": credit_score,
    "risk_label_encoded": risk_pred_num
}])

# Optional: Debug info to verify inputs and model features
st.write("Input to credit risk model:")
st.write(input_credit)

st.write("Input to cloud resource models:")
st.write(input_cloud)

st.write("CPU model expects features:", cpu_model.feature_names_in_)

# Predict Cloud Resources
cpu_pred = cpu_model.predict(input_cloud)[0]
storage_pred = storage_model.predict(input_cloud)[0]
cost_pred = cost_model.predict(input_cloud)[0]

# Show predictions in metrics with colors
risk_color_map = {"Low": "green", "Medium": "orange", "High": "red"}

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"### Predicted Credit Risk\n<span style='color:{risk_color_map[risk_pred]}'>{risk_pred}</span>", unsafe_allow_html=True)
col2.metric("Cloud CPU Hours", f"{cpu_pred:.2f} hrs")
col3.metric("Cloud Storage (GB)", f"{storage_pred:.2f} GB")
col4.metric("Estimated Cloud Cost", f"${cost_pred:.2f}")

st.markdown("---")

# Bar chart visualization
usage_data = pd.DataFrame({
    "Resources": ["CPU Hours", "Storage (GB)", "Estimated Cost ($)"],
    "Values": [cpu_pred, storage_pred, cost_pred]
})

st.bar_chart(usage_data.set_index("Resources"))

# Additional info or notes
st.markdown("""
---
**Note:**  
This dashboard predicts credit risk category and estimates cloud resource usage and costs based on the input financial and credit parameters.  
Use the sidebar to adjust input parameters and see real-time predictions.
""")
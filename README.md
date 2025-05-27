# Credit Risk & Cloud Resource Optimizer

This Streamlit app predicts credit risk categories and estimates cloud resource usage (CPU hours, storage) and costs based on user inputs related to financial and credit parameters.

## 🔍 Features

- Predict credit risk (Low, Medium, High) based on age, income, loan amount, credit history, etc.
- Estimate cloud CPU hours, storage in GB, and overall cost.
- Interactive and responsive dashboard using Streamlit.
- Visual representation of predicted resource usage.

## 🗂️ Project Structure

```
Credit_Risk_Cloud_Optimizer/
│
├── app/
│   └── dashboard.py                # Main Streamlit dashboard
│
├── data/
│   ├── processed/                 # Processed data files
│   ├── raw/                       # Raw synthetic input data
│   ├── synthetic_cloud_usage/    # Synthetic cloud usage data
│   └── synthetic_credit_data/    # Synthetic credit risk data
│
├── diagrams/                      # Architecture and model diagrams
│
├── model/
│   └── train_credit_model.py      # Credit risk model training script
│
├── models/
│   ├── credit_risk_model.pkl      # Trained classification model
│   ├── cpu_model.pkl              # CPU usage regression model
│   └── storage_model.pkl          # Storage usage regression model
│
├── notebooks/                     # Jupyter notebooks (EDA, testing)
│
├── scripts/
│   ├── generate_data.py           # Synthetic data generator
│   ├── predict.py                 # Combined prediction script
│   ├── train_cloud_model.py       # Cloud resource model training
│   └── train_credit_model.py      # Credit model training script
│
├── venv/                          # Virtual environment files
│
├── .gitignore
├── README.md
└── requirements.txt
```

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Shashipreethamgajji/Credit_Risk_Cloud_Optimizer.git
cd Credit_Risk_Cloud_Optimizer

# (Optional) Create and activate virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
# source venv/bin/activate # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app/dashboard.py
```

## 🚀 Deployment

The app is live and hosted using [Streamlit Community Cloud](https://streamlit.io/cloud):

👉 [Launch App](https://creditriskcloudoptimizer-plmqsy5zssfwgmgmpb2wmm.streamlit.app/)

## 👤 Author

**Shashi Preetham Gajji**  
📧 shashipreethamgajji@gmail.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/shashi-preetham-g-69042614b)

## 📜 License

This project is licensed under the MIT License.
````
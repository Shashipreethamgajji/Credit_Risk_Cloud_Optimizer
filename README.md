# Credit Risk & Cloud Resource Optimizer

This Streamlit app predicts credit risk categories and estimates cloud resource usage (CPU hours, storage) and costs based on user inputs related to financial and credit parameters.

## Features

- Predict credit risk (Low, Medium, High) from user inputs such as age, income, loan amount, credit history, and previous defaults.
- Estimate cloud CPU hours, storage in GB, and total estimated cloud costs.
- Interactive dashboard with real-time updates using Streamlit.
- Bar chart visualization of predicted cloud resource usage.

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/<shashipreethamgajji>/Credit_Risk_Cloud_Optimizer.git
cd Credit_Risk_Cloud_Optimizer
````

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or on Windows
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app/dashboard.py
```

---

## Deployment

This app can be deployed easily on [Streamlit Community Cloud](https://share.streamlit.io).

---

## Project Structure

* `app/dashboard.py`: Main Streamlit dashboard app.
* `models/`: Pre-trained machine learning models.
* `train_credit_model.py`: Script to train the credit risk classification model.
* `train_cloud_model.py`: Script to train cloud resource regression models.
* `requirements.txt`: Python dependencies.
* `README.md`: Project documentation.

---

## Author

Shashi Preetham Gajji — (https://www.linkedin.com/in/shashi-preetham-g-69042614b)

---

## License

This project is licensed under the MIT License.

---

## Step 2: Push to GitHub

If you haven’t created a repo yet:

* Go to [https://github.com/new](https://github.com/new)
* Name your repo `Credit_Risk_Cloud_Optimizer`
* Make it public (or private if you want)
* Don’t initialize with README or .gitignore (we’ll add manually)

Then, in your project folder:

```bash
git init
git add .
git commit -m "Initial commit - Credit Risk & Cloud Resource Optimizer app"
git branch -M main
git remote add origin https://github.com/<your-username>/Credit_Risk_Cloud_Optimizer.git
git push -u origin main
```
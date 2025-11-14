# 📡 Telecom Customer Churn Prediction  
### End-to-End Data Engineering + Machine Learning + Streamlit Deployment

This project predicts telecom customer churn using SQL-based processing, Pandas data engineering, ML modeling, and a fully deployed Streamlit web app.  
The solution uses real-world style IBM Telco data spread across five relational tables.

---

## 🗂 Folder Structure
```text
telecom-churn-app/
├── streamlit_app.py               # Streamlit web UI for churn prediction
├── svm_model.pkl                  # Final trained SVM model (94.32% accuracy)
├── feature_columns.pkl            # One-hot encoded feature list
├── requirements.txt               # Dependencies for local execution
├── telecom_churn_analysis.ipynb   # Full notebook: SQL → EDA → ML → Insights
└── .gitignore
```

---

## 🚀 Project Overview
This end-to-end churn prediction system includes:

```text
✔ Loading & merging multiple Telco tables  
✔ SQL-based exploration & joins  
✔ Cleaning & feature engineering  
✔ One-hot encoding  
✔ Logistic Regression + SVM training  
✔ Final prediction pipeline  
✔ Feature importance extraction  
✔ Churn business insights  
✔ Streamlit deployment
```

Live App:  
👉 https://telecom-churn-analysis.streamlit.app/

---

## ⚡ Workflow
```text
Step 1: Load all Telco datasets  
Step 2: Inspect tables & define join keys  
Step 3: Clean column names & prepare SQL load  
Step 4: SQL joins + exploratory queries  
Step 5: Merge all tables in Pandas for ML  
Step 6: Data cleaning & feature engineering  
Step 7: Exploratory Data Analysis (EDA)  
Step 8: Encoding, train-test split & model training  
Step 9: Insights + business recommendations  
```

---

## 📥 Step 1 — Load All Telco Churn Tables
Imported 5 relational datasets:

```text
• Demographics  
• Location  
• Services  
• Status  
• Population
```

Verified shapes and CustomerID consistency.

---

## 🔑 Step 2 — Inspect Tables & Join Keys
Checked column names using:

```text
.columns  
PRAGMA table_info()  
SQL table listing
```

Join keys identified:

```text
• Main Key → CustomerID  
• Zip Mapping → Location.Zip_Code = Population.ZipCode
```

---

## 🧹 Step 3 — Clean Columns & Prepare SQL Load
Applied transformations:

```text
• Replace spaces with underscores  
• Lowercase standardization  
• Fixed: Zip_Code vs ZipCode  
• Yes/No → 1/0  
• Loaded all tables into a temporary SQLite DB
```

---

## 🗃 Step 4 — SQL Joins & SQL Analysis
Using SQL queries:

```text
• Joined all 5 tables  
• Previewed merged results  
• State-wise churn  
• Contract-wise average charges  
• Satisfaction score analysis  
• Churn distribution checks
```

Validated consistency before ML.

---

## 🧩 Step 5 — Merge All Tables for ML
```python
master_df = demographics \
    .merge(location, on="CustomerID") \
    .merge(services, on="CustomerID") \
    .merge(status, on="CustomerID") \
    .merge(population, left_on="Zip_Code", right_on="ZipCode", how="left")
```

Final shape: **7043 × 51**

---

## 🛠 Step 6 — Data Cleaning & Feature Engineering
```text
• One-hot encoded categorical variables  
• Converted pricing fields → numeric  
• Removed leakage columns:  
    Churn_Reason, Churn_Category, Customer_Status  
    Quarter_x, Quarter_y  
• Ensured no missing values  
```

Dataset is ML-ready.

---

## 📊 Step 7 — Exploratory Data Analysis (EDA)
Key findings:

```text
• Churn Rate = 26.5%  
• Satisfaction score strongest churn link  
• Month-to-month contracts churn the most  
• Higher data usage → lower churn  
• California had highest churn  
```

Plotted churn counts, contract churn, revenue patterns, satisfaction trends.

---

## 🤖 Step 8 — Encoding, Train-Test Split & Model Training

**Feature Prep**
```text
• One-hot encoding  
• Train-test split (80/20)  
• StandardScaler inside SVM pipeline
```

### Models Trained
```text
1) Logistic Regression (Baseline)
   Accuracy = 83%

2) Linear SVM (Final Model)
   Accuracy  = 94.32%
   Precision = 0.889
   Recall    = 0.898
   F1 Score  = 0.894
```

Saved as:

```text
svm_model.pkl
feature_columns.pkl
```

---

## 🏆 Step 9 — Final Insights & Business Recommendations

### 📌 Top Features Driving Churn
```text
1. Satisfaction Score  
2. Number of Referrals  
3. Tenure in Months  
4. Online Security  
5. Dependents  
6. Contract Type  
7. Avg Monthly GB Download  
8. Unlimited Data  
9. Married  
10. Monthly Charge  
11. Streaming Services  
12. Internet Type  
```

### 📊 Business Insights
```text
• Low satisfaction → major churn driver  
• New customers (<12 months) churn more  
• 2-year contracts have lowest churn  
• Bundled services reduce churn  
• High monthly charges increase churn  
• Heavy internet users churn less  
```

### 🎯 Recommended Actions
```text
1) Improve customer satisfaction programs  
2) Promote long-term contracts with discounts  
3) Bundle services (Security + Streaming + Internet)  
4) Engage new customers in first 90 days  
5) Reduce price shock with flexible plans  
6) Increase referral rewards  
```

---

## 🌐 Streamlit App
Interactive churn predictor built with:

```text
• SVM model  
• Live UI for telecom customer attributes  
• Real-time prediction output
```

Run locally:
```bash
streamlit run streamlit_app.py
```

---

## 📦 Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yasaswini2004/telecom-churn-app.git
cd telecom-churn-app
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Launch Streamlit App
```bash
streamlit run streamlit_app.py
```

---

## 📝 Final Notes
This project demonstrates:

```text
• Multi-table SQL + Pandas data engineering  
• Full ML workflow (EDA → Modeling → Evaluation)  
• Feature importance insights  
• Business-focused churn interpretation  
• Deployed Streamlit application
```

Perfect for:

```text
• Data Science portfolios  
• ML Engineering interviews  
• End-to-end real-world demonstrations
```

---

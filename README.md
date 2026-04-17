# 📊 Customer Churn Analysis

## 📌 Problem Statement
Customer churn is a major challenge for businesses. Identifying why customers leave helps improve retention strategies and reduce revenue loss.

---

## 📂 Dataset
- 7043 customer records  
- Features include:
  - Demographics (gender, senior citizen)
  - Account details (tenure, contract type)
  - Services (internet, security, streaming)
  - Billing (payment method, monthly charges)

---

## 🛠 Tech Stack
- Python (Pandas, NumPy)
- Data Visualization (Matplotlib, Seaborn)

---

## 🔍 Data Preprocessing
- Converted `TotalCharges` to numeric (handled missing values)
- Checked for duplicates and null values
- Transformed categorical variables (e.g., SeniorCitizen)

---

## 📊 Key Insights

### 1. Churn Distribution
- ~26.5% customers churned :contentReference[oaicite:1]{index=1}  
- Majority of customers stayed

### 2. Tenure Impact
- Customers with **low tenure (1–2 months)** have high churn  
- Long-term customers are more likely to stay :contentReference[oaicite:2]{index=2}  

### 3. Contract Type
- **Month-to-month customers churn more**
- Long-term contracts (1–2 years) have lower churn :contentReference[oaicite:3]{index=3}  

### 4. Services Impact
- Customers without:
  - Online Security  
  - Tech Support  
👉 More likely to churn :contentReference[oaicite:4]{index=4}  

### 5. Payment Method
- Customers using **Electronic Check** have higher churn :contentReference[oaicite:5]{index=5}  

---

## 📈 Visualizations
(Add screenshots here)

- Churn distribution chart  
- Churn by tenure  
- Churn by contract  
- Service-based churn analysis  

---

## 💡 Business Recommendations

- Offer discounts for long-term contracts  
- Improve onboarding experience for new customers  
- Promote value-added services (security, support)  
- Encourage automatic payment methods  

---

## 🚀 How to Run

```bash
pip install pandas numpy matplotlib seaborn
python churn_analysis.py

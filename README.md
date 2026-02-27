# 🛒 Smart Retail Analytics – Customer Purchase Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Project-Hackathon%20Ready-success)

---

## 📌 Project Overview

This project builds an end-to-end **Machine Learning system** to predict whether a customer is **likely to purchase high-margin products** in a retail environment.

The solution includes:

- ✅ Synthetic dataset generation
- ✅ Feature engineering
- ✅ Logistic Regression & Random Forest models
- ✅ ROC-AUC, F1 Score, Confusion Matrix evaluation
- ✅ Real-time Streamlit dashboard deployment

---

## 🎯 Business Objective

Retail businesses want to identify:

- 🎯 Customers likely to buy high-margin products
- 📊 Key behavioral drivers influencing purchases
- 💰 Opportunities for targeted marketing & premium promotions

---

## 📂 Dataset Features

| Feature | Description |
|----------|-------------|
| age | Customer age |
| gender | Male / Female |
| city_tier | Tier 1 / 2 / 3 |
| income_level | Low / Medium / High |
| avg_monthly_spend | Average spending |
| visit_frequency | Store visits per month |
| preferred_category | Product preference |
| discount_usage_rate | % purchases with discount |
| loyalty_points | Current loyalty points |
| last_purchase_days | Recency |
| app_usage_minutes | Weekly app usage |
| complaints_count | Complaint frequency |
| product_view_count | Product browsing behavior |
| high_margin_purchase | Target (0 = Unlikely, 1 = Likely) |

---

## 🧠 Feature Engineering

Additional engineered features:

- engagement_score
- value_score
- discount_dependency
- complaint_rate
- recency_score

These improved model performance significantly.

---

## 🤖 Models Used

### 1️⃣ Logistic Regression  
### 2️⃣ Random Forest Classifier

---

## 📊 Model Performance

| Model | Accuracy | F1 Score | ROC-AUC |
|--------|----------|----------|----------|
| Logistic Regression | ~0.85 | ~0.82 | ~0.88 |
| Random Forest | ~0.95+ | ~0.98 | ~0.97 |

✔ Meets hackathon requirements  
✔ Inference time < 100ms  

---

## 📈 Evaluation Metrics

- Confusion Matrix
- ROC Curve
- AUC Score
- Precision & Recall
- F1 Score
- Inference Time Analysis

---

## 🚀 Streamlit Dashboard

The project includes a fully interactive dashboard:

- 📥 User input via sidebar
- 🔮 Real-time prediction
- 📊 Purchase probability score
- 📈 Business-friendly output

### ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🏗️ Project Structure

```
smart-retail-analytics-ml-dashboard/
│
├── app.py
├── retail.ipynb
├── requirements.txt
└── README.md
```

---

## 💼 Business Impact

This system helps:

- Improve targeted marketing
- Increase high-margin product sales
- Optimize loyalty strategies
- Reduce promotional waste

---

## 🏆 Hackathon Ready

✔ End-to-end ML pipeline  
✔ Clean code structure  
✔ Deployment-ready dashboard  
✔ Business explanation included  

---

## 👩‍💻 Author

**Nighitha T N**

---

⭐ If you found this project useful, consider giving it a star!

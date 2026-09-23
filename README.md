<div align="center">

# 📊 Customer Churn Analysis & Prediction

<img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
<img src="https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />

<p align="center">
  <b>An end-to-end exploratory data analysis, relational database storage, and insight extraction pipeline for subscription-based customer retention.</b>
</p>

</div>

---

## 🚀 About the Project
Understanding why customers leave is critical for any subscription service. This project analyzes a dataset of **1,500 customer records** across 23 distinct behavioral, demographic, and financial metrics[cite: 1]. The goal is to uncover primary drivers behind customer churn, evaluate subscription plan performance, and provide data-driven recommendations to improve retention.

---

## 📈 Dataset Overview
The dataset contains structured customer information covering demographics, engagement metrics, and account statuses.

* **Total Records:** 1,500 customers[cite: 1]
* **Total Features:** 23 attributes (including demographics, watch behavior, support interactions, and churn indicators)
* **Overall Churn Rate:** ~13.93% (209 churned vs. 1,291 active customers)

### Key Dataset Features
<details>
<summary><b>Click to expand column descriptions</b></summary>

| Category | Column Name | Description |
| :--- | :--- | :--- |
| **Demographics** | `Customer_ID`, `Age`, `Gender`, `Country` | Basic user identity and location data. |
| **Account Info** | `Account_Creation_Date`, `Subscription_Plan`, `Monthly_Charges`, `Payment_Method` | Billing and plan tier configurations. |
| **Engagement** | `Average_Watch_Hours_Per_Week`, `Login_Frequency_Per_Week`, `Devices_Registered` | Platform activity and consumption metrics. |
| **Support & Issues** | `Customer_Support_Calls`, `Streaming_Quality_Issues`, `Days_Since_Last_Login` | Friction points and user inactivity trackers. |
| **Target Variables** | `Churn_Status`, `Churn_Flag`, `Churn_Reason` | Binary and categorical labels denoting customer defection. |

</details>

---

## 📊 Key Findings & Insights

* **Plan Churn Disparity:** While Standard and Basic plans command the bulk of the user base, the **Premium subscription tier experienced the highest churn rate at 19.16%**, signaling potential value-proposition or pricing expectation gaps for high-tier users[cite: 1].
* **Primary Churn Motivations:** Among users who specified a reason for leaving, financial constraints (**"Too expensive"**) and technical frustrations were among the top drivers[cite: 1].
* **Engagement Indicators:** Churned users exhibited lower login frequencies and increased gaps (`Days_Since_Last_Login`), offering a clear behavioral early-warning indicator for the customer success team[cite: 1].

---

## 🛠️ Built With
* **Python** — Core programming language for data processing
* **Pandas & NumPy** — Data cleaning, slicing, and statistical aggregation
* **MySQL** — Relational database management and exploratory queries
* **Matplotlib & Seaborn** — Data visualization and exploratory plotting

---

## 🗄️ Database & SQL Analysis
The project includes a structured MySQL schema (`churn_project.sql`) used to run analytical queries to uncover metrics like churn rates per plan, regional distribution, and activity group breakdowns. 

```sql
-- Example snippet from churn_project.sql: Calculating churn rate by subscription plan
SELECT
    Subscription_Plan,
    COUNT(*) AS total_customers,
    SUM(Churn_Status = 'Churned') AS churned_customers,
    ROUND(
        SUM(Churn_Status = 'Churned') / COUNT(*) * 100,
        2
    ) AS churn_rate_percent
FROM customer_churn
GROUP BY Subscription_Plan
ORDER BY churn_rate_percent DESC;

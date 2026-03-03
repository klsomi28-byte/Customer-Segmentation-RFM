
# Customer Segmentation and RFM Analysis

## Project Overview
This project performs **Customer Segmentation** using the **RFM (Recency, Frequency, Monetary) model** on e-commerce transactional data. It integrates **Python**, **MySQL**, and **Power BI** to process data, calculate RFM scores, and create a visual dashboard for business insights.

The main goals of this project are:

- Clean and preprocess customer, orders, and payment data.
- Store and manage data in **MySQL** database.
- Calculate **RFM metrics** for each customer.
- Generate **RFM scores** (1–5) to segment customers.
- Visualize insights using **Power BI** dashboard.



## Repository Structure
Customer-Segmentation-RFM/
│
├── code/
│ ├── data_cleaning_upload.py # Python script to clean CSVs and upload to MySQL
│ └── rfm_analysis.py # Python script to calculate RFM and scores
│
├── output/
│ ├── rfm_final_output.csv # RFM metrics per customer
│ ├── rfm_final_output_with_scores.csv # RFM metrics with scores
│ └── customer_seg.pbix # Power BI dashboard
│
└── README.md


## Files Description

1. **Python Scripts (`code/`)**
   - `data_cleaning_upload.py` – Loads CSVs, cleans data, uploads to MySQL.
   - `rfm_analysis.py` – Merges tables, calculates RFM metrics, and exports results.

2. **Output Files (`output/`)**
   - `rfm_final_output.csv` – Contains customer-wise **Recency**, **Frequency**, and **Monetary** values.
   - `rfm_final_output_with_scores.csv` – RFM metrics along with **RFM scores (1–5)** and combined **RFM Score**.
   - `customer_seg.pbix` – **Power BI dashboard** showing visualizations for RFM analysis.


## Steps to Run

1. **Python Environment**
   - Install required packages:
     ```bash
     pip install pandas sqlalchemy mysql-connector-python
     ```
   - Run `data_cleaning_upload.py` to load and upload CSV data to MySQL.
   - Run `rfm_analysis.py` to calculate RFM metrics and export CSV files.

2. **MySQL Database**
   - Create a database `project1_db`.
   - Ensure Python scripts have the correct MySQL username, password, and database name.

3. **Power BI Dashboard**
   - Open `customer_seg.pbix` in Power BI Desktop.
   - Use the dashboard to explore customer segmentation insights:
     - RFM distribution
     - Top customers by revenue
     - Segmentation by RFM score

## RFM Model Explanation

| Metric    | Meaning                        |
|-----------|--------------------------------|
| Recency   | Days since last purchase       |
| Frequency | Number of purchases            |
| Monetary  | Total money spent by customer |

RFM scores (1–5) help identify:
- **High-Value Customers** – frequent, recent, high spenders.
- **Churn Risk Customers** – not recent, low frequency.



## Key Insights

- Total Revenue: *calculated from RFM output CSV*
- Total Customers Analyzed: *from RFM CSV count*
- Segmentation enables targeted marketing and business strategy planning.



## Author

**Sanjana K L** – Data Analytics Enthusiast  
Project done as part of **Customer Segmentation & RFM Analysis**  

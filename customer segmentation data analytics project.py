import pandas as pd
from sqlalchemy import create_engine
import urllib

# Encode password properly
password = urllib.parse.quote_plus("Somi@2005")

engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost:3306/project1_db")

print("Connected Successfully ")

# ---------------------------
# Load FULL CSV Files (Desktop Path)
# ---------------------------

customers = pd.read_csv(r"C:\Users\Dell\Desktop\Olist data ana project\olist_customers_dataset.csv")
orders = pd.read_csv(r"C:\Users\Dell\Desktop\Olist data ana project\olist_orders_dataset.csv")
payments = pd.read_csv(r"C:\Users\Dell\Desktop\Olist data ana project\olist_order_payments_dataset.csv")

print("CSV Loaded Successfully ")

# ---------------------------
# Upload to MySQL
# ---------------------------
customers.to_sql("customers", engine, if_exists="replace", index=False)
print("Customers Uploaded")

orders.to_sql("orders", engine, if_exists="replace", index=False)
print("Orders Uploaded")

payments.to_sql("payments", engine, if_exists="replace", index=False)
print("Payments Uploaded")

print("All Tables Imported Successfully ")


# -----------------------------
# Load Required Tables
# -----------------------------
orders = pd.read_sql("""
SELECT order_id, customer_id, order_purchase_timestamp 
FROM orders
""", engine)

customers = pd.read_sql("""
SELECT customer_id, customer_unique_id 
FROM customers
""", engine)

payments = pd.read_sql("""
SELECT order_id, payment_value 
FROM payments
""", engine)

print("Orders:", len(orders))
print("Customers:", len(customers))
print("Payments:", len(payments))

# -----------------------------
# Merge Tables
# -----------------------------
df = pd.merge(orders, customers, on="customer_id", how="inner")
df = pd.merge(df, payments, on="order_id", how="inner")

print("Rows after merge:", len(df))
print("Total Payment Sum:", df["payment_value"].sum())

# -----------------------------
# Convert Date Column
# -----------------------------
df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

# -----------------------------
# Calculate RFM
# -----------------------------
max_date = df["order_purchase_timestamp"].max()

rfm = df.groupby("customer_unique_id").agg({
    "order_purchase_timestamp": lambda x: (max_date - x.max()).days,
    "order_id": "count",
    "payment_value": "sum"
}).reset_index()

rfm.columns = ["customer_unique_id", "Recency", "Frequency", "Monetary"]




print("\nRFM Preview:")
print(rfm.head())

print("Total Revenue (Final Check):", rfm["Monetary"].sum())

# -----------------------------
# Export to CSV
# -----------------------------
rfm.to_csv("rfm_final_output.csv", index=False)
print("RFM File Exported Successfully ")

# -----------------------------
# Create RFM Scores (1-5)
# -----------------------------

rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5,4,3,2,1])
rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1,2,3,4,5])

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)


print("\nRFM Score Preview:")
print(rfm.head())

rfm.to_csv("rfm_final_output_with_scores.csv", index=False)
print("Final RFM with Scores Exported ")

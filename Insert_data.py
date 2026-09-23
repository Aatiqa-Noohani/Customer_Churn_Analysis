import pandas as pd
import mysql.connector

# -----------------------------------
# 1. Load CSV
# -----------------------------------

df = pd.read_csv("customer_churn.csv")

print("CSV loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# -----------------------------------
# 2. Connect to MySQL
# -----------------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aatiqa786",
    database="ott_churn_db"
)

cursor = conn.cursor()

print("Connected to MySQL!")


# -----------------------------------
# 3. Replace missing values with None
# -----------------------------------

df = df.where(pd.notnull(df), None)


# -----------------------------------
# 4. INSERT query
# -----------------------------------

insert_query = """
INSERT INTO customer_churn (
    Customer_ID,
    Age,
    Gender,
    Region,
    Account_Creation_Date,
    Subscription_Plan,
    Monthly_Charges,
    Payment_Method,
    Auto_Renewal,
    Contract_Length,
    Average_Watch_Hours_Per_Week,
    Favorite_Genre,
    Devices_Registered,
    Login_Frequency_Per_Week,
    Download_For_Offline_Count,
    Customer_Support_Calls,
    Streaming_Quality_Issues,
    Days_Since_Last_Login,
    Churn_Status,
    Churn_Reason
)
VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s
)
"""


# -----------------------------------
# 5. Convert DataFrame to tuples
# -----------------------------------

data = [
    tuple(row)
    for row in df.itertuples(index=False, name=None)
]

print("Values per row:", len(data[0]))


# -----------------------------------
# 6. Insert data
# -----------------------------------

cursor.executemany(insert_query, data)

conn.commit()

print("Data inserted successfully!")
print("Rows inserted:", cursor.rowcount)


# -----------------------------------
# 7. Close connection
# -----------------------------------

cursor.close()
conn.close()

print("MySQL connection closed.")



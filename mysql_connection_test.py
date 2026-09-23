import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aatiqa786",
        database="ott_churn"
    )

    print("MySQL connection successful! ✅")

    connection.close()

except mysql.connector.Error as e:
    print("MySQL connection failed ❌")
    print("Error:", e)
import mysql.connector

# 
bank_dtb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="efgh8041@"
    )
bank_cursor = bank_dtb.cursor()


bank_cursor.execute("create database mydatabase")
bank_dtb.commit()
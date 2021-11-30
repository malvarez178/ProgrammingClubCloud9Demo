import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.csf1wtezlwz9.us-west-1.rds.amazonaws.com",
  user="admin",
  password="password",
  port='3306'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE crud2")

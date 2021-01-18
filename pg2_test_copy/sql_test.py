import mysql.connector

mydb = mysql.connector.connect(database='postgres', user='postgres',password='password')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
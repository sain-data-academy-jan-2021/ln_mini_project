import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="test"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM person")

for x in mycursor:
  print(x)


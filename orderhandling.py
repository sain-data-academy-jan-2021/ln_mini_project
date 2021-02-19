import pymysql
from dotenv import load_dotenv
import os

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
  host,
  user,
  password,
  database
)
cursor = connection.cursor()


def print_orders_from_db():
    cursor = connection.cursor()
    cursor.execute( f'SELECT * FROM Orders')
    rows = cursor.fetchall()
    for row in rows:
        print(f'Order ID: {str(row[0])}, Status: {row[1]}, Courier: {row[2]}, Email: {row[3]}, Address: {row[4]}, Phone: {row[5]}, Items: {row[6]}, Total Cost: {row[7]}')
    cursor.close()



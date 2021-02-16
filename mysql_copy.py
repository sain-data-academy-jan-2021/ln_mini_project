import pymysql
import os
from dotenv import load_dotenv

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
)#up to here put in project


# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# # Execute SQL query
# cursor.execute( 'SELECT * FROM Couriers')

def print_all(table):
  cursor = connection.cursor()
  cursor.execute( f'SELECT * FROM {table}')
  rows = cursor.fetchall()
  if table == 'Couriers':
    for row in rows:
      print(f'Courier ID: {str(row[0])}, Courier Name: {row[1]}, Delivery Method: {row[2]}, Contact number: {row[3]}')
  if table == 'Products':
    for row in rows:
      print(f'Product ID: {str(row[0])}, Product Name: {row[1]}, Product Type: {row[2]}, Unit: {row[3]}, Price: {row[4]}')

  cursor.close()

def add_entry (table):
  #print each from database
  if table == 'Products':
    add_type = input(f'What type of item would you like to add to {table}? Press 1 for Drinks or 2 for Food')
    if add_type == '1':
      add_type = 'Drinks'
    if add_type == '2':
      add_type = 'Food'
    new_item = input(f'What item would you like to add to our {add_type} database?').title()
    new_item_cost = float(input(f'How much does a unit of {new_item} cost?'))
    new_unit = str(input(f'What is the quanity of a single unit of {new_item}. Include units'))
    cursor = connection.cursor()
    cursor.execute(F'INSERT INTO {table} (prod_name, prod_type, unit, price) VALUES ("{new_item}","{add_type}","{new_unit}",{new_item_cost})')

  if table == "Couriers":
    add_person = str(input(f'Who would you to add to {table}?')).title()
    delivery = str(input(f'What is {add_person}\'s prefered mode of delivery')).upper()
    add_numb = input(f'What phone number can {add_person} be reached on')
    if len(add_numb) == 11:
      cursor = connection.cursor()
      cursor.execute(f'INSERT INTO {table} (courier_name, delivery_method, contact_number) VALUES ("{add_person}","{delivery}","{add_numb}")')
    else: 
      print('Error. Phone numbers must be 11 digits. Please try again ')

  print(cursor.rowcount, "record inserted. New ID:",cursor.lastrowid)

  cursor.close()
  connection.commit() #need both when altering database 

def delete_entry(table, item_type, column): #item_type = product/item
  #print table

  delete_item = str(input(f'Which {item_type} would you like to delete from {table}?')).title()

  cursor = connection.cursor()
  cursor.execute(f'DELETE FROM {table} WHERE {column} = "{delete_item}"')

  print(cursor.rowcount, "record(s) deleted")

  cursor.close()
  connection.commit()

def update_entry(table, item_type, column1, column2): #table, item_type
    
    old_item = input(f'Which {item_type} from {table} do you want to update').title()
    update = input(f'What do you want to update {old_item} to?').title()

    cursor = connection.cursor()
    cursor.execute(f'UPDATE {table} SET {column1} = "{update}" WHERE {column2} = "{old_item}"')
    print(cursor.rowcount, "record(s) affected")
    print(f'Kindly update the properties of {update}')

    if table == 'Products':
      update1 = str(input(f'Press 1 if {update} is classed as a food, press 2 if {update} is classed as a drink.'))
      if update1 == '1':
        cursor.execute(f'UPDATE {table} SET prod_type = "Food" WHERE {column1} = "{update}"')
      if update1 == '2':
        cursor.execute(f'UPDATE {table} SET prod_type = "Drink" WHERE {column1} = "{update}"')

      update2 = input(f'What is the quanity of a single unit of {update}. Include unit measurements')
      cursor.execute(f'UPDATE {table} SET unit = "{update2}" WHERE {column1} = "{update}"')

      update3 = float(input(f'What is the cost of {update}'))
      cursor.execute(f'UPDATE {table} SET price = "{update3}" WHERE {column1} = "{update}"')

    
      cursor.execute(f'SELECT prod_name,prod_type,unit,price FROM {table} WHERE {column1} = "{update}"')
      newentry = cursor.fetchall()
      for x in newentry:
        print(f'New complete updated entry\n {x}')
    
    if table == 'Couriers':
      update1 = str(input(f'What is {update}\'s prefered delivered method'))
      cursor.execute(f'UPDATE {table} SET delivery_method = "{update1}" WHERE {column1} = "{update}"')

      update2 = str(input(f'What is {update}\'s mobile number'))
      cursor.execute(f'UPDATE {table} SET contact_number = "{update2}" WHERE {column1} = "{update}"')

      cursor.execute(f'SELECT * FROM {table} WHERE {column1} = "{update}"')
      newentry = cursor.fetchall()
      for x in newentry:
        print(f'New complete updated entry:\n {x}')

    cursor.close()
    connection.commit()

connection.close() #use when exiting app/ or press 0 to exit 

print_all('Products')
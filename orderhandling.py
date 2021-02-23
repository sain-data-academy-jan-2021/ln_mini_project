import pymysql
from dotenv import load_dotenv
import os
from tabulate import tabulate
from funcs_prod_courier import *

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

def execute_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()

def execute_sql_select(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall()

def choose_order(connection):
    print_food_db()
    chosen_product_ids = []
    existing_ids = [id[0] for id in execute_sql_select(connection, 'SELECT product_id FROM Products')]
    while True:
        id = input('Please choose products to order. When you have chosen all press 0:')
        quanity = input()
        if int(id) == 0:
            break
        elif int(id) not in existing_ids: 
            print('Invalid ID')
            continue 
        chosen_product_ids.append(id)
    return (chosen_product_ids)


def print_orders_from_db(connection):
    cursor = connection.cursor()
    cursor.execute( f'SELECT * FROM Orders')
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Order ID', 'Status','Courier','Email', 'Address','Phone', 'Items Purchased', 'Total Cost'], tablefmt='psql'))

def delete_order_in_db(connection):
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from Orders')]
    while True:
        print_orders_from_db(connection)
        id = int(input("What order would you like to delete from the list above?"))
        if id in existing_ids:
            execute_sql(connection, f'DELETE from Order_product where order_id = {id}')
            execute_sql(connection, f'DELETE from orders where order_id = {id}')
            break  
        else:
            print("This option is invalid")

def update_order_details(connection):
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from Orders')]
    chosen_products = [id[0] for id in execute_sql_select(connection, 'select product_id from products')]
    while True:
        print_orders_from_db(connection)
        id = int(input("What order would you like to update from the list above?"))
        if id in existing_ids:
            updated_order_name = input("Please enter the updated name")
            updated_order_address = input("Please eneter the updated address")
            updated_phone = input("Please enter the updated phone number")

            print_couriers_from_db()
            updated_courier = input("Please enter an updated courier from the list above")
            updated_status = input("Please enter the updated status of the order")
            execute_sql(connection, f'UPDATE orders SET name = "{updated_order_name}", address = "{updated_order_address}", phone = "{updated_phone}", courier = "{updated_courier}", status = "{updated_status}"')
            print_products__from_db()
            break
    for row in execute_sql_select(connection, 'SELECT product_id FROM Order_product'):
        existing_ids.append(row[0])
    while True:
        updated_items = int(input("Please enter the new items you would like to add to the order, Press 0 to continue"))
        if updated_items in chosen_products:
            chosen_products.append(updated_items)
            execute_sql(connection, f'UPDATE Order_product SET product_id = {updated_items} WHERE order_id = {id}')
            continue
        elif updated_items == 0:
            break


def add_order_database(connection):
    name = input('Please enter your full name for the order \n').capitalize()
    email = input('Please enter your email address\n')
    address = input('Please enter a delivery address \n')
    phone = input('Enter your phone number \n')
    courier = add_courier_to_order(connection)
    items = choose_order(connection)
    execute_sql(connection, f"insert into orders (name, email, address, phone, courier_id) values ('{name}', '{email}','{address}', '{phone}',{courier}")
    order_id = execute_sql_select(connection, 'SELECT max(order_id) from orders')[0][0]
    for item in items:
        execute_sql(connection, f"insert into Order_product (order_id, product_id) values ({order_id}, {item})")

def update_order_status_in_db(connection):
    print_orders_from_db(connection)
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from orders')]
    while True:
        id = int(input("Which order's status would you like to update?"))
        if id in existing_ids:
            updated_order_status = input("What is the new status of this order?")
            execute_sql(connection, f'UPDATE orders SET status = "{updated_order_status}"')
            break

def add_courier_to_order(connection):
    print_couriers_from_db()
    existing_ids = []
    for row in execute_sql_select(connection, 'SELECT courier_id FROM Couriers'):
        existing_ids.append(row[0])
    while True: 
        pick_courier = int(input("What courier would you like to choose?"))
        if pick_courier in existing_ids:
            return pick_courier
        else:
            continue

add_courier_to_order(connection)
=======

def update_order_status_in_db(connection):
    print_orders_from_db(connection)
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from orders')]
    while True:
        id = int(input("Which order's status would you like to update?"))
        if id in existing_ids:
            updated_order_status = input("What is the new status of this order?")
            execute_sql(connection, f'UPDATE orders SET status = "{updated_order_status}"')
            break

def add_courier_to_order(connection):
    print_couriers_from_db()
    existing_ids = []
    for row in execute_sql_select(connection, 'SELECT courier_id FROM couriers'):
        existing_ids.append(row[0])
    while True: 
        pick_courier = int(input("What courier would you like to choose?"))
        if pick_courier in existing_ids:
            return pick_courier
        else:
            continue

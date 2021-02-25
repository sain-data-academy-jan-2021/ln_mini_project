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

#-------------------------------------------------
def execute_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()
#-------------------------------------------------
def execute_sql_select(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall()
#-------------------------------------------------
def choose_order_items(connection): 

    print_whole_table("Products","prod_type")

    existing_ids = [id[0] for id in execute_sql_select(connection,'SELECT product_id FROM Products')]
    chosen_products_ids = []

    id = ''

    total_cost = 0
    final_basket = []
    while id !=0:
        id = int(input('Please choose the ID to order. When you have chosen all press 0:'))
        
        if id not in existing_ids and id !=0: 
            print('Invalid ID. Please try again')

        elif id in existing_ids:
            quantity = int(input('How many do you want')) 
            cursor.execute(f'SELECT (prod_name, unit, price) FROM Products where product_id = "{id}"')
            myresult = cursor.fetchall()
            for x in myresult:
                basket = (f'Product: {x[0]}, Unit: {x[1]}, Quantity: {quantity}, Price: {x[2]* quantity}')

                price = x[2] * quantity

            total_cost = total_cost + price
            chosen_products_ids.extend([id] * quantity )
            final_basket.append(basket)

   
    print('Order Summary:') 
    for x in final_basket: 
        print(x)      
    print(f'Your order costs £{total_cost}')      
    return (chosen_products_ids)
    return total_cost
        
#------------------------------------------------- 
def add_to_order_product(connection):
    cursor = connection.cursor()
    order_id = execute_sql_select(connection,'SELECT MAX(order_id) FROM Orders')[0][0]
    chosen_products_ids = choose_order_items(connection)
    for product_id in chosen_products_ids:
        execute_sql(connection, f'INSERT INTO Order_product (order_id, product_id) VALUES ({order_id}, {product_id})')
    cursor.close()
    connection.commit()
#------------------------------------------------- 
def print_orders_from_db(connection):
    cursor = connection.cursor()
    cursor.execute( f'SELECT * FROM Orders')
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Order ID', 'Status','Courier','Email', 'Address','Phone', 'Items Purchased', 'Total Cost'], tablefmt='psql'))
#-------------------------------------------------
def delete_order_in_db(connection):
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from Orders')]
    while True:
        print_orders_from_db(connection)
        id = int(input("What order would you like to delete from the list above? Select an order ID"))
        if id in existing_ids:
            execute_sql(connection, f'DELETE from Order_product where order_id = {id}')
            execute_sql(connection, f'DELETE from orders where order_id = {id}')
            break  
        else:
            print("This option is invalid")
#-------------------------------------------------
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
            updated_status = update_order_status_in_db()
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

#-------------------------------------------------
def add_order_database(connection):

    print('Tell us about yourself...\n')
    name = str(input('Please enter your full name for the order \n')).capitalize()
    email = str(input('Please enter your email address\n'))
    address = str(input('Please enter a delivery address \n'))
    phone = str(input('Enter your phone number \n'))

    courier = add_courier_to_order(connection)
    execute_sql(connection, f'INSERT INTO Orders (name, courier_id, email, address, phone) VALUES ("{name}","{courier}", "{email}","{address}","{phone}")')

    add_to_order_product(connection)
    

    execute_sql(connection, f'UPDATE Orders SET cost_total = {total_cost}, items = {chosen_products_ids} WHERE email = "{email}"')
    print('Thank you for your order')


#-------------------------------------------------
def update_order_status_in_db(connection):
    print_orders_from_db(connection)
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from orders')]
    while True:
        id = int(input("Which order's status would you like to update?"))
        if id in existing_ids:
            updated_order_status = input("What is the new status of this order? Choose one: Preparing, Cancelled, Complete ")
            execute_sql(connection, f'UPDATE orders SET status = "{updated_order_status}"')
            break
#-------------------------------------------------
def add_courier_to_order(connection):
    print_whole_table('Couriers','courier_id')
    print('Choose a courier from their ID')
    existing_ids = []
    for row in execute_sql_select(connection, 'SELECT courier_id FROM Couriers'):
        existing_ids.append(row[0])
    while True: 
        pick_courier = int(input("What courier would you like to choose?"))
        if pick_courier in existing_ids:
            return pick_courier
        else:
            continue

choose_order_items(connection)
# add_order_database(connection)
# add_to_order_product(connection)
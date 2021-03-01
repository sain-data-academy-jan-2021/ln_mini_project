import pymysql
from dotenv import load_dotenv
import os
from tabulate import tabulate
from functions import *

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

#-------------------------------------------------------------------------------------------------------------------------------------------------
def execute_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()
##-------------------------------------------------------------------------------------------------------------------------------------------------
def execute_sql_select(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall()
#-------------------------------------------------------------------------------------------------------------------------------------------------
def choose_order_items(connection): #done
    
    print_whole_table("Products","prod_type")

    existing_ids = [id[0] for id in execute_sql_select(connection,'SELECT product_id FROM Products')]
    chosen_products_ids = []

    id = ''

    total_cost = 0
    final_basket = []
    while id !=0:
        clear_terminal()
        print_whole_table("Products","prod_type")
        try:
            id = int(input('Please choose the ID to order. When you have chosen all press 0:'))
         
            if id not in existing_ids and id !=0: 
                print('Invalid ID. Please try again')

            elif id in existing_ids:
        
                quantity = int(input('How many do you want: ')) 
                myresult = execute_sql_select(connection,f'SELECT prod_name, unit, price FROM Products where product_id = "{id}"')
                for x in myresult:
                    basket = (f'Product: {x[0]}, Unit: {x[1]}, Quantity: {quantity}, Price: {x[2]* quantity}')

                    price = x[2] * quantity

                total_cost = total_cost + price
                chosen_products_ids.extend([id] * quantity )
                final_basket.append(basket)

        except ValueError:
            print('Please enter a number') 

    # print('-' * len(basket))
    print('Order Summary:\n') 
    # print('-' * len(basket))
    for x in final_basket: 
        print(x)      
    print(f'Your order costs £{total_cost}\n')      
    return chosen_products_ids, total_cost       
#-------------------------------------------------------------------------------------------------------------------------------------------------
def add_to_order_product(connection):
 #done
    cursor = connection.cursor()
    order_id = execute_sql_select(connection,'SELECT MAX(order_id) FROM Orders')[0][0]
    chosen_products_ids = choose_order_items(connection)
    for product_id in chosen_products_ids[0]:
        execute_sql(connection, f'INSERT INTO Order_product (order_id, product_id) VALUES ({order_id}, {product_id})')
    cursor.close()
    connection.commit()

    return chosen_products_ids
#-------------------------------------------------------------------------------------------------------------------------------------------------
def print_orders_from_db(connection):

    clear_terminal()
    banner()
    cursor = connection.cursor()
    cursor.execute( f'SELECT * FROM Orders')
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Order ID', 'Status','Name','Courier ID', 'Address','Phone', 'Items Purchased', 'Total Cost'], tablefmt='psql'))

    item_breakdown(connection)

    print('\n')
#-------------------------------------------------
def delete_order_in_db(connection): #done
    
    clear_terminal()
    banner()
    id = ''
    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from Orders')]
        
    while True:
        print_orders_from_db(connection)
        id = int(input("Which order would you like to delete from the list above? Select an order ID. Press '0' to return to previous menu\n"))
        if id in existing_ids:
            execute_sql(connection, f'DELETE from Order_product where order_id = {id}')
            execute_sql(connection, f'DELETE from Orders where order_id = {id}')
            print(cursor.rowcount, "record(s) deleted from order\n")
            print('Loading edited table...')
            sleep(2)

        elif id == 0:
            break

        else: 
            print("This not a valid order number. Please choose from the order_id list")
            continue
#-------------------------------------------------------------------------------------------------------------------------------------------------
# def update_order_details(connection):
#     existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from Orders')]
#     chosen_products = [id[0] for id in execute_sql_select(connection, 'select product_id from Products')]
#     while True:
#         print_orders_from_db(connection)
#         id = int(input("What order would you like to update from the list above?"))
#         if id in existing_ids:
#             updated_order_name = input("Please enter the updated name or l").title()
#             updated_order_address = input("Please enter the updated address").title()
#             updated_phone = input("Please enter the updated phone number").title()
            
#             if len(updated_phone) !=11 or len(updated_order_address) <= 1 or len(updated_order_name) <=1:
#                 print('Invalid amount of characters in one or more updated entries. Please try again')
#                 continue
#             else:
#                 print_whole_table("Couriers","courier_id")
#                 updated_courier = input("Please enter an updated courier from the list above")
#                 updated_status = update_order_status_in_db(connection)
#                 execute_sql(connection, f'UPDATE Orders SET name = "{updated_order_name}", address = "{updated_order_address}", phone = "{updated_phone}", courier = "{updated_courier}", status = "{updated_status}"')
#                 print_whole_table("Products","prod_type")
#                 break

#     for row in execute_sql_select(connection, 'SELECT product_id FROM Order_product'):
#         existing_ids.append(row[0])
#     while True:
#         updated_items = int(input("Please enter the new items you would like to add to the order, Press 0 to continue"))
#         if updated_items in chosen_products:
#             chosen_products.append(updated_items)
#             execute_sql(connection, f'UPDATE Order_product SET product_id = {updated_items} WHERE order_id = {id}')
#             continue
#         elif updated_items == 0:
#             break
#-------------------------------------------------------------------------------------------------------------------------------------------------
def add_order_database(connection):#done

    while True:
        clear_terminal()
        banner()
        print('Tell us about yourself...\n')
        name = (input('Please enter your full name to start you order or press 0 to return to previous menu\n')).capitalize()
        if name != 0 and len(name) <=1 :
            break
        email = str(input('Please enter your email address\n'))
        address = str(input('Please enter a delivery address \n'))
        phone = str(input('Enter your phone number \n'))
        
        if len(phone) != 11 or len(email)<= 1 or len(address) <= 1:
            print('Invalid number of characters in one or more entries. Please try again') 
            continue 
        
        else:
            courier = add_courier_to_order(connection)
            execute_sql(connection, f'INSERT INTO Orders (name, courier_id, email, address, phone) VALUES ("{name}","{courier}", "{email}","{address}","{phone}")')
            
            total_cost = ''
            chosen_products = add_to_order_product(connection)
            total_cost = chosen_products[1]
            chosen_products_ids = chosen_products[0]

            execute_sql(connection, f'UPDATE Orders SET cost_total = {total_cost} WHERE email = "{email}"')
            print('Thank you for your order\n')
            choice = str(input('Do you want to order something else? press any key to continue or 0 to return to previous menu'))
            if choice == '0':
                break
            else: 
                continue
#-------------------------------------------------------------------------------------------------------------------------------------------------
def update_order_status_in_db(connection):#done
    
    # clear_terminal()
    # banner()

    # print('Here are our existing orders...')
    # print_orders_from_db(connection)

    existing_ids = [id[0] for id in execute_sql_select(connection, 'select order_id from Orders')]
    status = ['Preparing','Cancelled','Completed']
    id = ''
    while id !=0:
        clear_terminal()
        banner()

        print('Here are our existing orders...')
        print_orders_from_db(connection)

        id = int(input("Which order's status would you like to update? or press 0 to return to previous menu\n"))
        if id in existing_ids:
            updated_order_status = input("What is the new status of this order? Enter either: Preparing, Cancelled or Completed\n").title()
            if updated_order_status in status:
                execute_sql(connection, f'UPDATE Orders SET status = "{updated_order_status}" where order_id = {id}\n')
                print(f'Thank you for updating the status of Order {id} to {updated_order_status}\n')
                sleep(2)
                
            else:
                print('Please enter a valid status')
                continue
        else: 
            print('Please enter a valid order number')
            continue
#-------------------------------------------------------------------------------------------------------------------------------------------------
def add_courier_to_order(connection): #done
    clear_terminal()
    banner()

    print_whole_table('Couriers','courier_id')
    print('Choose a courier from their ID\n')
    existing_ids = []
    for row in execute_sql_select(connection, 'SELECT courier_id FROM Couriers'):
        existing_ids.append(row[0])
    while True: 
        pick_courier = int(input("Which courier would you like to choose?\n"))
        if pick_courier in existing_ids:
            return pick_courier
        else:
            continue
#-------------------------------------------------------------------------------------------------------------------------------------------------
def item_breakdown(connection):

    joins = execute_sql_select(connection, 
    '''SELECT o.name AS 'Customer Name',
    o.address as Address,
    o.phone as 'Phone Number',
    c.courier_name as Courier,
    o.status as Status,
    o.order_id as 'Order ID',
    GROUP_CONCAT(p.prod_name separator ', ') AS Items 
    FROM Orders o
    LEFT JOIN Order_product op 
    ON op.order_id = o.order_id
    LEFT JOIN Products p 
    ON op.product_id = p.product_id
    LEFT JOIN Couriers c 
    ON o.courier_id = c.courier_id
    GROUP BY o.order_id;''')

    breakdown = []

    order = int(input('Enter an order ID to view the breakdown of items ordered or press 0 to skip\n\n'))

    for x in joins:
        if x[5] == order:
            print(x[6])
#-------------------------------------------------------------------------------------------------------------------------------------------------
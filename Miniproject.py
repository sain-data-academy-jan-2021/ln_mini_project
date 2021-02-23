import os
from time import sleep
from funcs_prod_courier import *
from orderhandling import *
from display_functions import *
import pymysql
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
)
cursor = connection.cursor()


banner()
print('Loading main menu...')
sleep(3)

option = main_menu_input()
if option == '1':
    option = ''
    option = menu_input('Product')
    if option == '1':
        print_products__from_db()
    elif option == '2':
        add_entry ('Products')
    elif option == '3':
        update_entry('Products', 'product', 'prod_name', 'prod_name')
    elif option == '4':
        delete_entry('Products', 'product', 'prod_name') 
    elif option == '0':
        main_menu_input()
    else:
        print('Invalid selection. Please choose again')

elif option == '2':
    option = ''
    option = menu_input('Courier')
    if option == '1':
        print_couriers_from_db()
    elif option == '2':
        add_entry ('Products')
    elif option == '3':
        update_entry('Couriers', 'courier', 'courier_name', 'courier_name')
    elif option == '4':
        delete_entry('Couriers', 'courier', 'courier_name')
    elif option == '0':
        main_menu_input()
    else:
        print('Invalid selection. Please choose again')
        

elif option == '3':
        option = ''
        option = menu_input('order')
        if option == '1':
            print_orders_from_db(connection)
        elif option == '2':
            add_order_database(connection)
        elif option == '3':
            update_order_details(connection) 
        elif option == '4':
            delete_order_in_db(connection)
        elif option == '0':
            main_menu_input()
        else:
            print('Invalid selection. Please choose again')   

elif option == '0':     
        print("Exiting..")
        exit_app()

else:
    print('Invalid Selection. Please select either option: 1, 2 or 3.')
    
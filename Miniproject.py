import os
from time import sleep
from functions import *
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

option = ''
while True: 
    option = main_menu_input()
    if option == '1':
        while True:
            option = ''
            option = menu_input('Product')
            if option == '1':
                print_whole_table("Products",'product_id')
                sub_menu('Product')
            elif option == '2':
                add_product()
            elif option == '3':
                update_product_entry('Products')   
            elif option == '4':
                delete_entry('Products', 'product', 'prod_name') 
            elif option == '0':
                break
            else:
                print('Invalid selection. Please choose again')

    elif option == '2':
        while True:
            option = ''
            option = menu_input('Courier')
            if option == '1':
                print_whole_table("Couriers", "courier_id")
                sub_menu('Courier')
            elif option == '2':
                add_courier()
            elif option == '3':
                update_courier_entry()
            elif option == '4':
                delete_entry('Couriers', 'courier', 'courier_name')
            elif option == '0':
                break
            else:
                print('Invalid selection. Please choose again')

            

    elif option == '3':
            while True:
                option = ''
                os.system('clear')
                option = menu_input('Order')
                if option == '1':
                    print_orders_from_db(connection)
                    sub_menu('Order')   
                elif option == '2':
                    add_order_database(connection)
                elif option == '3':
                    update_order_status_in_db(connection)
                elif option == '4':
                    delete_order_in_db(connection)
                elif option == '0':
                    break
                else:
                    print('Invalid selection. Please choose again')   

    elif option == '0':     
            print("Exiting..")
            exit_app()

    else:
        print('Invalid Selection. Please select either option: 1, 2 or 3.')
    
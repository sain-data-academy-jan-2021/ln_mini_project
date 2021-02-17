import os,pymysql,csv
from time import sleep
#from functions import *
#from mysql_copy import *
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

newbranch = practice

def clear_terminal():
    os.system('clear')
def exit_app():
    border = len('Thanks for stopping by Jammed Packed Lunches! See you soon.') * '*'
    print('\n' + border)
    print('Thanks for stopping by JAM\'D PACKED LUNCHES! See you soon.')
    print(border + '\n')
    connection.close()
    exit()
def main_menu_input():
    clear_terminal()
    #banner
    main_menu = (
        f' 0 - Exit app \n 1 - View product menu \n 2 - View courier menu \n 3 - View order menu')
    print(main_menu)
    option = input("\n\nWhat would you like to do? Choose an option number")
    return option
def menu_input(field): 
    print(f'\n\n{field} menu')
    print('------------------------------------------------------')
    menu =(f' 0 - Return back to main menu \n 1 - View all {field}s \n 2 - Create new {field} entry \n 3 - Update {field} \n 4 - Delete {field}')
    print(menu)

    option = input("\nWhat would you like to do ? Choose an option number")
    return option
def exit_app():
    border = len('Thanks for stopping by Jammed Packed Lunches! See you soon.') * '*'
    print('\n' + border)
    print('Thanks for stopping by JAM\'D PACKED LUNCHES! See you soon.')
    print(border + '\n')
    exit()
def banner():
    cafe_name = ''
    cafe_name = str('* WELCOME TO \'JAM\'D PACKED LUNCHES*')
    border = len(cafe_name) * '*'
    print('\n' + border)
    print(cafe_name)
    print(border + '\n')
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

    choice = input('Press 0 to return to main menu')
    if choice == '0':
        main_menu_input()

    cursor.close()
def add_entry (table):   
    while True:    
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

            print(cursor.rowcount, "record inserted. New ID:",cursor.lastrowid)
            cursor.close()
            connection.commit() 
    
        choice = input('Press 0 to return to main menu or any key to continue add another')
        if choice == '0':
            main_menu_input()
            break
        else:
            continue

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

            print(cursor.rowcount, "record inserted. New ID:",cursor.lastrowid)
            cursor.close()
            connection.commit() 
    
            choice = input('Press 0 to return to main menu or any key to continue update another')
            if choice == '0':
                main_menu_input()
                break
            else: 
                continue

    cursor.close()
    connection.commit() #need both when altering database 

    choice = input('Press 0 to return to main menu or any key to continue')
    if choice == '0':
        main_menu_input() 
def delete_entry(table, item_type, column): #item_type = product/item
    while True:
        delete_item = str(input(f'Which {item_type} would you like to delete from {table}?')).title()

        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM {table} WHERE {column} = "{delete_item}"')

        print(cursor.rowcount, "record(s) deleted")

        cursor.close()
        connection.commit()

        choice = input('Press 0 to return to main menu or any key to delete another item')
        if choice == '0':
            main_menu_input()
            break
def update_entry(table, item_type, column1, column2): #table, item_type, need error handlinh
    while True:
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
        
        cursor.close()
        connection.commit()
        
        choice = input('Press 0 to return to main menu or any key to continue update another')
        if choice == '0':
            main_menu_input()
            break
        else:
            continue
        
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
 
        choice = input('Press 0 to return to main menu or any key to continue update another')
        if choice == '0':
            main_menu_input()
            break
        else:
            continue


banner()
print('Loading main menu...')
sleep(3)

option = main_menu_input()
if option == '1':
    option = ''
    option = menu_input('Product')
    if option == '1':
        print_all('Products')
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
        print_all('Couriers')
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
        

#elif option == '3':
    #     option = ''
    #     option = menu_input(order)
    #     if option == '1':
    #        print(orders)
    #     elif option == '2': #CREATE NEW ORDER
    #         #ASK CUSTOMER NAME,ADDRESS,NUMBER 
    #         #ASK FOR NAME AND PRICE
    #         #CHOOSE PRODUCT UNTIL 0 TO CANCEL
    #     elif option == '3':
    #         #UPDATE ORDER STATUS
    #         #SELECT PRODUCT OR 0 TO BACK TO MAIN 
    #         #ASK USER FOR DATA OR LEAVE BLANK TO SKIP
    #         #ASK USER TO UPDATE ORDER PROPERTY 
    #     elif option == '4':
    #         #DELETE ORDER
    #         #DELETE OR 0 TO CANCEL
    #         #REMOVE ITEM
    #     elif option == '0': #SAVE STATE APP & EXIT/BACK TO MAIN MENU
    #         main_menu_input()
    #     else:
    #         print('Invalid selection. Please choose again')   

    # else:
    #     print('Invalid Selection. Please select either option: 1, 2 or 3.')
    

elif option == '0':     
        print("Exiting..")
        exit_app()
import pymysql
from dotenv import load_dotenv
import os
from tabulate import tabulate
from display_functions import *
from time import sleep

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

def clear_terminal(): 
    os.system('clear')

def execute_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    connection.commit()
#---------------------
def execute_sql_select(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall()
# --------------------------------------------------
def print_whole_table (table, column):
    clear_terminal()
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table} ORDER BY {column}')
    if table == 'Products':
        headers = ['Product ID', 'Product Name','Product Type','Unit','Price']
    if table == 'Couriers':
        headers = ['Courier ID', 'Courier Name','Contact Number']
    myresult = cursor.fetchall()
    print(tabulate(myresult,headers, tablefmt='psql')) 
    cursor.close()
# -----------------------------------------------
def print_drinks_db():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products where prod_type = 'Drink'")
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name','Product Type','Unit','Price'], tablefmt='psql'))
    cursor.close()
    connection.close()
# -------------------------------------------------
def print_food_db():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products where prod_type = 'Food'")
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name','Product Type','Unit','Price'], tablefmt='psql'))
    cursor.close()
    connection.close()


def delete_entry(table, item_type, column): #item_type = product/item CORRECT
    clear_terminal()
    banner()
    print('Here our our existing products..')

    print_whole_table(f'{table}',f'{column}')

    while True:
        delete_item = str(input(f'Which {item_type} would you like to delete from {table}? Press 0 to return to previous menu')).title()
        if delete_item !='0':
            item_check = execute_sql_select(connection, f'select * from {table} WHERE {column} = "{delete_item}"')

            if len(item_check) == 0:
                print(f'{delete_item} does not exist and cannot be deleted. Please try again')
                continue

            else:
                cursor = connection.cursor() 
                cursor.execute(f'DELETE FROM {table} WHERE {column} = "{delete_item}"')
                print(cursor.rowcount, "record(s) deleted")
                cursor.close()
                connection.commit()
                continue
        
        if delete_item == '0':
            break
                
# -----------------------------------------------
def add_product(): 
    clear_terminal()  

    while True:
        print('Here our our existing products..')
        print_whole_table("Products", "prod_type")
        add_type = str(input(f'What type of item would you like to add to Products? Press 1 for Drinks or 2 for Food'))
        if add_type == '2' :
            add_type = 'Food'
        if add_type == '1' :
            add_type = 'Drink'
        else:
            print('Invalid type entered. Please retry and either enter 1 or 2!')
            sleep(2)
            continue 

        new_item = input(f'What item would you like to add to our {add_type} database?').title()
        new_item_cost = float(input(f'How much does a unit of {new_item} cost?'))
        new_unit = str(input(f'What is the quanity of a single unit of {new_item}. Include units'))
        cursor = connection.cursor()
        cursor.execute(F'INSERT INTO Products (prod_name, prod_type, unit, price) VALUES ("{new_item}","{add_type}","{new_unit}",{new_item_cost})')

        print(cursor.rowcount, "record inserted. New ID:",cursor.lastrowid)
        cursor.close()
        connection.commit() 

        choice = str(input('Do you want to add another item? Press any key to continue or 0 to return to previous menu'))
        if choice == '0':
            break
        else:
            continue
# -----------------------------------------------
def add_courier():
    cursor = connection.cursor()
    clear_terminal()
    banner()
    while True: 
        banner()
        add_person = str(input(f'Who would you to add to Couriers?\n')).title()
        add_numb = input(f'What phone number can {add_person} be reached on\n')
        if len(add_numb) == 11:
            cursor.execute(f'INSERT INTO Couriers (courier_name, contact_number) VALUES ("{add_person}","{add_numb}")')
        else:
            print('Error. Phone numbers must be 11 digits. Please try again')
            

        print(cursor.rowcount, "courier inserted. New ID:",cursor.lastrowid)

        connection.commit() 

        choice = str(input('Do you want to add another person? Press any key to continue or 0 to return to previous menu'))
        if choice == '0':
            break
        else:
            continue

    cursor.close()

# -----------------------------------------------
def update_product_entry():
    
    print_products_table()
 
    existing_prods = [id[0] for id in execute_sql_select(connection, 'select prod_name from Products')]
    while True:
        old_item = input(f'Which item from Products do you want to update or press 0 to return to main menu').title()
        if old_item != '0':
            update = input(f'What do you want to update {old_item} to?').title()
            if old_item in existing_prods:
                cursor = connection.cursor()
                cursor.execute(f'UPDATE Products SET prod_name = "{update}" WHERE prod_name = "{old_item}"')
                print(cursor.rowcount, "record(s) affected")
                print(f'Kindly update the properties of {update}. Skip any properties you do not wish to update by pressing \'s\'  to continue')

                update1 = str(input(f'Press 1 if {update} is classed as a food, press 2 if {update} is classed as a drink.'))
                if update1 == '1':
                    cursor.execute(f'UPDATE Products SET prod_type = "Food" WHERE prod_name = "{update}"')
                if update1 == '2':
                    cursor.execute(f'UPDATE Products SET prod_type = "Drink" WHERE prod_name = "{update}"')
                else:
                    print('Invalid entry. Try again')
                    continue

                update2 = input(f'What is the quanity of a single unit of {update}. Include unit measurements')
                if update2 != 's':
                    cursor.execute(f'UPDATE Products SET unit = "{update2}" WHERE prod_name = "{update}"')
                else:
                    pass
                
                update3 = input(f'What is the cost of {update}')
                if update3 == 's':
                    pass 
                else:
                    update3 = float(update3)
                    cursor.execute(f'UPDATE {table} SET price = "{update3}" WHERE {column} = "{update}"')

                cursor.execute(f'SELECT prod_name,prod_type,unit,price FROM Products WHERE prod_name = "{update}"')
                newentry = cursor.fetchall()
                for x in newentry:
                    print(f'New complete updated entry\n {x}')
            else: 
                print(f'{old_item} can not be updated because it does not exist. Please enter an existing product')

            cursor.close()
            connection.commit()

        else: 
            main_menu_input() #see if you can access main menu from outiside function 
            break

# def update_courier_entry(): #loop not working second time
    
    existing_ids = [id[0] for id in execute_sql_select(connection, 'SELECT courier_id FROM Couriers')]
    
    cursor = connection.cursor()

    while True:
        print_whole_table("Couriers","courier_id")
        try:
            id = int(input(f'Choose an id to begin update or press 0 to return to main menu'))

            if id == 0:
                break    

            if id != 0 and id in existing_ids:
                update = str(input(f'What do you want to update Courier {id}\'s name to? Press Enter to skip').title())
                if len(update) == 0:
                    update_phone = input(f'No name added. Update phone number of courier {id} instead or press enter to skip')
                    if len(update_phone) >0:
                        execute_sql(connection, f'UPDATE Couriers SET contact_number = "{update_phone}" WHERE courier_name = "{id}"')
                        print(cursor.rowcount, "record(s) affected")
                        continue 
                    elif len(update_phone) == 0:
                        print(f'No number added for courier {id}. Update another courier')
                        continue 
                else:
                    cursor.execute(f'UPDATE Couriers SET courier_name = "{update}" WHERE courier_id = "{id}"')
                    print(cursor.rowcount, "record(s) affected")
                    connection.commit()
                    pass
            else: 
                print(f'{id} can not be updated because this entry does not exist. Please enter an existing product')
                continue  

            update2 = str(input(f'Please insert an updated number or press Enter to skip'))
            if len(update2) == 0:
                connection.commit()
                pass
           
            else:
                cursor.execute(f'UPDATE Couriers SET contact_number = "{update2}" WHERE courier_name = "{update}"')
                print(cursor.rowcount, "record(s) affected")
                connection.commit() 
                pass   

            newentry = cursor.fetchall()
            for x in newentry:
                print(f'New complete updated entry\n {x}')
        
            cursor.close()
            
        except: ValueError
        print('Please insert a number as valid ID')
        

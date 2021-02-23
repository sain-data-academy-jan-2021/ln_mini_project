import pymysql
from dotenv import load_dotenv
import os
from tabulate import tabulate
from orderhandling import *
from display_functions import *

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


def execute_sql_select(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()
    return cursor.fetchall()

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
# -----------------------------------------------
def add_product ():   
    add_type = input(f'What type of item would you like to add to Products? Press 1 for Drinks or 2 for Food')
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
# -----------------------------------------------
def add_courier ():

    add_person = str(input(f'Who would you to add to Couriers?')).title()
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


    cursor.close()
    connection.commit()
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
            # main_menu_input() #see if you can access main menu from outiside function 
            break
def update_courier_entry(): 

print_courier_table()


    while True:
        old_item = input(f'Which item from Couriers do you want to update or press 0 to return to main menu').title()
        existing_names = [id[0] for id in execute_sql_select(connection, 'select courier_name from Couriers')
        ]if old_item != '0':
            update = input(f'What do you want to update {old_item} to?').title()
            if old_item in existing_names:
                cursor = connection.cursor()
                cursor.execute(f'UPDATE Products SET prod_name = "{update}" WHERE prod_name = "{old_item}"')
                print(cursor.rowcount, "record(s) affected")
                print(f'Kindly update the properties of {update}. Skip any properties you do not wish to update by pressing \'s\'  to continue')

                update1 = str(input(f'What is {update}\'s prefered delivered method'))
    #           cursor.execute(f'UPDATE {table} SET delivery_method = "{update1}" WHERE {column1} = "{update}"')
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
            # main_menu_input() #see if you can access main menu from outiside function 
            break

    #  
    # update2 = str(input(f'What is {update}\'s mobile number'))
    # cursor.execute(f'UPDATE {table} SET contact_number = "{update2}" WHERE {column1} = "{update}"')

    # cursor.execute(f'SELECT * FROM {table} WHERE {column1} = "{update}"')
    # newentry = cursor.fetchall()
    # for x in newentry:
    #     print(f'New complete updated entry:\n {x}')

    # cursor.close()
    # connection.commit()
        else:
            continue
# ----------------------------
def print_drinks_db():
    cursor.execute("SELECT * FROM Products where prod_type = 'Drink'")
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name','Product Type','Unit','Price'], tablefmt='psql'))
# -------------------------------------------------
def print_food_db():
    cursor.execute("SELECT * FROM Products where prod_type = 'Food'")
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name','Product Type','Unit','Price'], tablefmt='psql'))

# --------------------------------------------------
def print_products_table ():
    cursor = connection.cursor()
    cursor.execute( f'SELECT * FROM Products')
    myresult = cursor.fetchall()
    print(tabulate(myresult,headers=['Product ID', 'Product Name','Product Type','Unit','Price'], tablefmt='psql'))
# -----------------------------------------------
def print_courier_table (): 
    cursor = connection.cursor()
    cursor.execute( f'SELECT * FROM Couriers')
    myresult = cursor.fetchall()
    print(tabulate(myresult,headers=['Courier ID', 'Courier Name','Delivery Method','Contact Number'], tablefmt='psql'))
# -----------------------------------------------
def print_drinks_db():
    cursor.execute("SELECT * FROM Products where prod_type = 'Drink'")
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name','Product Type','Unit','Price'], tablefmt='psql'))
# -------------------------------------------------
def print_food_db():
    cursor.execute("SELECT * FROM Products where prod_type = 'Food'")
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name','Product Type','Unit','Price'], tablefmt='psql'))


update_product_entry()
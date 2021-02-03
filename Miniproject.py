# # # Start app with relevant imports 
import os
from time import sleep
#------------------------------------------------------------
#VARIABLES 
cafe_name = '* WELCOME TO \'JAM\'D PACKED LUNCHES'

product_list = []    
file = open("products.txt", 'r')
product_list = [line.rstrip() for line in file] 
file.close()

courier_list = []
file = open('couriers.txt','r')
courier_list = [line.rstrip() for line in file]
file.close

#FUNCTIONS 
def clear_terminal():
    os.system('clear')
#-----------------------------------------------------------
def exit_app():
    border = len('Thanks for stopping by Jammed Packed Lunches! See you soon.') * '*'
    print('\n' + border)
    print('Thanks for stopping by JAM\'D PACKED LUNCHES! See you soon.')
    print(border + '\n')
    exit()
#--------------------------------------------------------------
def banner():
    border = len(cafe_name) * '*'
    print('\n' + border)
    print(cafe_name)
    print(border + '\n')
#--------------------------------------------------------------
def main_menu_input():
    clear_terminal()
    banner()
    main_menu = {'0': 'Exit app', '1':'View product menu', '2':'View courier menu'}
    for key,value in main_menu.items():
        print(key,value)

    option = input("\n\nWhat would you like to do? Choose an option number")
    return option
# ---------------------------------------------------------------
def product_menu_input(): 
    banner()
    print('Product Menu')
    print('------------------------------------------------------')
    product_menu = {0:'Return back to main menu', 1:'View all products', 2: 'Create new product', 3:'Update a product', 4: 'Delete a product'}
    for key,value in product_menu.items():
        print(key,value)

    option = input("\nWhat would you like to do? Choose an option number")
    return option 
    # ---------------------------------------------------------------
def courier_menu_input(): 
    banner()
    print('Courier Menu')
    print('------------------------------------------------------')
    courier_menu = {0:'Return back to main menu', 1:'View all couriers', 2: 'Add courier', 3:'Update courier name', 4: 'Delete a courier'}
    for key,value in courier_menu.items():
        print(key,value)

    option = input("\nWhat would you like to do? Choose an option number")
    return option 
#-----------------------------------------------------------------------
def print_products(): 
    clear_terminal()
    banner()
    print("\nHere is our current product selection\n")
    for product in product_list:
        print(product)
#-----------------------------------------------------------------------
def print_couriers(): 
    clear_terminal()
    banner()
    print("\nHere is our current courier selection\n")
    for person in courier_list:
        print(person)
#-----------------------------------------------------------------------
def create_product(): 
    clear_terminal()
    banner()
    new_product = input("\nPlease enter a new product ")
    product_list.append(new_product)
    print("\nThank you for introducing %s!\n" % new_product.title())
    sleep(3)8
    print_products()

    file = open("products.txt", 'a')
    file.write('\n' + new_product)
#-----------------------------------------------------------------------
def create_courier(): 
    clear_terminal()
    banner()
    new_courier = input("\nPlease enter a new courier\'s name")
    courier_list.append(new_courier)
    print("\nThank you for introducing %s!\n" % new_courier.title())
    sleep(3)
    print_couriers()

    file = open("products.txt", 'a')
    file.write('\n' + new_courier)
#-----------------------------------------------------------------------
def update_product():
    clear_terminal()
    banner()
    print_products()
    update_product = input('Please enter the product you want to update\n')
    update_product = update_product.title()
    if update_product in product_list:
        index_value = product_list.index(update_product)
        update = input(f'What would you like to update {update_product} to?')
        product_list[index_value] = update.title()
        print('Thank you for your update')
        sleep(3)
        print_products()
    
        file = open("products.txt", 'w')
        for line in product_list:
            file.write(line +'\n')

        # check = input ('Do yu want to continue: yes/no')
        # if check = yes: 
        #     update_product()
        # else:
        #     product_menu()
    else:    
        print('Please enter an existing product to update')     
#-----------------------------------------------------------------------
def update_courier():
    clear_terminal()
    banner()
    print_couriers()
    update_courier = input('Please enter the courier you want to update\n')
    update_courier= update_courier.title()
    if update_courier in courier_list:
        index_value = courier_list.index(update_courier)
        update = input(f'What would you like to update {update_courier} to?')
        courier_list[index_value] = update.title()
        print('Thank you for your update')
        sleep(3)
        print_couriers()

        file = open("couriers.txt", 'w')
        for line in product_list:
            file.write(line +'\n')
    else:    
        print('Please enter an existing courier to update')     
#-------------------------------------------------------------
def delete_product(): 
    clear_terminal()
    banner()
    print_products()
    delete_product = input('Please enter the product you want to delete\n')
    delete_product = delete_product.title()
    if delete_product in product_list:
        index_value = product_list.index(delete_product)
        del product_list[index_value]
        print('\n\n' + delete_product + 'has been deleted. Thank you.')
        sleep(3)
        print_products()
    else:
        print('Please choose an existing entry to delete')

    file = open("products.txt", 'w')
    for line in product_list:
        file.write(line +'\n')
#-------------------------------------------------------------
def delete_couriers(): 
    clear_terminal()
    banner()
    print_couriers()
    delete_couriers = input('Please enter the courier you want to delete\n')
    delete_couriers = delete_couriers.title()
    if delete_couriers in courier_list:
        index_value = product_list.index(delete_product)
        del product_list[index_value]
        print('\n\n' + delete_product + 'has been deleted. Thank you.')
        sleep(3)
        print_products()
    else:
        print('Please choose an existing entry to delete')

    file = open("couriers.txt", 'w')
    for line in courier_list:
        file.write(line +'\n')

banner()
option = ''
option = main_menu_input()

if option == '1':
    option = ''
    option = product_menu_input()
    if option == '1':
        print_products()
    elif option == '2':
        create_product()
    elif option == '3':
        update_product()
    elif option == '4':
        delete_product()
    elif option == '0':
        main_menu_input()
    else:
        print('Invalid selection. Please choose again')

elif option == '2':
    option = ''
    option = courier_menu_input()   
    if option == '1':
        print_couriers()
    elif option == '2':
        create_courier()
    elif option == '3':
        update_courier()
    elif option == '4':
        delete_couriers()
    elif option == '0':
        main_menu_input()
    else:
        print('Invalid selection. Please choose again')
elif option == '0':
        print("Exiting..")
        exit_app()
else:
    print("\nInvalid Selection\n")

    
#save app state ask instructor 
#add loops 
#add or cancels 

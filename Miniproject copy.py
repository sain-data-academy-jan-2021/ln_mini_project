# # # # # Start app with relevant imports 
# import os


import csv 
# # #------------------------------------------------------------
# # #VARIABLES 
# # cafe_name = '* WELCOME TO \'JAM\'D PACKED LUNCHES'

# # product_list = []    
# # file = open("products.txt", 'r')
# # product_list = [line.rstrip() for line in file] 
# # file.close()

# # courier_list = []
# # file = open('couriers.txt','r')
# # courier_list = [line.rstrip() for line in file]
# # file.close

# # #FUNCTIONS 
# # def clear_terminal():
# #     os.system('clear')
# # #-----------------------------------------------------------
# # def exit_app():
# #     border = len('Thanks for stopping by Jammed Packed Lunches! See you soon.') * '*'
# #     print('\n' + border)
# #     print('Thanks for stopping by JAM\'D PACKED LUNCHES! See you soon.')
# #     print(border + '\n')
# #     exit()
# # #--------------------------------------------------------------
# # def banner():
# #     border = len(cafe_name) * '*'
# #     print('\n' + border)
# #     print(cafe_name)
# #     print(border + '\n')
# # #--------------------------------------------------------------
# # def main_menu_input():
# #     clear_terminal()
# #     banner()
# #     main_menu = {'0': 'Exit app', '1':'View product menu', '2':'View courier menu'}
# #     for key,value in main_menu.items():
# #         print(key,value)

# #     option = input("\n\nWhat would you like to do? Choose an option number")
# #     return option
# # # ---------------------------------------------------------------
# # def product_menu_input(): 
# #     banner()
# #     print('Product Menu')
# #     print('------------------------------------------------------')
# #     product_menu = {'0':'Return back to main menu', '1':'View all products', '2': 'Create new product', '3':'Update a product', '4': 'Delete a product'}
# #     for key,value in product_menu.items():
# #         print(key,value)

# #     option = input("\nWhat would you like to do? Choose an option number")
# #     return option 
# #     # ---------------------------------------------------------------
# # def courier_menu_input(): 
# #     banner()
# #     print('Courier Menu')
# #     print('------------------------------------------------------')
# #     courier_menu = {'0':'Return back to main menu', '1':'View all couriers', '2': 'Add courier', '3':'Update courier name', '4': 'Delete a courier'}
# #     for key,value in courier_menu.items():
# #         print(key,value)

# #     option = input("\nWhat would you like to do? Choose an option number")
# #     return option 

# # # def item_menu(item, list)
# # #     print(list)
# # #     choice = input(f'1) view {item}, 2) create {item}, 3) Update {item}, 4) Delete {item} ')

# # #     while choice != '0':
# # #         if choice == '1':
# # #             add_item = input(f'What {item} would you like to add')
# # #             list.append(add_item)
# # #             print(list)
# # #         elif choice == '2':
# # #             update_item = input('choose one to update')
# # #             if update in list 
# # #             update_item_new = input(f'What {item} would you like to update')
# # #             list.remove(update_item) 
# # #             list.append(update_item_new)
# # #             print(list)
# # #         else: 
# # #             print('Invalid Entry')

# # #----------------------------------------------------------------------

def print_couriers_or_products(selection, list): #import csv file with products. 
    print(f'Here is our {selection} list: \n')
    list =[]
    for each in list:
        print(each)
# # #-----------------------------------------------------------------------
def load_files(list, filename):
    
    list = []    
    file = open(filename , 'r')
    list = [line.rstrip() for line in file] 
    file.close()
    return (list)

def add_product_or_courier(addition,list,filename):

    entry = input(f'Please enter the {addition} you would to add:').title()

    if entry in list :
        print(f'It looks like {entry} is already on our system. Please try again')
    else:
        list.append(entry)
        print("\nThank you for introducing %s!\n" % entry.title())
        print(f'Here\'s our current {addition} list:\n')
        for each in list:
            print(item)

        file = open(filename, 'a')
        file.write('\n' + entry)
        file.close()

# #-----------------------------------------------------------------------
def update_courier_or_product(selection,list,filename): 
     
    update = input(f'Please enter the {selection} you want to update\n')
    update = update.title()

    if update in list:
        index_value = list.index(update)
        new = input(f'What would you like to update {update} to?').title()
        list[index_value] = new.title()
        print('Thank you for your update')
        sleep(3)
    
        file = open(filename, 'w')
        for line in list:
            file.write(line +'\n')
    else:    
        print('Please enter an existing product to update') 
        #Print list    

# # update_courier_or_product('product','products','products.txt')
# load_files('products','products.txt')
# print(products)

# # #----------------------------------------------------------------------- 
# # #-------------------------------------------------------------
# # def delete_product(): 
# #     clear_terminal()
# #     banner()
# #     print_products()
# #     delete_product = input('Please enter the product you want to delete\n')
# #     delete_product = delete_product.title()
# #     if delete_product in product_list:
# #         index_value = product_list.index(delete_product)
# #         del product_list[index_value]
# #         print('\n\n' + delete_product + 'has been deleted. Thank you.')
# #         sleep(3)
# #         print_products()
# #     else:
# #         print('Please choose an existing entry to delete')

# #     file = open("products.txt", 'w')
# #     for line in product_list:
# #         file.write(line +'\n')
# # #-------------------------------------------------------------
# # def delete_couriers(): 
# #     clear_terminal()
# #     banner()
# #     print_couriers()
# #     delete_couriers = input('Please enter the courier you want to delete\n')
# #     delete_couriers = delete_couriers.title()
# #     if delete_couriers in courier_list:
# #         index_value = product_list.index(delete_product)
# #         del product_list[index_value]
# #         print('\n\n' + delete_product + 'has been deleted. Thank you.')
# #         sleep(3)
# #         print_products()
# #     else:
# #         print('Please choose an existing entry to delete')

# #     file = open("couriers.txt", 'w')
# #     for line in courier_list:
# #         file.write(line +'\n')

# # banner()
# # option = ''
# # option = main_menu_input()

# # if option == '1':
# #     option = ''
# #     option = product_menu_input()
# #     if option == '1':
# #         print_products()
# #     elif option == '2':
# #         create_product()
# #     elif option == '3':
# #         update_product()
# #     elif option == '4':
# #         delete_product()
# #     elif option == '0':
# #         main_menu_input()
# #     else:
# #         print('Invalid selection. Please choose again')

# # elif option == '2':
# #     option = ''
# #     option = courier_menu_input()   
# #     if option == '1':
# #         print_couriers()
# #     elif option == '2':
# #         create_courier()
# #     elif option == '3':
# #         update_courier()
# #     elif option == '4':
# #         delete_couriers()
# #     elif option == '0':
# #         main_menu_input()
# #     else:
# #         print('Invalid selection. Please choose again')
# # elif option == '0':
# #         print("Exiting..")
# #         exit_app()
# # else:
# #     print("\nInvalid Selection\n")

    
# # #save app state ask instructor 
# # #add loops 
# # #add or cancels 

def print_all(filename, what): 
    with open( filename , 'r') as file:
        csv_file = csv.DictReader(file)
        print(f'Here is our current list of {what}:\n')
        for row in csv_file:
            print (dict(row))

def fill_lists(filename): #ask colin. 
    with open( filename , 'r') as file:
        csv_file = csv.DictReader(file)
        list_ = list(csv_file)
        return list_
        
        file.close()
products = fill_lists('products.csv')




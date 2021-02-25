import os

def clear_terminal(): 
    os.system('clear')

def main_menu_input():
    clear_terminal()
    banner()
    print(f'\n\nMain menu')
    print('------------------------------------------------------')
    main_menu = (
        f' 0 - Exit app \n 1 - View product menu \n 2 - View courier menu \n 3 - View order menu')
    print(main_menu)
    option = str(input("\n\nWhat would you like to do? Choose an option number"))
    return option
#-------------------------------------------------
def menu_input(field): 
    clear_terminal()
    banner()
    print(f'\n\n{field} menu')
    print('------------------------------------------------------')
    menu =(f' 0 - Return back to main menu \n 1 - View all {field}s \n 2 - Create new {field} entry \n 3 - Delete {field}')
    if field == 'Order':
        menu =(f' 0 - Return back to main menu \n 1 - View all {field}s \n 2 - Create new {field} entry \n 3 - Update {field} status \n 4 - Delete {field}')
    print(menu)


    option = str(input("\nWhat would you like to do ? Choose an option number"))
    return option
#-------------------------------------------------
def exit_app():
    border = len('Thanks for stopping by Jammed Packed Lunches! See you soon.') * '*'
    print('\n' + border)
    print('Thanks for stopping by JAM\'D PACKED LUNCHES! See you soon.')
    print(border + '\n')
    exit()
#-------------------------------------------------
def banner():
    os.system('clear')
    cafe_name = ''
    cafe_name = str('* WELCOME TO \'JAM\'D PACKED LUNCHES*')
    border = len(cafe_name) * '*'
    print('\n' + border)
    print(cafe_name)
    print(border + '\n')

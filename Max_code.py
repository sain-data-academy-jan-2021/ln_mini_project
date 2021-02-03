
import os
os.system("clear")
import utils.functions as functions
import login
from time import sleep 


hot_drinks = [] 
cold_drinks = []
alco_drinks = []

with open("data/hot_drinks.txt", "r") as file:
    for product in file:
        hot_drinks.append(product.strip())

with open("data/cold_drinks.txt", "r") as file:
    for product in file:
        cold_drinks.append(product.strip())

with open("data/alco_drinks.txt", "r") as file:
    for product in file:
        alco_drinks.append(product.strip())

menu_select = ""
acceptable_values = [0, 1, 2, 3] 
   
while menu_select not in acceptable_values:
    menu_select = functions.main_menu()

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
while menu_select != "0":
    if menu_select == 1:

        num_select = input("1.) Hot Drinks Menu     2.) Cold Drinks Menu    3.) Alcoholic Drinks Menu   0.) Exit. ")
        

        while num_select != "0":
            if num_select == "1":
                functions.item_menu("Hot Drink", hot_drinks)
                
            elif num_select == "2":
                functions.item_menu("Cold Drink", cold_drinks)
                
            elif num_select == "3":
                functions.item_menu("Alcoholic Drink", alco_drinks)

                
            else:
                print("Please enter a vaild number.")

            num_select = input("1.) Hot Drinks Menu     2.) Cold Drinks Menu    3.) Alcoholic Drinks Menu   0.) Exit. ")

        with open("data/hot_drinks.txt", "w") as file:
            for drink in hot_drinks:
                file.write(drink + '\n')
        with open("data/cold_drinks.txt", "w") as file:
            for drink in cold_drinks:
                file.write(drink + '\n')
        with open("data/alco_drinks.txt", "w") as file:
            for drink in alco_drinks:
                file.write(drink + '\n')
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------ 
        
        print("Thankyou. Here is our full menu list.")
        print(hot_drinks)
        print(cold_drinks)
        print(alco_drinks)

        menu_select = functions.main_menu()

        # drinks = input("Alright, Lets get you started. What would you like to drink? ")

        # drink_amount = [1, 2, 3, 4, 5]



        # if drinks in hot_drinks:
        #     how_many_hot = input("Nice choice on a cold day like today! How many would you like? ")
        #     how_many_num_hot = int(how_many_hot)
        #     if how_many_num_hot in drink_amount:
        #         print("Great, we'll have those ready for you in a moment.")
        #     else:
        #         print("Sorry, maximum 5 per customer. Please try again.")  



        # elif drinks in cold_drinks:
        #     how_many_cold = input("Nothing better that a nice cold refreshment! How many would you like? ")
        #     how_many_num_cold = int(how_many_cold)
        #     if how_many_num_cold in drink_amount:
        #         print("Great, we'll have those ready for you in a moment.")
        #     else:
        #         print("Sorry, maximum 5 per customer. Please try again.")


        # elif drinks in alco_drinks:
        #     age_check = int(input("Awesome, we just need to make sure you are old enough. Please enter age: "))
        #     age_limit = 18
        #     if age_check >= age_limit:
        #         how_many_alco = input("Thankyou. How many would you like? ")
        #         how_many_num_alco = int(how_many_alco)
        #         if how_many_num_alco in drink_amount:
        #             print("Great, we'll have those ready for you soon!")
        #         else:
        #             print("Sorry, maximum 5 per customer. Please try again.")
        #     elif age_check < age_limit:
        #         print("Sorry, you are too young to buy these products. Please try again.")
        #     else:
        #         print("Sorry, invalid selection. Please try again.")

            
        # else:
        #     print("Sorry we dont have that available right now. Please make another selection.")


    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------


    elif menu_select == 2:

        courier_names = []
    
        with open("data/courier_list.txt", "r") as file:
            for name in file:
                courier_names.append(name.strip())
        
        functions.item_menu("Courier ", courier_names)


        with open("data/courier_list.txt", "w") as file:
            for name in courier_names:
                file.write(name + '\n')

        menu_select = functions.main_menu()


    # -------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------
        


    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    elif menu_select == 0:
        print('Thankyou!')
        exit()

rate = input("Thankyou for your order. Would you mind leaving a review for us today? ")

rate_y = ["Yes", "yes", "y", "Y"]
rate_n = ["No", "no", "n", "N"]
rate_stars = [1,2,3,4,5]

if rate in rate_y:
        rate_stars_y = int(input("Thankyou! How many stars out of 5 would you give our service? "))
        print("Thanks, we'll take that onboard. Until next time!")
elif rate in rate_n:
    print("Ok no problem. Until next time!")
else:
        print("Sorry, invalid selection. Please try again.")




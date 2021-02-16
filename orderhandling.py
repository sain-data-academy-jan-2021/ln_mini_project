# order = input('What would you like to order or 0 to exit').title()
# pr
print('Hi')

# totalCost = 0
# while order!='q':
#     for line in file:
#         data = line.split(',')
#         item_desc = data[0]
#         item_price = float(data[1])
#     # if item_desc == order:
#         print(item_desc + ' - £' + str(item_price))
#         totalCost = totalCost + item_priceq
#     order = input('Choose another item or q to finish')        
#     else:
#          order == 'q':
#             break
# print('Total cost = £' + str(totalCost))

# file.close()

#  while True:
#         print("*" * 32 + "PAYMENT" + "*" * 33 + "\n") # Header &amp; Styling
#         total_price = 0 # alloc/init a variable to handle total_price
 
#         report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())&#91;:19] + "\n" + " " * 17 + "-" * 35 #building up report string header
#         i = 0
#         while i &lt; len(list_item_order): #Enumarating order array items and summing up its prices * quantities
#             if(list_item_order&#91;i] != 0):
#                 if (i >= 0) and (i &lt; 40):
#                     report_new += "\n" + " " * 17 + str(list_foods&#91;i]) + "  x  " + str(list_item_order&#91;i]) # string appending the formated food name and formated order structure from quantity and final price
#                     print(" " * 17 + str(list_foods&#91;i]) + "  x  " + str(list_item_order&#91;i])) #print it out
#                     total_price += list_item_price&#91;i] * list_item_order&#91;i] # Calculating the total price for food
#                 if (i >= 40) and (i &lt; 80):
#                     report_new += "\n" + " " * 17 + str(list_drinks&#91;i - 40]) + "  x  " + str(list_item_order&#91;i])
#                     print(" " * 17 + str(list_drinks&#91;i - 40]) + "   x  " + str(list_item_order&#91;i]))
#                     total_price += list_item_price&#91;i] * list_item_order&#91;i] # Calculating the total price for drinks
#                 if (i >= 80) and (i &lt; 100):
#                     report_new += "\n" + " " * 17 + str(list_services&#91;i - 80])
#                     print(" " * 17 + str(list_services&#91;i - 80]))
#                     total_price += list_item_price&#91;i] * list_item_order&#91;i] # Calculating the total price for services
#                 i += 1
#             else:
#                 i += 1

#     input_1 = str(input("Please Select Your Operation: ")).upper()
#         if (input_1 == 'P'):
#             print("\n" * 10)
#             print("Successfully Paid!")
#             file_report = open('files'+navigator_symbol+'report.fsd', 'a') # Save it into a file
#             file_report.write(report_new)
#             file_report.close()
#             def_default() #Reset the program for the name order
#         elif (input_1 == 'M'):
#             print("\n" * 10)
#             def_main() #Navigate back to the main menu
#             break
#         elif (input_1 == 'R'):
#             print("\n" * 10)
#             def_report() # Navigate to the reports
#             break
#         elif ('E' in input_1) or ('e' in input_1):
#             print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
#             break
#         else:
#             print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try a
#          try:        #Cautions Error Handling to prevent program crashing and hand out exceptions as a readable error to notify user
#                 int(input_1)
#                 if ((int(input_1) &lt;= len(list_foods) and int(input_1) > 0) or (int(input_1) &lt;= len(list_drinks) + 40 and int(input_1) > 40)):
#                      try:
#                         print("\n" + "_" * 72 + "\n" + str(list_foods&#91;int(input_1) - 1])) # Handling Food Selection / The try/Execpt to handle out of index error as if it  not exists in the array
#                      except:
#                         pass
#                      try:
#                          print("\n" + "_" * 72 + "\n" + str(list_drinks&#91;int(input_1) - 41])) # Handling Drinks Selection / The try/Execpt to handle out of index error as if it  not exists in the array
#                      except:
#                         pass
 
#                      input_2 = input("How Many You Want to Order?: ").upper() # Handling Quantity input
#                      if int(input_2) > 0:
#                         list_item_order&#91;int(input_1) - 1] += int(input_2) # adding item to Orders Array
#                         print("\n" * 10)
#                         print("Successfully Ordered!")
#                         def_food_drink_order() # Return food/drinks Menu
#                         break
#                      else:
#                         print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
#             # except:
#                 print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

# #tabuate
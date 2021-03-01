# ef choose_order_items(connection): #done

#     print_whole_table("Products","prod_type")

#     existing_ids = [id[0] for id in execute_sql_select(connection,'SELECT product_id FROM Products')]
#     chosen_products_ids = []

#     id = ''

#     total_cost = 0
#     final_basket = []
#     while id !=0:

#         id = int(input('Please choose the ID to order. When you have chosen all press 0:'))
        
#         if id not in existing_ids and id !=0: 
#             print('Invalid ID. Please try again')

#         elif id in existing_ids:
#             quantity = int(input('How many do you want')) 
#             myresult = execute_sql_select(connection,f'SELECT prod_name, unit, price FROM Products where product_id = "{id}"')
#             for x in myresult:
#                 basket = (f'Product: {x[0]}, Unit: {x[1]}, Quantity: {quantity}, Price: {x[2]* quantity}')

#                 price = x[2] * quantity

#             total_cost = total_cost + price
#             chosen_products_ids.extend([id] * quantity )
#             print(chosen_products_ids)
#             final_basket.append(basket)



#             SQL JOIN: 


# SELECT o.name AS 'Customer Name',
#  o.address as Address,
#  o.phone as 'Phone Number',
#  o.name as Courier,
#  o.status as Status,
#  GROUP_CONCAT(p.prod_name separator ', ') AS Items 
# FROM Orders o
# LEFT JOIN Order_product op 
#  ON op.order_id = o.order_id
# LEFT JOIN Products p 
#  ON op.product_id = p.product_id
# LEFT JOIN Couriers c 
#  ON o.courier_id = c.courier_id
# GROUP BY o.order_id;

#  @patch('orderhandling.execute_sql_select') 
#     @patch('builtins.input')
#     def test_choose_extreme_order_items(self, mock_input, mock_execute):
#         #Assemble
#         mock_execute.side_effect = [((4,), (9,), (12,), (13,)), (('Carrot cake', 'slice', 2.29),), (('Coke', '500ml', 0.60),)]
#         # connection = None
#         mock_input.side_effect = ['4','50','9','60','0']
#         expected = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9], 150.5
#         #Act
#         actual = choose_order_items(None)
#         #Assert
#         self.assertEqual(actual,expected)



import unittest
from unittest.mock import patch
from functions import *
from unittest import mock
from orderhandling import choose_order_items


# @patch('functions.print_whole_table',lambda x,y: None) #always goes last w lambda

class TestFunctions(unittest.TestCase):

    # # @patch('functions.input')
    # # @patch('functions.execute_sql_select')
    # # def test_delete_entry_breaks_on_zero(self, mock_select, mock_input): #arguements mirror order to patchs
    # # #happy, common
    # #     #Assemble 
    # #     mock_input.return_value = '0'

    # #     #Act 
    # #     delete_entry('test', 'test', 'test')

    # #     #Assert 
    # #     assert mock_select.call_count == 0 

    # # @patch('functions.input')
    # # @patch('functions.execute_sql_select')
    # # @patch('functions.execute_sql')
    # # def test_delete_entry_calls_correct_sql(self, mock_execute, mock_select, mock_input):

    # #     #Assemble
    # #     mock_select.return_value = 'a'

    # #     expected = ('DELETE FROM Testtable WHERE testitem = "1"')
    # #     mock_input.side_effect = [1,0]

    # #     #Act
    # #     delete_entry('Testtable','testcolumn', 'testitem')

    # #     #Assert
    # #     mock_execute.assert_called_with(mock.ANY, expected)

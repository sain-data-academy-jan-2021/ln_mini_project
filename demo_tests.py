import unittest
from unittest.mock import patch
from functions import *
from unittest import mock
from orderhandling import choose_order_items


class TestFunctions(unittest.TestCase):

    #HAPPY PATH - COMMON CASE - ENTERING SUITABLE INTEGER :)
    # -------------------------------------------------------------------- 
    @patch('orderhandling.execute_sql_select') 
    @patch('builtins.input')
    def test_choose_normalamount_order_items(self, mock_input, mock_execute):
        #Assemble
        mock_execute.side_effect = [((4,), (9,), (12,), (13,)), (('Carrot cake', 'slice', 2.29),), (('Coke', '500ml', 0.60),)]
        # connection = None
        mock_input.side_effect = ['4','1','9','1','0']
        
        expected = [4,9], 2.89
        #Act
        actual = choose_order_items(None)
        #Assert
        self.assertEqual(actual,expected)

    # #UNHAPPY PATH - EDGE CASE - MINIMUM :(
    # # -------------------------------------------------------------------- 
    @patch('orderhandling.execute_sql_select') 
    @patch('builtins.input')
    def test_choose_minimum_order_items(self, mock_input, mock_execute):
        #Assemble
        mock_execute.side_effect = [((4,), (9,), (12,), (13,)), (('Carrot cake', 'slice', 2.29),), (('Coke', '500ml', 0.60),)]
        # connection = None
        mock_input.side_effect = ['4','0','0']
        expected = [],0
        actual = choose_order_items(None)
        #Assert
        self.assertEqual(actual,expected) 

    # #UNHAPPY PATH - EDGE CASE - 'MAXIMUM' :( 
    # # -------------------------------------------------------------------- 
    @patch('orderhandling.execute_sql_select') #EDGE CASE MAXIMUM(10,000)
    @patch('builtins.input')
    def test_choose_extreme_order_items(self, mock_input, mock_execute):
        #Assemble
        mock_execute.side_effect = [((4,), (9,), (12,), (13,)), (('Carrot cake', 'slice', 2.29),), (('Coke', '500ml', 0.60),)]
        # connection = None
        mock_input.side_effect = ['4','1','9','10000','0']
        list = [4,]
        for x in range(0,10000):
            list.extend([9])
        expected = list,6002.29
        #Act
        actual = choose_order_items(None)
        #Assert
        self.assertEqual(actual,expected)

    # #UNHAPPY PATH - CORNER CASE - NOT ENTERING AN INTEGER :( 
    # # ----------------------------------------------------------------
     
    @patch('orderhandling.execute_sql_select')                        
    @patch('builtins.input')
    def test_choose_strquantity_order_items(self, mock_input, mock_execute):
        #Assemble
        mock_execute.side_effect = [((4,), (9,), (12,), (13,)), (('Carrot cake', 'slice', 2.29),)]
        # connection = None
        mock_input.side_effect = ['two','4','1','0']
        expected = [4],2.29
        actual = choose_order_items(None)
        #Assert#1
        self.assertEqual(actual,expected) 
        #Assert#2
        self.assertRaises(ValueError) 
        print('ValueError captured')
    
if __name__ == '__main__':
    unittest.main()

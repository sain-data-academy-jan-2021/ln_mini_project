code = input('Enter code of your order')
file = open(#import csv file#,'r')

totalCost = 0
while (code!='#quit')
    for line in file 
    data = line.split(',')
    item_code = data[0]
    item_desc = data[1]
    item_price = float(data[2])
    if item_code == code 
        print(item_code + '-' + item_desc + ' - £' + str(item_price)
        total_cost = total_cost
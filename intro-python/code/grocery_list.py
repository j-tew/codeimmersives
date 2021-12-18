grocery_list = {'2021-1-3':{'milk': 4.99},
                '2021-1-10':{'milk': 4.99,'eggs': 6.99, 'beer': 14.99},
                '2021-1-17':{'Milk': 4.99,'eggs': 7.99, 'coffee': 6.79},
                '2021-1-24':{'milk': 4.49,'diapers': 16.99, 'flour': 3.99},
                '2021-2-1':{'Broccoli': 2.99,'Onions': 1.99, 'peppers': 3.69},
                '2021-2-6':{'milk': 4.99,'eggs': 6.99, 'beer': 19.99},
                '2021-2-17':{'milk': 5.09,'broccoli': 2.79, 'beer': 21.99},
                '2021-2-28':{'Diapers': 4.99,'eggs': 6.99, 'beer': 17.99},
                '2021-3-5':{'Coffee': 6.19,'eggs': 6.99, 'beer': 18.99},
                '2021-3-13':{'diapers': 4.99,'eggs': 6.49, 'Onions': 2.39},
                '2021-3-20':{'Flour': 4.19,'Beer': 17.99, 'Diapers': 12.99},
                '2021-4-1':{'milk': 5.29,'eggs': 7.59,'Flour': 4.39}}

# What was the total grocery bill for each month
Jan = [groceries for day,groceries in grocery_list.items() if day[5] == '1']
Feb = [groceries for day,groceries in grocery_list.items() if day[5] == '2']
Mar = [groceries for day,groceries in grocery_list.items() if day[5] == '3']

print(Jan, Feb, Mar)
# What was the average price paid for each commodity (remove misspellings) 


# Create a dictionary with the item name as key and the value a tuple with (the number of times item purchased,Total spent across all months)


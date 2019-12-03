# Compulsory Task 1

# List containing menu items
menu = ['burger', 'chips', 'pizza', 'hot-dog']

# Dictionary that has the stock number of each item
stock = {'burger': '10',
         'chips': '20',
         'pizza': '5',
         'hot-dog': '15'}

# # Dictionary that has the price value for each item
price = {'burger': '20',
         'chips': '10',
         'pizza': '50',
         'hot-dog': '12'}

# Declares an empty string that will be used to do the final calculation
total_all = 0

# This loop will run for every item in the list
for food in menu:
    total_item_value = int(stock[food]) * int(price[food])
    total_all += total_item_value

# Prints out the total value of all the items
print('The total value of all the items in the cafe is: R' + str(total_all))





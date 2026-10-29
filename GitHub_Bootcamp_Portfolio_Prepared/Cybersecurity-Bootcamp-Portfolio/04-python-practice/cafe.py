# create a list containing the items sold in the cafe
items_sold = ["coffee", "tea", "sandwich", "cake", "juice"]

#creat a dictionary containing the amount of stock
# for each item on the manue
stock = {
    "coffee": 10,
    "tea": 15,
    "sandwich": 5,
    "cake": 8,
    "juice": 12
}

# create a dictionary containing the price 
# of each item on the menu
prices = {
    "coffee": 60,
    "tea": 20,
    "sandwich": 50,
    "cake": 30,
    "juice": 25
}

# Creat a variable to store the total value of all the stock in the cafe
total_stock_value = 0

# loop through the items sold in the cafe
for item in items_sold:
    # calculate the value of the stock for the currentitem
    # stock quantity is multiplied by the price of the item
    item_stock_value = stock[item] * prices[item]

    # add the value of the current item to the total stock value
    total_stock_value = total_stock_value + item_stock_value

    #Print the total worth of the stock in the cafe
    print("Total Stock VAlue: ", total_stock_value)

# ask user to input three names of three products
product1 = input("Enter the name of the first product: ")       
product2 = input("Enter the name of the second product: ")       
product3 = input("Enter the name of the third product: ")

# ask user to input the prices of the three products
price_product1 = float(input("Enter the price of the first product: "))
price_product2 = float(input("Enter the price of the second product: "))
price_product3 = float(input("Enter the price of the third product: "))


# calculate the total price of all three products
total_price = float(price_product1 + price_product2 + price_product3)
total_price = round(total_price, 2)  
print(total_price)

# calculate the average price of the three products
average_price = float((price_product1 + price_product2 + price_product3) / 3)
average_price = round(average_price, 2)
print(average_price)


# The Total of [product1], [product2], [product3] is Rxx,xx
# and the average price of the items is Rxx,xx.”
print(f"The total of : {product1}, {product2}, {product3} is \
      R{total_price:.2f}, and the average price is R{average_price:.2f}")



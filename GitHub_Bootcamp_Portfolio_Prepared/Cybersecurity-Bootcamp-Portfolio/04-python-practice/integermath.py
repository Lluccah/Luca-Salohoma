# request user for 3 integers
number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))

# the sum of the numbers
sum_result = number1 + number2 + number3
print(sum_result)
# the first number minus the second number
subtraction_result = number1 - number2
print(subtraction_result)

# the third number multiplied by the first number
multiplication_result = number3 * number1
print(multiplication_result)    

# the sum of all three numbers divided by the third number
division_result = ((number1 + number2 + number3) / number3)
print(division_result)
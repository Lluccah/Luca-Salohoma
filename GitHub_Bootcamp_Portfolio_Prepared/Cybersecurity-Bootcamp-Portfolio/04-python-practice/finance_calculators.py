''' this program calculates either investment interest or bond repayments\
    based on user input'''

import math

# Display menu options to the user

print("investment - to calculate the amount of interest \
you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Prompt user to choose either 'investment' or 'bond'
# Store the input in a variable called 'calculation'
# Use a conditional statement to check the value of 'calculation'
# Perform calculations based on user choice
# If 'investment', calculate investment interest
# If 'bond', calculate bond repayments
# Prompt user to choose either 'investment' or 'bond'

calculation = input("enter either 'investment' or 'bond'\
 from the menu above \n").lower()\

if calculation == "investment":

    # if user's input is 'investment', calculate investment interest
    # Get user input for investment calculations
    # Prompt user for principal amount, interest rate, years, and interest type
    # Store inputs in appropriate variables
    # Use a conditional statement to check the interest type

    principal = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate\
(as a percentage, e.g., 5 for 5%): ")) / 100
    years = int(input("Enter the number of years you plan to invest: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    if interest_type == "simple":
        total_amount = principal * (1 + rate * years)
    elif interest_type == "compound":
        total_amount = principal * math.pow((1 + rate), years)
    else:
        print("Invalid interest type selected.\
  Please choose either 'simple' or 'compound'.")
        
# Display the total amount after the investment period

    print(f"The total amount after {years} years is: R{int(total_amount):.2f}")

# If 'bond', calculate bond repayments
# Get user input for bond calculations

elif calculation == "bond":

    # Prompt user for present value, interest rate, and months
    # Store inputs in appropriate variables
    # Calculate the monthly repayment using the bond formula
    
    principal = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the annual interest rate \
(as a percentage, e.g., 5 for 5%): ")) / 100
    months = int(input("Enter the number of months\
 you plan to take to repay the bond: "))
    
    # Calculate the monthly interest rate

    monthly_rate = annual_rate / 12

    monthly_payment = (monthly_rate * principal) / \
        (1 - math.pow((1 + monthly_rate), -months))
    print(f"The monthly payment for the bond is: R{monthly_payment:.2f}")

    # Display the monthly repayment amount
    # handle the case where the user input is invalid

else:
    print("Invalid selection. Please choose either 'investment' or 'bond'.")

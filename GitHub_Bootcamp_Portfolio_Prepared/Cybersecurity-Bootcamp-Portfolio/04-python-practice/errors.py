# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") 
# missing closing quotation mark
# syntax error fixed
print("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # name error name 'age_Str' is not defined
age = int(age_Str) # indention error
print("I'm "  +  str(age) +  " years old.") # indention error

    # Variables declaring additional years and printing the total years of age
years_from_now = int("3")
total_years = age + years_from_now # type error cannot concatenate 'str' and 'int' objects

print("The total number of years:" + str(total_years)) # missing parentheses in print statement

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12 + 6 # syntax error invalid syntax
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # missing parentheses in print statement

#HINT, 330 months is the correct answer
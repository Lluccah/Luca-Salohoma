# Program demonstrating different types of errors

name = "Alex"

# COMPILATION/SYNTAX ERROR 1:
# Missing closing quotation mark.
# Python cannot understand this line because the string is not closed.
message = "Hello, Alex

# COMPILATION/SYNTAX ERROR 2:
# Missing colon (:) after the if statement.
# Python requires a colon before the indented code block.
if name == "Alex"
    print("Welcome, Alex!")

age = 20

# RUNTIME ERROR:
# Dividing by zero causes a ZeroDivisionError when this line runs.
result = age / 0

# LOGICAL ERROR:
# The program adds 10 instead of subtracting 10.
# The code runs, but produces the wrong answer.
future_age = age + 10

print("Your age in 10 years is:", future_age)

# Import the os module to check whether a file exists
import os


# Define a function to perform calculations
def calculate():

    # Use try to handle errors if the user enters invalid input
    try:

        # Ask the user to enter the first number
        # Convert the input from a string to a float
        num1 = float(input("Enter the first number: "))

        # Ask the user to enter the second number
        # Convert the input from a string to a float
        num2 = float(input("Enter the second number: "))

        # Ask the user which mathematical operation to perform
        operation = input("Enter an operation (+, -, *, /): ").strip()

        # Check if the user selected addition
        if operation == "+":
            answer = num1 + num2

        # Check if the user selected subtraction
        elif operation == "-":
            answer = num1 - num2

        # Check if the user selected multiplication
        elif operation == "*":
            answer = num1 * num2

        # Check if the user selected division
        elif operation == "/":

            # Check whether the second number is zero
            # Division by zero is not allowed
            if num2 == 0:
                print("Error: You cannot divide by zero.")
                return  # Stop this function if division is impossible

            # Divide the first number by the second number
            answer = num1 / num2

        else:
            # Display an error if the operation is not supported
            print("Invalid operation. Please use +, -, *, or /.")
            return  # Stop the function when the operation is invalid

        # Display the calculation result
        print(f"Answer: {answer:g}")

        # Create a string containing the complete equation and answer
        # The :g format removes unnecessary decimal zeros
        equation = f"{num1:g} {operation} {num2:g} = {answer:g}"

        # Open equations.txt in append mode
        # Append mode adds new equations without deleting old ones
        # encoding="utf-8" supports standard text encoding
        with open("equations.txt", "a", encoding="utf-8") as file:

            # Write the equation to the file
            # \n moves the next equation to a new line
            file.write(equation + "\n")

        # Tell the user that the calculation was saved
        print("Calculation saved successfully.")

    # Handle errors when the user enters something that is not a number
    except ValueError:
        print("Error: Please enter valid numbers.")

    # Handle errors that may occur when writing to the file
    except OSError as error:
        print(f"File error: Could not save the calculation. {error}")


# Define a function to display previous calculations
def print_equations():

    # Check whether equations.txt exists
    if not os.path.exists("equations.txt"):

        # Inform the user if the file has not been created
        print("No previous calculations found.")

        # Stop the function because there is no file to read
        return

    # Use try to handle possible file-reading errors
    try:

        # Open equations.txt in read mode
        with open("equations.txt", "r", encoding="utf-8") as file:

            # Read all the saved equations into a list
            equations = file.readlines()

            # Check if the file contains no equations
            if not equations:
                print("No previous calculations found.")

            else:
                # Display a heading before listing the equations
                print("\nPrevious calculations:")

                # Loop through each saved equation
                for equation in equations:

                    # Print the equation without extra whitespace
                    # strip() removes the newline at the end
                    print(equation.strip())

    # Handle errors that occur while reading the file
    except OSError as error:
        print(f"File error: Could not read the calculations. {error}")


# Start the main program loop
# The loop keeps the calculator running until the user exits
while True:

    # Display the calculator menu
    print("\n===== Simple Calculator =====")
    print("1. Perform a calculation")
    print("2. View previous calculations")
    print("3. Exit")

    # Ask the user to choose an option
    # strip() removes spaces before and after the input
    choice = input("Choose an option (1-3): ").strip()

    # If the user enters 1, perform a calculation
    if choice == "1":
        calculate()

    # If the user enters 2, display saved equations
    elif choice == "2":
        print_equations()

    # If the user enters 3, exit the program
    elif choice == "3":
        print("Thank you for using the calculator.")

        # Break stops the while loop
        break

    # Handle any menu choice other than 1, 2, or 3
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
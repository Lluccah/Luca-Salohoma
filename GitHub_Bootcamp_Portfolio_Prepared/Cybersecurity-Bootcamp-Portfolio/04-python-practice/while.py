# Program to calculate the average of user-entered numbers until -1 is entered
# Initialize total and count variables to store the sum and count of numbers
total = 0
count = 0

# Start an infinite loop to continuously ask for user input
# keep asking for numbers until the user enters -1
while True:
    try:
       user_input = int(input("Enter a number "))
# handle the case where the input is not a valid number       
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
# check if the user entered -1 to exit the loop    
    if user_input == -1:
        break

    total += user_input
    count += 1    
# After exiting the loop, calculate and print the average of the entered numbers
# Check if count is greater than 0 to avoid division by zero
if count > 0:
# calculate the average    
    average = total / count
    print("Average:", average)
# if no numbers were entered, print a message

else:
    print("No numbers were entered.")       
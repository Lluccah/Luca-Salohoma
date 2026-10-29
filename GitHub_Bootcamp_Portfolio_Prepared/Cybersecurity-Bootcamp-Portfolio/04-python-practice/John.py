 # john program

# create an empty list to store all incorrect names entered by the user
incorrect_name = []

# ask user to enter their name
name = input("Enter your name: ")

# keep asking the user to enter their name until they enter "John"
while name != "John":
    # add the incorrect name  to the list of incorrect names
    incorrect_name.append(name)

# ask the user to enter their name again
    name = input("Incorrect name. Please enter your name again: ")

# print the heading before printing the list of the incorrect names entered by the user
print("Incorrect names entered:", incorrect_name)   

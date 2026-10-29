
# open the DOB.txt file in read mode 
with open(r"C:/Users/fefem/OneDrive/Luca Desk top/Cyber security School/DOB.txt", "r") as file:
    # read all lines from the file
    contents = file.readlines()

    # print the name section
    print("Name:")

    # go through every line in the file
    for line in contents:
        # Remove spaces and newline character
        line = line.strip()

        # split the line into saparate words 
        parts = line.split()

        # print the person's name and last name 
        print(parts[0], parts[1])

        # print the birthdate section
    print("\nBirthdate:") 

    # go through every line in the file
    for line in contents:
        # Remove spaces and newline character
        line = line.strip()

        # split the line into saparate words 
        parts = line.split()

        # print the birthdate (day, month, and year)
        print(parts[2], parts[3], parts[4])


    
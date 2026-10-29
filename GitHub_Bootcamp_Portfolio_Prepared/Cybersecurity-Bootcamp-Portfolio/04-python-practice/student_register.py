# Ask the user how many students are registering
num_students = int(input("How many students are registering? "))

# Open the file called reg_form.txt
# "w" means write mode
with open("reg_form.txt", "w") as file:
    # create a for loop that repeats for each student
    for i in range(num_students):
        # Ask the user the enter the students ID number 
        student_id = input("Enter the ID number for student: ")

        # Write the student ID number into the txt file 
        # \n moves to the next line
        file.write(student_id + "\n")

        # Write a dotted line after each student ID number for better readability
        # The * 30 creats 30 dots in a row
        file.write("." * 30 + "\n")

        # Display a massage when the registration is complete
        print("Registration complete for student ID:", student_id)
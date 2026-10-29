
# Create the Course class
class Course:

    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Method to display the head office location
    def head_office_location(self):
        print("The head office is located in Cape Town.")


# Create the OOPCourse subclass
# OOPCourse inherits from the Course class
class OOPCourse(Course):

    # Constructor for the OOPCourse class
    def __init__(self):

        # Store the description of the course
        self.description = "OOP Fundamentals"

        # Store the name of the trainer
        self.trainer = "Mr Anon A. Mouse"

    # Method to display the course description and trainer
    def trainer_details(self):
        print("Course:", self.description)
        print("Trainer:", self.trainer)

    # Method to display the course ID
    def show_course_id(self):
        print("Course ID: #12345")


# Create an object of the OOPCourse class
course_1 = OOPCourse()

# Call the contact_details method inherited from Course
course_1.contact_details()

# Call the head_office_location method from Course
course_1.head_office_location()

# Call the trainer_details method from OOPCourse
course_1.trainer_details()

# Call the show_course_id method from OOPCourse
course_1.show_course_id()


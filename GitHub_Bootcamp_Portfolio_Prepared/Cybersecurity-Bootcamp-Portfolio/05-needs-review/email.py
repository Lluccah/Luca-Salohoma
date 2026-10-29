
# Create an Email class
class Email:

    # Create the constructor
    # It receives the email address, subject, and email content
    def __init__(self, email_address, subject_line, email_content):

        # Store the sender's email address
        self.email_address = email_address

        # Store the subject of the email
        self.subject_line = subject_line

        # Store the content of the email
        self.email_content = email_content

        # New emails have not been read yet
        self.has_been_read = False

    # Create a method to mark an email as read
    def mark_as_read(self):

        # Change has_been_read from False to True
        self.has_been_read = True


# Create an empty list to store Email objects
inbox = []


# Create a function to add sample emails to the inbox
def populate_inbox():

    # Create the first email object
    email_1 = Email(
        "welcome@hyperiondev.com",
        "Welcome to HyperionDev!",
        "Welcome to HyperionDev! We are happy to have you."
    )

    # Add the first email to the inbox
    inbox.append(email_1)

    # Create the second email object
    email_2 = Email(
        "support@hyperiondev.com",
        "Great work on the bootcamp!",
        "Keep up the great work on your coding journey."
    )

    # Add the second email to the inbox
    inbox.append(email_2)

    # Create the third email object
    email_3 = Email(
        "results@hyperiondev.com",
        "Your excellent marks!",
        "Congratulations on your excellent marks!"
    )

    # Add the third email to the inbox
    inbox.append(email_3)


# Create a function to display all emails in the inbox
def list_emails():

    # Display a heading
    print("\nInbox:")

    # enumerate() gives us both the index and the email object
    for index, email in enumerate(inbox):

        # Display the index and subject of each email
        print(f"{index} {email.subject_line}")


# Create a function to read a selected email
def read_email(index):

    # Check that the index is valid
    if index < 0 or index >= len(inbox):
        print("Invalid email number.")
        return

    # Get the email at the selected position
    email = inbox[index]

    # Display the email details
    print("\n---------- Email ----------")
    print(f"From: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content: {email.email_content}")

    # Mark the email as read
    email.mark_as_read()

    # Inform the user that the email has been marked as read
    print(f"\nEmail from {email.email_address} marked as read.\n")


# Populate the inbox with the three sample emails
populate_inbox()


# Start the main program loop
while True:

    # Display the menu
    print("\n========== Email Simulator ==========")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit")

    # Ask the user to choose an option
    choice = input("Enter your choice: ").strip()

    # Option 1: Read an email
    if choice == "1":

        # Display the emails so the user can select one
        list_emails()

        try:
            # Ask the user which email they want to read
            email_index = int(input("\nEnter the email number to read: "))

            # Read the selected email
            read_email(email_index)

        # Handle invalid input such as letters
        except ValueError:
            print("Please enter a valid number.")

    # Option 2: View unread emails
    elif choice == "2":

        # Display a heading
        print("\nUnread emails:")

        # Keep track of whether we found an unread email
        unread_found = False

        # Loop through all emails in the inbox
        for index, email in enumerate(inbox):

            # Check whether the email has been read
            if not email.has_been_read:

                # Display the index and subject
                print(f"{index} {email.subject_line}")

                # An unread email was found
                unread_found = True

        # If no unread emails were found
        if not unread_found:
            print("There are no unread emails.")

    # Option 3: Quit the application
    elif choice == "3":

        # Display a goodbye message
        print("\nThank you for using the Email Simulator.")
        break

    # Handle an invalid menu choice
    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")
```

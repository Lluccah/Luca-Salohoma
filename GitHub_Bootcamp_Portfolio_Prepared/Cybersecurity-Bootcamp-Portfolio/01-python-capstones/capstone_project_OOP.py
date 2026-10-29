
# Import the csv module to read and write inventory.txt
import csv


# Create a class to represent a shoe in the inventory
class Shoe:

    # Initialise the attributes for each shoe object
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    # Return the cost of one shoe
    def get_cost(self):
        return self.cost

    # Return the quantity of shoes in stock
    def get_quantity(self):
        return self.quantity

    # Return the shoe details as a readable string
    def __str__(self):
        return (
            f"Country: {self.country}\n"
            f"Code: {self.code}\n"
            f"Product: {self.product}\n"
            f"Cost: R{self.cost:.2f}\n"
            f"Quantity: {self.quantity}"
        )


# Create an empty list to store Shoe objects
shoes_list = []


# Read shoe data from inventory.txt
def read_shoes_data():

    # Clear the list to prevent duplicate records if loaded again
    shoes_list.clear()

    try:
        # Open the inventory file in read mode
        with open("inventory.txt", "r", newline="",
                  encoding="utf-8") as file:

            # Read the CSV file using the column headings
            reader = csv.DictReader(file)

            # Check that the file contains the required columns
            required_columns = {
                "Country", "Code", "Product", "Cost", "Quantity"
            }

            if not reader.fieldnames or not required_columns.issubset(
                    reader.fieldnames):
                print("Error: The inventory file has incorrect headings.")
                return

            # Read each shoe record from the file
            for line_number, row in enumerate(reader, start=2):

                try:
                    # Get the information for the current shoe
                    country = row["Country"].strip()
                    code = row["Code"].strip()
                    product = row["Product"].strip()
                    cost = float(row["Cost"])
                    quantity = int(row["Quantity"])

                    # Check that the values are valid
                    if not country or not code or not product:
                        raise ValueError("A text field is empty.")

                    if cost < 0 or quantity < 0:
                        raise ValueError("Negative values are not allowed.")

                    # Create a Shoe object from the file data
                    shoe = Shoe(
                        country, code, product, cost, quantity
                    )

                    # Add the shoe object to the list
                    shoes_list.append(shoe)

                except (ValueError, TypeError, AttributeError) as error:
                    # Report an invalid record without stopping the
                    # program from reading the remaining records
                    print(
                        f"Invalid data on line {line_number}: {error}"
                    )

        # Display how many records were loaded
        print(f"Loaded {len(shoes_list)} shoe records.")

    # Handle a missing inventory file
    except FileNotFoundError:
        print("Error: inventory.txt was not found.")

    # Handle other file-related errors
    except OSError as error:
        print(f"Error reading the inventory file: {error}")


# Save the current shoe list to inventory.txt
def update_inventory_file():

    try:
        # Open the file in write mode to save the current records
        with open("inventory.txt", "w", newline="",
                  encoding="utf-8") as file:

            # Define the column headings in the correct order
            fieldnames = [
                "Country", "Code", "Product", "Cost", "Quantity"
            ]

            # Create a CSV writer
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the headings as the first row
            writer.writeheader()

            # Write every shoe object to the file
            for shoe in shoes_list:
                writer.writerow({
                    "Country": shoe.country,
                    "Code": shoe.code,
                    "Product": shoe.product,
                    "Cost": shoe.cost,
                    "Quantity": shoe.quantity
                })

        return True

    # Handle errors when saving the inventory
    except OSError as error:
        print(f"Error saving inventory.txt: {error}")
        return False


# Allow the user to add a new shoe
def capture_shoes():

    print("\n--- Capture New Shoe ---")

    # Ask the user for the shoe details
    country = input("Enter country: ").strip()
    code = input("Enter shoe code: ").strip()
    product = input("Enter product name: ").strip()

    # Make sure the text fields are not empty
    if not country or not code or not product:
        print("Country, code and product cannot be empty.")
        return

    # Check that the shoe code is not already in the inventory
    for shoe in shoes_list:
        if shoe.code.lower() == code.lower():
            print("This shoe code already exists.")
            return

    # Ask for a valid cost
    while True:
        try:
            cost = float(input("Enter cost: "))

            if cost < 0:
                print("Cost cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number for the cost.")

    # Ask for a valid whole-number quantity
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a whole number for the quantity.")

    # Create a new Shoe object
    new_shoe = Shoe(country, code, product, cost, quantity)

    # Add the object to the inventory list
    shoes_list.append(new_shoe)

    # Save the updated list to the file
    if update_inventory_file():
        print(f"{product} was added to the inventory.")
    else:
        # Remove the new object if saving failed
        shoes_list.remove(new_shoe)
        print("The new shoe could not be saved.")


# Display all shoes in the inventory
def view_all():

    # Check whether there are any shoes to display
    if not shoes_list:
        print("\nThe inventory is empty.")
        return

    print("\n--- All Shoes in Inventory ---")

    # Print the details of every shoe object
    for shoe in shoes_list:
        print(shoe)
        print("-" * 35)


# Find the shoe with the lowest quantity and restock it
def re_stock():

    # Make sure there are shoes to check
    if not shoes_list:
        print("\nThe inventory is empty.")
        return

    # Find the shoe with the smallest quantity
    lowest_shoe = min(shoes_list, key=lambda shoe: shoe.quantity)

    # Display the shoe that needs restocking
    print("\n--- Restock Information ---")
    print(lowest_shoe)

    # Ask whether the user wants to restock this shoe
    choice = input(
        "Would you like to restock this shoe? (yes/no): "
    ).strip().lower()

    if choice == "yes":

        # Ask how many additional shoes to add
        while True:
            try:
                amount = int(input("Enter quantity to add: "))

                if amount <= 0:
                    print("Enter a number greater than zero.")
                    continue

                break

            except ValueError:
                print("Please enter a valid whole number.")

        # Remember the original quantity in case saving fails
        old_quantity = lowest_shoe.quantity

        # Increase the stock quantity
        lowest_shoe.quantity += amount

        # Save the updated quantity to the inventory file
        if update_inventory_file():
            print(
                f"Stock updated. New quantity: "
                f"{lowest_shoe.quantity}"
            )
        else:
            # Restore the original quantity if saving failed
            lowest_shoe.quantity = old_quantity
            print("The stock update could not be saved.")

    elif choice == "no":
        print("No stock was added.")

    else:
        print("Invalid choice. Please enter yes or no.")


# Search for a shoe by its code
def search_shoe():

    # Ask the user to enter the shoe code
    search_code = input("Enter the shoe code: ").strip()

    # Look through the inventory for a matching code
    for shoe in shoes_list:
        if shoe.code.lower() == search_code.lower():

            # Display and return the matching shoe object
            print("\n--- Shoe Found ---")
            print(shoe)
            return shoe

    # Inform the user if no matching shoe exists
    print("No shoe was found with that code.")
    return None


# Calculate and display the total value of every stock item
def value_per_item():

    # Check whether there are shoes in the inventory
    if not shoes_list:
        print("\nThe inventory is empty.")
        return

    print("\n--- Value of Each Stock Item ---")

    # Calculate the value of each product
    for shoe in shoes_list:

        # Value is the cost multiplied by the quantity
        total_value = shoe.get_cost() * shoe.get_quantity()

        # Display the result with clear labels
        print(f"Product: {shoe.product}")
        print(f"Code: {shoe.code}")
        print(f"Cost per shoe: R{shoe.cost:.2f}")
        print(f"Quantity: {shoe.quantity}")
        print(f"Total value: R{total_value:.2f}")
        print("-" * 35)


# Find the shoe with the highest quantity
def highest_qty():

    # Check whether there are shoes in the inventory
    if not shoes_list:
        print("\nThe inventory is empty.")
        return

    # Find the shoe with the greatest quantity
    highest_shoe = max(shoes_list, key=lambda shoe: shoe.quantity)

    # Display the shoe that has the highest stock
    print("\n--- Shoe with Highest Quantity ---")
    print(highest_shoe)
    print(f"{highest_shoe.product} is available for sale.")


# Load the existing inventory when the program starts
read_shoes_data()


# Keep displaying the menu until the user exits
while True:

    print("\n========== NIKE INVENTORY MANAGER ==========")
    print("1. View all shoes")
    print("2. Search for a shoe by code")
    print("3. Restock shoe with lowest quantity")
    print("4. Calculate value per item")
    print("5. Show shoe with highest quantity")
    print("6. Capture a new shoe")
    print("7. Exit")
    print("============================================")

    # Get the user's menu choice
    choice = input("Choose an option (1-7): ").strip()

    # Run the function selected by the user
    if choice == "1":
        view_all()

    elif choice == "2":
        search_shoe()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        value_per_item()

    elif choice == "5":
        highest_qty()

    elif choice == "6":
        capture_shoes()

    elif choice == "7":
        print("Thank you for using the Nike Inventory Manager.")
        break

    else:
        # Handle invalid menu selections
        print("Invalid choice. Please enter a number from 1 to 7.")
        
"""
Nike warehouse inventory manager.

Keep this Python file and inventory.txt in the same folder.
The program reads and updates inventory.txt.
"""

import csv
import os

INVENTORY_FILE = os.path.join(os.path.dirname(__file__), "inventory.txt")


class Shoe:
    """Stores information about one shoe product."""

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of one item."""
        return self.cost

    def get_quantity(self):
        """Return the number of items in stock."""
        return self.quantity

    def __str__(self):
        """Return a readable description of this shoe."""
        return (
            f"Country: {self.country}, Code: {self.code}, "
            f"Product: {self.product}, Cost: R{self.cost:.2f}, "
            f"Quantity: {self.quantity}"
        )


shoes_list = []


def read_shoes_data():
    """Read shoe records from inventory.txt into shoes_list."""
    shoes_list.clear()

    try:
        with open(INVENTORY_FILE, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            required_headers = {
                "Country", "Code", "Product", "Cost", "Quantity"
            }
            if not reader.fieldnames or not required_headers.issubset(
                set(reader.fieldnames)
            ):
                print("Error: inventory.txt has missing or incorrect headers.")
                return

            for line_number, row in enumerate(reader, start=2):
                try:
                    shoe = Shoe(
                        row["Country"].strip(),
                        row["Code"].strip(),
                        row["Product"].strip(),
                        row["Cost"].strip(),
                        row["Quantity"].strip(),
                    )
                    shoes_list.append(shoe)
                except (TypeError, ValueError):
                    print(
                        f"Warning: Skipping invalid inventory row "
                        f"{line_number}."
                    )

    except FileNotFoundError:
        print("Error: inventory.txt was not found.")
        print("Keep inventory.py and inventory.txt in the same folder.")
    except OSError as error:
        print(f"Could not read inventory.txt: {error}")


def update_inventory_file():
    """Save all current shoe records back to inventory.txt."""
    try:
        with open(INVENTORY_FILE, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["Country", "Code", "Product", "Cost", "Quantity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for shoe in shoes_list:
                writer.writerow({
                    "Country": shoe.country,
                    "Code": shoe.code,
                    "Product": shoe.product,
                    "Cost": f"{shoe.cost:g}",
                    "Quantity": shoe.quantity,
                })
        return True
    except OSError as error:
        print(f"Could not save inventory.txt: {error}")
        return False


def capture_shoes():
    """Ask the user for a new shoe record and save it."""
    print("\nEnter the new shoe details.")
    country = input("Country: ").strip()
    code = input("Code: ").strip()
    product = input("Product: ").strip()

    try:
        cost = float(input("Cost: R"))
        quantity = int(input("Quantity: "))
        if cost < 0 or quantity < 0:
            print("Cost and quantity cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid number for cost and quantity.")
        return

    if not country or not code or not product:
        print("Country, code, and product cannot be empty.")
        return

    shoes_list.append(Shoe(country, code, product, cost, quantity))
    if update_inventory_file():
        print("Shoe added successfully.")
    else:
        shoes_list.pop()


def view_all():
    """Display all shoe records."""
    if not shoes_list:
        print("No inventory records were loaded.")
        return

    print("\n--- All Shoes ---")
    for shoe in shoes_list:
        print(shoe)


def re_stock():
    """Find the shoe with the lowest stock and optionally add stock."""
    if not shoes_list:
        print("No inventory records were loaded.")
        return

    lowest_stock_shoe = min(shoes_list, key=lambda shoe: shoe.quantity)
    print("\nShoe with the lowest quantity:")
    print(lowest_stock_shoe)

    answer = input("Do you want to add stock to this shoe? (yes/no): ")
    if answer.strip().lower() == "yes":
        try:
            amount = int(input("How many items would you like to add? "))
            if amount <= 0:
                print("Please enter a quantity greater than zero.")
                return
        except ValueError:
            print("Please enter a whole number.")
            return

        lowest_stock_shoe.quantity += amount
        if update_inventory_file():
            print("Stock updated successfully.")
            print(lowest_stock_shoe)
        else:
            lowest_stock_shoe.quantity -= amount


def search_shoe():
    """Find and display a shoe by its code."""
    code_to_find = input("Enter the shoe code to search for: ").strip()

    for shoe in shoes_list:
        if shoe.code.lower() == code_to_find.lower():
            print(shoe)
            return shoe

    print("No shoe with that code was found.")
    return None


def value_per_item():
    """Display the total stock value for every shoe product."""
    if not shoes_list:
        print("No inventory records were loaded.")
        return

    print("\n--- Stock Values ---")
    for shoe in shoes_list:
        total_value = shoe.cost * shoe.quantity
        print(
            f"{shoe.product}: R{shoe.cost:.2f} x {shoe.quantity} "
            f"= R{total_value:.2f}"
        )


def highest_qty():
    """Display the shoe with the largest quantity in stock."""
    if not shoes_list:
        print("No inventory records were loaded.")
        return

    shoe_with_highest_qty = max(shoes_list, key=lambda shoe: shoe.quantity)
    print("\nShoe with the highest quantity:")
    print(shoe_with_highest_qty)


def main():
    """Run the inventory menu."""
    read_shoes_data()

    if not shoes_list:
        print("No inventory data was loaded. Check inventory.txt.")

    while True:
        print("\n===== Nike Warehouse Inventory =====")
        print("1. Capture new shoe")
        print("2. View all shoes")
        print("3. Restock shoe with lowest quantity")
        print("4. Search for a shoe")
        print("5. Calculate value per product")
        print("6. Show shoe with highest quantity")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            capture_shoes()
        elif choice == "2":
            view_all()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()

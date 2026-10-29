"""
Task Manager Capstone

This program allows users to:
- Log in using credentials stored in user.txt.
- Register new users without allowing duplicate usernames.
- Add and view tasks stored in tasks.txt.
- View, complete, and edit tasks assigned to the logged-in user.
- Generate task and user overview reports.
- Allow the administrator to view statistics from the report files.

The program expects user.txt and tasks.txt to be in the same folder
as this Python file.
"""

# ===== Importing libraries =====
import os
from datetime import datetime, date

# Date format used by tasks.txt and the report calculations.
DATETIME_STRING_FORMAT = "%Y-%m-%d"


# ===== File and data helper functions =====

def load_users():
    """Read user.txt and return a dictionary of usernames and passwords."""
    if not os.path.exists("user.txt"):
        # Create the default administrator account if user.txt is missing.
        with open("user.txt", "w", encoding="utf-8") as default_file:
            default_file.write("admin;password")

    username_password = {}

    with open("user.txt", "r", encoding="utf-8") as user_file:
        for line in user_file.read().splitlines():
            if not line.strip():
                continue

            username, password = line.split(";", 1)
            username_password[username] = password

    return username_password


def save_users(username_password):
    """Write all usernames and passwords back to user.txt."""
    with open("user.txt", "w", encoding="utf-8") as out_file:
        user_data = [
            f"{username};{password}"
            for username, password in username_password.items()
        ]
        out_file.write("\n".join(user_data))


def load_tasks():
    """Read tasks.txt and return a list of task dictionaries."""
    if not os.path.exists("tasks.txt"):
        # Create an empty tasks file if it does not exist.
        with open("tasks.txt", "w", encoding="utf-8"):
            pass

    task_list = []

    with open("tasks.txt", "r", encoding="utf-8") as task_file:
        for task in task_file.read().splitlines():
            if not task.strip():
                continue

            # Split only the first five semicolons so a description
            # containing a semicolon is not accidentally broken.
            task_components = task.split(";", 5)

            if len(task_components) != 6:
                print(f"Skipping invalid task record: {task}")
                continue

            current_task = {
                "username": task_components[0],
                "title": task_components[1],
                "description": task_components[2],
                "due_date": datetime.strptime(
                    task_components[3], DATETIME_STRING_FORMAT
                ),
                "assigned_date": datetime.strptime(
                    task_components[4], DATETIME_STRING_FORMAT
                ),
                "completed": task_components[5] == "Yes",
            }

            task_list.append(current_task)

    return task_list


def save_tasks(task_list):
    """Write the current task list back to tasks.txt."""
    with open("tasks.txt", "w", encoding="utf-8") as task_file:
        task_list_to_write = []

        for task in task_list:
            str_attrs = [
                task["username"],
                task["title"],
                task["description"],
                task["due_date"].strftime(DATETIME_STRING_FORMAT),
                task["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                "Yes" if task["completed"] else "No",
            ]
            task_list_to_write.append(";".join(str_attrs))

        task_file.write("\n".join(task_list_to_write))


def display_task(task, task_number=None):
    """Display one task in a clear, labelled format."""
    if task_number is not None:
        print(f"Task Number: {task_number}")

    display = (
        f"Task:\t\t\t{task['title']}\n"
        f"Assigned to:\t\t{task['username']}\n"
        f"Date assigned:\t\t"
        f"{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        f"Due date:\t\t"
        f"{task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        f"Task complete:\t\t{'Yes' if task['completed'] else 'No'}\n"
        f"Task description:\n{task['description']}\n"
    )

    print(display)


# ===== Required task functions =====

def reg_user(username_password):
    """
    Register a new user.

    Duplicate usernames are rejected and the user is allowed to retry.
    The new password must also match the confirmation password.
    """
    while True:
        new_username = input("New Username: ").strip()

        # Prevent duplicate usernames.
        if new_username in username_password:
            print("Error: That username already exists. " \
            "Please choose another" \
            " username.")
            continue

        if new_username == "":
            print("Error: Username cannot be blank.")
            continue

        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")

        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue

        # Add the new user to the dictionary and save it.
        username_password[new_username] = new_password
        save_users(username_password)

        print("New user added successfully.")
        return


def add_task(username_password, task_list):
    """
    Add a new task.

    The task must be assigned to an existing username and must have
    a valid due date in YYYY-MM-DD format.
    """
    task_username = input("Name of person assigned to task: ").strip()

    if task_username not in username_password:
        print("User does not exist. Please enter a valid username.")
        return

    task_title = input("Title of Task: ").strip()
    task_description = input("Description of Task: ").strip()

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ").strip()
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT
            )
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": date.today(),
        "completed": False,
    }

    task_list.append(new_task)
    save_tasks(task_list)

    print("Task successfully added.")


def view_all(task_list):
    """Display every task in the task list."""
    if not task_list:
        print("There are no tasks to display.")
        return

    print("\n========== ALL TASKS ==========")

    for number, task in enumerate(task_list, start=1):
        display_task(task, number)
        print("-----------------------------------")


def view_mine(current_user, username_password, task_list):
    """
    Display tasks assigned to the current user.

    The user can:
    - Enter a task number to work with that task.
    - Enter -1 to return to the main menu.
    - Mark an incomplete task as complete.
    - Edit the assignee and/or due date of an incomplete task.
    """
    while True:
        user_tasks = [
            task for task in task_list
            if task["username"] == current_user
        ]

        if not user_tasks:
            print("You have no tasks assigned to you.")
            return

        print("\n========== MY TASKS ==========")

        # Give the user's tasks their own visible task numbers.
        for number, task in enumerate(user_tasks, start=1):
            display_task(task, number)
            print("-----------------------------------")

        print("Enter the task number to edit/view.")
        print("Enter -1 to return to the main menu.")

        try:
            task_number = int(input("Task number: "))
        except ValueError:
            print("Please enter a valid task number.")
            continue

        if task_number == -1:
            return

        if task_number < 1 or task_number > len(user_tasks):
            print("Invalid task number.")
            continue

        selected_task = user_tasks[task_number - 1]

        # Show the selected task before asking what the user wants to do.
        print("\n========== SELECTED TASK ==========")
        display_task(selected_task, task_number)

        if selected_task["completed"]:
            print("This task is already complete.")
            print("Completed tasks cannot be edited.")
            continue

        while True:
            action = input(
                "Enter 'c' to mark complete, 'e' to edit, or 'b' to go back: "
            ).strip().lower()

            if action == "c":
                selected_task["completed"] = True
                save_tasks(task_list)
                print("Task marked as complete.")
                break

            if action == "e":
                edit_task(selected_task, username_password)
                save_tasks(task_list)
                print("Task updated successfully.")
                break

            if action == "b":
                break

            print("Invalid option. Please choose c, e, or b.")


def edit_task(task, username_password):
    """
    Edit the assignee and/or due date of an incomplete task.

    Pressing Enter keeps the existing value.
    """
    print("\nLeave a field blank to keep its current value.")

    # Allow the username to be changed only to an existing user.
    while True:
        new_username = input(
            f"New username [{task['username']}]: "
        ).strip()

        if new_username == "":
            break

        if new_username not in username_password:
            print("User does not exist. Please enter a valid username.")
            continue

        task["username"] = new_username
        break

    # Allow the due date to be changed.
    while True:
        new_due_date = input(
            "New due date "
            f"[{task['due_date'].strftime(DATETIME_STRING_FORMAT)}]: "
        ).strip()

        if new_due_date == "":
            break

        try:
            task["due_date"] = datetime.strptime(
                new_due_date, DATETIME_STRING_FORMAT
            )
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


# ===== Report functions =====

def generate_task_overview(task_list):
    """Generate task_overview.txt using the current task data."""
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task["completed"])
    uncompleted_tasks = total_tasks - completed_tasks

    today = date.today()
    overdue_uncompleted = sum(
        1
        for task in task_list
        if not task["completed"] and task["due_date"].date() < today
    )

    if total_tasks > 0:
        percentage_incomplete = (uncompleted_tasks / total_tasks) * 100
        percentage_overdue = (overdue_uncompleted / total_tasks) * 100
    else:
        percentage_incomplete = 0
        percentage_overdue = 0

    with open("task_overview.txt", "w", encoding="utf-8") as report_file:
        report_file.write("TASK OVERVIEW\n")
        report_file.write("==============================\n")
        report_file.write(f"Total tasks: {total_tasks}\n")
        report_file.write(f"Completed tasks: {completed_tasks}\n")
        report_file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        report_file.write(
            f"Overdue uncompleted tasks: {overdue_uncompleted}\n"
        )
        report_file.write(
            f"Percentage of tasks incomplete: {percentage_incomplete:.2f}%\n"
        )
        report_file.write(
            f"Percentage of tasks overdue and incomplete: "
            f"{percentage_overdue:.2f}%\n"
        )


def generate_user_overview(username_password, task_list):
    """Generate user_overview.txt using the current user and task data."""
    total_users = len(username_password)
    total_tasks = len(task_list)
    today = date.today()

    with open("user_overview.txt", "w", encoding="utf-8") as report_file:
        report_file.write("USER OVERVIEW\n")
        report_file.write("==============================\n")
        report_file.write(f"Total users: {total_users}\n")
        report_file.write(f"Total tasks: {total_tasks}\n\n")

        for username in username_password:
            user_tasks = [
                task for task in task_list
                if task["username"] == username
            ]

            user_total = len(user_tasks)
            user_completed = sum(
                1 for task in user_tasks if task["completed"]
            )
            user_incomplete = user_total - user_completed
            user_overdue_incomplete = sum(
                1
                for task in user_tasks
                if not task["completed"]
                and task["due_date"].date() < today
            )

            if total_tasks > 0:
                percentage_of_all_tasks = (
                    user_total / total_tasks
                ) * 100
            else:
                percentage_of_all_tasks = 0

            if user_total > 0:
                percentage_completed = (
                    user_completed / user_total
                ) * 100
                percentage_incomplete = (
                    user_incomplete / user_total
                ) * 100
                percentage_overdue_incomplete = (
                    user_overdue_incomplete / user_total
                ) * 100
            else:
                percentage_completed = 0
                percentage_incomplete = 0
                percentage_overdue_incomplete = 0

            report_file.write(f"Username: {username}\n")
            report_file.write(f"Tasks assigned: {user_total}\n")
            report_file.write(
                f"Percentage of all tasks assigned: "
                f"{percentage_of_all_tasks:.2f}%\n"
            )
            report_file.write(
                f"Percentage of user's tasks completed: "
                f"{percentage_completed:.2f}%\n"
            )
            report_file.write(
                f"Percentage of user's tasks incomplete: "
                f"{percentage_incomplete:.2f}%\n"
            )
            report_file.write(
                f"Percentage of user's tasks overdue and incomplete: "
                f"{percentage_overdue_incomplete:.2f}%\n"
            )
            report_file.write("\n")


def generate_reports(username_password, task_list):
    """Generate both required overview report files."""
    generate_task_overview(task_list)
    generate_user_overview(username_password, task_list)
    print("Reports generated successfully:")
    print("- task_overview.txt")
    print("- user_overview.txt")


def display_statistics(username_password, task_list):
    """
    Display administrator statistics.

    Reports are generated first if either report file does not exist.
    The statistics displayed here are read from the report files.
    """
    if not os.path.exists("task_overview.txt") or not os.path.exists(
        "user_overview.txt"
    ):
        generate_reports(username_password, task_list)

    print("\n========== TASK OVERVIEW ==========")
    with open("task_overview.txt", "r", encoding="utf-8") as report_file:
        print(report_file.read())

    print("========== USER OVERVIEW ==========")
    with open("user_overview.txt", "r", encoding="utf-8") as report_file:
        print(report_file.read())


# ===== Login function =====

def login(username_password):
    """Keep asking for login details until a valid login is entered."""
    while True:
        print("\nLOGIN")
        current_user = input("Username: ").strip()
        current_pass = input("Password: ")

        if current_user not in username_password:
            print("User does not exist.")
            continue

        if username_password[current_user] != current_pass:
            print("Wrong password.")
            continue

        print("Login Successful!")
        return current_user


# ===== Main program =====

def main():
    """Run the Task Manager program."""
    username_password = load_users()
    task_list = load_tasks()

    current_user = login(username_password)

    while True:
        print()
        menu = input(
            "Select one of the following Options below:\n"
            "r - Registering a user\n"
            "a - Adding a task\n"
            "va - View all tasks\n"
            "vm - View my tasks\n"
            "gr - Generate reports (admin only)\n"
            "ds - Display statistics (admin only)\n"
            "e - Exit\n"
            ": "
        ).lower()

        # Required function call for registering a user.
        if menu == "r":
            reg_user(username_password)

        # Required function call for adding a task.
        elif menu == "a":
            add_task(username_password, task_list)

        # Required function call for viewing all tasks.
        elif menu == "va":
            view_all(task_list)

        # Required function call for viewing the current user's tasks.
        elif menu == "vm":
            view_mine(current_user, username_password, task_list)

        # Only the administrator can generate reports.
        elif menu == "gr":
            if current_user == "admin":
                generate_reports(username_password, task_list)
            else:
                print("Only the administrator can generate reports.")

        # Only the administrator can display statistics.
        elif menu == "ds":
            if current_user == "admin":
                display_statistics(username_password, task_list)
            else:
                print("Only the administrator can display statistics.")

        elif menu == "e":
            print("Goodbye!!!")
            break

        else:
            print("You have made a wrong choice. Please try again.")


# Start the program.
if __name__ == "__main__":
    main()

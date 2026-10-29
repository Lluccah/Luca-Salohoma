#!/usr/bin/python3

"""
This script processes command-line arguments to simulate a simplified echo
command. It joins the arguments together and prints the result to stdout.

Usage:
    python echo.py
    python echo.py Hello World
"""

import sys


def array_to_string(arr):
    """
    Converts a list of strings into one string with spaces between them.
    """

    # join() combines all the items in the list.
    # " " means that a space is placed between each item.
    return " ".join(arr)


if __name__ == "__main__":
    # sys.argv contains the command-line arguments.
    # sys.argv[0] is the name of the Python program.

    # [1:] removes the program name and keeps the user's arguments.
    arguments = sys.argv[1:]

    # Convert the arguments into one string and print the result.
    # If there are no arguments, this prints a blank line.
    print(array_to_string(arguments))
    
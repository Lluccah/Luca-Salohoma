#!/usr/bin/python3

"""
This script searches for a specified string (needle) within lines of input
and prints those lines where the needle is found.

Usage:
    python grep.py needle
    python grep.py needle filename
"""

import sys


def match(source, needle):
    """
    Searches for a specified string within the input.

    source = the input lines to search
    needle = the text we are looking for
    """

    # Go through each line in the input.
    for line in source:

        # Check if the search text is found in the current line.
        if needle in line:

            # Print the line if the search text was found.
            # end="" prevents print() from adding an extra blank line.
            print(line, end="")


if __name__ == "__main__":
    # sys.argv contains the command-line arguments.
    # sys.argv[0] is the program name.

    # Check whether the user entered a search string.
    if len(sys.argv) < 2:
        print("Usage: python grep.py needle [filename]")
        sys.exit(1)

    # The first argument after the program name is the search string.
    needle = sys.argv[1]

    # If there is only one argument, use standard input.
    # Example:
    # echo "Hello World" | python grep.py Hello
    if len(sys.argv) == 2:
        match(sys.stdin, needle)

    # If there are two arguments, the second one is the filename.
    elif len(sys.argv) == 3:
        filename = sys.argv[2]

        # Try to open the file and search through it.
        try:
            with open(filename, "r", encoding="utf-8") as file:
                match(file, needle)

        # Display an error if the file does not exist.
        except FileNotFoundError:
            print(f"grep.py: {filename}: No such file or directory")
            sys.exit(1)

    # Display an error if too many arguments were supplied.
    else:
        print("Usage: python grep.py needle [filename]")
        sys.exit(1)
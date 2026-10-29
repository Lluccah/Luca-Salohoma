#!/usr/bin/python3

"""
This script processes input either from standard input (stdin) or from a
specified file. Reads lines from stdin or a file and prints them to standard
output (stdout).
"""
import sys


def std_in():
    """Read from standard input and print each line to standard output."""
    # sys.stdin contains any text piped or typed into the program.
    for line in sys.stdin:
        # end="" keeps the newline that is already at the end of each line.
        print(line, end="")


def infile(file):
    """Read a file and print its contents to standard output."""
    try:
        # Open the file in read mode.
        with open(file, "r", encoding="utf-8") as input_file:
            # Read and print each line from the file.
            for line in input_file:
                print(line, end="")
    except FileNotFoundError:
        # Show an error message if the file cannot be found.
        print(f"cat.py: {file}: No such file or directory")
        sys.exit(1)


if __name__ == "__main__":
    # sys.argv[0] is the program name.
    # If a filename is supplied, read from that file.
    if len(sys.argv) > 1:
        infile(sys.argv[1])
    else:
        # If no filename is supplied, read from standard input.
        std_in()

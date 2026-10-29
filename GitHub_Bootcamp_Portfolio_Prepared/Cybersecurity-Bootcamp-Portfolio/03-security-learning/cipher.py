
# cipher.py
# This program uses a Caesar cipher to encode a message.
# Each letter is shifted 15 positions forward in the alphabet.
# Uppercase and lowercase letters are handled separately.
# Spaces, numbers, and punctuation remain unchanged.


# Define a function that takes a message as an argument.
def encode_message(message):

    # Create an empty string to store the encoded characters.
    encoded_message = ""

    # Use a for loop to check every character in the message.
    for char in message:

        # Check whether the character is a lowercase letter.
        if 'a' <= char <= 'z':

            # ord() converts a character to its ASCII number.
            # For example, ord('a') returns 97.
            # Subtracting ord('a') gives a position from 0 to 25.
            position = ord(char) - ord('a')

            # Add 15 to move forward in the alphabet.
            # % 26 ensures the position wraps around after 'z'.
            # For example, 'p' becomes 'e'.
            new_position = (position + 15) % 26

            # chr() converts the number back into a letter.
            # Adding ord('a') restores the lowercase ASCII value.
            encoded_message += chr(new_position + ord('a'))

        # Check whether the character is an uppercase letter.
        elif 'A' <= char <= 'Z':

            # Convert the uppercase character into a position.
            # For example, 'A' becomes 0 and 'Z' becomes 25.
            position = ord(char) - ord('A')

            # Shift the position forward by 15 letters.
            # % 26 makes the alphabet cyclical.
            new_position = (position + 15) % 26

            # Convert the new position into an uppercase letter.
            encoded_message += chr(new_position + ord('A'))

        else:
            # If the character is not a letter, leave it unchanged.
            # This includes spaces, numbers, and punctuation.
            encoded_message += char

    # Return the complete encoded message to the caller.
    return encoded_message


# Ask the user to type a message that they want to encode.
message = input("Enter a message to encode: ")

# Call the encode_message() function.
# Store the returned encoded text in a variable.
encoded_message = encode_message(message)

# Print the encoded message on the screen.
print("Encoded message:", encoded_message)

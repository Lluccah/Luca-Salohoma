# function to print Dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        # Correction 1 
        # change the dictionary[k] to dictionary[key].
        # The variable created by the for loop is called "key", not "k"

        print(dictionary[key])

# Dictionary Containing Simpsons Catchphrases
simpson_catch_phrases: dict[str, str] = {
    "lisa": "BART!",
    "bart": " Eat My Shorts!",
    "marge": "Mmm~mmmmm",
    "homer": "d'oh!",
    "maggie": "(Pacifier suck)"
}

# Correction 2
# the function rxpects two arguments:
# the dictionary 
# a list containing the keys
# changed: 
# print_values_of(simpson_catch_phrases,"lisa", "brat","homer")

# call the function and provide the dictionary
# and a list containing the keys we want to print
print_values_of(simpson_catch_phrases, ["lisa", "bart", "homer"])

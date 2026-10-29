# alternative part 1
# alternative character uppercase/lowercase

# ask user to input a string
User_string = input("Enter a string: ")
# initialize an empty string to store the result
alternative_characters = ""
# loop through each character in the string
for i in range(len(User_string)):
# check if the index is even or odd 
# if the index is even, convert to uppercase   
    if i % 2 == 0:
        alternative_characters += User_string[i].upper()
# if the index is odd, convert to lowercase
    else:
        alternative_characters += User_string[i].lower()

# print the result

print("alternative characters results: ")
print(alternative_characters)   

# alternative part 2

# split the string into words
words = User_string.split()
# initialize an empty string to store the result

alternative_words = ""
# loop through each word in the list
for i in range(len(words)):
# check if the index is even or odd 
# if the index is even, convert the word to lowercase    
    if i % 2 == 0:
        alternative_words += words[i].lower() + " "
# if the index is odd, convert the word to uppercase        
    else:
        alternative_words += words[i].upper() + " "
#join the list of words back into a single string        
result_words = " ".join(alternative_words)
# print the result
print("alternative words results: ")
print(alternative_words)    
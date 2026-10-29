# ask user to input the name of favorite restaurant
restaurant_name = input("Enter the name of your favorite restaurant: ") 

# store into a varaible called string_fav
string_fav = restaurant_name

# request user to input favorite number
favorite_number = input("Enter your favorite number: ")

# store into a vsariable called int_fav
int_fav = int(favorite_number)

print(string_fav)
print(int_fav)

# cast string_fav into an integer
casted_string = str(string_fav)    
print(casted_string)
# casting string_fav into an interger will cause an error,because the data
# type stored in the variable called string_fav is not a number.
# integer can only store wholenumbers without decimal points
# therefore trying to cast a string that contains letters into an integer will
# cause an error.


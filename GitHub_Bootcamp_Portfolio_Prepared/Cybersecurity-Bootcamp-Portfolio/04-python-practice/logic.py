# logixcal_error.py

print("=== The world 's Most Confidential Calculator ===")

age = int(input("How old are you? "))

# logical error: 
# the program mistakenly adds two 100 instead of subtracing them
# when calculating the year you were born

current_year = 2024
birth_year = current_year + age  # Logical error here

print(f"You were born in the year: {birth_year}")   
print("According to this calculator,you are officially a" "centenarian!")
print(" time traveler from the future! ")
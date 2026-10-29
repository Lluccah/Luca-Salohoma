# list of friends
# create a list containing the names of your friends
friends_names = ["Francisco Salohoma", "Kefentse Mongwe", "Luccah Nicolau"]

# Print the first friends name
print(friends_names[0])

# Print the last friends name
print(friends_names[-1])

# Print the length of the list
print(len(friends_names))

# list of friends ages
# create a list containing the ages of your friends
# the ages should correspond to the names in the friends_names list
friends_ages = [25, 30, 28]

# use a loop to print each friends name with their age
# Print each friends name with their age
for i in range(len(friends_names)):
    # Print the friends name and their corresponding age
    print(f"{friends_names[i]} is {friends_ages[i]} years old.")
    
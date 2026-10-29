# import the statistics module
# such as mean() and median()

import statistics
# Creat an empty list to store the 10 numbers
numbers = []
# ask the user to input 10 floating-point numbers
for i in range(10):
    number = float(input(f"enter float {i+1}: "))

    # Add the number to the list
    numbers.append(number)

# calculate the total of all the numbers
total = sum(numbers)

# print the total
print("Total:", total)

# find the largest number in the list
maximum = max(numbers)

# find the index (position) of the largest number
max_index = numbers.index(maximum)

# print the index of the maximum number
print("Index of the maximum:", max_index)

# Find the smallest number in the list
minimum = min(numbers)

# find the index (position) of the smallest number
min_index = numbers.index(minimum)

# print the index of the minimum number
print("Index of the minimum:", min_index)

# Calculate the average (mean) of the numbers
mean = statistics.mean(numbers)

# round the average to two decimal places and print it
print("Average:", round(mean, 2))

#calculate the median using the statistics module
median = statistics.median(numbers)

# Print the median
print("Median:", median)

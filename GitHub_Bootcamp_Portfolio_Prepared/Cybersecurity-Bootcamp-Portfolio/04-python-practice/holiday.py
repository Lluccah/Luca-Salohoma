
# This function calculates the total cost of the hotel stay.
# It takes the number of nights as an argument.
def hotel_cost(num_nights):

    # Set the price that the hotel charges per night.
    price_per_night = 100

    # Multiply the number of nights by the price per night
    # to calculate the total hotel cost.
    total = num_nights * price_per_night

    # Return the total cost to the program.
    return total


# This function calculates the cost of the plane ticket.
# It takes the chosen city as an argument.
def plane_cost(city_flight):

    # Check if the user chose Cape Town.
    if city_flight == "Cape Town":
        return 1500

    # Check if the user chose Windhoek.
    elif city_flight == "Windhoek":
        return 5000

    # Check if the user chose Luanda.
    elif city_flight == "Luanda":
        return 7000

    # Check if the user chose Brazil.
    elif city_flight == "Brazil":
        return 9000

    # If the user enters a city that is not available,
    # return 0.
    else:
        return 0


# This function calculates the total cost of renting a car.
# It takes the number of rental days as an argument.
def car_rental(rental_days):

    # Set the price for renting the car for one day.
    price_per_day = 200

    # Multiply the number of rental days by the daily price
    # to calculate the total car rental cost.
    total = rental_days * price_per_day

    # Return the total car cost.
    return total


# This function calculates the complete holiday cost.
# It takes three arguments:
# num_nights = number of nights at the hotel
# city_flight = destination city
# rental_days = number of days the car is rented
def holiday_cost(num_nights, city_flight, rental_days):

    # Call the hotel_cost() function to calculate
    # the cost of the hotel.
    hotel = hotel_cost(num_nights)

    # Call the plane_cost() function to calculate
    # the total cost of the flight.
    flight = plane_cost(city_flight)

    # Call the car_rental() function to calculate
    # the total cost of the rental car.
    car = car_rental(rental_days)

    # Add the hotel, flight and car costs together.
    total = hotel + flight + car

    # Return the total cost.
    return total


# Display the available destinations to the user.
print("Available destinations:")
print("1. Cape Town")
print("2. Windhoek")
print("3. Luanda")
print("4. Brazil")


# Ask the user to enter their chosen destination.
# The input is stored in the city_flight variable.
city_flight = input("Enter your destination: ")


# Ask the user how many nights they will stay at the hotel.
# int() converts the user input from text into a whole number.
num_nights = int(input("Enter the number of nights: "))


# Ask the user how many days they want to rent a car.
# int() converts the user input into a whole number.
rental_days = int(input("Enter the number of car rental days: "))


# Call the hotel_cost() function to calculate the hotel cost.
hotel = hotel_cost(num_nights)


# Call the plane_cost() function to calculate the flight cost.
flight = plane_cost(city_flight)


# Call the car_rental() function to calculate the car rental cost.
car = car_rental(rental_days)


# Call the holiday_cost() function to calculate
# the total cost of the entire holiday.
total = holiday_cost(num_nights, city_flight, rental_days)


# Print a heading to make the output easier to read.
print("\n===== HOLIDAY DETAILS =====")


# Display the user's chosen destination.
print("Destination:", city_flight)


# Display the number of nights at the hotel.
print("Number of nights:", num_nights)


# Display the total hotel cost.
print("Hotel cost: R", hotel)


# Display the flight cost.
print("Flight cost: R", flight)


# Display the number of days the car will be rented.
print("Car rental days:", rental_days)


# Display the total car rental cost.
print("Car rental cost: R", car)


# Print a line to separate the individual costs
# from the final total.
print("---------------------------")


# Display the total cost of the holiday.
print("Total holiday cost: R", total)


# Print a final line to make the output look neat.
print("===========================")



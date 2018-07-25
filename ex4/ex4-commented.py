cars = 100

#Assigns the value to the variable
space_in_a_car = 4.0

#Assigns the value to the variable
drivers = 30

#Assigns the value to the variable
passengers = 90

#Assigns the value to the variable
cars_not_driven = cars - drivers

#Assigns the value of a variable to a variable
cars_driven = drivers

#Assigns the multiplication of two variables to a variable
carpool_capacity = cars_driven * space_in_a_car

#Assigns the division of two variables to a variable
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")

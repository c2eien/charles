cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers/cars_driven

print('There are', cars,'cars available.')
print('There are only', drivers,'drivers available.')
print('There will be',cars_not_driven,'empty cars today.')
print('We can transport', carpool_capacity,'people today.')
print('We have',passengers,'to carpool today.')
print('We need to put about', average_passengers_per_car,'in each car.')

#testing out other ways to pass variable into print
print('cars'+str(cars)) #concatenate
print('cars %s' % (cars))  #pass as tuple
print('cars {}'.format(cars)) #using .format

# # What does %s, %r, and %d do again?
# You'll learn more about this as you continue, 
# but they are "formatters." They tell Python to take the variable on the right and put it in to replace the %s with its value.
# %r is used for debugging and inspection, so it's not necessary that it be pretty.


# They are called string formatting operations.

# The difference between %s and %r is that %s uses the str function and %r uses the repr function.
 # the biggest difference in practice is that 
 # repr for strings includes quotes and all special characters are escaped.
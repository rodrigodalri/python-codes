'''
author: Rodrigo Dal Ri
email: rodrigodalri1995@gmail.com
'''

#------------------------------------------------------------------------------------------------------------------------------------
# merge two dictionaries
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)


#------------------------------------------------------------------------------------------------------------------------------------
# Different ways to test multiple flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')


#------------------------------------------------------------------------------------------------------------------------------------
# How to sort a Python dict by value (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
print(xs)

# Or:
import operator
sorted(xs.items(), key=operator.itemgetter(1))
print(xs)


#------------------------------------------------------------------------------------------------------------------------------------
# Using namedtuple is way shorter than defining a class manually:
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car.mileage)

# We get a nice string repr for free:
print(my_car)
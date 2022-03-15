# CAC-102-13 Exercise Modules & Packages
# Write functions for each of the items below.
# Call the function to ensure the results are correct.

print('\n1.On page 155 of your book, do 8-15 through 8-17')
# 1.On page 155 of your book, do 8-15 through 8-17
print('\nPrinting Models')
# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file
# called printing_functions.py. Write an import statement at the top of printing_models.py, and
# modify the file to use the imported functions.


import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a
# separate file. Import the function into your main program file, and call the function using each
# of these approaches:
# importing basic_function
import basic_function
basic_function.my_mood()
# importing the function hello_world from basic_function

from basic_function import my_mood
print(my_mood())
# importing the function hello_ world and giving it the alias hw from the
# basic function

from basic_function import my_mood as mm
print(mm())
# importing the basic_function module and giving it the alias bf

import basic_function as bf
bf.my_mood()
# importing all functions from the module basic_function

from basic_function import*
print(my_mood())

# 8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make
# sure they follow the styling guidelines described in this section.


print('2.On page 180 of your book, do 9-10 through 9-12')
# 2.On page 180 of your book, do 9-10 through 9-12
from restaurant import Restaurant
dairy_queen = Restaurant('Dairy Queen', 'Ice Cream')
dairy_queen.open_restaurant()

#9-11
from admin import Admin
zayphod = Admin('zayphod', 'beeblebrox', 277, 'fifth@planet.org', 'black')
zayphod.privileges()

#9-12
from admin import Admin
zayphod = Admin('zayphod', 'beeblebrox', 277, 'fifth@planet.org', 'black')
zayphod.privileges()

print('3.On page 181 of your book, do 9-16 ')
# 3.On page 181 of your book, do 9-16
# 9-16. Python Module of the Week: One excellent resource for exploring the Python
# standard library is a site called Python Module of the Week. Go to https://pymotw.com/ and look at
# the table of contents. Find a module that looks interesting to you and read about it, perhaps
# starting with the random module.

# https://pymotw.com/3/json/index.html
# Python objects as JSON strings, and decode JSON strings into Python objects.
# The json module provides an API similar to pickle for converting in-memory Python objects to a
# serialized representation known as JavaScript Object Notation (JSON). Unlike pickle,
# JSON has the benefit of having implementations in many languages (especially JavaScript). It is
# most widely used for communicating between the web server and client in a REST API, but is also
# useful for other inter-application communication needs.

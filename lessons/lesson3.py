# All About Strings
# What is a string?
# A string is a sewuence of characters. It can be defined with either  single
# or double quotes.
alpha = 'Hello'

# double quotes
beta = "Python"

# print results
print(alpha)
print(beta)

# A multi-line string uses three single or three double quotes and allows
# a string to be created on mutiple lines.
multi = '''This string can be seen
on multiple lines so you could do
paragraphs if you wanted'''
print(multi)


# Missing a line somewhere
# getting a specific index using the square bracket []
charlie = 'Happy'
print(charlie[2])

# if you put in a value of the index that is higher than the number of
# characters -1 you will generate an error
# print(charlie[5])

# slicing in range of charachters
# using the same square brackets, you can output a range of characters
# from a string. This is called slicing. You use a colon to separate the
# start and end of the slice.
delta = 'Enjoy Python'
print(delta[2:5])
# output should be joy

# negative slicing we use negative numbers, instead of starting from zero
# it begins at the end of the string
print(delta[-5:-2])
# output should be yth

# What is check string
# This technique is the ability to compare a set of characters with the string
# variable. This result wll be either True or False. We use in or not it
# keywords for checking string
# using the keyword
txt = 'This is a test sentence'
result1 = 'is' in txt

# using the not keyword
txt2 = 'This other phrase is also a test'
result2 = 'th' not in txt2

print(result1)
print(result2)

# String concatenation in Python is the ability to join 2 or more strings
# using the plus operator.
# Basic Concatenation
cat1 = "Happy"
cat2 = "Friday"
combine = cat1 + cat2
print(combine)
combine2 = cat1 + " " + cat2
print(combine2)

cat3 = 'Sample'
combine3 = cat3 + ' Code'
print(combine3)

# longer concatenation with more than 2 values
combine4 = cat1 + ' ' + cat2 + ' ' + combine3
print(combine4)

# What about strings and a number
# combine5 = cat3 + 5
# print(combine5)

# Basic strin gformat methos using only a curly brace
age = 4
msg1 = 'My dog is {} years old'
print(msg1.format(age))

# string format using indexing
msg2 = 'My dog {1} is {0} years old'
print(msg2.format(age, 'Spot'))

# Optional format
name = 'John'
total = 34.9856
msg3 = 'Hello {0}, your order comes to {1:6.2f}'
print(msg3.format(name, total))

# octal escape sequence '\110\145\154\154\157'
value_0 = '\110\145\154\154\157'
print(value_0)

#Escape Sequence allows you to use some charachters that are reserves using
# a backslash
value_more = 'That\'s a cool toy. \tCan I\n play with it?'
print(value_more)

# String Methods are methods built in Python
value_string = ' Hello, World '

# strip() method
print(value_string.strip())

# lower() method
print(value_string.lower())

# upper() method
print(value_string.upper())

# replace() method
print(value_string.replace('e', 'a'))

# split() method
print(value_string.split(','))

value_more = 'hello python'

# capitalize() method
print(value_more.capitalize())

value_upper = 'PYTHON'

# casefold() method
print(value_upper.casefold())

# center() method
print(value_more.center(40))

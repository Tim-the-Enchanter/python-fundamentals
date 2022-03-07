# CAC-102-5 Exercise 5 - Operators
# 1. On page 78 of your book, do 5-1 of the Try it Yourself. Put all your code in your exercise5.py file.
# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each
# test and your prediction for the results of each test. Create at least ten tests. Have at least five tests evaluate
# to True and another five tests evaluate to False.

car = 'lambo'
print("\n1 Is car == 'fake lambo'? I predict False.")
print(car == 'fake lambo')
# car (lambo) is not equal == to (lambo) because i said so

print("\n2 Is car == 'lambo'? I predict True.")
print(car == 'lambo')
# car (lambo) is equal == to (lambo)

car = 'Ford'
print("\n3 Is car == 'ford'? I predict False.")
print(car == 'ford')
# # car (Ford) is not equal to (ford)

print("\n4 Is car == 'beetle'? I predict Falso.")
print(car == 'beetle')
# car (Ford) is equal to (Ford)

car = 'chevy'
print("\n5 Is car == 'chevy'? I predict True.")
print(car == 'chevy')
# # car (chevy) is equal to (chevy)

print("\n6 Is car == 'gmc'? I predict True.")
print(car == 'chevy')
# car (gmc) is equal to (chevy)

car = 'AcurA'
print("\n7 Is car == 'acura'? I predict True.")
print(car == 'AcurA')
# car (AcurA) is equal to (acura)

print("\n8 Is car == 'ACURA'? I predict True.")
print(car == 'AcurA')
# car (ACURA) is equal to (AcurA)

car = 'Honda'
print("\n9 Is car == 'Jag'? I predict False.")
print(car == 'Jag')
# car (Jag) is not equal to (Honda)

print("\n10 Is car == 'Nissan'? I predict False.")
print(car == 'Nissan')
# car (Nissan) is not equal to (Honda)

# 2. On page 78 of your book, create new examples that meet the bullet points of 5-2.
# Put your code for this in your exercise5.py file.

# Tests for equality and inequality with strings
car = 'volvo'
car == 'volvo'
print("\nIt is True, the car == a Volvo.")
print(car == 'volvo')
print("\nIt is not True, the car != a Volvo.")
print(car != 'volvo')


# Tests using the lower() method
car = 'JeeP'
print("\nIt is not True, the car == a JeeP.")
print(car == 'jeep')
print("\nIt is True, the car == a JeeP.")
print(car.lower() == 'jeep')

# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
num1 = '21'
print("\nTrue 21 is > 20")
print(num1 > '20')
print("\nFalse 21 is not < 10")
print(num1 < '10')
print("\nFalse 21 is not >= than 29")
print(num1 >= '29')
print("\nTrue 21 is <= than 3")
print(num1 <= '3')

# Tests using the and keyword and the or keyword
num1 = 30
num2 = 10


def sam1_and():
    result = num1 > 69 and num2 > 9
    print(result)


sam1_and()


def sam1_or():
    result = num1 > 25 or num2 > 9
    print(result)


sam1_or()


def sam2_and():
    result = num1 < 13 and num2 > 5
    print(result)


sam2_and()


def sam2_or():
    result = num1 >= 30 or num2 > 7
    print(result)


sam2_or()


# Test whether an item is in a list
print("in list, True.")
supplies = ['pens', 'textbook', 'paper']


def samp_in(arg):
    result = arg in supplies
    print(result)


samp_in('Pens'.lower())

# Test whether an item is not in a list
print("not in list, False.")
toppings = ['onions', 'peppers', 'bacon']


def samp_in(arg):
    result = arg not in toppings
    print(result)


samp_in('onions')

# 3. Write a function that will take 2 arguments. Inside the function provide examples of all the
# arithmetic operators. Provide a variable for each solution and print the results of each.

# num1 = 30 & num2 = 10


def arth_op(arg1, arg2):
    result = num1 + num2
    print(result)
    result = num2 - num1
    print(result)
    result = num1 * num2
    print(result)
    result = num1 / num2
    print(result)


arth_op(0, 0)

# 4. Write a function that takes only 1 argument. Inside the function provide examples of
# Assignment operators: modulus equals, minus equals, exponent equals & plus equals. Provide a
# variable for each solution and print the results of each.


def assign(value):
    value %= 10
    print(value)
    value -= 69
    print(value)
    value **= -100
    print(value)
    value += 777
    print(value)


assign(777)

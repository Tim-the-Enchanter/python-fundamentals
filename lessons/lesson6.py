# Lesson 6 - Control Flow Statements

# Boolean
#  These methods are either True or false, uses the method bool()
def boolean_sample():
    print(bool('sample'))
    print(bool(0.0))


# boolean_sample()


# if statement
# Used to find if the condition is true
def basic_if(arg1, arg2):
    if arg1 > arg2:
        print('arg 1 is greater than arg2.')

    if arg1 == arg2:
        print('Both values are the same')


# basic_if(10, 5)


# What is Elif?
# The elif is a keyword used when the first condition is false, and you want to try another condition
def basic_elif(val1, val2):
    if val1 > val2:
        print('Value 1 is greater than Value 2.')
    elif val1 < val2:
        print('Value 2 is greater than value 1.')
    elif val1 == val2:
        print('Value 1 and Value 2 are equal')


# basic_elif(10, 10)

# What is else?
# When an if statement evaluates to false an else keyword can be used to execute other code in place
# of the true statement.
def else_example(arg):
    if arg > 15:
        print('arg is greater than 15')
    else:
        print('Our argument is less than 15')


# else_example(10)


# else with elif
def check_grade(arg):
    if arg == 'A':
        print('Excellent!')
    elif arg == 'B':
        print('Good!')
    elif arg == 'C':
        print('Average!')
    elif arg == 'D':
        print('Below average!')
    else:
        print('Not a valid grade!')


# check_grade(input())


value_1 = 14


def nested_example(arg, arg2):
    if value_1 > arg:
        print('value 1 is greater than arg 1')
        if value_1 > arg2:
            print('value 1 is greater than arg 2')
        else:
            print('value 1 is less than arg 2')


# nested_example(5, 30)


# Ternary statements

golf = 42
hotel = 24

# if shorthand
result = golf if golf > hotel else hotel
# print(result)

# print('both are equal' if golf == hotel else 'golf is greater' if golf > hotel else 'hotel is greater')


# what the one above would look like in a function
def if_short_decoded():
    if golf == hotel:
        print('both are equal')
    elif golf > hotel:
        print('golf is greater')
    else:
        print('hotel is greater')


# if_short_decoded()

# and & or keyword
def combined(arg1, arg2, arg3):
    if arg1 > arg2 and arg1 >= arg3:
        print('Argument 1 is the greatest.')
    if arg2 > arg3 or arg2 <= arg3:
        print('Argument 2 is greater than 3 but not 1.')


combined(30, 20, 30)


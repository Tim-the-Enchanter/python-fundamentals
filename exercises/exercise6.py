# CAC-102-6 Exercise 6 - Control Flow Statements
# 1. On page 84 of your book, do 5-3.


# 5-3a Write an if statement to test whether the alien’s color is green. If
# it is, print a message that the player just earned 5 points.
alien_color = 'green'


def color_test1():
    if 'green' in alien_color:
        print('5-3a You Just Earned 5 Points!')

# Write one version of this program that passes the if test and
# another that fails. (The version that fails will have no output.)
    if 'green' in alien_color:
        print('5-3b1 You Just Earned 5 Points!')

    if 'blue' in alien_color:
        print('You Just Earned 5 Points!')
    else:
        print('5-3b2 No Output ;P')


color_test1()


# 2 On page 84 of your book, do 5-4.
def color_test2():
    if 'green' in alien_color:
        print('You Just Earned 5 Points!')
    if 'yellow' != alien_color:
        print('Bonus Shot, You Earned 10 points!')
    else:
        print('Try Again...')
    if 'red' in alien_color:
        print('Bonus Shot, You Earned 10 points!')
    else:
        print('Try Again...')


color_test2()


# 3 On page 84 of your book, do 5-5.
def color_test3():
    alien_color_1 = 'green'
    if 'green' in alien_color_1:
        print('You\'ve earned 5 points for shooting the green alien')
    elif 'yellow' in alien_color_1:
        print('You\'ve earned 10 points for shooting the yellow alien!')
    else:
        print('You\'ve earned 15 points for shooting the red alien!')


color_test3()


def color_test3a():
    alien_color_1 = 'yellow'
    if 'green' in alien_color_1:
        print('You have earned 5 points for shooting the green alien')
    elif 'yellow' in alien_color_1:
        print('You have earned 10 points for shooting the yellow alien!')
    else:
        print('You have earned 15 points for shooting the red alien!')


color_test3a()


def color_test3b():
    alien_color_1 = 'red'
    if 'green' in alien_color_1:
        print('You have earned 5 points for shooting the green alien')
    elif 'yellow' in alien_color_1:
        print('You have earned 10 points for shooting the yellow alien!')
    else:
        print('You have earned 15 points for shooting the red alien!')


color_test3b()


# 4 On page 84 of your book, do 5-6.
def color_test4():
    age = 43
    if age < 2:
        print('You are a baby!')
    elif 2 <= age < 4:
        print('You are a toddler!')
    elif 3 <= age < 13:
        print('You are a kid!')
    elif 13 <= age < 20:
        print('You are a teenager!')
    elif 20 <= age < 65:
        print('You are an adult!')
    else:
        print('You are an elder!')


color_test4()


# 5 Write a function that takes an argument. Check this argument to see if it is a Boolean using the
# bool method. Call the method and use the below values as your argument. Using comments,
# provide the name of the argument and if it was true or false from running the code.

a = 12
b = 1.2
c = 0
d = 0.4
e = 0.0


def check_if_bool1():
    print(bool(a))


def check_if_bool2():
    print(bool(b))


def check_if_bool3():
    print(bool(c))


def check_if_bool4():
    print(bool(d))


def check_if_bool5():
    print(bool(e))


check_if_bool1()
# check_if_bool1() prints True
check_if_bool2()
# check_if_bool2() prints True
check_if_bool3()
# check_if_bool3() prints False by default because it's a zero
check_if_bool4()
# check_if_bool4() prints True
check_if_bool5()
# check_if_bool5() prints False by default because it's a zero







# For Number 5 of this task, I say "Call the method and use the below values as your argument".
# I did not put any arguments in the lab, so use the below values. As of the time of this clarification,
# only 2 have completed and used your own, so I will grade yours separate. Everyone else should use the below values.
# 12, 1.2, 0, 0.4, 0.0

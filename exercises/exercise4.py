# CAC-102-4 Exercise 3 - Numbers
# 1. On page 29 of your book, In the Try it Yourself section do the following tasks.
# Put all your code in your exercise4.py file.
# 2-8. Number Eight: Write addition, subtraction, multiplication, and division operations that
# each result in the number 8. Be sure to enclose your operations in print() calls to see the results.
print(4+4)
print(16-8)
print(32//4)
print(2*4)


# 2-9. Favorite Number: Use a variable to represent your favorite number. Then, using that
# variable, create a message that reveals your favorite number. Print that message.
fav_num = 7
message = f"Hello, My favorite number is {fav_num}"
print(message)


# 2. Assign variables to the following sets of numbers. Use underscores to make them more
# readable. Write a function called number_sets and print each variable inside the function.
# Call all the function to verify your results. a. 456234 b. 68423791 c. 13794628 d. 96374
num1 = 45_6_234
num2 = 68_423_791
num3 = 13_79_46_28
num4 = 9_63_74
number_sets = num1, num2, num3, num4
print(number_sets)


# 3. Write a function that will take 2 arguments. Using Type conversion, convert the first argument
# from int to float. Convert the second argument from float to int. Call the function and provide
# the correct values for each argument to verify your results. One argument should be a float and
# the other an int


def flo_int():
    print(float(num3), int(num4))


print(flo_int())


# 4. Write a function that will have two inputs. The first input method should ask “What is your
# favorite movie” the second input method should ask “How many times have you seen it?”. The
# second input should be inside an int function. Each input method should be assigned to a
# variable. In a print statement using placeholders, the output result should be “I have seen
# {favorite movie} {number of times} times”.

movie = input('What is your favorite movie?')
reply1 = int(input('How many times have you seen it?'))

message = 'I have seen {0} {1} times'
print(message.format(movie, reply1))
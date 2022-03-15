# CAC-102-12 Exercise Exception Handling
# Write functions for each of the items below.
# Call the function to ensure the results are correct.

print('\n1.On page 201 of your book, do 10-6 of the Try it Yourself.')
# 1.On page 201 of your book, do 10-6 of the Try it Yourself.

# 10-6. Addition: One common problem when prompting for numerical input occurs when
# people provide text instead of numbers. When you try to convert the input to an int, you’ll get
# a ValueError. Write a program that prompts for two numbers. Add them together and print
# the result. Catch the ValueError if either input value is not a number, and print a friendly error
# message. Test your program by entering two numbers and then by entering some text instead
# of a number.


def sample_addition_else():
    try:
        x = input("Enter a number: ")
        x = int(x)

        y = input("Enter another number: ")
        y = int(y)
    except ValueError:
        print("Try again with a numerical value \ninstead of a written value.")
        sample_addition_else()
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")


sample_addition_else()


print('\n2.On page 202 of your book, do 10-7 of the Try it Yourself.')
# 2.On page 202 of your book, do 10-7 of the Try it Yourself.

# Enter a number: Traceback (most recent call last):
#   File "C:\MyRepository\python-fundamentals\exercises\exercise12.py", line 60, in <module>
#
#   File "C:\MyRepository\python-fundamentals\exercises\exercise12.py", line 44, in whileloop_addition
#     x = input("Enter a number: ")
#   File "C:\Python310\lib\codecs.py", line 319, in decode
#     def decode(self, input, final=False):
# KeyboardInterrupt

# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user
# can continue entering numbers even if they make a mistake and enter text instead of a number.
# Im not sure I know what i missed, to tired to try to figure it out but it was in an infinte loop
# edit: i added an if break escape to y and that seemed to fix it?
print('Hit the \'E\' key to stop loop')


def whileloop_addition():
    while True:
        try:
            x = input("Enter a number: ")
            if x == 'e':
                break
            x = int(x)

            y = input("Enter another number: ")
            if y == 'e':
                break
            y = int(y)

        except ValueError:
            print("Try again with a numerical value \ninstead of a written value.")
            whileloop_addition()
        else:
            sum = x + y
            print(f"The sum of {x} and {y} is {sum}.")


whileloop_addition()
pass

print('\n3.On page 202 of your book, do 10-8 of the Try it Yourself.')
# 3.On page 202 of your book, do 10-8 of the Try it Yourself.
# Make two files, cats.txt and dogs.txt. Store at least three names of cats
# in the first file and three names of dogs in the second file.
# Write a program that tries to read these files and print the contents
# of the file to the screen. Wrap your code ina try-except block to catch
# the FileNotFound error, and print a friendly message if a file is missing.
# Move one of the files to a different location on your system, and make sure
# the code in the except block executes properly.


def cats_dogs_names():
    filenames = ['cats.txt', 'dogs.txt']

    for filename in filenames:
        print(f"\nReading file: {filename}")
        try:
            with open(filename) as f:
                contents = f.read()
                print(contents)
        except FileNotFoundError:
            print("  \n(=^ェ^=) Errr Woof Woof Meow..file not found")


cats_dogs_names()

print("  \n(=^ェ^=) Fowoooond It!")
print("  \nFilename: xdogs.txt")


def xdogs_names():
    filename = ['xdogs.txt']

    for filename in filename:
        print(f"\nReading file: {filename}")
        try:
            with open(filename) as f:
                contents = f.read()
                print(contents)
        except FileNotFoundError:
            print("  \n(=^ェ^=) Errr Woof Woof Meow..file not found")


xdogs_names()


print('\n4.On page 202 of your book, do 10-9 of the Try it Yourself.')
# 4.On page 202 of your book, do 10-9 of the Try it Yourself.
# Modify your except block in Exercise 10-8 to fail silently if either file is missing.


def cats_dogs_names2():
    filenames = ['cats.txt', 'dogs.txt']

    for filename in filenames:
        print(f"\nReading file: {filename}")
        try:
            with open(filename) as f:
                contents = f.read()

        except FileNotFoundError:
            pass

        else:
            print(f"\nReading file: {filename}")
            print(contents)


cats_dogs_names2()
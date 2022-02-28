# 1 Error Correction
# Code Below
# Received error message
# PEP 8: W292 no newline at end of file
# letting me know that there was no new line.
# Also, hitting "enter" or "return" in the middle of a sentence intuitively added a hash mark.

print("Hello World")

# 2 Zen Output

# Try It yourself 2-11 >import this returned :
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# 3 2-1
# Code Below
# added variable "message"
# added print function to display "Hello Python Classroom" value as output
# changed value to "Hello Python World"
message = "Hello Python Classroom!"
print(message)
message = "Hello Python World!"
print(message)

# Playing with Code Below
# added variable "affirm"
# added print function to display "Roger Roger" value as output
affirm = "Roger Roger!"
print(affirm)


# 4 8-1
# I defined a function to display a doc string and print the doc string by calling the function.
def display_message():
    """Display a simple message."""
    print("I am learning how to define a function.")
    print("Stacking Messages Is Fun!")


display_message()

# 4 8-2
# I defined a function book to display a doc string One of my favorite books is Alice in Wonderland
# and print the doc string by calling the function.

# My first attempt, I got errors.
# Traceback (most recent call last):
#  File "C:\MyRepository\python-fundamentals\exercises\exercise1.py", line 71, in <module>
#    print(title)
# NameError: name 'title' is not defined. Did you mean: 'tuple'?
# Finally figured out I had been missing the correct print function.
# Went back and re read the chapters to see what I missed.

def favorite_book(book_name):
    """display my favorite book"""
    print(f'One of my favorite books is {book_name.title()}')


favorite_book('Alice in Wonderland')

# I defined that I was calling the function, gave it a name and details.
# In the body, I updated the doc string and print code for the function to operate
# In the last line I called the function with code to display the output as print.
# Then, for fun, I just reused the code from the book to customize a greeting.


def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('Roger')

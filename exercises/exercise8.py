# CAC-102-8 Exercise - Collections
# Write functions for each of the items below. Call the function to ensure the results are correct.
# 1. On page 89 of your book, do 5-8 &5-9 of the Try it Yourself.
# 5-8 Hello Admin
# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
# 5-9 No Users
# If the list is empty, print the message We need to find some users! Remove all of the usernames
# from your list, and make sure the correct message is printed.
user_names = ['admin', 'director', 'coordinator', 'member', 'user', 'temporary']


def usernames():

    if user_names:
        for username in user_names:
            if username == 'admin':
                print("Hello admin, who are we banning today?")
            else:
                print(f"Hello {username}, we aren\'t accepting anymore logins today.")
    else:
        print("We need to find some users!")


usernames()


# 2.On page 89 of your book, do 5-10 of the Try it Yourself.
# 5-10 Checking Usernames
# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. Make sure one or two of the new usernames are
# also in the current_users list.
# Loop through the new_users list to see if each new username has already been used.
# If it has, print a message that the person will need to enter a new username.
# If a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case-insensitive. If 'John' has been used, 'JOHN' should not be accepted.
# (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
current_users = 'Sam', 'John', 'Sally', 'Deon', 'Janice', 'sam', 'john', 'SALLY', 'deon', 'janice'
new_users = 'DEON', 'Keaneau', 'Bill', 'Ted', 'JeanGray', 'sally'

current_users_lower = [user.lower() for user in current_users]


def user_check():

    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f"Try again {new_user}, that name is unavailable.")
        else:
            print(f"User Accepted, {new_user} is available.")


user_check()

# 3.On page 89 of your book, do 5-11 of the Try it Yourself.
# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2, and 3.
# Store the numbers 1 through 9 in a list.
# Loop through the list.
# Use an if-elif-else chain inside the loop to print the proper ordinal
# ending for each number. Your output should read "1st 2nd 3rd 4th
# 5th 6th 7th 8th 9th", and each result should be on a separate line.
numbers = list(range(1,10))


def num_check():

    for number in numbers:
        if number == 1:
            print("1st")
        elif number == 2:
            print("2nd")
        elif number == 3:
            print("3rd")
        else:
            print(f"{number}th")


num_check()

# 4.On page 99 of your book, do 6-1 of the Try it Yourself.
# 6-1. Person: Use a dictionary to store information about a person you know. Store their first
# name, last name, age, and the city in which they live. You should have keys such as first_name,
# last_name, age, and city. Print each piece of information stored in your dictionary.
person = {
    'first_name': 'Tim',
    'last_name': 'Donnelley',
    'age': 43,
    'city': 'Andover',
    }


def user_entry():

    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])


user_entry()

# 5.On page 112 of your book, do 6-7 of the Try it Yourself.
# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new
# dictionaries representing different people, and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know
# about each person.
people = []

person = {
    'first_name': 'Tim',
    'last_name': 'Donnelley',
    'age': 43,
    'city': 'Andover',
    }
people.append(person)

person = {
    'first_name': 'Bobcat',
    'last_name': 'Goldthwait',
    'age': 56,
    'city': 'NewYork',
}
people.append(person)

person = {
    'first_name': 'Willie',
    'last_name': 'Nelson',
    'age': 72,
    'city': 'Bumtruck',
}
people.append(person)


def people_store():
    for person in people:
        name = f"{person['first_name'].title()} {person['last_name'].title()}"
        age = person['age']
        city = person['city'].title()

        print(f"{name}, of {city}, is {age} years old.")


people_store()
# CAC-102-9 Exercise - Functions & Classes

# 1a. 8-3 T-Shirt: Write a function called make_shirt() that accepts a size and the text of a
# message that should be printed on the shirt. The function should print a sentence summarizing
# the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second
# time using keyword arguments.

def make_shirt(size, message):
    """Shirt size and message detail."""
    print(f"\nThis is going to be a {size} T-shirt")
    print(f'with, "{message}" as the message.')


make_shirt('XL', 'I Love Peaches n Cream')
make_shirt(message="Keywords", size='Argumental(S)')


# 1b. 8-4 Large Shirts: Modify the make_shirt() function so that shirts are large by default with a
# message that reads I love Python. Make a large shirt and a medium shirt with the default
# message, and a shirt of any size with a different message.

def make_shirt(size='large', message='i love python <3'):
    """Shirt size and message detail."""
    print(f"\nThis is going to be a {size} T-shirt")
    print(f'with, "{message}" as the message.')


make_shirt()
make_shirt(size='medium')
make_shirt('XL', 'Wanna see my Python?...CODE!')


# 1c. 8-5 Cities: Write a function called describe_city() that accepts the name of a city and its
# country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give
# the parameter for the country a default value. Call your function for three different cities, at
# least one of which is not in the default country.

def describe_city(city, country='default country'):
    """Describes a city and its location"""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)


describe_city('\nMERICA')
describe_city('dumpsterFIRE', 'putin\'s ruSSia (ಠ益ಠ╬ )')
describe_city('wicheeta','kansaw')
describe_city('default city')


# 2a. 8-9 Messages: Make a list containing a series of short text messages. Pass the list to a function
# called show_messages(), which prints each text message.

def show_messages(messages):
    """Print the messages."""
    for message in messages:
        print(message)


# looked up emoticons to take a break...decompress from getting hung up trying to figure this out!
messages = ["\nSometimes", "you feel", "like a nut", "Sometimes", "you don\'t", "┐(ﾟ⊿ﾟ)┌"]
show_messages(messages)


# 2b. 8-10 Sending Messages: Start with a copy of your program from Exercise 8-9. Write a
# function called send_messages() that prints each text message and moves each message to a
# new list called sent_messages as it’s printed. After calling the function, print both of your lists
# to make sure the messages were moved correctly.

def show_messages(messages):
    """Print the messages."""
    print("\nList View")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Print each message and move them to sent."""
    print("\nDelivering Msgs")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
# showing messages to be pop() to sent before pop method is applied

messages = ["Sometimes", "you feel", "like a nut", "Sometimes", "you don\'t", "┐(ﾟ⊿ﾟ)┌"]
show_messages(messages)


sent_messages = []
send_messages(messages, sent_messages)


print("\nFinal lists:")
print(messages)
print(sent_messages)


# 2c. 8-11 Archived Messages: Start with your work from Exercise 8-10. Call the function
# send_messages() with a copy of the list of messages. After calling the function, print both of
# your lists to show that the original list has retained its messages.


def show_messages(messages):
    """Print the messages."""
    print("\nList View")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Print each message and move them to sent."""
    print("\nDelivering Msgs")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["Sometimes", "you feel", "like a nut", "Sometimes", "you don\'t", "┐(ﾟ⊿ﾟ)┌"]
show_messages(messages)


sent_messages = []
send_messages(messages[:], sent_messages)


print("\nFinal lists:")
print(messages)
print(sent_messages)


# 3a. 9-1 Restaurant: Make a class called Restaurant. The __init__() method for Restaurant
# should store two attributes: a restaurant_name and a cuisine_type. Make a method called
# describe_restaurant() that prints these two pieces of information, and a method called
# open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually,
# and then call both methods.

class Restaurant:
    """Restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Restaurant description"""
        msg = f"{self.restaurant_name} has {self.cuisine_type}."
        print(f"{msg}")

    def open_restaurant(self):
        """Indicates the restaurant is open."""
        msg = f"{self.restaurant_name} is open 24/7."
        print(f"{msg}")


restaurant = Restaurant('Quiktrip', 'Pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 3b 9-2 Three Restaurants: Start with your class from Exercise 9-1. Create three different
# instances from the class, and call describe_restaurant() for each instance.

class Restaurant:
    """Restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Restaurant description"""
        msg = f"{self.restaurant_name} has {self.cuisine_type}."
        print(f"{msg}")

    def open_restaurant(self):
        """Indicates the restaurant is open."""
        msg = f"{self.restaurant_name} is open 24/7."
        print(f"{msg}")


quik_trip = Restaurant('Quiktrip', 'Pizza and Sammiches')
quik_trip.describe_restaurant()

noodle_hut = Restaurant('NoodleHut', '...Nooooodles')
noodle_hut.describe_restaurant()

taco_hell = Restaurant('Taco Bell', 'crap, no thanks')
taco_hell.describe_restaurant()

# 3c. 9-3 Users: Make a class called User. Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile. Make a
# method called describe_user() that prints a summary of the user’s information. Make another
# method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each


class User():
    """Saved User Profile"""

    def __init__(self, first_name, last_name, login, contact, fav_color, ):
        """Initialize user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.contact = contact
        self.login = login.title()
        self.fav_color = fav_color.title()

    def describe_user(self):
        """User file summary"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Login: {self.login}")
        print(f"  Contact: {self.contact}")
        print(f"  Favorite Color: {self.fav_color}")

    def greet_user(self):
        """Greet the user"""
        print(f"\nYou have successfully logged in, {self.login}!")


tim = User('tim', 'donnelley', 'timdonnl', 'timd@mail.com', 'blue')
tim.describe_user()
tim.greet_user()

bill = User('bill', 'murray', 'bilmurr', 'zombie@land.con', 'red')
bill.describe_user()
bill.greet_user()

zayphod = User('zayphod', 'beeblebrox', 'zaphbrox', 'fifth@planet.org', 'black')
zayphod.describe_user()
zayphod.greet_user()

# 4a. 9-4 Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute
# called number_served with a default value of 0. Create an instance called restaurant from this
# class. Print the number of customers the restaurant has served, and then change this value and
# print it again.
# Add a method called set_number_served() that lets you set the number of customers that
# have been served. Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of
# customers who’ve been served. Call this method with any number you like that could represent
# how many customers were served in, say, a day of business.


class Restaurant:
    """Restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Restaurant description"""
        msg = f"{self.restaurant_name} has {self.cuisine_type}."
        print(f"{msg}")

    def open_restaurant(self):
        """Indicates the restaurant is open."""
        msg = f"{self.restaurant_name} is open 24/7."
        print(f"{msg}")

    def set_number_served(self, number_served):
        """Indicates the number of customers served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Served number in increments."""
        self.number_served = additional_served


restaurant = Restaurant('\nNoodleHut', '...Nooooodles')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 78
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(135)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(456)
print(f"Number served: {restaurant.number_served}")

# 4b. 9-5 Login Attempts: Add an attribute called login_attempts to your User class from
# Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments
# the value of login_attempts by 1. Write another method called reset_login_attempts() that
# resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call
# reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.


class User():
    """Saved User Profile"""

    def __init__(self, first_name, last_name, login, contact, fav_color, ):
        """Initialize user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.contact = contact
        self.login = login.title()
        self.fav_color = fav_color.title()
        self.login_attempts = 0

    def describe_user(self):
        """User file summary"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Login: {self.login}")
        print(f"  Contact: {self.contact}")
        print(f"  Favorite Color: {self.fav_color}")

    def greet_user(self):
        """Greet the user"""
        print(f"\nYou have successfully logged in, {self.login}!")

    def increment_login_attempts(self):
        """incremented login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts"""
        self.login_attempts = 0


zayphod = User('zayphod', 'beeblebrox', 'zaphbrox', 'fifth@planet.org', 'black')
zayphod.describe_user()
zayphod.greet_user()

print("\nMaking 3 login attempts...")
zayphod.increment_login_attempts()
zayphod.increment_login_attempts()
zayphod.increment_login_attempts()
print(f"  Login attempts: {zayphod.login_attempts}")

print("Resetting login attempts...")
zayphod.reset_login_attempts()
print(f"  Login attempts: {zayphod.login_attempts}")


# CAC-102-11 Exercise - Inheritance & Polymorphism


print('\n1. On page 173 of your book, do 9-6 of the Try it Yourself.')
# An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand
# that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166)
# or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.


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


class IceCreamStand(Restaurant):
    """Ice cream stand class."""

    def __init__(self, name, cuisine_type='ice cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the new flavors."""
        print("\nHere's some new flavors to try:")
        for flavor in self.flavors:
            print(f"(✿◠‿°)づ{flavor.title()}")


bozos = IceCreamStand('\nBozo\'s')
bozos.flavors = ['clown shirt', 'choco cotton', 'monkey butt', 'chewed gum']

bozos.describe_restaurant()
bozos.show_flavors()


print('\n2. On page 173 of your book, do 9-7 of the Try it Yourself.')

# An administrator is a special kind of user. Write a class called Admin that inherits
# from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171).
# Add an attribute, privileges, that stores a list of strings like "can add post",
# "can delete post", "can ban user", and so on. WRite a method called show_privileges()
# that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.


class User:
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


class Admin(User):
    """Admin privileges."""

    def __init__(self, first_name, last_name, login, contact, fav_color):
        """Initialize the admin."""
        super().__init__(first_name, last_name, login, contact, fav_color)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges for this user."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


zayphod = Admin('zayphod', 'beeblebrox', 'zaphbrox', 'fifth@planet.org', 'black')
zayphod.describe_user()

zayphod.privileges = ['can ban user', 'can delete post', 'can use company cc',]

zayphod.show_privileges()


print('\n3. On page 173 of your book, do 9-8 of the Try it Yourself.')
# Write a separate Privileges class. The class should have one attribute, privileges,
# that stores a list of strings as described in Exercise 9-7. Move the show_privileges()
# method to this class. Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.


class User:
    """Saved User Profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """User file summary."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Greet the User."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize no privileges.
        self.privileges = Privileges()


class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


zayphod = Admin('zayphod', 'beeblebrox', 'zaphbrox', 'fifth@planet.org', 'black')
zayphod.describe_user()

zayphod.privileges.show_privileges()

print("\n- New privileges added")
zayphod_privileges = ['can ban user', 'can delete post', 'can use company cc',]
zayphod.privileges.privileges = zayphod_privileges
zayphod.privileges.show_privileges()


print('\n4.Using your horse objects from the Encapsulation exercise, '
      'create your 2 child objects and save them in horse.py')
# 4.Using your horse Objects from the Encapsulation exercise, create your 2 child
# objects from the OOP section of the previous class. Use the property decorator
# for your child objects. Put both children objects inside your horse.py file.


print('(╯°□°）╯')
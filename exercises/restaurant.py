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
# CAC-102-14 Exercise Testing Your Code
print('\n1.On page 215 of your book, do 11-1')
# 1.On page 215 of your book, do 11-1
# 11-1. City, Country: Write a function that accepts two parameters: a city name and a country
# name. The function should return a single string of the form City, Country, such as
# Santiago, Chile. Store the function in a module called city_functions.py.
# Create a file called test_cities.py that tests the function you just wrote (remember that you
# need to import unittest and the function you want to test). Write a method called
# test_city_country() to verify that calling your function with values such as 'santiago' and
# 'chile' results in the correct string. Run test_cities.py, and make sure test_city_country()
# passes.
import unittest


def describe_city(name, country):
    return f'{name}, {country}'


class CitiesTest(unittest.TestCase):
    def test_city_country(self):
        andover_usa = describe_city('andover', 'usa')
        self.assertEqual(andover_usa, 'andover, usa')



print('\n2.On page 216 of your book, do 11-2')
# 2.On page 216 of your book, do 11-2
# 11-2. Population: Modify your function so it requires a third parameter, population. It
# should now return a single string of the form City, Country – population xxx, such as
# Santiago, Chile – population 5000000. Run test_cities.py again. Make sure
# test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run test_cities.py again, and
# make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies you can call your
# function with the values 'santiago', 'chile', and 'population=5000000'. Run test_cities.py
# again, and make sure this new test passes.


def describe_city_2(name, country, population):
    result = f'{name}, {country}'
    if population:
        result += f', {population}'
    return result


class CitiesTest2(unittest.TestCase):
    def test_describe_city_2(self):
        andover_us_pop = describe_city_2('andover', 'usa', '500000')
        self.assertEqual(andover_us_pop, 'andover, usa, 500000')


print('\n3.On page 221 of your book, do 11-3')
# 3.On page 221 of your book, do 11-3
# 11-3. Employee: Write a class called Employee. The __init__() method should take in a first
# name, a last name, and an annual salary, and store each of these as attributes. Write a method
# called give_raise() that adds $5,000 to the annual salary by default but also accepts a different
# raise amount.
# Write a test case for Employee. Write two test methods, test_give_default_raise() and
# test_give_custom_raise(). Use the setUp() method so you don’t have to create a new
# employee instance in each test method. Run your test case, and make sure both tests pass.


class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.ryan = Employee('ryan', 'michelle', 50000)

    def test_raise(self):
        self.ryan.give_raise()
        self.assertEqual(self.ryan.salary, 55000)

    def test_custom_raise(self):
        self.ryan.give_raise(10000)
        self.assertEqual(self.ryan.salary, 60000)


if __name__ == '__main__':
    unittest.main()


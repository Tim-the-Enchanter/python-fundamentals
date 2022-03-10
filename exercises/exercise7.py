# CAC-102-7 Exercise - Looping

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
def try_it1():
    for nums1 in range(1, 21):
        print(nums1)


try_it1()


# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd
# numbers from 1 to 20. Use a for loop to print each number.
def try_it2():
    for nums2 in range(1, 21, 2):
        print(nums2)


try_it2()


# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the
# numbers in your list.
def try_it3():
    for nums3 in range(3, 31, 3):
        print(nums3)


try_it3()


# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is
# written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer
# from 1 through 10), and use a for loop to print out the value of each cube.
def try_it4():
    cubes = []
    for value in range(1, 11):
        cube = value ** 3
        cubes.append(cube)
    print(cubes)


try_it4()

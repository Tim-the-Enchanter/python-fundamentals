# All about numbers
# Numeric types are broken down in to three distinct categories: int, float & complex

# int in detail
val_int1 = 42
val_int2 = 8164888888
val_int3 = -4456889
val_int4 = 123456789987654321

# print values
print(val_int1)
print(val_int2)
print(val_int3)
print(val_int4)

# get type of one of our values above
print(type(val_int4))

# Float in detail
val_float1 = 3.14
val_float2 = 2.13456
val_float3 = -234.45

# Print values of float
print(val_float1)
print(val_float2)
print(val_float3)

# Scientific Notation
val_float4 = 25E4
val_float5 = 42e9
val_float6 = -98.6E2

print(val_float4)
print(val_float5)
print(val_float6)

# Get the type of a float value
print(type(val_float2))

# Complex in partial detail
val_complex = 3j
val_complex2 = -5j

print(val_complex)
print(val_complex2)

# The methods below will convert an integer to different numeric system values
print(bin(22))
print(oct(22))
print(hex(22))

value = 0b10110
print(value)

# Taking values that are strings and converting, while also converting
# numbers to string
value1 = float(34)
value2 = int(34.5)
value3 = str(89.3)
value4 = str(48)
value5 = int('45')
value6 = float('23.5')

# print values used in converting
print(value1)
print(value2)
print(value3)
print(value4)
print(value5)
print(value6)

# input allows for user to provide information for us to use
name = input('What is your name?')
movie = input('What is your favorite movie?')

message = 'My name is {0} and my favorite movie is {1}'
print(message.format(name, movie))


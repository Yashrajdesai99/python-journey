"""
variables.py
Basic use of variables and data types
"""

# Basic variables
name = "Yashraj"
age = 18
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


# Check types
print("\nTypes:")
print(type(name), type(age), type(height), type(is_student))


# Multiple assignment
a, b, c = 10, 20, 30
print("\nValues:", a, b, c)


# Type casting
x = "100"
y = int(x)
z = float(age)

print("\nCasting:", y, z)


# Basic math
num1, num2 = 10, 5
print("\nMath:")
print(num1 + num2, num1 - num2, num1 * num2, num1 / num2)


# Strings
first = "Yash"
last = "Raj"
full = first + " " + last

print("\nFull Name:", full)
print("Length:", len(full))


# Simple real example
student = "Amit"
marks = 85
print(f"\n{student} scored {marks} marks")


# Constant style
PI = 3.14159
print("\nPI:", PI)

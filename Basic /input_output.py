"""
input_output.py
Basic input and output in Python
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\nUser Info:")
print("Name:", name)
print("Age:", age)
print("City:", city)

print(f"\n{name} is {age} years old and lives in {city}")

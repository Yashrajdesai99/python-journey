"""
type_casting_operators.py
Type casting + basic operators
"""

# Type casting
x = "50"
y = int(x)

a = 10
b = float(a)

print("Casting:")
print(y, type(y))
print(b, type(b))


# Operators
num1 = 10
num2 = 3

print("\nOperators:")
print("Add:", num1 + num2)
print("Sub:", num1 - num2)
print("Mul:", num1 * num2)
print("Div:", num1 / num2)
print("Mod:", num1 % num2)


# Small logic
value = input("\nEnter a number: ")
value = int(value)

print("Double:", value * 2)
print("Half:", value / 2)

print("=== Student Manager ===")

name = input("Enter student name: ")
age = int(input("Enter age: "))
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

marks = [m1, m2, m3]

total = sum(marks)
avg = total / len(marks)

subjects = ("Math", "Science", "English")

student = {
    "name": name,
    "age": age,
    "marks": marks,
    "avg": avg
}

unique_marks = set(marks)

print("\n--- Student Data ---")
print("Name:", student["name"])
print("Age:", student["age"])
print("Subjects:", subjects)
print("Marks:", student["marks"])
print("Total:", total)
print("Average:", avg)

print("\nUnique Marks:", unique_marks)

print("\n--- Result ---")
if avg >= 50:
    print(f"{name} Passed 🎉")
else:
    print(f"{name} Failed ❌")

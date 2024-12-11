students = ["Alice", "Bob", "Charlie", "Diana"]
name = input("Enter name to search: ")

if name in students:
    print(f"Found at index: {students.index(name)}")
else:
    print("Name not found.")

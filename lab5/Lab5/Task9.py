def display_students(students):
    if not students:
        print("No students in the list.")
    else:
        print("List of Students:")
        for student in students:
            print(student)

def add_student(students, name):
    students.append(name)
    print(f"{name} has been added.")

def remove_student(students, name):
    if name in students:
        students.remove(name)
        print(f"{name} has been removed.")
    else:
        print(f"{name} not found in the list.")

def main():
    students = []
    
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter the name of the student to add: ")
            add_student(students, name)
        elif choice == '2':
            name = input("Enter the name of the student to remove: ")
            remove_student(students, name)
        elif choice == '3':
            display_students(students)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

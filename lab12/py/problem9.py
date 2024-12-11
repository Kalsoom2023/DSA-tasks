students = []

while True:
    print("1. Add Student\n2. Remove Student\n3. Display Students\n4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        student = input("Enter student name to add: ")
        students.append(student)
    elif choice == 2:
        student = input("Enter student name to remove: ")
        if student in students:
            students.remove(student)
        else:
            print("Student not found.")
    elif choice == 3:
        print("Students:", students)
    elif choice == 4:
        break
    else:
        print("Invalid choice.")

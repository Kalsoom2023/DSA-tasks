def search_student(students, name_to_find):
    try:
        index = students.index(name_to_find)
        print(f"{name_to_find} found at index: {index}")
    except ValueError:
        print(f"{name_to_find} is not present in the list.")

def main():
    students = ["Ali", "Amna", "Mahnoor", "Lizzie", "Kalsoom"]

    name = input("Enter the name of the student to search for: ")

    search_student(students, name)

if __name__ == "__main__":
    main()

print("==============================")
print("   STUDENT MANAGEMENT SYSTEM")
print("==============================")

students = []

while True:
    print()
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter student course: ")

        student = [name, age, course]
        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        print()
        print("STUDENT LIST")

        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print("------------------------------")
                print("Name:", student[0])
                print("Age:", student[1])
                print("Course:", student[2])

    elif choice == "3":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice!")
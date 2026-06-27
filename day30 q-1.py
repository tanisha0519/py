roll = []
name = []
marks = []
while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        roll.append(input("Enter Roll Number: "))
        name.append(input("Enter Student Name: "))
        marks.append(float(input("Enter Marks: ")))
        print("Student record added successfully.")
    elif choice == 2:
        if len(roll) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for i in range(len(roll)):
                print("Roll No.:", roll[i])
                print("Name    :", name[i])
                print("Marks   :", marks[i])
                print("------------------------")
    elif choice == 3:
        r = input("Enter Roll Number to search: ")
        if r in roll:
            i = roll.index(r)
            print("Roll No.:", roll[i])
            print("Name    :", name[i])
            print("Marks   :", marks[i])
        else:
            print("Student not found.")
    elif choice == 4:
        r = input("Enter Roll Number to update: ")
        if r in roll:
            i = roll.index(r)
            name[i] = input("Enter New Name: ")
            marks[i] = float(input("Enter New Marks: "))
            print("Student record updated successfully.")
        else:
            print("Student not found.")
    elif choice == 5:
        r = input("Enter Roll Number to delete: ")
        if r in roll:
            i = roll.index(r)
            del roll[i]
            del name[i]
            del marks[i]
            print("Student record deleted successfully.")
        else:
            print("Student not found.")
    elif choice == 6:
        print("Thank you! Exiting Student Record System.")
        break
    else:
        print("Invalid choice! Please try again.")
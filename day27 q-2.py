employees = {}
while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))
        employees[emp_id] = {
            "Name": name,
            "Salary": salary
        }
        print("Employee added successfully.")
    elif choice == 2:
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for emp_id, details in employees.items():
                print("Employee ID:", emp_id)
                print("Name:", details["Name"])
                print("Salary:", details["Salary"])
                print("---------------------------")
    elif choice == 3:
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in employees:
            print("Employee ID:", emp_id)
            print("Name:", employees[emp_id]["Name"])
            print("Salary:", employees[emp_id]["Salary"])
        else:
            print("Employee not found.")
    elif choice == 4:
        emp_id = input("Enter Employee ID to update: ")
        if emp_id in employees:
            name = input("Enter New Name: ")
            salary = float(input("Enter New Salary: "))
            employees[emp_id]["Name"] = name
            employees[emp_id]["Salary"] = salary
            print("Employee record updated successfully.")
        else:
            print("Employee not found.")
    elif choice == 5:
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee record deleted successfully.")
        else:
            print("Employee not found.")
    elif choice == 6:
        print("Thank you! Exiting Employee Management System.")
        break
    else:
        print("Invalid choice! Please try again.")
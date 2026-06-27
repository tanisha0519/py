emp_id = []
emp_name = []
emp_salary = []
while True:
    print("\n===== MINI EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        emp_id.append(input("Enter Employee ID: "))
        emp_name.append(input("Enter Employee Name: "))
        emp_salary.append(float(input("Enter Employee Salary: ")))
        print("Employee added successfully.")
    elif choice == 2:
        if len(emp_id) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for i in range(len(emp_id)):
                print("Employee ID :", emp_id[i])
                print("Employee Name :", emp_name[i])
                print("Salary :", emp_salary[i])
                print("--------------------------")
    elif choice == 3:
        eid = input("Enter Employee ID to search: ")
        if eid in emp_id:
            i = emp_id.index(eid)
            print("Employee ID :", emp_id[i])
            print("Employee Name :", emp_name[i])
            print("Salary :", emp_salary[i])
        else:
            print("Employee not found.")
    elif choice == 4:
        eid = input("Enter Employee ID to update: ")
        if eid in emp_id:
            i = emp_id.index(eid)
            emp_name[i] = input("Enter New Name: ")
            emp_salary[i] = float(input("Enter New Salary: "))
            print("Employee record updated successfully.")
        else:
            print("Employee not found.")
    elif choice == 5:
        eid = input("Enter Employee ID to delete: ")
        if eid in emp_id:
            i = emp_id.index(eid)
            del emp_id[i]
            del emp_name[i]
            del emp_salary[i]
            print("Employee record deleted successfully.")
        else:
            print("Employee not found.")
    elif choice == 6:
        print("Thank you! Exiting Mini Employee Management System.")
        break
    else:
        print("Invalid choice! Please try again.")
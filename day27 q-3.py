employees = {}
while True:
    print("\n===== Salary Management System =====")
    print("1. Add Employee")
    print("2. View Salary Details")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))
        hra = float(input("Enter HRA: "))
        da = float(input("Enter DA: "))
        total_salary = basic + hra + da
        employees[emp_id] = {
            "Name": name,
            "Basic": basic,
            "HRA": hra,
            "DA": da,
            "Total Salary": total_salary
        }
        print("Employee salary record added successfully.")
    elif choice == 2:
        if len(employees) == 0:
            print("No records found.")
        else:
            print("\nSalary Details:")
            for emp_id, details in employees.items():
                print("Employee ID:", emp_id)
                print("Name:", details["Name"])
                print("Basic Salary:", details["Basic"])
                print("HRA:", details["HRA"])
                print("DA:", details["DA"])
                print("Total Salary:", details["Total Salary"])
                print("-----------------------------")
    elif choice == 3:
        emp_id = input("Enter Employee ID to update: ")
        if emp_id in employees:
            basic = float(input("Enter New Basic Salary: "))
            hra = float(input("Enter New HRA: "))
            da = float(input("Enter New DA: "))
            total_salary = basic + hra + da
            employees[emp_id]["Basic"] = basic
            employees[emp_id]["HRA"] = hra
            employees[emp_id]["DA"] = da
            employees[emp_id]["Total Salary"] = total_salary
            print("Salary updated successfully.")
        else:
            print("Employee not found.")
    elif choice == 4:
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee record deleted successfully.")
        else:
            print("Employee not found.")
    elif choice == 5:
        print("Thank you! Exiting Salary Management System.")
        break
    else:
        print("Invalid choice! Please try again.")
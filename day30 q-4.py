students = []
def add_student():
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    students.append([name, marks])
def view_students():
    if len(students) == 0:
        print("No Records")
    else:
        for s in students:
            print("Name:", s[0], "Marks:", s[1])
while True:
    print("\n1.Add 2.View 3.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        add_student()
    elif ch == 2:
        view_students()
    elif ch == 3:
        break
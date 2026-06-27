print("===== Marksheet Generation System =====")
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
english = int(input("Enter marks in English: "))
maths = int(input("Enter marks in Mathematics: "))
science = int(input("Enter marks in Science: "))
computer = int(input("Enter marks in Computer: "))
hindi = int(input("Enter marks in Hindi: "))
total = english + maths + science + computer + hindi
percentage = total / 5
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
if english >= 33 and maths >= 33 and science >= 33 and computer >= 33 and hindi >= 33:
    result = "PASS"
else:
    result = "FAIL"
print("\n========== MARKSHEET ==========")
print("Student Name :", name)
print("Roll Number  :", roll)
print("-------------------------------")
print("English      :", english)
print("Mathematics  :", maths)
print("Science      :", science)
print("Computer     :", computer)
print("Hindi        :", hindi)
print("-------------------------------")
print("Total Marks  :", total, "/500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("Result       :", result)
print("===============================")
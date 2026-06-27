rows=int(input("Enter number of rows:"))
column=int(input("Enter number od column:"))\
A=[]
print("Enter element for first matrix:")
for i in range(rows):
    row=[]
    for j in range(column):
        row.append(int(input()))
        A.append(row)
print("Transpose of matrix:")
for i in range(column):
    for j in range(rows):
        print(A[j][i],end="")
        print()


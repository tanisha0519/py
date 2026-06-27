rows=int(input("Enter number of rows:"))
column=int(input("Enter number od column:"))\
A=[]
print("Enter element for first matrix:")
for i in range(rows):
    row=[]
    for j in range(column):
        row.append(int(input()))
        A.append(row)
B=[]
print("Enter element for second matrix:")
for i in range(rows):
    row=[]
    for j in range(column):
        row.append(int(input()))
        B.append(row)
C=[]
print("Enter element for third matrix:")
for i in range(rows):
    row=[]
    for j in range(column):
        row.append(A[i][j]-B[i][j])
        C.append(row)
print("Difference in matrices:")
for i in C:
    print(i)
    
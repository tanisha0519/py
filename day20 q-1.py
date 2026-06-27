rows=int(input("Enter number of rows:"))
column=int(input("Enter number od column:"))
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
        row.append(0)
        C.append(row)
        for i in range(rows):
            for j in range(column):
                for k in range(column):
                    C[i][j]+=A[i][k]*B[k][j]
print("Product of matrices:")
for i in C:
    print(i)

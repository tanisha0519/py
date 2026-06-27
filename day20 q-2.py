rows=int(input("Enter number of rows:"))
column=int(input("Enter number od column:"))
A=[]
print("Enter element for first matrix:")
for i in range(rows):
    row=[]
    for j in range(column):
        row.append(int(input()))
        A.append(row)
        flag=True
        for i in range(n):
            for j in range(n):
                if A [i][j]!= A[j][i]:
                    flag= False
                    break
                if flag:
                    print("Matrix is symmetric")
                else:
                    print("Matrix is not symmetric")

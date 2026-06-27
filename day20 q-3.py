rows=int(input("Enter number of rows:"))
column=int(input("Enter number od column:"))
A=[]
print("Enter element for first matrix:")
for i in range(rows):
    row=[]
    for j in range(column):
        row.append(int(input()))
        A.append(row)
        for i in range(rows):
            row_sum=0
            for j in range(column):
                row_sum += A[i][j]
                print("Sum of rows:",i+1,row_sum)



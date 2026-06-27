rows=int(input("Enter number of rows:"))
column=int(input("Enter number od column:"))
A=[]
print("Enter element for first matrix:")
for i in range(rows):
    row=[]
    for j in range(column):
        row.append(int(input()))
        A.append(row)
        for j in range(column):
            column_sum=0
            for i in range(row):
                column_sum += A[i][j]
                print("Sum of rows:",i+1,column_sum)

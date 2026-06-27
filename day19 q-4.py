rows=int(input("Enter number of rows:"))
column=int(input("Enter number od column:"))
A=[]
print("Enter element for first matrix:")
for i in range(rows):
    row=[]
    for j in range(column):
        row.append(int(input()))
        A.append(row)
main_diagonal=0
secondary_diagonal=0
for i in range(n):
    main_diagonal+=A[i][i]
    secondar_diagonal+=A[i][n-1-i]
print("Main diagonalsum:",main_diagonal)
print("secondar diagonal sum:",secondary_diagonal)
print("Total diagonal sum:",main_diagonal+secondary_diagonal)

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

def read_matrix(name):
    print(f"Enter elements for {name} matrix:")
    M = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(int(input()))
        M.append(row)
    return M

A = read_matrix('first')
B = read_matrix('second')
C = read_matrix('third')

print("Sum of matrices:")
for i in range(rows):
    row_sum = []
    for j in range(columns):
        row_sum.append(A[i][j] + B[i][j] + C[i][j])
    print(row_sum)



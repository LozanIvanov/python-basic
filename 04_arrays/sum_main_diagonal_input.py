n=int(input("Enter the size of the matrix (n x n): "))
matrix=[]

for i in range(n):
    row=[]
    for j in range(n):
        value=float(input(f"Element at position [{i}][{j}]:"))
        row.append(value)
    matrix.append(row)   

sum_diagonal=0

for i in range(n):
    sum_diagonal+=matrix[i][i]

if sum_diagonal.is_integer():
    print(int(sum_diagonal))
else:
    print(sum_diagonal)

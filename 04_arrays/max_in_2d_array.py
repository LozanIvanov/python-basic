matrix = [
    [5, 8, 2],
    [7, 9, 1],
    [4, 6, 3]
]
max_value=matrix[0][0]

for row in matrix:
    for num in row:
        if num>max_value:
            max_value=num

print(f"The largest number in the 2D array is: {max_value}")
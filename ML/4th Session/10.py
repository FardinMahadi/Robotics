matrix = []

print("Enter 3x3 matrix")

for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    while len(row) != 3:
        print("Please enter exactly 3 numbers.")
        row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

transpose = []
for j in range(3):
    new_row = []
    for i in range(3):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

print("\nOriginal matrix:")
for row in matrix:
    print(row)

print("\nTranposed matrix:")
for row in transpose:
    print(row)
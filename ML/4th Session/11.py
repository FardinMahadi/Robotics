def generate_pascals_triangle(n):
    traingle = []

    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = traingle[i-1]
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])
            row.append(1)        
        traingle.append(row)
    return traingle

n = int(input("Enter a number: "))
triangle = generate_pascals_triangle(n)

for row in triangle:
    print(' '.join(map(str, row)).center(n*2))

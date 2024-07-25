def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Start the row with 1
        row = [1]
        # Generate the middle elements
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        # End the row with 1
        row.append(1)
        triangle.append(row)

    return triangle

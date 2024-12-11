grid = [[1, 2], [3, 4]]

# Add a row
grid.append([5, 6])
print("After adding a row:", grid)

# Add a column
for row in grid:
    row.append(0)
print("After adding a column:", grid)

# Sum of elements
print("Sum of elements:", sum(sum(row) for row in grid))

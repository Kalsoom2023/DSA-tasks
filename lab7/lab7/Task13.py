def display(grid):
    for row in grid:
        print(" ".join(map(str, row)))
    print() 

def addrow(grid, new_row):
    grid.append(new_row)

def addcolumn(grid, new_col):
    if len(new_col) != len(grid):
        print("Error")
        return
    
    for i in range(len(grid)):
        grid[i].append(new_col[i])

def sum_of_elements(grid):
    total = 0
    for row in grid:
        total += sum(row)
    return total

def main():
    # Initialize an empty grid
    grid = []

    # Adding rows
    addrow(grid, [1, 2, 3])
    addrow(grid, [4, 5, 6])
    addrow(grid, [7, 8, 9])
    
    print("Initial grid:")
    display(grid)


    addrow(grid, [10, 11, 12])
   
    display(grid)

    addcolumn(grid, [13, 14, 15, 16])
   
    display(grid)

    totalsum = sum_of_elements(grid)
    print("Sum:", totalsum)

if __name__ == "__main__":
    main()

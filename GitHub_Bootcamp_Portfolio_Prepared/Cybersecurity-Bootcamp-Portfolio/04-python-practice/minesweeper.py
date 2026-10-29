
# Create a function that takes a grid as input
def minesweeper(grid):

    # Get the number of rows in the grid
    rows = len(grid)

    # Get the number of columns in the grid
    cols = len(grid[0])

    # Create an empty list to store the completed grid
    result = []

    # Loop through each row
    for row in range(rows):

        # Create an empty list for the current row
        new_row = []

        # Loop through each column
        for col in range(cols):

            # If the current position contains a mine
            if grid[row][col] == "#":

                # Keep the mine symbol unchanged
                new_row.append("#")

            else:
                # Start the mine counter at zero
                mine_count = 0

                # Check the row above, current row, and row below
                for r in range(row - 1, row + 2):

                    # Check the column to the left, current column,
                    # and column to the right
                    for c in range(col - 1, col + 2):

                        # Make sure the position is inside the grid
                        if 0 <= r < rows and 0 <= c < cols:

                            # Ignore the current position itself
                            # Check whether the surrounding position is a mine
                            if (r != row or c != col) and \
                                    grid[r][c] == "#":

                                # Increase the mine counter by one
                                mine_count += 1

                # Add the number of nearby mines to the current row
                new_row.append(mine_count)

        # Add the completed row to the result grid
        result.append(new_row)

    # Return the completed grid
    return result


# Example input grid
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Call the function and save the result
output = minesweeper(grid)

# Print the resulting grid
print("Minesweeper output:")
for row in output:
    print(row)
 
                                        
                                        
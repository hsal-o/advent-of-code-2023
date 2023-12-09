def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

GEAR = '*'
grid = []


def main():
    # Sample lines
    lines = get_lines_from_file("input.txt")

    # Process each line and add values
    for line in lines:
        grid.append(list(line.strip()))

    row_count = len(grid)
    width_count = len(grid[0])

    gear_ratio = 0

    # Go through entire grid
    for y in range(0, row_count):
        for x in range(0, width_count):

            # Check if current char is a gear
            if(grid[y][x] == GEAR):
                # Create neighbor list
                neighbor_numbers = [] 

                # Create a smaller portion grid for efficiency
                portion_grid_row_count = 7
                portion_grid_col_count = 7
                portion_grid = [['.'] * portion_grid_col_count for i in range(portion_grid_row_count)]
                start_x =   int(x - (portion_grid_col_count-1)/2)
                end_x =     int(x + ((portion_grid_col_count-1)/2) + 1)
                start_y =   int(y - (portion_grid_row_count-1)/2)
                end_y =     int(y + ((portion_grid_row_count-1)/2) + 1)
                # Start copying values from grid to portion grid
                for _y in range(start_y, end_y):
                    for _x in range(start_x, end_x):
                        # If cell is in range
                        if(_x >= 0 and _x < width_count and _y >= 0 and _y < row_count):
                            # Create portion grid
                            portion_grid[_y - start_y][_x - start_x] = grid[_y][_x]

                # Look in a 3x3 grid around the center of portion_grid for adjacent numbers
                center_x = int(portion_grid_col_count/2)
                center_y = int(portion_grid_row_count/2)
                for _y in range(center_y-1, center_y+2):
                    for _x in range(center_x-1, center_x+2):
                        char = portion_grid[_y][_x]

                        # If neighbor is a number
                        if(char.isdigit()):
                            number = char

                            ## Using number grabbed, grab digits before and after to fully build
                            # Add digits to the left
                            for nx in range(_x-1, -1, - 1):
                                if(nx >= 0):
                                    if(portion_grid[_y][nx].isdigit()):
                                        number = portion_grid[_y][nx] + number
                                        portion_grid[_y][nx] = '.'
                                    else:
                                        break

                            # Add digits to the right
                            for nx in range(_x+1, portion_grid_col_count):
                                if(nx < portion_grid_col_count):
                                    if(portion_grid[_y][nx].isdigit()):
                                        number = number + portion_grid[_y][nx]
                                        portion_grid[_y][nx] = '.'
                                    else:
                                        break
                            
                            # print(f"number: {number}")
                            # Add number to our neighbor list
                            neighbor_numbers.append(int(number))
                    
                # If this gear has exactly two number neighbors
                if(len(neighbor_numbers) == 2):
                    gear_ratio += neighbor_numbers[0] * neighbor_numbers[1]

    print(f'gear_ratio: {gear_ratio}')


if __name__ == "__main__":
    main()



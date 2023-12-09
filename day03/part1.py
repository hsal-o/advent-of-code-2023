def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None


def main():
    # Sample lines
    lines = get_lines_from_file("input.txt")

    grid = []

    # Process each line and add values
    for line in lines:
        grid.append(list(line.strip()))

    row_count = len(grid)
    width_count = len(grid[0])

    sum = 0

    y = 0
    while y < row_count:
        x = 0
        while x < width_count:
            # We hit a digit
            if(grid[y][x].isdigit()):
                
                # Index to keep track where to place x at the end
                last_index = x+1

                # Boolean flag
                added_to_sum = False

                # Check to see if number neighbors symbol
                for _y in range(y-1, y+2):
                    for _x in range(x-1, x+2):
                        # Check if the coordinate is valid
                        if(_x >= 0 and _x < width_count and _y >= 0 and _y < row_count):
                            char = grid[_y][_x]

                            # We found a neighbor and we havent added this number to sum yet
                            if(not(char).isdigit() and char != '.' and not added_to_sum):
                                
                                # Process number
                                number = grid[y][x]

                                # Add digits to the left
                                for _x in range(x-1, -1, - 1):
                                    if(_x >= 0):
                                        if(grid[y][_x].isdigit()):
                                            number = grid[y][_x] + number
                                        else:
                                            break

                                # Add digits to the right
                                for _x in range(x+1, width_count):
                                    if(_x < width_count):
                                        if(grid[y][_x].isdigit()):
                                            number = number + grid[y][_x]
                                        else:
                                            last_index = _x+1
                                            break
                                else:
                                    # Reached end of the line
                                    last_index = width_count
                                
                                # print(f"adding number {number}")
                                sum += int(number)
                                added_to_sum = True

                # Skip all the following numbers
                if(added_to_sum):
                    x = last_index
                else:
                    x += 1
            else:
                # Continue to next char
                x += 1
        # Continue to next row
        y += 1

    print(f"sum: {sum}")


if __name__ == "__main__":
    main()



import itertools

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
class Coord():
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return f"({self.y}, {self.x})"

def find_coord(char):
    global grid

    # print_grid()
    for row_index, row in enumerate(grid):
        for col_index, tile in enumerate(row):
            if(tile == char):
                return row_index, col_index
    else:
        # Couldnt find char, can assume we will so this code will never run
        return -1, -1

def number_galaxies():
    global grid, galaxy_count

    curr_galaxy = 1
    for y, row in enumerate(grid):
        for x in range(0, len(row)):
            if(grid[y][x] == '.'):
                continue

            grid[y][x] = f'{curr_galaxy}'
            curr_galaxy += 1

    galaxy_count = curr_galaxy

def print_grid():
    global grid

    for y, row in enumerate(grid):
        print(f"{y}:\t{row}")

    print()

def insert_empty_row(row_index):
    global empty_rows

    empty_rows.append(row_index)

def insert_empty_col(col_index):
    global empty_col

    empty_cols.append(col_index)

def expand_universe():
    global grid

    # Expand empty rows
    y = 0
    while(y < len(grid)):
        if(all(i == '.' for i in grid[y])):
            insert_empty_row(y)
        y += 1

    # Expand empty columms
    x = 0
    while(x < len(grid[0])):
        for y in range(0, len(grid)):
            if(grid[y][x] != '.'):
                break
        else:
            insert_empty_col(x)
        x += 1

def main():
    global grid, coord_list, galaxy_count
    # Input text
    lines = get_lines_from_file("input.txt")

    for line in lines:
        grid.append(list(line.strip()))

    # Replace #'s in grid with numbers
    number_galaxies()
    expand_universe()

    for i in range(1, galaxy_count):
        # y, x = find_coord(f'{i}')
        # coord_list.append(Coord(y, x))
        coord_list.append(find_coord(f'{i}'))

    # We want to iterate over UNIQUE combinations, avoid duplicates
    # (1, 0), (2, 4) == (2, 4), (1, 0)
    sum = 0
    for (y0, x0), (y1, x1) in itertools.combinations(coord_list, 2):
        empty_row_count = 0
        for empty_row in empty_rows:
            lower_bound = min(y0, y1)
            upper_bound = max(y0, y1)
            if(lower_bound < empty_row < upper_bound):
                empty_row_count += 1
        row_count = abs(y0 - y1) - empty_row_count + (empty_row_count * empty_size)

        empty_col_count = 0
        for empty_col in empty_cols:
            lower_bound = min(x0, x1)
            upper_bound = max(x0, x1)
            if(lower_bound < empty_col < upper_bound):
                empty_col_count += 1
        col_count = abs(x0 - x1) - empty_col_count + (empty_col_count * empty_size)

        sum += row_count + col_count
        # print(f"({y0}, {x0}) -> ({y1}, {x1}) crosses {empty_row_count} empty rows!")
        # print(f"{grid[y0][x0]} -> {grid[y1][x1]} takes {row_count + col_count} steps")

    print(f"sum: {sum}")

if __name__ == "__main__":
    grid = []
    coord_list = []
    galaxy_count = 0
    empty_rows = []
    empty_cols = []
    empty_size = 1000000
    main()

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
    global grid

    grid.insert(row_index, ['.'] * len(grid[0]))
    # print(f"inserted new row at {row_index}")

def insert_empty_col(col_index):
    global grid

    for row in grid:
        row.insert(col_index, '.')


def expand_universe():
    global grid

    # Expand empty rows
    y = 0
    while(y < len(grid)):
        if(all(i == '.' for i in grid[y])):
            insert_empty_row(y+1)
            y += 2
        else:
            y += 1

    # Expand empty columms
    x = 0
    while(x < len(grid[0])):
        for y in range(0, len(grid)):
            if(grid[y][x] != '.'):
                break
        else:
            insert_empty_col(x+1)
            x += 2
            continue
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

    print(f"galaxy_count: {galaxy_count}")

    # We want to iterate over UNIQUE combinations, avoid duplicates
    # (1, 0), (2, 4) == (2, 4), (1, 0)
    sum = 0
    for (y0, x0), (y1, x1) in itertools.combinations(coord_list, 2):
        sum += abs(y0 - y1) + abs(x0 - x1)

    print(f"sum: {sum}")

if __name__ == "__main__":
    grid = []
    coord_list = []
    galaxy_count = 0
    main()

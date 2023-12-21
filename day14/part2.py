import time

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def process_lines(lines):
    global grid

    for line in lines:
        grid.append(list(line.strip()))

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if(grid[y][x] == 'O'):
                rock_list.append((y, x))

    # print(f"process_lines():")
    # for y, x in rock_list:
    #     print(f"({y}, {x})")


def tilt_north():
    global grid, rock_list

    for i, (y, x) in enumerate(rock_list):

        grid[y][x] = '.'
        _y = y
        while(_y >= 0 and grid[_y][x] == '.'):
            _y -= 1
        _y += 1
        grid[_y][x] = 'O'

        rock_list[i] = (_y, x)

    rock_list = sorted(rock_list)

def tilt_east():
    global grid, rock_list

    rock_list.reverse()

    for i, (y, x) in enumerate(rock_list):

        grid[y][x] = '.'
        _x = x
        while(_x < len(grid[0]) and grid[y][_x] == '.'):
            _x += 1
        _x -= 1
        grid[y][_x] = 'O'

        rock_list[i] = (y, _x)

    rock_list = sorted(rock_list)

def tilt_south():
    global grid, rock_list

    rock_list.reverse()

    for i, (y, x) in enumerate(rock_list):

        grid[y][x] = '.'
        _y = y
        while(_y < len(grid) and grid[_y][x] == '.'):
            _y += 1
        _y -= 1
        grid[_y][x] = 'O'

        rock_list[i] = (_y, x)

    rock_list = sorted(rock_list)

def tilt_west():
    global grid, rock_list

    for i, (y, x) in enumerate(rock_list):

        grid[y][x] = '.'
        _x = x
        while(_x >= 0 and grid[y][_x] == '.'):
            _x -= 1
        _x += 1
        grid[y][_x] = 'O'

        rock_list[i] = (y, _x)

    rock_list = sorted(rock_list)

def print_grid():
    global grid

    for row in grid:
        print(row)

    print("---------------------------")

def perform_cycle():
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()

def calculate_load():
    global grid, rock_list

    sum = 0
    for (y, x) in rock_list:
        load = len(grid) - y
        sum += load

    return sum

def main():
    lines = get_lines_from_file("input.txt")

    start = time.time()
    process_lines(lines)
    
    for i in range(0, 1000):
        perform_cycle()

    # print_grid()

    print(f"sum: {calculate_load()}")

    elapsed_time = time.time() - start
    print(f"elapsed_time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    grid = []
    rock_list = []
    main()
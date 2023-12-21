import time
import copy

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

def process_lines(lines):
    global grid, rock_list

    for line in lines:
        grid.append(list(line.strip()))

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == 'O':
                rock_list.append((y, x))

def get_cycle_length():
    n_grid = copy.deepcopy(grid)
    n_rock_list = copy.deepcopy(rock_list)

    seen_rocks = {tuple(n_rock_list)}
    cycle_length = 0

    while True:
        n_grid, n_rock_list = perform_cycle(n_grid, n_rock_list)
        cycle_length += 1

        if tuple(n_rock_list) in seen_rocks:
            break

        seen_rocks.add(tuple(n_rock_list))

    print(f"cycle_length: {cycle_length}")

    return cycle_length

def compute_final_state(cycles):
    global grid, rock_list

    cycle_length = get_cycle_length()
    remaining_cycles = cycles % cycle_length

    for _ in range(remaining_cycles):
        grid, rock_list = perform_cycle(grid, rock_list)

def print_grid():
    global grid

    for row in grid:
        print(row)

    print("---------------------------")

def tilt_north(grid, rock_list):
    for i, (y, x) in enumerate(rock_list):

        grid[y][x] = '.'
        _y = y
        while(_y >= 0 and grid[_y][x] == '.'):
            _y -= 1
        _y += 1
        grid[_y][x] = 'O'

        rock_list[i] = (_y, x)

    rock_list = sorted(rock_list)

    return grid, rock_list

def tilt_east(grid, rock_list):
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

    return grid, rock_list

def tilt_south(grid, rock_list):
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

    return grid, rock_list

def tilt_west(grid, rock_list):
    for i, (y, x) in enumerate(rock_list):

        grid[y][x] = '.'
        _x = x
        while(_x >= 0 and grid[y][_x] == '.'):
            _x -= 1
        _x += 1
        grid[y][_x] = 'O'

        rock_list[i] = (y, _x)

    rock_list = sorted(rock_list)

    return grid, rock_list

def perform_cycle(grid, rock_list):
    grid, rock_list = tilt_north(grid, rock_list)
    grid, rock_list = tilt_west(grid, rock_list)
    grid, rock_list = tilt_south(grid, rock_list)
    grid, rock_list = tilt_east(grid, rock_list)

    return grid, rock_list

def calculate_load():
    global grid, rock_list

    sum = 0
    for (y, x) in rock_list:
        load = len(grid) - y
        # print(f"({y}, {x}); load: {load}")
        sum += load

    return sum

def main():
    lines = get_lines_from_file("input.txt")

    start = time.time()
    process_lines(lines)
    
    cycles = 1000
    compute_final_state(cycles)

    # print_grid()

    sum = calculate_load()
    print(f"sum: {sum}")

    elapsed_time = time.time() - start
    print(f"elapsed_time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    grid = []
    rock_list = []
    main()

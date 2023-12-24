import time
from enum import Enum
import numpy as np
import re 

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

letter_to_direction = {
    0: Direction.EAST,
    1: Direction.SOUTH,
    2: Direction.WEST,
    3: Direction.NORTH
}

def get_next_coord(y, x, dir, num_steps):
    if(dir == Direction.EAST):
        x += num_steps
    elif(dir == Direction.SOUTH):
        y += num_steps
    elif(dir == Direction.WEST):
        x -= num_steps
    elif(dir == Direction.NORTH):
        y -= num_steps

    return y, x

def shoelace(x_y):
    # Have to set dtype=object, other ints would be too small and cause overflow
    x_y = np.array(x_y, dtype=object)
    x_y = x_y.reshape(-1, 2)

    x = x_y[:, 0]
    y = x_y[:, 1]

    S1 = np.sum(x * np.roll(y, -1), dtype=object)
    S2 = np.sum(y * np.roll(x, -1), dtype=object)

    area = 0.5 * np.abs(S1 - S2)

    return area

def get_area(lines):
    orig_coords = []

    y, x = 0, 0
    for i, line in enumerate(lines):

        raw_data = re.sub(r'[()#]', "", (line.strip().split())[2:][0])
        num_steps = int(raw_data[:len(raw_data)-1], 16)
        dir = letter_to_direction[int(raw_data[len(raw_data)-1])]
            
        orig_coords.append((y, x))

        if(i == len(lines) - 1):
            orig_coords.append(orig_coords[0])
 
        y, x = get_next_coord(y, x, dir, num_steps)

    perimeter = 0
    for i in range(1, len(orig_coords)):
        py, px = orig_coords[i-1]
        y, x = orig_coords[i]

        perimeter += abs(y - py) + abs(x - px)

    area = shoelace(orig_coords)
    true_area = int(area + (perimeter / 2) + 1)
    return true_area


def main():
    start_time = time.time()

    # Input text
    lines = get_lines_from_file("input.txt")

    area = get_area(lines)
    print(f"area: {area}")

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

if __name__ == "__main__":
    main()

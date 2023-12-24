import time
from enum import Enum
import numpy as np

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
    'U': Direction.NORTH,
    'R': Direction.EAST,
    'D': Direction.SOUTH,
    'L': Direction.WEST
}


class Coord():
    def __init__(self, y, x, dir=None):
        self.y = y
        self.x = x
        self.dir = dir

    def __str__(self):
        return f"({self.y}, {self.x}), dir = {self.dir}"

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
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area

def get_area(lines):
    orig_coords = []

    y, x = 0, 0
    for i, line in enumerate(lines):

        step_data = (line.strip().split())[:2]
        dir = letter_to_direction[step_data[0]]
        num_steps = int(step_data[1])
            
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

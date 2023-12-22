from enum import Enum
import time

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

class Coord():
    def __init__(self, y, x, direction):
        self.y = y
        self.x = x
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.y == other.y and self.x == other.x and self.direction == other.direction
        return False
    
    def __hash__(self):
        return hash((self.y, self.x, self.direction))
    
def get_next_movement(direction):
    # return y, x

    if(direction == Direction.RIGHT):
        return 0, 1
    elif(direction == Direction.DOWN):
        return 1, 0
    elif(direction == Direction.LEFT):
        return 0, -1
    elif(direction == Direction.UP):
        return -1, 0
    
def get_next_direction(tile, direction):
    if(tile == '.'):
        return [direction]
    elif(tile == '/'):
        if(direction == Direction.RIGHT): 
            return [Direction.UP]
        elif(direction == Direction.DOWN):
            return [Direction.LEFT]
        elif(direction == Direction.LEFT):
            return [Direction.DOWN]
        elif(direction == Direction.UP):
            return [Direction.RIGHT]
    elif(tile == '\\'):
        if(direction == Direction.RIGHT): 
            return [Direction.DOWN]
        elif(direction == Direction.DOWN):
            return [Direction.RIGHT]
        elif(direction == Direction.LEFT):
            return [Direction.UP]
        elif(direction == Direction.UP):
            return [Direction.LEFT]
    elif(tile == '|'):
        if(direction in [Direction.RIGHT, Direction.LEFT]):
            return [Direction.UP, Direction.DOWN]
        else:
            return [direction]
    elif(tile == '-'):
        if(direction in [Direction.UP, Direction.DOWN]):
            return [Direction.RIGHT, Direction.LEFT]
        else:
            return [direction]

    
def process_lines(lines):
    global grid

    for line in lines:
        grid.append(list(line.strip()))

def get_energized_count(grid, start_y, start_x, start_direction):
    # Keep track of coords we've stepped on and the direction they were stepped on
    visited_coords = set()
    visited_coords.add(Coord(start_y, start_x, start_direction))

    # Consider if we are stepping right into a splitter
    next_directions = get_next_direction(grid[start_y][start_x], start_direction)

    # List of current beam coordinates, consider edge case of startting on splitter
    beam_coords = []
    for direction in next_directions:
        beam_coords.append(Coord(start_y, start_x, direction))

    # Keep going until we are out of beams
    while(len(beam_coords) > 0):
        # Grab a beam
        curr_beam = beam_coords.pop(0)
        # Calculate beam's next placement
        _y, _x = get_next_movement(curr_beam.direction)
        # print(f"({curr_beam.y}, {curr_beam.x}) -> ({curr_beam.y + _y}, {curr_beam.x + _x})")
        curr_beam.y += _y
        curr_beam.x += _x

        # Check if beam is in valid bounds
        if(curr_beam.y >= 0 and curr_beam.y < len(grid) and curr_beam.x >= 0 and curr_beam.x < len(grid[0])):
            # Check if beam has not already been recorded
            if(curr_beam not in visited_coords):
                # Set coord as visited
                visited_coords.add(curr_beam)

                # Check for any splitting and add next beam(s) to queue to be ran
                next_directions = get_next_direction(grid[curr_beam.y][curr_beam.x], curr_beam.direction)
                for direction in next_directions:
                    beam_coords.append(Coord(curr_beam.y , curr_beam.x, direction))

    # Possibility of some coords having more tha 1 beam running through it.
    # Filter out coords to retrieve UNIQUE coords that were stepped on regardless of direction
    unique_coords = {(coord.y, coord.x) for coord in visited_coords}

    return len(unique_coords)

def main():
    global grid

    start = time.time()

    lines = get_lines_from_file("input.txt")
    process_lines(lines)

    print(f"total: {get_energized_count(grid, 0, 0, Direction.RIGHT)}")

    elapsed_time = time.time() - start
    print(f"elapsed_time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    grid = []
    main()
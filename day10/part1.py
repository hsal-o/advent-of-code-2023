from enum import Enum

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Tile:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

    def __str__(self):
        return f"Tile({self.row}, {self.col}): {self.value}"
    
POSSIBLE_NEIGHBOR = {
    Direction.NORTH:    ['|', '7', 'F'],
    Direction.EAST:     ['-', 'J', '7'],
    Direction.SOUTH:    ['|', 'L', 'J'],
    Direction.WEST:     ['-', 'L', 'F']
}

def is_possible_neighbor(curr_pipe, neighbor_pipe, neighbor_direction):
    if(curr_pipe == '|'):
        if(neighbor_direction == Direction.NORTH):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.NORTH])
        elif(neighbor_direction == Direction.EAST):
            return False
        elif(neighbor_direction == Direction.SOUTH):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.SOUTH])
        elif(neighbor_direction == Direction.WEST):
            return False

    elif(curr_pipe == '-'):
        if(neighbor_direction == Direction.NORTH):
            return False
        elif(neighbor_direction == Direction.EAST):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.EAST])
        elif(neighbor_direction == Direction.SOUTH):
            return False
        elif(neighbor_direction == Direction.WEST):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.WEST])
        
    elif(curr_pipe == 'L'):
        if(neighbor_direction == Direction.NORTH):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.NORTH])
        elif(neighbor_direction == Direction.EAST):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.EAST])
        elif(neighbor_direction == Direction.SOUTH):
            return False
        elif(neighbor_direction == Direction.WEST):
            return False
        
    elif(curr_pipe == 'J'):
        if(neighbor_direction == Direction.NORTH):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.NORTH])
        elif(neighbor_direction == Direction.EAST):
            return False
        elif(neighbor_direction == Direction.SOUTH):
            return False
        elif(neighbor_direction == Direction.WEST):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.WEST])
        
    elif(curr_pipe == '7'):
        if(neighbor_direction == Direction.NORTH):
            return False
        elif(neighbor_direction == Direction.EAST):
            return False
        elif(neighbor_direction == Direction.SOUTH):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.SOUTH])
        elif(neighbor_direction == Direction.WEST):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.WEST])

    elif(curr_pipe == 'F'):
        if(neighbor_direction == Direction.NORTH):
            return False
        elif(neighbor_direction == Direction.EAST):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.EAST])
        elif(neighbor_direction == Direction.SOUTH):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.SOUTH])
        elif(neighbor_direction == Direction.WEST):
            return False

    elif(curr_pipe == 'S'):
        if(neighbor_direction == Direction.NORTH):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.NORTH])
        elif(neighbor_direction == Direction.EAST):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.EAST])
        elif(neighbor_direction == Direction.SOUTH):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.SOUTH])
        elif(neighbor_direction == Direction.WEST):
            return (neighbor_pipe in POSSIBLE_NEIGHBOR[Direction.WEST])


def find_location(char):
    global grid

    for row_index, row in enumerate(grid):
        for col_index, tile in enumerate(row):
            if(tile == char):
                return row_index, col_index
    else:
        # Couldnt find char, can assume we will so this code will never run
        return -1, -1

def get_neighbor(direction, curr_row, curr_col):
    global grid
    if(direction == Direction.NORTH):
        n_row = curr_row - 1
        n_col = curr_col
    elif(direction == Direction.EAST):
        n_row = curr_row
        n_col = curr_col + 1
    elif(direction == Direction.SOUTH):
        n_row = curr_row + 1
        n_col = curr_col
    elif(direction == Direction.WEST):
        n_row = curr_row
        n_col = curr_col - 1
    
    if(0 <= n_row < len(grid) and 0 <= n_col < len(grid[0])):
        return Tile(grid[n_row][n_col], n_row, n_col)
    else:
        return None

def get_pipeline_length(start_row, start_col):
    global grid, pipeline

    step_count = 0

    curr_row = start_row
    curr_col = start_col
    prev_row = -1
    prev_col = -1
    while(True):
        # print(f"grid[{curr_row}][{curr_col}]: {grid[curr_row][curr_col]}")
        step_count += 1

        for direction in Direction:
            neighbor = get_neighbor(direction, curr_row, curr_col)

            if(neighbor == None):
                continue

            if(is_possible_neighbor(grid[curr_row][curr_col], neighbor.value, direction)):
                if(prev_row == neighbor.row and prev_col == neighbor.col):
                    # Ignore previous neighbor
                    pass
                else:
                    # Move pointer to next neighbor and keep going through the pipe
                    prev_row = curr_row
                    prev_col = curr_col
                    curr_row = neighbor.row
                    curr_col = neighbor.col
                    break
        else:
            # We reach here once we loop back to start
            # print(f"Looped back around to start")
            break
                
    return step_count

def main():
    global grid 
    # Input text
    lines = get_lines_from_file("input.txt")

    grid = []

    for line in lines:
        grid.append(list(line.strip()))

    start_row, start_col = find_location('S')
    max_step = int(get_pipeline_length(start_row, start_col) / 2)
    print(f"max_step: {max_step}")



if __name__ == "__main__":
    main
    grid = []
    pipeline = set()
    start_row = -1
    start_col = -1
    main()

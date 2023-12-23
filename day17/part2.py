import time
from collections import defaultdict
import heapq

# Code adapted from Neil Thistlethwaite's solution: https://www.youtube.com/watch?v=lkMGDa1-Eo4&ab_channel=NeilThistlethwaite

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

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def adjs(curr_coord, last_dir, num_steps):
    if(num_steps < 10):
        cx, cy = curr_coord
        dx, dy = directions[last_dir]
        yield((cx + dx, cy + dy), last_dir, num_steps + 1)
    if(num_steps >= 4):
        for new_dir in ((last_dir - 1)%4, (last_dir + 1) % 4):
            cx, cy = curr_coord
            dx, dy = directions[new_dir]
            yield((cx + dx, cy + dy), new_dir, 1)

def main():
    global grid
    start_time = time.time()

    lines = get_lines_from_file("input.txt")
    process_lines(lines)
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    # Starting states, consider starting by going to right, or going to the bottom
    start_1 = ((0, 0), 1, 0)
    start_2 = ((0, 0), 1, 0)

    # Priority queue
    pq = []
    heapq.heappush(pq, (0, start_1))
    heapq.heappush(pq, (0, start_2))
    # Create dictionary with default value of key that doesnt exist to infinity
    dists = defaultdict(lambda : float("inf"))
    # We do not consider the starting block's weight
    dists[start_1] = 0

    # Dijkstra's algorithm
    while(len(pq) > 0):
        dist, (curr_coord, last_dir, num_steps) = heapq.heappop(pq)

        # If we reached the bottom right
        if(curr_coord == (num_rows - 1, num_cols - 1) and num_steps >= 4):
            print(f"dist: {dist}")
            break
        for adj in adjs(curr_coord, last_dir, num_steps):
            new_x, new_y = adj[0]
            # If new_x, new_y out of bounds, skip
            if(new_x not in range(num_rows) or new_y not in range(num_cols)):
                continue

            # Grab weight on current coord
            weight = int(grid[new_x][new_y])

            # If new combined weight is less
            if dist + weight < dists[adj]:
                dists[adj] = dist + weight
                heapq.heappush(pq, (dists[adj], adj))

    elapsed_time = time.time() - start_time
    print(f"elapsed_time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    grid = []
    main()
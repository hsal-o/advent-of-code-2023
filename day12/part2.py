import time

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
# Memoisation to prevent recalculation of repeated chunks
cache = {}


def count(cfg, nums):
    # Base cases:
    # Configuration is empty;
    # Valid IF there are not expected blocks of # left
    if(cfg == ""):
        return 1 if nums == () else 0
    
    # Expecting no more blocks;
    # Valid if no more # left in cfg
    if nums == ():
        return 0 if '#' in cfg else 1
    
    # Check if we cached this chunk previously
    key = (cfg, nums)
    if(key in cache):
        return cache[key]
    
    result = 0

    # Handling if ? is a . or #
    if(cfg[0] in ".?"):
        # Treat ? as a .
        result += count(cfg[1:], nums)

    if(cfg[0] in "#?"):
        # Treat ? as a #

        # Conditions to see if block is valid
        # 1) There are enough springs left. (nums[0] <= len(cfg))
        # 2) All springs in the following num[0] indices must be '#'. ('.' not in cfg[:nums[0]])
        # 3) Next spring after expected blocks of # MUST be '.' operation. 
        #       - 2 Cases
        #           - Current block of '#''s are at the end and have no '.' at the end. (nums[0] == len(cfg))
        #           - There are springs afterwards, so the immediate next one must be '.' operational. (cfg[nums[0]] != '#')
        
        if((nums[0] <= len(cfg)) and ('.' not in cfg[:nums[0]]) and ((nums[0] == len(cfg)) or (cfg[nums[0]] != '#'))):
            # Get rid of the first nums[0] + 1 items
            result += count(cfg[nums[0] + 1:], nums[1:])

    # Cache result for possible future use
    cache[key] = result

    return result

def main():
    start_time = time.time()

    # Input text
    lines = get_lines_from_file("input.txt")

    total = 0
    for line in lines:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(',')))

        # "Unfolding" the input
        cfg = '?'.join([cfg] * 5)
        nums *= 5

        total += count(cfg, nums)

    print(f"total: {total}")

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

if __name__ == "__main__":
    main()

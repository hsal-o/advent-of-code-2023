import math

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

class Node:
    def __init__(self, name, left_node, right_node):
        self.name = name
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self):
        return f"name: '{self.name}', left_node: '{self.left_node}', right_node: '{self.right_node}'"

def process_lines(lines):
    global node_dict, instructions

    instructions = lines[0].strip()

    line_data = lines[2:]

    for line in line_data:
        raw_node_data = line.split("=")
        node_data = raw_node_data[1].replace("(", "").replace(")", "").split(",")

        node_name = raw_node_data[0].strip()
        left_node = node_data[0].strip()
        right_node = node_data[1].strip()

        node_dict[node_name] = Node(node_name, left_node, right_node)

# First attempt, was abandoned
def brute_force():
    # Collect all starting nodes
    for key in node_dict.keys():
        if(key.endswith('A')):
            start_nodes.append(node_dict[key])
        elif(key.endswith('Z')):
            end_nodes.append(node_dict[key])

    curr_nodes = start_nodes
    step_count = 0
    i = 0
    while(True):
        instruction = instructions[i]

        if(instruction == MOVE_LEFT):
            # Move every current node to their left node
            for x in range(0, len(curr_nodes)):
                curr_nodes[x] = node_dict[curr_nodes[x].left_node]
        elif(instruction == MOVE_RIGHT):
            # Move every curret node to their right node
            for x in range(0, len(curr_nodes)):
                curr_nodes[x] = node_dict[curr_nodes[x].right_node]

        step_count += 1

        if(all(node.name.endswith('Z') for node in curr_nodes)):
            break

        i += 1
        if(i >= len(instructions)):
            i = 0

    print(f"step_count: {step_count}")

def get_step_count(start_node):
    curr_node = start_node
    step_count = 0
    i = 0
    while(True):
        # print(f"curr_node: {curr_node}, step_count: {step_count}")
        instruction = instructions[i]

        if(instruction == MOVE_LEFT):
            curr_node = node_dict[curr_node.left_node]
        elif(instruction == MOVE_RIGHT):
            curr_node = node_dict[curr_node.right_node]

        step_count += 1

        if(curr_node.name.endswith('Z')):
            break

        i += 1
        if(i >= len(instructions)):
            i = 0

    # print(f"step_count: {step_count}")
    return step_count

# Find least common multiple
def find_lcm(num_list):
    lcm = num_list[0]
    for num in num_list:
        lcm = math.lcm(lcm, num)
    return lcm

def main():
    # Input text
    lines = get_lines_from_file("input.txt")
    
    process_lines(lines)

    # Collect all starting nodes and ending nodes
    for key in node_dict.keys():
        if(key.endswith('A')):
            start_nodes.append(node_dict[key])
        elif(key.endswith('Z')):
            end_nodes.append(node_dict[key])

    # Have set to hold step counts (unique values only)
    step_counts = set()

    for start_node in start_nodes:
        step_counts.add(get_step_count(start_node))

    lcm = find_lcm(list(step_counts))

    print(f"lcm: {lcm}")

if __name__ == "__main__":
    node_dict = {}

    start_nodes = []
    end_nodes = []

    instructions = ""

    START_NODE = "AAA"
    END_NODE = "ZZZ"
    MOVE_LEFT = 'L'
    MOVE_RIGHT = 'R'
    main()

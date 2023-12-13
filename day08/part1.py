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



def main():
    # Input text
    lines = get_lines_from_file("input.txt")
    
    process_lines(lines)

    curr_node = node_dict[START_NODE]

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

        if(curr_node.name == END_NODE):
            break

        i += 1
        if(i >= len(instructions)):
            i = 0


    print(f"step_count: {step_count}")

if __name__ == "__main__":
    node_dict = {}
    instructions = ""

    START_NODE = "AAA"
    END_NODE = "ZZZ"
    MOVE_LEFT = 'L'
    MOVE_RIGHT = 'R'
    main()

from enum import Enum
import re

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
class Operation(Enum):
    EQUALS = '='
    DASH = '-'

class Step:
    def __init__(self, label, box, operation, focal_len):
        self.label = label
        self.box = box
        self.operation = operation
        self.focal_len = focal_len

    def get_command(self):
        if(self.focal_len != -1):
            return f"{self.label}{self.operation.value}{self.focal_len}"
        else:
            return f"{self.label}{self.operation.value}"

    def __str__(self):
        if(self.focal_len != -1):
            return f"label: {self.label}, box: {self.box}, operation: {self.operation}, focal_len: {self.focal_len}"
        else:
            return f"label: {self.label}, box: {self.box}, operation: {self.operation}"

class Lens:
    def __init__(self, label, focal_len):
        self.label = label
        self.focal_len = focal_len

    def __str__(self):
        return f"[{self.label} {self.focal_len}]"

class Box:
    def __init__(self, number):
        self.number = number
        self.lenses = []

    def remove_lens(self, lens_label):
        self.lenses = [lens for lens in self.lenses if lens.label != lens_label]

    def add_lens(self, lens_label, focal_len):
        # See if lens already exists
        for lens in self.lenses:
            # If lens exists under label
            if(lens.label == lens_label):
                lens.focal_len = focal_len
                break
        else:
            # Add new lens to box
            self.lenses.append(Lens(lens_label, focal_len))

    def is_empty(self):
        return len(self.lenses) == 0

    def print_lenses(self):
        string = ""
        for lens in self.lenses:
            string += str(lens) + " "
        return string

    def __str__(self):
        return f"Box {self.number}: {self.print_lenses()}"

def process_lines(lines):
    line = [line.strip() for line in lines][0]

    return line.split(',')

def hash(label):
    curr_value = 0
    for char in label:
        curr_value += ord(char)
        curr_value *= 17
        curr_value = curr_value % 256
    return curr_value

def process_steps(strings):
    global label_hashes

    steps = []

    # Extract label, operation, and focal length if it exists
    for string in strings:
        string_data = re.split('([=-])', string)

        label = string_data[0]

        if(label not in label_hashes):
            label_hashes[label] = hash(label)

        box = label_hashes[label]

        operation = Operation.EQUALS if string_data[1] == '=' else Operation.DASH
        focal_len = int(string_data[2]) if string_data[2] != '' else -1

        step = Step(label, box, operation, focal_len)
        # print(f"step: {step}")
        steps.append(step)

    return steps

def perform_steps(steps):
    global box_map

    for step in steps:
    
        if(step.operation == Operation.DASH):
            # Go to box and remove the lens with the given label IF it is present
            box_map[step.box].remove_lens(step.label)
        elif(step.operation == Operation.EQUALS):
            # Add lens to box or update pre-existing lens if it exists
            box_map[step.box].add_lens(step.label, step.focal_len)

        # print(f"After \"{step.get_command()}\"")
        # print_nonempty_boxes()
        # print()

def initialize_boxes():
    global box_map

    for i in range(0, 256):
        box_map[i] = Box(i)

def print_nonempty_boxes():
    global box_map

    for i in range(0, 256):
        box = box_map[i]

        if(not box.is_empty()):
            print(box)

def main():
    global box_map

    initialize_boxes()

    lines = get_lines_from_file("input.txt")
    strings = process_lines(lines)
    steps = process_steps(strings)
    perform_steps(steps)

    nonempty_boxes = [box_map[box] for box in box_map if not box_map[box].is_empty()]

    focusing_power = 0
    for box in nonempty_boxes:
        sum = 0
        for i, lens in enumerate(box.lenses):
            focus_power = (box.number + 1) * (i+1) * lens.focal_len
            # print(f"{lens.label}: {(box.number + 1)} * {(i+1)} * {lens.focal_len} = {focus_power}")
            sum += focus_power
        focusing_power += sum
    print(f"focusing_power: {focusing_power}")
        
if __name__ == "__main__":
    label_hashes = {}
    box_map = {}
    main()
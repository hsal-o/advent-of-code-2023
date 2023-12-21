def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def process_lines(lines):
    line = [line.strip() for line in lines][0]

    return line.split(',')

def hash(string):
    curr_value = 0
    for char in string:
        curr_value += ord(char)
        curr_value *= 17
        curr_value = curr_value % 256
    return curr_value

def process_strings(strings):
    sum = 0
    for string in strings:
        sum += hash(string)
    return sum

def main():
    lines = get_lines_from_file("input.txt")

    strings = process_lines(lines)

    print(f"sum: {process_strings(strings)}")

if __name__ == "__main__":
    main()
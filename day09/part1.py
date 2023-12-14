def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def process_line(line):
    global number_sequences

    # Extract number sequece
    number_sequence = [int(num) for num in line.split()]
    # Push to number sequences
    number_sequences.append(number_sequence)

def get_next_num(sequence):
    sub_sequence = []

    # Calculate next sequence
    for i in range(0, len(sequence) - 1):
        sub_sequence.append(sequence[i+1] - sequence[i])

    # If sub sequence is all 0, just return last number of sequence
    if(all(num == 0 for num in sub_sequence)):
        return sequence[-1]
    else:
        # Otherwise keep going deeper
        return sequence[-1] + get_next_num(sub_sequence)

def main():
    # Input text
    lines = get_lines_from_file("input.txt")

    for line in lines:
        process_line(line)

    sum = 0
    for sequence in number_sequences:
        # print(f"get_next_num({sequence}): {get_next_num(sequence)}")
        sum += get_next_num(sequence)

    print(f"sum: {sum}")
 
if __name__ == "__main__":
    number_sequences = []
    main()

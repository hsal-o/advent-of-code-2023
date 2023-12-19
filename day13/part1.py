def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def process_lines(lines):
    global list_patterns
    
    pattern = []

    for raw_line in lines:
        line = raw_line.strip()

        if(not line):
            list_patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)

    list_patterns.append(pattern)

def process_rows_cols(pattern):
    rows = pattern
    cols = []

    num_rows = len(rows)
    row_length = len(rows[0])

    for i in range(0, row_length):
        col = ""
        for j in range(0, num_rows):
            col += (rows[j])[i]
        cols.append(col)

    return rows, cols

def find_reflection_index(list):
    for i in range(0, len(list) - 1):
        left = i
        right = i + 1

        found_reflection = True
        while(left >= 0 and right < len(list)):
            if(list[left] == list[right]):
                # Both match
                left -= 1
                right += 1
            else:
                found_reflection = False
                break

        if(found_reflection):
            return i
        
    return -1

            


def process_pattern(pattern):
    rows, cols = process_rows_cols(pattern)

    row_reflection_index = find_reflection_index(rows)
    col_reflection_index = find_reflection_index(cols)

    if(row_reflection_index != -1):
        # print(f"num above row inflection: {row_reflection_index + 1}")
        return (row_reflection_index +1 ) * 100
    elif(col_reflection_index != -1):
        # print(f"num left col inflection: {col_reflection_index + 1}")
        return (col_reflection_index + 1)


def main():
    global grid, coord_list, galaxy_count
    # Input text
    lines = get_lines_from_file("input.txt")

    process_lines(lines)

    sum = 0
    for pattern in list_patterns:
        sum += process_pattern(pattern)

    print(f"sum: {sum}")

if __name__ == "__main__":
    list_patterns = []
    main()


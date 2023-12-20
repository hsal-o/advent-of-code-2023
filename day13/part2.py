import copy

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

def swap(string, index):
    orig_char = string[index]
    if(orig_char == '.'):
        new_char = '#'
    elif(orig_char == '#'):
        new_char = '.'

    return string[:index] + new_char + string[index+1:]

def find_reflection_result(list, old_reflection_result = -1, is_rows=False, is_cols=False):
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
        
        # Calculate reflection result
        if(is_rows):
            result = (i + 1 ) * 100
        elif(is_cols):
            result = (i + 1)

        # This means this is the first time we are calling this function, to find original reflection result
        if(found_reflection and old_reflection_result == -1):
            return result
        
        # This is only called once we are trying to determine smudges and new reflection results
        if(found_reflection and old_reflection_result != -1 and result != old_reflection_result):
            return result
        
    return -1

def find_new_reflection_result(list, old_reflection_result, is_rows=False, is_cols=False):
    # Brute force
    # Go character by character to find smudge
    for i in range(0, len(list)):
        for j in range(0, len(list[0])):

            # Make deepcopy to swap out the smudge
            list_copy = copy.deepcopy(list)
            list_copy[i] = swap(list_copy[i], j)
            
            # Calculate new reflection result
            new_reflection_result = find_reflection_result(list_copy, old_reflection_result=old_reflection_result, is_rows=is_rows, is_cols=is_cols)

            # Return if we found a valid result
            if(new_reflection_result != -1 and new_reflection_result != old_reflection_result):
                return new_reflection_result
    else:
        return -1


def process_pattern(pattern):
    rows, cols = process_rows_cols(pattern)

    # Find original reflection result
    row_reflection_result = find_reflection_result(rows, is_rows=True)
    col_reflection_result = find_reflection_result(cols, is_cols=True)
    old_reflection_result = max(row_reflection_result, col_reflection_result)

    # Find new reflection result considering smudge, making sure we dont re-find previous reflection
    row_reflection_result = find_new_reflection_result(rows, old_reflection_result, is_rows=True)
    col_reflection_result = find_new_reflection_result(cols, old_reflection_result, is_cols=True)

    return max(row_reflection_result, col_reflection_result)


def main():
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







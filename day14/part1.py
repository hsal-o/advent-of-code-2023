import time

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def process_lines(lines):
    global cols

    lines = [line.strip() for line in lines]

    num_rows = len(lines)
    row_length = len(lines[0])

    for i in range(0, row_length):
        col = []
        for j in range(0, num_rows):
            # print(f"(lines[{j}])[{i}]: {(lines[j])[i]}")
            col.append((lines[j])[i])
        cols.append(col)

def process_cols():
    global cols

    sum = 0
    for col in cols:

        for i in range(0, len(col)):
            if(col[i] == 'O'):
                col[i] = '.'

                j = i
                while(j >= 0 and col[j] == '.'):
                    j -= 1

                new_index = j+1
                col[new_index] = 'O'
                
                sum += len(col) - new_index

    # for col in cols:
    #     print(col)

    return sum



    

def main():
    lines = get_lines_from_file("input.txt")

    start = time.time()
    process_lines(lines)

    print(f"sum: {process_cols()}")

    elapsed_time = time.time() - start
    print(f"elapsed_time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    cols = []
    main()
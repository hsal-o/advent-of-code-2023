number_dict = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
}

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def find_substring(substring):
    for number in number_dict:
        if(number in substring):
            return number_dict[number]
    return None

def find_first_digit(line):

    for i in range(1, len(line) + 1):
        substring = line[:i]
        result = find_substring(substring)
        if(result != None):
            return result

    return None # Couldnt find digit


def find_first_digit_reversed(line):

    for i in range(len(line)-1, -1, -1):
        substring = line[i:]
        result = find_substring(substring)
        if(result != None):
            return result

    return None # Couldnt find digit

def extract_calibration_value(line):
    # Find the first and last digits in the line
    first_digit = find_first_digit(line)
    last_digit = find_first_digit_reversed(line)

    # Check if both first and last digits are found
    if first_digit != None and last_digit != None:
        # Combine the digits to form a two-digit number
        calibration_value = (first_digit * 10) + last_digit
        return calibration_value
    else:
        return None

def main():
    # Input lines
    lines = get_lines_from_file("input.txt")

    sum_of_calibrations = 0

    # Process each line and add values
    for line in lines:
        calibration_value = extract_calibration_value(line)
        if calibration_value != None:
            sum_of_calibrations += calibration_value

    # Print out sum of all values
    print(f"Sum of calibration values: {sum_of_calibrations}")

if __name__ == "__main__":
    main()

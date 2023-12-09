def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

def find_first_digit(line):
    for char in line:
        if char.isdigit():
            return int(char)
    return None # Couldnt find digit

def extract_calibration_value(line):
    # Find the first and last digits in the line
    first_digit = find_first_digit(line)
    last_digit = find_first_digit(reversed(line))

    # Check if both first and last digits are found
    if first_digit != None and last_digit != None:
        # Combine the digits to form a two-digit number
        calibration_value = (first_digit * 10) + last_digit
        return calibration_value
    else:
        return None

def main():
    # Sample lines
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

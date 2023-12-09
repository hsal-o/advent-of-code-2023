def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

def process_card(card):
    match_count = 0
    point_count = 0

    # Card comes in the form ['Card X : a b c d | e f g h']
    card_data = card.split(":") # Split card into ['Card X', 'a b c d | e f g h']

    card_tag = card_data[0].split() # Portion of the data regarding the card @
    card_number = int(card_tag[1]) # Extract card #

    number_data = card_data[1].split("|") # Portion of the data regarding the numbers

    # Extract numbers from number data
    winning_numbers = number_data[0].split()
    playing_numbers = number_data[1].split()

    for winning_number in winning_numbers:
        if(winning_number in playing_numbers):
            match_count += 1

    if(match_count > 0):
        point_count = 2 ** (match_count - 1)

    #print(f"Card {card_number} has {point_count} points")

    return point_count



def main():
    # Input text
    cards = get_lines_from_file("input.txt")

    # Process each line and add values
    point_sum = 0
    for card in cards:
        point_sum += process_card(card)

    print(f"point_sum: {point_sum}")


if __name__ == "__main__":
    main()

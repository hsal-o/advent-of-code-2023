import time

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

cards = get_lines_from_file("input.txt")
card_dict = {}
card_wins_dict = {}

def process_card(card_number):
    # Check if card number is valid
    if(card_number >= len(cards)):
        return

    # For every winning number, process next number
    for x in range(1, card_wins_dict[card_number]+1):
        # If card number is valid / in table
        if(x in card_dict):
            next_number = card_number+x
            card_dict[next_number] += 1
            process_card(next_number) 

def preprocess_card(card):
    match_count = 0

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

    card_wins_dict[card_number] = match_count
    

def main():
    start_time = time.time()

    for key in range(1, len(cards) + 1):
        card_dict[key] = 1
        card_wins_dict[key] = 0

    for card in cards:
        preprocess_card(card)

    # Process each line and add values
    for x in range(1, len(cards)+1):
        process_card(x)

    card_count = sum(card_dict.values())

    print(card_count)

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")


if __name__ == "__main__":
    main()

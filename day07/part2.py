from enum import Enum
from collections import Counter
from functools import cmp_to_key
import time

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
label_strengths = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}

class Hand_Type(Enum):
    FIVE_OF_A_KIND =    7
    FOUR_OF_A_KIND =    6
    FULL_HOUSE =        5
    THREE_OF_A_KIND =   4
    TWO_PAIR =          3
    ONE_PAIR =          2
    HIGH_CARD =         1

class Hand:
    def __init__(self, hand, bid, type):
        self.hand = hand
        self.bid = bid
        self.type = type

    def __str__(self):
        return f"hand: {self.hand}, bid: {self.bid}, type: {self.type}"

def calculate_highest_type(hand):
    joker = 'J'
    
    if(joker in hand):
        orig_type = calculate_type(hand)
        new_type = orig_type

        # print(f"orig_type: {orig_type}")

        joker_count = hand.count(joker)

        if(orig_type == Hand_Type.FIVE_OF_A_KIND):
            pass # Do nothing
        elif(orig_type == Hand_Type.FOUR_OF_A_KIND):
            # 4-J's -> FIVE_OF_A_KIND is achievable
            # 1-J's -> FIVE_OF_A_KIND is achievable
            new_type = Hand_Type.FIVE_OF_A_KIND
            pass
        elif(orig_type == Hand_Type.FULL_HOUSE):
            # 3-J's -> FIVE_OF_A_KIND is achievable
            # 2-J's -> FIVE_OF_A_KIND is achievable
            new_type = Hand_Type.FIVE_OF_A_KIND
            pass
        elif(orig_type == Hand_Type.THREE_OF_A_KIND):
            # 3-J's -> FOUR_OF_A_KIND is achievable
            # 1-J's -> FOUR_OF_A_KIND is achievable
            new_type = Hand_Type.FOUR_OF_A_KIND
            pass
        elif(orig_type == Hand_Type.TWO_PAIR):
            # 2-J's -> FOUR_OF_A_KIND is achievable
            # 1-J's -> FULL_HOUSE is achievable

            if(joker_count == 2):
                new_type = Hand_Type.FOUR_OF_A_KIND
            elif(joker_count == 1):
                new_type = Hand_Type.FULL_HOUSE

            pass
        elif(orig_type == Hand_Type.ONE_PAIR):
            # 2-J's -> THREE_OF_A_KIND is achievable 
            # 1-J's -> THREE_OF_A_KIND is achievable, 
            #          WO_PAIR is achievable

            new_type = Hand_Type.THREE_OF_A_KIND
            pass
        elif(orig_type == Hand_Type.HIGH_CARD):
            # 1-J's -> ONE_PAIR is achievable
            new_type = Hand_Type.ONE_PAIR
            pass
        
        if(new_type.value > orig_type.value):
            return new_type
        else:
            return orig_type

    else :
        return calculate_type(hand)


def calculate_type(hand):
    counter = Counter(hand)

    if(5 in counter.values()):
        return Hand_Type.FIVE_OF_A_KIND # All of a kind
    elif(4 in counter.values() and 1 in counter.values()):
        return Hand_Type.FOUR_OF_A_KIND # 4 of a kind
    elif(3 in counter.values() and 2 in counter.values()):
        return Hand_Type.FULL_HOUSE # 3 of a kind + 2 of a kind
    elif(3 in counter.values() and 1 in counter.values()):
        return Hand_Type.THREE_OF_A_KIND # 3 of a kind + 2 distinct
    elif(sum(count == 2 for count in counter.values()) == 2):
        return Hand_Type.TWO_PAIR # Exactly 2 pairs
    elif(sum(count == 2 for count in counter.values()) == 1):
        return Hand_Type.ONE_PAIR # Exactly 1 pair
    else:
        return Hand_Type.HIGH_CARD

def process_line(line):
    global hands_list

    line_data = line.split()

    hand = line_data[0]
    bid = int(line_data[1])
    type = calculate_highest_type(hand)

    # print(f"hand: {hand}, bid: {bid}, type: {type}")
    hands_list.append(Hand(hand, bid, type))

# Custom compare function for sort function
def compare_hands(hand_1, hand_2):
    if(hand_1.type.value > hand_2.type.value):
        return 1
    elif(hand_1.type.value < hand_2.type.value):
        return -1
    else:
        for i in range(0, len(hand_1.hand)):
            card_1 = hand_1.hand[i]
            card_2 = hand_2.hand[i]

            if(label_strengths[card_1] > label_strengths[card_2]):
                return 1 # Hand 1 is greater
            elif(label_strengths[card_2] > label_strengths[card_1]):
                return -1 # Hand 2 is greater
        return 0 # Both hands are equal

def main():
    start_time = time.time()

    # Input text
    lines = get_lines_from_file("input.txt")

    for line in lines:
        process_line(line)

    hands_list.sort(key=cmp_to_key(compare_hands))

    total_winnings = 0
    for i in range(0, len(hands_list)):
        rank = i + 1
        total_winnings += rank * hands_list[i].bid
        # print(f"hand: {hands_list[i]}, rank: {rank}")

    print(f"total_winnings: {total_winnings}")

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

if __name__ == "__main__":
    hands_list = []
    main()

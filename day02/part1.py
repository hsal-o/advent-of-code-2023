def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

CONSTRAINTS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def process_game(game):
    # Game comes in the form "[Game Tag] : [Game Rounds]""
    game_data = game.split(":") # Split the game into game tag and rounds
    game_tag = game_data[0].split() # Game tag is [ "Game", "<Number>""]
    game_number = int(game_tag[1]) # Grab Number from Game tag

    rounds = game_data[1].split(";")

    for round in rounds:
        round_data = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        #hand full of items the elf shows you
        items = round.split(",")

        for collection in items:
            collection_data = collection.strip().split()
            cube_color = collection_data[1]
            cube_count = int(collection_data[0])

            round_data[cube_color] = cube_count

        for cube_color in round_data:
            if(round_data[cube_color] > CONSTRAINTS[cube_color]):
                return 0
            
    return game_number


def main():
    games = get_lines_from_file("input.txt")

    id_sum = 0
    for game in games:
        id_sum += process_game(game)

    print(f"id_sum: {id_sum}")
            

if __name__ == "__main__":
    main()
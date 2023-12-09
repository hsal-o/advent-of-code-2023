def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None

def process_game(game):
    # Game comes in the form "[Game Tag] : [Game Rounds]""
    game_data = game.split(":") # Split the game into game tag and rounds

    cube_data = { }

    rounds = game_data[1].split(";")
    for round in rounds:
        #hand full of items the elf shows you
        items = round.split(",")

        for collection in items:
            collection_data = collection.strip().split()
            cube_color = collection_data[1]
            cube_count = int(collection_data[0])

            if(cube_count > cube_data.get(cube_color, 0)):
                cube_data[cube_color] = cube_count

    power = 0
    for cube_color in cube_data:
        if(power == 0):
            power = cube_data[cube_color]
            continue

        power *= cube_data[cube_color]

    return power


def main():
    games = get_lines_from_file("input.txt")

    power_sum = 0
    for game in games:
            power_sum += process_game(game)

    print(f"power_sum: {power_sum}")
            

if __name__ == "__main__":
    main()
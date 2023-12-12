def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def __str__(self):
        return f"Distance: {self.distance}, Record: {self.record}"
    
def process_lines(lines):
    global race_list
    time_data = lines[0].split(":")[1].strip().split()
    distance_data = lines[1].split(":")[1].strip().split()

    time_data = [int(x) for x in time_data]
    distance_data = [int(x) for x in distance_data]

    for i in range(0, len(time_data)):
        race_list.append(Race(time_data[i], distance_data[i]))



def main():
    # Input text
    lines = get_lines_from_file("input.txt")

    process_lines(lines)

    result = 0
    for race in race_list:
        counter = 0
        for i in range(1, race.time):
            if(i * (race.time - i) > race.distance):
                counter += 1

        # print(f"There are {counter} different ways to win")

        if(counter != 0):
            if(result != 0): 
                result *= counter
            else:
                result = counter

    print(f"result: {result}")




if __name__ == "__main__":
    race_list = []
    main()

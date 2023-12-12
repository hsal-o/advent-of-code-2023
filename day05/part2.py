# Not working

from enum import Enum
import time

def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
class SeedRange:
    def __init__(self, start, range):
        self.start = start
        self.end = start + range

    def __str__(self):
        return f"start: {self.start}; end: {self.end}"

class Line:
    def __init__(self, dest, src, range):
        self.dest_start = dest
        self.dest_end = dest + range
        self.src_start = src
        self.src_end = src + range

    def __str__(self):
        return f"dest_start: {self.dest_start}; dest_end: {self.dest_end}; src_start: {self.src_start}; src_end: {self.src_end}"

class Mode(Enum):
    SEED_TO_SOIL = 0
    SOIL_TO_FERT = 1
    FERT_TO_WATER = 2
    WATER_TO_LIGHT = 3
    LIGHT_TO_TEMP = 4
    TEMP_TO_HUMID = 5
    HUMID_TO_LOC = 6

def process_seeds(line):
    global seeds
    # Line is in form "seeds: x x x x x"
    line_data = line.split(":") # Split line into ["seeds", "x x x x x"]

    seeds_data = line_data[1].split() # Extract seeds as strings ["x", "x", "x", "x", "x"]
    seeds_data = [int(num) for num in seeds_data] # Convert all seeds into ints


    for x in range(0, len(seeds_data), 2):
        seeds.append(SeedRange(seeds_data[x], seeds_data[x+1]))

    # for seed_pair in seeds:
    #     print(seed_pair)

def extract_line_data(line):
    line_data = line.split()
    return Line(int(line_data[0]), int(line_data[1]), int(line_data[2]))

def process_x_to_y(map, line):
    global seeds, seed_to_soil_map, soil_to_fert_map, fert_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid_map, humid_to_loc_map
    map.append(extract_line_data(line))

def process_lines(lines):
    mode = None

    for line in lines:
        if("seeds" in line):
            process_seeds(line)
        elif("seed-to-soil" in line):
            mode = Mode.SEED_TO_SOIL
        elif("soil-to-fertilizer" in line):
            mode = Mode.SOIL_TO_FERT
        elif("fertilizer-to-water" in line):
            mode = Mode.FERT_TO_WATER
        elif("water-to-light" in line):
            mode = Mode.WATER_TO_LIGHT
        elif("light-to-temperature" in line):
            mode = Mode.LIGHT_TO_TEMP
        elif("temperature-to-humidity" in line):
            mode = Mode.TEMP_TO_HUMID
        elif("humidity-to-location" in line):
            mode = Mode.HUMID_TO_LOC
        elif(not line.strip()): # If line is empty
            continue
        else:
            if(mode == Mode.SEED_TO_SOIL):
                process_x_to_y(seed_to_soil_map, line)
            elif(mode == Mode.SOIL_TO_FERT):
                process_x_to_y(soil_to_fert_map, line)
            elif(mode == Mode.FERT_TO_WATER):
                process_x_to_y(fert_to_water_map, line)
            elif(mode == Mode.WATER_TO_LIGHT):
                process_x_to_y(water_to_light_map, line)
            elif(mode == Mode.LIGHT_TO_TEMP):
                process_x_to_y(light_to_temp_map, line)
            elif(mode == Mode.TEMP_TO_HUMID):
                process_x_to_y(temp_to_humid_map, line)
            elif(mode == Mode.HUMID_TO_LOC):
                process_x_to_y(humid_to_loc_map, line)

def print_debug():
    global seeds, seed_to_soil_map, soil_to_fert_map, fert_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid_map, humid_to_loc_map
    
    print(f"seeds")
    print(seeds)
    print(f"seed_to_soil_map")
    for line in seed_to_soil_map:
        print(line)
    print(f"soil_to_fert_map")
    for line in soil_to_fert_map:
        print(line)
    print(f"fert_to_water_map")
    for line in fert_to_water_map:
        print(line)
    print(f"water_to_light_map")
    for line in water_to_light_map:
        print(line)
    print(f"light_to_temp_map")
    for line in light_to_temp_map:
        print(line)
    print(f"temp_to_humid_map")
    for line in temp_to_humid_map:
        print(line)
    print(f"humid_to_loc_map")
    for line in humid_to_loc_map:
        print(line)

def translate_value(map, value):
    for line in map:
        if(value >= line.src_start and value <= line.src_end):
            # print(f"// {line.src_start} <= {value}  <= {line.src_end}")
            trans = value - line.src_start  
            return line.dest_start + trans
    return value

def main():
    start_time = time.time()

    # Sample lines
    lines = get_lines_from_file("input.txt")

    process_lines(lines)
    #print_debug()

    for seed_range in seeds:
        for x in range(seed_range.start, seed_range.end):
            #print(f"Seed: {x}")
            _x = translate_value(seed_to_soil_map, x)
            # print(f" Soil: {x}")
            _x = translate_value(soil_to_fert_map, _x)
            # print(f"  Fertlizer: {x}")
            _x = translate_value(fert_to_water_map, _x)
            # print(f"   Water: {x}")
            _x = translate_value(water_to_light_map, _x)
            # print(f"    Light: {x}")
            _x = translate_value(light_to_temp_map, _x)
            # print(f"     Temp: {x}")
            _x = translate_value(temp_to_humid_map, _x)
            # print(f"      Humidity: {x}")
            _x = translate_value(humid_to_loc_map, _x)
            # print(f"       Location: {x}")
            # print(f"Seed {x} -> Fertilizer {_x}")
            locations.append(_x)


    # for x in seeds:
    #     # print(f"Seed: {x}")
    #     _x = translate_value(seed_to_soil_map, x)
    #     # print(f" Soil: {x}")
    #     _x = translate_value(soil_to_fert_map, _x)
    #     # print(f"  Fertlizer: {x}")
    #     _x = translate_value(fert_to_water_map, _x)
    #     # print(f"   Water: {x}")
    #     _x = translate_value(water_to_light_map, _x)
    #     # print(f"    Light: {x}")
    #     _x = translate_value(light_to_temp_map, _x)
    #     # print(f"     Temp: {x}")
    #     _x = translate_value(temp_to_humid_map, _x)
    #     # print(f"      Humidity: {x}")
    #     _x = translate_value(humid_to_loc_map, _x)
    #     # print(f"       Location: {x}")
    #     # print(f"Seed {x} -> Fertilizer {_x}")
    #     locations.append(_x)

    print(f"Lowest Location #: {min(locations)}")

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

if __name__ == "__main__":
    seeds = []
    seed_to_soil_map = []
    soil_to_fert_map = []
    fert_to_water_map = []
    water_to_light_map = []
    light_to_temp_map = []
    temp_to_humid_map = []
    humid_to_loc_map = []
    locations = []
    main()

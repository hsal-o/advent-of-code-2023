import time

def get_min_seed(seeds, blocks):
    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            dst, src, rng = map(int, line.split())
            ranges.append(list((dst, src, rng)))

        nseeds = []
        for seed in seeds:
            for dst, src, rng in ranges:
                if seed in range(src, src + rng):
                    nseeds.append(seed - src + dst)
                    break
            else:
                nseeds.append(seed)

        seeds = nseeds

    return min(seeds)

def main():
    start_time = time.time()

    seeds, *blocks = open("input.txt").read().split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))

    min_seed = get_min_seed(seeds, blocks)
    print(f"min_seed: {min_seed}")

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

if __name__ == "__main__":
    main()



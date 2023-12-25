import time

def get_min_seed(seeds, blocks):
    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            dst, src, rng = map(int, line.split())
            ranges.append(list((dst, src, rng)))

        nseeds = []
        while(len(seeds) > 0):
            start, end = seeds.pop()
            for dst, src, rng in ranges:
                # Check if overlap exists
                overlap_start = max(start, src)
                overlap_end = min(end, src + rng)
                if(overlap_start < overlap_end):
                    nseeds.append((overlap_start - src + dst, overlap_end - src + dst))
                    if(overlap_start > start):
                        seeds.append((start, overlap_start))
                    if(end > overlap_end):
                        seeds.append((overlap_end, end))
                    break
            else:
                nseeds.append((start, end))        

        seeds = nseeds

    return min(seeds)[0]

def main():
    start_time = time.time()

    inputs, *blocks = open("input.txt").read().split("\n\n")
    inputs = list(map(int, inputs.split(":")[1].split()))

    # Seeds will now contain ranges of seeds
    seeds = []
    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i+1]))

    min_seed = get_min_seed(seeds, blocks)
    print(f"min_seed: {min_seed}")

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

if __name__ == "__main__":
    main()



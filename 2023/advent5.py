mappings = []
for line in open("advent5.txt"):
    line = line.strip()

    if not line:
        continue

    if "seeds" in line:
        _, seeds = line.split(":")
        seeds = list(map(int, seeds.strip().split()))
        continue

    if "map" in line:
        mappings.append([])
        continue

    mappings[-1].append(tuple(map(int, line.split())))


def get_dest(seed, mapp):
    for dest, source, length in mapp:
        if source <= seed < source + length:
            return dest + (seed - source)
    return seed


locations = []
for seed in seeds:
    temp_seed = seed

    for mapp in mappings:
        temp_seed = get_dest(temp_seed, mapp)

    locations.append(temp_seed)
print(min(locations))

# part 2


def get_dest_ranges(seed_start, seed_length, mapp):
    ranges = []

    for dest_start, source_start, length in mapp:
        # both in range
        if (source_start <= seed_start < source_start + length) and (
            source_start < seed_start + seed_length <= source_start + length
        ):
            ranges.append((dest_start + (seed_start - source_start), seed_length))
            return ranges

        # begin in range but end not
        if (source_start <= seed_start < source_start + length) and not (
            source_start < seed_start + seed_length <= source_start + length
        ):
            ranges.append(
                (
                    dest_start + (seed_start - source_start),
                    source_start + length - seed_start,
                )
            )
            ranges.extend(
                get_dest_ranges(
                    source_start + length,
                    (seed_start + seed_length) - (source_start + length),
                    mapp,
                )
            )
            return ranges

        # end in range but begin not
        if not (source_start <= seed_start < source_start + length) and (
            source_start < seed_start + seed_length <= source_start + length
        ):
            ranges.append((dest_start, seed_start + seed_length - source_start))

            ranges.extend(get_dest_ranges(seed_start, source_start - seed_start, mapp))
            return ranges

    return [(seed_start, seed_length)]


seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]


for i, mapp in enumerate(mappings):
    temp_seeds = []

    for seed_range in seeds:
        temp_seeds.extend(get_dest_ranges(*seed_range, mapp))
        pass

    seeds = temp_seeds

print(min([l for (l, ll) in seeds]))

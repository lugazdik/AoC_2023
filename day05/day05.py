def read_input(
    input_path: str,
) -> tuple[list[int], list[list[tuple[int, int, int]]]]:
    with open(input_path, "r") as f:
        split_by_empty_line = f.read().split("\n\n")
        seeds = list(map(int, split_by_empty_line[0].split(":")[1].strip().split()))
        converters = []
        for category in split_by_empty_line[1:]:
            converter = []
            for interval in category.split("\n")[1:]:
                converter.append(tuple(map(int, interval.split())))
            converters.append(converter)
        return seeds, converters


def find_seed_destination(
    seed: int,
    converters: list[tuple[int, int, int]],
) -> int:
    for interval in converters:
        if interval[1] <= seed < interval[1] + interval[2]:
            return interval[0] + seed - interval[1]
    return seed


def part1(
    seeds: list[int],
    converters: list[list[tuple[int, int, int]]],
) -> int:
    for converter in converters:
        new_seeds = []
        for seed in seeds:
            new_seeds.append(find_seed_destination(seed, converter))
        seeds = new_seeds
    return min(seeds)


def find_interval_overlap(a: int, b: int, x: int, y: int):
    if a < x and y < b:
        # a-x-y-b
        return [(x, y)], [(a, x - 1), (y + 1, b)]
    elif a < x <= b:
        # a-x-b-y
        return [(x, b)], [(a, x - 1)]
    elif a <= y < b:
        # x-a-y-b
        return [(a, y)], [(y + 1, b)]
    elif x <= a and b <= y:
        # x-a-b-y
        return [(a, b)], []
    else:
        # a-b-x-y or x-y-a-b
        return [], [(a, b)]


def part2(seeds: list[int], converters: list[list[tuple[int, int, int]]]):
    seed_pairs = [
        (seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)
    ]
    converters = [
        [[dest - start, start, start + size - 1] for dest, start, size in converter]
        for converter in converters
    ]
    for converter in converters:
        new_ranges = []
        for seed_pair in seed_pairs:
            unprocessed = [seed_pair]
            for offset, converter_start, converter_end in converter:
                new_unprocessed = []
                for seed_start, seed_end in unprocessed:
                    found_interval, extra = find_interval_overlap(
                        seed_start, seed_end, converter_start, converter_end
                    )
                    new_unprocessed += extra
                    new_ranges += [(a + offset, b + offset) for a, b in found_interval]
                unprocessed = new_unprocessed
            new_ranges += unprocessed
        seed_pairs = new_ranges

    return min(start for start, _ in seed_pairs)


input_seeds, input_converters = read_input("day05.txt")
print(part1(input_seeds, input_converters))
print(part2(input_seeds, input_converters))

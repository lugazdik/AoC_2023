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


def find_seed_destinqation(
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
            new_seeds.append(find_seed_destinqation(seed, converter))
        seeds = new_seeds
    return min(seeds)


input_seeds, input_converters = read_input("day05.txt")
print(part1(input_seeds, input_converters))

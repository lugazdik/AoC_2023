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


def does_fully_contain(a, b, x, y):
    return (a <= x <= b and a <= y <= b) or (x <= a <= y and x <= b <= y)


def does_overlap(a, b, x, y):
    return a <= x <= b or a <= y <= b or x <= a <= y or x <= b <= y


def find_seed_interval_destination(
    seed_interval: tuple[int, int], converters: list[tuple[int, int, int]]
) -> list[tuple[int, int]]:
    result_intervals = []
    for interval in converters:
        if interval[1] <= seed_interval[0]:
            if seed_interval[0] + seed_interval[1] <= interval[1] + interval[2]:
                return result_intervals + [
                    (interval[0] + seed_interval[0] - interval[1], seed_interval[1])
                ]
            if seed_interval[0] < interval[1] + interval[2]:
                covered_start = interval[0] + seed_interval[0] - interval[1]
                covered_end = interval[2] - (seed_interval[0] - interval[1])
                # print(
                #     f"partial {seed_interval}, {interval} = {(covered_start, covered_end)}, continue with {(covered_start + covered_end, seed_interval[1] - covered_end)}"
                # )
                result_intervals.append((covered_start, covered_end))
                seed_interval = (
                    covered_start + covered_end,
                    seed_interval[1] - covered_end,
                )
            else:
                pass
                # print(
                #     f"no overlap converter bigger {seed_interval}, {interval} = {seed_interval}"
                # )
        else:
            if seed_interval[0] + seed_interval[1] > interval[1]:
                not_covered_start = seed_interval[0]
                not_covered_end = interval[1] - seed_interval[0]
                covered_start = interval[0]
                covered_end = seed_interval[1] - not_covered_end
                # print(
                #     f"SECOND partial covered  {seed_interval}, {interval} = {(covered_start, covered_end)}, continue with {(not_covered_start, not_covered_end)}"
                # )
                result_intervals.append((covered_start, covered_end))
                seed_interval = (not_covered_start, not_covered_end)
            elif (
                seed_interval[0] <= interval[1]
                and seed_interval[0] + seed_interval[1] > interval[1] + interval[2]
            ):
                print(f"interval fully covered by seed {seed_interval}, {interval}")
            else:
                pass
                # print(
                #     f"NOT IMPLEMENTED seed start smaller than converter {seed_interval}, {interval}, continue"
                # )
    if seed_interval:
        result_intervals.append(seed_interval)
    return result_intervals


def part2(
    seeds: list[int],
    converters: list[list[tuple[int, int, int]]],
) -> int:
    seed_pairs = []
    for index in range(0, len(seeds), 2):
        seed_pairs.append((seeds[index], seeds[index + 1]))
    for converter in converters:
        new_seed_pairs = []
        for seed_pair in seed_pairs:
            new_seed_pairs += find_seed_interval_destination(seed_pair, converter)
        seed_pairs = new_seed_pairs
    return min(seed_pairs, key=lambda x: x[0])[0]


input_seeds, input_converters = read_input("day05.txt")
# print(part1(input_seeds, input_converters))
print(f"result {part2(input_seeds, input_converters)}")

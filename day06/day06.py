import math


def compute_minimum_hold_time(time: int, distance: int) -> int:
    # time = hold_time + run_time
    # distance = hold_time * run_time
    for hold_time in range(time // 2):
        run_time = time - hold_time
        if hold_time * run_time > distance:
            return hold_time


def part1(input_path: str) -> int:
    with open(input_path, "r") as f:
        time, distance = (
            list(map(int, line.strip().split(": ")[1].split()))
            for line in f.readlines()
        )
    winning_ways = []
    for time, distance in list(zip(time, distance)):
        minimum_hold_time = compute_minimum_hold_time(time, distance)
        maximum_hold_time = time - minimum_hold_time
        winning_ways.append(maximum_hold_time - minimum_hold_time + 1)
    return math.prod(winning_ways)


def part2(input_path: str) -> int:
    with open(input_path, "r") as f:
        time, distance = (
            int("".join(line.strip().split(": ")[1].split())) for line in f.readlines()
        )
    minimum_hold_time = compute_minimum_hold_time(time, distance)
    maximum_hold_time = time - minimum_hold_time
    return maximum_hold_time - minimum_hold_time + 1


path = "day06.txt"
print(part1(path))
print(part2(path))

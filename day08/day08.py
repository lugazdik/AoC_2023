from math import lcm
from itertools import cycle


def read_input(input_path: str) -> dict[str, list[str] | dict[str, str]]:
    with open(input_path, "r") as f:
        split_file = f.read().split("\n\n")
        moves = [*split_file[0]]
        conversions = {}
        for line in split_file[1].split("\n"):
            split_line = line.split(" = ")
            left_right_split = split_line[1].split(", ")
            conversions[split_line[0]] = {
                "left": left_right_split[0].replace("(", ""),
                "right": left_right_split[1].replace(")", ""),
            }
        return {"moves": moves, "conversions": conversions}


def find_end_state(
    parsed_input: dict[str, list[str] | dict[str, str]],
    start_state: str,
    end_states: set[str],
) -> int:
    steps = 0
    current_state = start_state
    for move in cycle(parsed_input["moves"]):
        if move == "L":
            current_state = parsed_input["conversions"][current_state]["left"]
        elif move == "R":
            current_state = parsed_input["conversions"][current_state]["right"]
        steps += 1
        if current_state in end_states:
            return steps


def part1(parsed_input: dict[str, list[str] | dict[str, str]]) -> int:
    return find_end_state(parsed_input, "AAA", ["ZZZ"])


def part2(parsed_input: dict[str, list[str] | dict[str, str]]) -> int:
    current_states = [
        state for state in parsed_input["conversions"].keys() if state.endswith("A")
    ]
    end_states = {
        state for state in parsed_input["conversions"].keys() if state.endswith("Z")
    }
    end_steps = [
        find_end_state(parsed_input, start, end_states) for start in current_states
    ]
    return lcm(*end_steps)


prepared_file = read_input("day08.txt")
print(part1(prepared_file))
print(part2(prepared_file))

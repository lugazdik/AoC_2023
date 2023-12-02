import math


def read_input(input_path: str):
    with open(input_path, "r") as f:
        parsed_input = {}
        for line in f.readlines():
            split_line = line.strip().split(":")
            game_id = int(split_line[0].split(" ")[1])
            parsed_input[game_id] = [
                {
                    item.split(" ")[1]: int(item.split(" ")[0])
                    for item in draw.split(", ")
                }
                for draw in split_line[1].strip().split("; ")
            ]
        return parsed_input


def part1(
    parsed_input: dict[int, list[dict[str, int]]],
    max_cubes: dict[str, int],
) -> int:
    possible_game_ids = []
    for game_id, draws in parsed_input.items():
        possible = True
        for draw in draws:
            for color, amount in draw.items():
                if amount > max_cubes[color]:
                    possible = False
                    break
        if possible:
            possible_game_ids.append(game_id)
    return sum(possible_game_ids)


def part2(parsed_input: dict[int, list[dict[str, int]]]) -> int:
    result = 0
    for _, draws in parsed_input.items():
        cube_count = {"blue": 0, "green": 0, "red": 0}
        for draw in draws:
            for color, amount in draw.items():
                if cube_count[color] < amount:
                    cube_count[color] = amount
        result += math.prod(cube_count.values())
    return result


maximum_number_of_cubes = {"blue": 14, "green": 13, "red": 12}
prepared_file = read_input("day02.txt")
print(part1(prepared_file, maximum_number_of_cubes))
print(part2(prepared_file))

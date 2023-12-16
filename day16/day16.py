def read_input(input_path: str) -> list[list[str]]:
    with open(input_path, "r") as f:
        return [[*line.strip()] for line in f.readlines()]


def find_energized_tiles(
    parsed_input: list[list[str]], starting_position: tuple[int, int, str]
) -> int:
    max_height = len(parsed_input)
    max_width = len(parsed_input[0])
    to_check = [starting_position]
    visited = set()
    while to_check:
        current = to_check.pop()
        if current in visited:
            continue
        visited.add(current)
        x, y, direction = current
        if direction == "R":
            if y + 1 < max_width:
                if parsed_input[x][y + 1] == "|":
                    to_check.extend([(x, y + 1, "U"), (x, y + 1, "D")])
                elif parsed_input[x][y + 1] == "/":
                    to_check.append((x, y + 1, "U"))
                elif parsed_input[x][y + 1] == "\\":
                    to_check.append((x, y + 1, "D"))
                else:
                    to_check.append((x, y + 1, "R"))
        elif direction == "D":
            if x + 1 < max_height:
                if parsed_input[x + 1][y] == "-":
                    to_check.extend([(x + 1, y, "R"), (x + 1, y, "L")])
                elif parsed_input[x + 1][y] == "/":
                    to_check.append((x + 1, y, "L"))
                elif parsed_input[x + 1][y] == "\\":
                    to_check.append((x + 1, y, "R"))
                else:
                    to_check.append((x + 1, y, "D"))
        elif direction == "L":
            if y - 1 >= 0:
                if parsed_input[x][y - 1] == "|":
                    to_check.extend([(x, y - 1, "U"), (x, y - 1, "D")])
                elif parsed_input[x][y - 1] == "/":
                    to_check.append((x, y - 1, "D"))
                elif parsed_input[x][y - 1] == "\\":
                    to_check.append((x, y - 1, "U"))
                else:
                    to_check.append((x, y - 1, "L"))
        elif direction == "U":
            if x - 1 >= 0:
                if parsed_input[x - 1][y] == "-":
                    to_check.extend([(x - 1, y, "R"), (x - 1, y, "L")])
                elif parsed_input[x - 1][y] == "/":
                    to_check.append((x - 1, y, "R"))
                elif parsed_input[x - 1][y] == "\\":
                    to_check.append((x - 1, y, "L"))
                else:
                    to_check.append((x - 1, y, "U"))
    unique_visited_tiles = set((item[0], item[1]) for item in visited)
    # -1 because we start outside the grid
    return len(unique_visited_tiles) - 1


def part2(parsed_input: list[list[str]]) -> int:
    max_visited = 0
    max_height = len(parsed_input)
    max_width = len(parsed_input[0])
    for i in range(max_height):
        num_visited = find_energized_tiles(parsed_input, (i, -1, "R"))
        if num_visited > max_visited:
            max_visited = num_visited
        num_visited = find_energized_tiles(parsed_input, (i, max_width, "L"))
        if num_visited > max_visited:
            max_visited = num_visited
    for i in range(max_width):
        num_visited = find_energized_tiles(parsed_input, (-1, i, "D"))
        if num_visited > max_visited:
            max_visited = num_visited
        num_visited = find_energized_tiles(parsed_input, (max_height, i, "U"))
        if num_visited > max_visited:
            max_visited = num_visited
    return max_visited


prepared_file = read_input("day16.txt")
print(find_energized_tiles(prepared_file, (0, -1, "R")))
print(part2(prepared_file))

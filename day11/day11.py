def read_input(input_path: str) -> list[list[str]]:
    with open(input_path, "r") as f:
        return [[*(line.strip())] for line in f.readlines()]


def find_galaxies(parsed_map: list[list[str]]) -> list[tuple[int, int]]:
    galaxies = []
    for i, row in enumerate(parsed_map):
        for j, position in enumerate(row):
            if position == "#":
                galaxies.append((i, j))
    return galaxies


def find_empty_lines(
    parsed_map: list[list[str]],
) -> tuple[list[int], list[int]]:
    empty_rows = []
    empty_columns = []
    for i, row in enumerate(parsed_map):
        if all(position == "." for position in row):
            empty_rows.append(i)
        if all(current_row[i] == "." for current_row in parsed_map):
            empty_columns.append(i)
    return empty_rows, empty_columns


def compute_distances_with_expansion(
    parsed_map: list[list[str]], expanding_rate: int = 2
) -> int:
    galaxies = find_galaxies(parsed_map)
    empty_rows, empty_columns = find_empty_lines(parsed_map)
    distances = 0
    for i, galaxy in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            smaller_x, bigger_x = min(galaxy[0], galaxies[j][0]), max(
                galaxy[0], galaxies[j][0]
            )
            smaller_y, bigger_y = min(galaxy[1], galaxies[j][1]), max(
                galaxy[1], galaxies[j][1]
            )
            y_diff = bigger_y - smaller_y
            for column in empty_columns:
                if smaller_y < column < bigger_y:
                    y_diff += expanding_rate - 1
            x_diff = bigger_x - smaller_x
            for row in empty_rows:
                if smaller_x < row < bigger_x:
                    x_diff += expanding_rate - 1
            distances += x_diff + y_diff
    return distances


prepared_file = read_input("day11.txt")
print(compute_distances_with_expansion(prepared_file, 2))
print(compute_distances_with_expansion(prepared_file, 1000000))

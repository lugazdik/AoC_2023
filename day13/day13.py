def read_input(input_path: str) -> list[list[list[str]]]:
    with open(input_path, "r") as f:
        grids = []
        for grid in f.read().split("\n\n"):
            current_grid = []
            for line in grid.split("\n"):
                current_grid.append([*line])
            grids.append(current_grid)
        return grids


def check_vertical(grid: list[list[str]], index: int) -> int:
    left_side = list(range(index, -1, -1))
    right_side = list(range(index + 1, len(grid[0])))
    for i, j in zip(left_side, right_side):
        for line in grid:
            if line[i] != line[j]:
                return 0
    return index + 1


def check_horizontal(grid: list[list[str]], index: int) -> int:
    left_side = list(range(index, -1, -1))
    right_side = list(range(index + 1, len(grid)))
    for i, j in zip(left_side, right_side):
        if grid[i] != grid[j]:
            return 0
    return index + 1


def part1(parsed_input: list[list[list[str]]]) -> int:
    verticals = 0
    horizontals = 0
    for grid in parsed_input:
        found = False
        for i in range(len(grid) - 1):
            if (horizontal := check_horizontal(grid, i)) != 0:
                horizontals += 100 * horizontal
                found = True
                break
        if not found:
            for i in range(len(grid[0]) - 1):
                if (vertical := check_vertical(grid, i)) != 0:
                    verticals += vertical
                    break
    return verticals + horizontals


prepared_file = read_input("day13.txt")
print(part1(prepared_file))

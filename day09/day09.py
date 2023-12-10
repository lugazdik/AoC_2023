def read_input(input_path: str) -> list[list[int]]:
    with open(input_path, "r") as f:
        return [list(map(int, line.strip().split())) for line in f]


def compute_line(line: list[int], part2: bool = False) -> int:
    differences = [second - first for first, second in zip(line, line[1:])]
    if all(difference == 0 for difference in differences):
        return 0
    return (
        differences[0] - compute_line(differences, part2)
        if part2
        else differences[-1] + compute_line(differences, part2)
    )


def compute_result(parsed_input: list[list[int]], part2: bool = False) -> int:
    result = 0
    for line in parsed_input:
        result += (
            line[0] - compute_line(line, part2)
            if part2
            else line[-1] + compute_line(line, part2)
        )
    return result


prepared_file = read_input("day09.txt")
print(compute_result(prepared_file, part2=False))
print(compute_result(prepared_file, part2=True))

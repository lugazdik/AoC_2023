def read_input(
    input_path: str,
) -> tuple[list[tuple[int, int, int]], list[tuple[int, int]]]:
    parts = []
    symbols = []
    with open(input_path, "r") as f:
        for row, line in enumerate(f.readlines()):
            row_numbers = []
            number = ""
            number_start_index = -1
            for column, symbol in enumerate(line.strip()):
                if symbol.isnumeric():
                    number += symbol
                    if number_start_index == -1:
                        number_start_index = column
                else:
                    if number:
                        row_numbers.append(
                            (
                                int(number),
                                number_start_index,
                                number_start_index + len(number) - 1,
                            )
                        )
                        number = ""
                        number_start_index = -1
                    if symbol != ".":
                        symbols.append((row, column))
            if number:
                row_numbers.append(
                    (
                        int(number),
                        number_start_index,
                        number_start_index + len(number) - 1,
                    )
                )
            parts.append(row_numbers)
        return parts, symbols


def read_input2(
    input_path: str,
) -> tuple[list[tuple[int, int, int]], list[tuple[int, int]]]:
    parts = []
    symbols = []
    with open(input_path, "r") as f:
        for row, line in enumerate(f.readlines()):
            row_numbers = []
            number = ""
            number_start_index = -1
            for column, symbol in enumerate(line.strip()):
                if symbol.isnumeric():
                    number += symbol
                    if number_start_index == -1:
                        number_start_index = column
                else:
                    if number:
                        row_numbers.append(
                            (
                                int(number),
                                number_start_index,
                                number_start_index + len(number) - 1,
                            )
                        )
                        number = ""
                        number_start_index = -1
                    if symbol == "*":
                        symbols.append((row, column))
            if number:
                row_numbers.append(
                    (
                        int(number),
                        number_start_index,
                        number_start_index + len(number) - 1,
                    )
                )
            parts.append(row_numbers)
        return parts, symbols


def part1(
    parts: list[tuple[int, int, int]],
    symbols: list[tuple[int, int]],
) -> int:
    result = []
    rows = []
    for row, row_parts in enumerate(parts):
        row_counting = []
        for row_part in row_parts:
            for symbol in symbols:
                if abs(row - symbol[0]) > 1 or (
                    abs(row_part[1] - symbol[1]) > 1
                    and abs(row_part[2] - symbol[1]) > 1
                ):
                    continue
                else:
                    row_counting.append(row_part[0])
                    result.append(row_part[0])
        rows.append(row_counting)
    return sum(result)


def part2(
    parts: list[tuple[int, int, int]],
    symbols: list[tuple[int, int]],
) -> int:
    result = {}
    for symbol in symbols:
        result[symbol] = []
        for row, row_parts in enumerate(parts):
            for row_part in row_parts:
                if abs(row - symbol[0]) > 1 or (
                    abs(row_part[1] - symbol[1]) > 1
                    and abs(row_part[2] - symbol[1]) > 1
                ):
                    continue
                else:
                    result[symbol].append(row_part[0])
    gear_ratio = 0
    for values in result.values():
        if len(values) == 2:
            gear_ratio += values[0] * values[1]
    return gear_ratio


parsed_parts, parsed_symbols = read_input("day03.txt")
print(part1(parsed_parts, parsed_symbols))
parsed_parts2, parsed_symbols2 = read_input2("day03.txt")
print(part2(parsed_parts2, parsed_symbols2))

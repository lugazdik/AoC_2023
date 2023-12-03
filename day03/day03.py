def read_input(
    input_path: str,
) -> tuple[list[tuple[int, int, int]], list[tuple[int, int, str]]]:
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
                        symbols.append((row, column, symbol))
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


def is_adjacent(row, start, end, symbol_row, symbol_column):
    if abs(row - symbol_row) > 1 or (
        abs(start - symbol_column) > 1 and abs(end - symbol_column) > 1
    ):
        return False
    return True


def part1(
    parts: list[tuple[int, int, int]],
    symbols: list[tuple[int, int, str]],
) -> int:
    result = []
    for row, row_parts in enumerate(parts):
        for row_part in row_parts:
            for symbol in symbols:
                if is_adjacent(
                    row,
                    row_part[1],
                    row_part[2],
                    symbol[0],
                    symbol[1],
                ):
                    result.append(row_part[0])
                    break
    return sum(result)


def part2(
    parts: list[tuple[int, int, int]],
    symbols: list[tuple[int, int, str]],
) -> int:
    result = {}
    for symbol in symbols:
        if symbol[2] != "*":
            continue
        result[symbol] = []
        for row, row_parts in enumerate(parts):
            for row_part in row_parts:
                if is_adjacent(
                    row,
                    row_part[1],
                    row_part[2],
                    symbol[0],
                    symbol[1],
                ):
                    result[symbol].append(row_part[0])
    gear_ratio = 0
    for values in result.values():
        if len(values) == 2:
            gear_ratio += values[0] * values[1]
    return gear_ratio


parsed_parts, parsed_symbols = read_input("day03.txt")
print(part1(parsed_parts, parsed_symbols))
print(part2(parsed_parts, parsed_symbols))

"""Description: Advent of Code (https://adventofcode.com/2023/day/1)"""
digit_dict = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def read_input(input_path: str):
    with open(input_path, "r") as f:
        return f.readlines()


def part1(parsed_input: list[str]):
    line_digits = []
    for line in parsed_input:
        line_digits.append([digit for digit in line if digit in digit_dict.values()])
    return sum(int(digits[0] + digits[-1]) for digits in line_digits)


def part2(parsed_input: list[str]):
    line_digits = []
    for line in parsed_input:
        digits = []
        for i, symbol in enumerate(line):
            if symbol in digit_dict.values():
                digits.append(symbol)
            else:
                for key, value in digit_dict.items():
                    if line[i:].startswith(key):
                        digits.append(value)
                        break
        line_digits.append(digits)
    return sum(int(digits[0] + digits[-1]) for digits in line_digits)


prepared_file = read_input("day01.txt")
print(part1(prepared_file))
print(part2(prepared_file))

def parse_card_numbers(card_numbers: str) -> set[int]:
    return {int(number) for number in card_numbers.split()}


def read_input(input_path: str) -> dict[int, dict[str, set[int]]]:
    with open(input_path, "r") as f:
        parsed_input = {}
        for line in f.readlines():
            split_line = line.strip().split(":")
            card_id = int(split_line[0].split()[1])
            split_card_numbers = str(split_line[1]).strip().split(" | ")
            winning_numbers = parse_card_numbers(split_card_numbers[0])
            card_numbers = parse_card_numbers(split_card_numbers[1])
            parsed_input[card_id] = {
                "winning_numbers": winning_numbers,
                "card_numbers": card_numbers,
                "card_copies": 1,
            }
        return parsed_input


def part1(input_data: dict[int, dict[str, set[int]]]) -> int:
    points = 0
    for card_data in input_data.values():
        num_of_winning_numbers = len(
            card_data["winning_numbers"] & card_data["card_numbers"]
        )
        points += (
            pow(2, num_of_winning_numbers - 1) if num_of_winning_numbers > 0 else 0
        )
    return points


def part2(input_data: dict[int, dict[str, set[int]]]) -> int:
    for card_id, card_data in input_data.items():
        num_of_winning_numbers = len(
            card_data["winning_numbers"] & card_data["card_numbers"]
        )
        new_cards = list(range(card_id + 1, card_id + num_of_winning_numbers + 1))
        for new_card in new_cards:
            input_data[new_card]["card_copies"] += card_data["card_copies"]
    return sum(data["card_copies"] for data in input_data.values())


prepared_file = read_input("day04.txt")
print(part1(prepared_file))
print(part2(prepared_file))

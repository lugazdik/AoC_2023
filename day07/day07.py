from collections import Counter


class Hand:
    cards: list[str]
    bid: int
    power: int

    card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, cards: list[str], bid: int):
        self.cards = cards
        self.bid = bid
        self.power = self.calculate_power()

    def calculate_power(self) -> int:
        counted_cards = Counter(self.cards)
        if (max_parity := max(counted_cards.values())) == 5:
            # five of a kind
            return 7
        if max_parity == 4:
            # four of a kind
            return 6
        if max_parity == 3:
            if min(counted_cards.values()) == 2:
                # full house
                return 5
            # three of a kind
            return 4
        if max_parity == 2:
            if Counter(counted_cards.values())[2] == 2:
                # two pairs
                return 3
            # one pair
            return 2
        # high card
        return 1

    def __eq__(self, other: "Hand") -> bool:
        if self.power == other.power:
            if self.cards == other.cards:
                return True
        return False

    def __lt__(self, other: "Hand") -> bool:
        if self.power < other.power:
            return True
        if self.power == other.power:
            for i, card in enumerate(self.cards):
                if self.card_order.index(card) < self.card_order.index(other.cards[i]):
                    return False
                if self.card_order.index(card) > self.card_order.index(other.cards[i]):
                    return True
        return False


def read_input(input_path: str) -> list[Hand]:
    with open(input_path, "r") as f:
        result = []
        for line in f.readlines():
            split_line = line.strip().split()
            result.append(Hand([*split_line[0]], int(split_line[1])))
        return result


def part1(parsed_input: list[Hand]) -> int:
    sorted_hands = sorted(parsed_input, reverse=True)
    return sum(
        hand.bid * rank
        for hand, rank in zip(sorted_hands, range(len(sorted_hands), 0, -1))
    )


prepared_file = read_input("day07.txt")
print(part1(prepared_file))

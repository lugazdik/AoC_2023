from collections import Counter


class Hand:
    cards: list[str]
    bid: int
    power: int

    def __init__(self, cards: list[str], bid: int, part2: bool = False):
        self.cards = cards
        self.bid = bid
        self.power = self.calculate_power(part2)
        self.card_order = (
            ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
            if part2
            else ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        )

    def calculate_power(self, with_jokers: bool = False) -> int:
        counted_cards = Counter(self.cards)
        if with_jokers:
            joker_parity = counted_cards.pop("J", 0)
            max_parity = max(counted_cards.values()) if counted_cards else 0
            min_parity = min(counted_cards.values()) if counted_cards else 5
            max_parity += joker_parity
        else:
            max_parity = max(counted_cards.values())
            min_parity = min(counted_cards.values())
        if (max_parity) == 5:
            return 7  # five of a kind
        if max_parity == 4:
            return 6  # four of a kind
        if max_parity == 3:
            if min_parity == 2:
                return 5  # full house
            return 4  # three of a kind
        if max_parity == 2:
            if Counter(counted_cards.values())[2] == 2:
                return 3  # two pairs
            return 2  # one pair
        return 1  # high card

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


def read_input(input_path: str, part2: bool = False) -> list[Hand]:
    with open(input_path, "r") as f:
        result = []
        for line in f.readlines():
            split_line = line.strip().split()
            result.append(Hand([*split_line[0]], int(split_line[1]), part2))
        return result


def compute_result(parsed_input: list[Hand]) -> int:
    sorted_hands = sorted(parsed_input, reverse=True)
    return sum(
        hand.bid * rank
        for hand, rank in zip(sorted_hands, range(len(sorted_hands), 0, -1))
    )


print(compute_result(read_input("day07.txt", part2=False)))
print(compute_result(read_input("day07.txt", part2=True)))

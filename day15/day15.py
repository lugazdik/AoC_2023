from collections import defaultdict


def read_input(input_path: str) -> list[str]:
    with open(input_path, "r") as f:
        return f.read().split(",")


def compute_hash(input_string: str) -> int:
    current_value = 0
    for letter in input_string:
        current_value = (current_value + ord(letter)) * 17 % 256
    return current_value


def part1(parsed_input: list[str]) -> int:
    results = []
    for item in parsed_input:
        results.append(compute_hash(item))
    return sum(results)


def part2(parsed_input: list[str]) -> int:
    hash_map = defaultdict(list)
    for item in parsed_input:
        if "=" in item:
            label, value = item.split("=")
            computed_hash = compute_hash(label)
            found = False
            for saved_value in hash_map[computed_hash]:
                if saved_value["label"] == label:
                    saved_value["value"] = int(value)
                    found = True
                    break
            if not found:
                hash_map[computed_hash].append({"label": label, "value": int(value)})
        elif "-" in item:
            label = item.split("-")[0]
            computed_hash = compute_hash(label)
            for saved_value in hash_map[computed_hash]:
                if saved_value["label"] == label:
                    hash_map[computed_hash].remove(saved_value)
                    break
    results = []
    for key, value in sorted(hash_map.items(), key=lambda x: x[0]):
        index = 1
        for item in value:
            results.append((key + 1) * index * item["value"])
            index += 1
    return sum(results)


prepared_file = read_input("day15.txt")
print(part1(prepared_file))
print(part2(prepared_file))

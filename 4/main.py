NUMBER_OF_LINES = 187


def main_part_one() -> None:
    res = 0
    input = open("input.txt", "r")
    line = input.readline()

    while line:
        winning, card_numbers = _parse_line(line)
        match_count = _get_match_count(winning, card_numbers)
        res += _calculate_card_score(match_count)
        line = input.readline()

    input.close()
    print(res)


def main_part_two() -> None:
    cards_count = [1] * NUMBER_OF_LINES
    with open("input.txt", "r") as input:
        for i, line in enumerate(input):
            winning, card_numbers = _parse_line(line)
            match_count = _get_match_count(winning, card_numbers)
            for _ in range(cards_count[i]):
                _update_number_of_cards(cards_count, i + 1, match_count)

    print(sum(cards_count))


def _parse_line(line: str) -> (set, set):
    line = line.rstrip("\n")
    line = line.split(": ")[-1]
    winning_numbers, card_numbers = line.split(" | ")
    winning_numbers = {int(x) for x in winning_numbers.split()}
    card_numbers = {int(x) for x in card_numbers.split()}
    return winning_numbers, card_numbers


def _get_match_count(winning: set, card_numbers: set) -> int:
    return len(winning.intersection(card_numbers))


def _calculate_card_score(match_count: int) -> int:
    if not match_count:
        return 0
    return 2 ** (len(match_count) - 1)


def _update_number_of_cards(
    number_of_cards: list[int], idx: int, match_count: int
) -> None:
    for x in range(idx, min(idx + match_count, len(number_of_cards))):
        number_of_cards[x] += 1


if __name__ == "__main__":
    main_part_two()

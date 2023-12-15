from typing import Union

BAG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def main_part_one() -> None:
    res = 0
    input = open("input.txt", "r")

    line = input.readline()
    while line:
        id, game = _extract_data_from_line(line)
        if _is_game_possible(game):
            res += id

        line = input.readline()

    input.close()
    print(res)


def main_part_two() -> None:
    res = 0
    input = open("input.txt", "r")

    line = input.readline()
    while line:
        _, game = _extract_data_from_line(line)
        fewer_dice = _get_fewest_dice(game)
        res += _get_set_power(fewer_dice)

        line = input.readline()

    input.close()
    print(res)


def _extract_data_from_line(line: str) -> Union[int, list[dict]]:
    sets_list = []

    line = line.lstrip("Game ")
    line = line.rstrip("\n")
    id, *game_sets = line.split(": ")
    game_sets = game_sets[0].split("; ")
    for game_set in game_sets:
        set_dict = {}
        dice_sets = game_set.split(", ")
        for dice_set in dice_sets:
            number, *color = dice_set.split(" ")
            set_dict[color[0]] = int(number)
        sets_list.append(set_dict)
    return int(id), sets_list


def _is_game_possible(game_sets: list[dict]) -> bool:
    for game_set in game_sets:
        for color, number in game_set.items():
            if number > BAG[color]:
                return False
    return True


def _get_fewest_dice(game_sets: list[dict]) -> dict:
    fewest = {
        "blue": 0,
        "green": 0,
        "red": 0,
    }
    for game_set in game_sets:
        for color, number in game_set.items():
            fewest[color] = max(number, fewest[color])
    return fewest


def _get_set_power(fewer_dice: dict) -> int:
    res = 1
    for count in fewer_dice.values():
        res *= count
    return res


if __name__ == "__main__":
    main_part_two()

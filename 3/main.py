SEEN_MARK = "."


def get_gear_ratio_part_one(input: str) -> None:
    res = 0
    matrix = _split_into_matrix(input)
    symbol_neighbors = _get_symbol_neighbors(matrix)

    for x, y in symbol_neighbors:
        if not matrix[x][y].isdigit():
            continue

        number_coordinates = _get_number_coordinates(matrix, x, y)
        res += _get_number_from_coordinates(matrix, number_coordinates)
        _mark_coordinates_as_seen(matrix, number_coordinates)

    return res


def _get_symbol_neighbors(matrix: list[list[str]]) -> list[tuple]:
    symbol_neighbors = []

    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if not _is_symbol(matrix[i][j]):
                continue

            symbol_neighbors += _get_neighbors(i, j, number_of_rows, number_of_columns)
    return symbol_neighbors


def _is_symbol(char: str) -> bool:
    return not (char.isdigit() or char == ".")


def get_gear_ratio_part_two(input: str) -> None:
    res = 0
    matrix = _split_into_matrix(input)
    asterisk_neighbors = _get_asterisk_neighbors(matrix)

    asterisk_numbers = {}
    for asterisk, neighbors in asterisk_neighbors.items():
        asterisk_numbers[asterisk] = []
        for x, y in neighbors:
            if not matrix[x][y].isdigit():
                continue

            number_coordinates = _get_number_coordinates(matrix, x, y)
            asterisk_numbers[asterisk].append(
                _get_number_from_coordinates(matrix, number_coordinates)
            )
            _mark_coordinates_as_seen(matrix, number_coordinates)

    for numbers in asterisk_numbers.values():
        if len(numbers) != 2:
            continue
        res += numbers[0] * numbers[1]

    return res


def _split_into_matrix(input: str) -> list[list[str]]:
    lines = input.split("\n")[:-1]
    return [list(line) for line in lines]


def _get_asterisk_neighbors(matrix: list[list[str]]) -> dict[tuple, list[tuple]]:
    asterisk_neighbors = {}

    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if matrix[i][j] != "*":
                continue
            asterisk_neighbors[(i, j)] = _get_neighbors(
                i, j, number_of_rows, number_of_columns
            )
    return asterisk_neighbors


def _get_neighbors(row: int, col: int, number_of_rows: int, number_of_columns: int):
    neighbors = []
    row_min = max(row - 1, 0)
    row_max = min(row + 1, number_of_rows)
    col_min = max(col - 1, 0)
    col_max = min(col + 1, number_of_columns)
    for x in range(row_min, row_max + 1):
        for y in range(col_min, col_max + 1):
            if (x, y) == (row, col):
                continue
            neighbors.append((x, y))
    return neighbors


def _get_number_coordinates(
    matrix: list[list[tuple]], row: int, col: int
) -> tuple[int, int, int]:
    """
    Searches to the left and to the right of matrix[row][col] to find
    the start and end coordinates of a number.
    """
    max_col = len(matrix[0])
    start_col = col
    while start_col - 1 >= 0 and matrix[row][start_col - 1].isdigit():
        start_col -= 1
    end_col = col
    while end_col + 1 < max_col and matrix[row][end_col + 1].isdigit():
        end_col += 1
    return row, start_col, end_col


def _get_number_from_coordinates(
    matrix: list[list[str]], number_coordinates: tuple[int, int, int]
) -> int:
    row, start_col, end_col = number_coordinates
    number_chars = matrix[row][start_col : end_col + 1]
    return int("".join(number_chars))


def _mark_coordinates_as_seen(
    matrix: list[list[str]], number_coordinates: tuple[int, int, int]
) -> None:
    row, start_col, end_col = number_coordinates
    for col in range(start_col, end_col + 1):
        matrix[row][col] = SEEN_MARK


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
        print("Part One")
        res_one = get_gear_ratio_part_one(content)
        print(res_one)
        print("Part Two")
        res_two = get_gear_ratio_part_two(content)
        print(res_two)

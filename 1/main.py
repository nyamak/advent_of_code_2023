def main_part_one() -> None:
    res = 0
    file = open("input.txt", "r")
    line = file.readline()
    while line:
        line_nums = [int(char) for char in line if char.isdigit()]
        if line_nums:
            number = int(f"{line_nums[0]}{line_nums[-1]}")
            res += number
        line = file.readline()
    file.close()

    print(res)


def main_part_two() -> None:
    res = 0
    file = open("input.txt", "r")
    line = file.readline()
    while line:
        print("before: " + line)
        line = _replace_written_digits(line)
        print("after: " + line)
        line_nums = [int(char) for char in line if char.isdigit()]
        if line_nums:
            number = int(f"{line_nums[0]}{line_nums[-1]}")
            res += number
            print(number)
        line = file.readline()
    file.close()

    print(res)


def _replace_written_digits(line: str) -> str:
    """
    Replace written digits for actual digits with first character if it's the
    possible last character of another digit and the last character if it's
    the possible first character of another digit, to account for overlap.
    """
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "4")
    line = line.replace("five", "5e")
    line = line.replace("six", "6")
    line = line.replace("seven", "7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    line = line.replace("zero", "0o")
    return line


if __name__ == "__main__":
    main_part_two()
